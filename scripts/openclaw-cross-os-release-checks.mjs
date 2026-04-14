#!/usr/bin/env node

import { createServer } from "node:http";
import { spawn } from "node:child_process";
import { createWriteStream, existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { createServer as createNetServer } from "node:net";

const args = parseArgs(process.argv.slice(2));
const sourceDir = requireArg(args, "source-dir");
const provider = requireArg(args, "provider");
const mode = args["mode"] ?? "both";
const outputDir = resolve(requireArg(args, "output-dir"));
const previousVersion = args["previous-version"]?.trim() || "";

const providerConfig = {
  openai: {
    secretEnv: "OPENAI_API_KEY",
    authChoice: "openai-api-key",
    model: "openai/gpt-5.4",
  },
  anthropic: {
    secretEnv: "ANTHROPIC_API_KEY",
    authChoice: "apiKey",
    model: "anthropic/claude-sonnet-4-6",
  },
  minimax: {
    secretEnv: "MINIMAX_API_KEY",
    authChoice: "minimax-global-api",
    model: "minimax/MiniMax-M2.7",
  },
};

if (!Object.hasOwn(providerConfig, provider)) {
  throw new Error(`Unsupported provider "${provider}".`);
}

if (!new Set(["fresh", "upgrade", "both"]).has(mode)) {
  throw new Error(`Unsupported mode "${mode}".`);
}

mkdirSync(outputDir, { recursive: true });
const logsDir = join(outputDir, "logs");
mkdirSync(logsDir, { recursive: true });

const selectedProvider = providerConfig[provider];
const providerSecretValue = process.env[selectedProvider.secretEnv]?.trim();
if (!providerSecretValue) {
  throw new Error(`Missing ${selectedProvider.secretEnv}.`);
}

const summary = {
  platform: process.platform,
  runnerOs: process.env.OPENCLAW_RELEASE_CHECK_OS ?? "",
  runnerLabel: process.env.OPENCLAW_RELEASE_CHECK_RUNNER ?? "",
  provider,
  mode,
  previousVersion: previousVersion || null,
  sourceDir: resolve(sourceDir),
  sourceSha: "",
  candidateVersion: "",
  candidateTgz: "",
  baselineSpec: previousVersion ? `openclaw@${previousVersion}` : "openclaw@latest",
  fresh: { status: mode === "upgrade" ? "skipped" : "pending" },
  upgrade: { status: mode === "fresh" ? "skipped" : "pending" },
};

let overallFailed = false;

try {
  const build = await prepareCandidate({
    sourceDir: resolve(sourceDir),
    logsDir,
  });
  summary.sourceSha = build.sourceSha;
  summary.candidateVersion = build.candidateVersion;
  summary.candidateTgz = build.candidateTgz;

  const tgzServer = await startStaticFileServer({
    filePath: build.candidateTgz,
    logPath: join(logsDir, "candidate-http-server.log"),
  });

  try {
    if (mode === "fresh" || mode === "both") {
      try {
        summary.fresh = await runFreshLane({
          build,
          logsDir,
          providerConfig: selectedProvider,
          providerSecretValue,
        });
      } catch (error) {
        overallFailed = true;
        summary.fresh = {
          status: "fail",
          error: formatError(error),
        };
      }
    }

    if (mode === "upgrade" || mode === "both") {
      try {
        summary.upgrade = await runUpgradeLane({
          build,
          baselineSpec: summary.baselineSpec,
          candidateUrl: tgzServer.url,
          logsDir,
          providerConfig: selectedProvider,
          providerSecretValue,
        });
      } catch (error) {
        overallFailed = true;
        summary.upgrade = {
          status: "fail",
          error: formatError(error),
        };
      }
    }
  } finally {
    await tgzServer.close();
  }
} catch (error) {
  overallFailed = true;
  summary.setup = {
    status: "fail",
    error: formatError(error),
  };
}

writeSummary(outputDir, summary);

if (overallFailed) {
  process.exit(1);
}

async function prepareCandidate(params) {
  const packageJsonPath = join(params.sourceDir, "package.json");
  const packageJson = JSON.parse(readFileSync(packageJsonPath, "utf8"));
  const sourceSha = (
    await runCommand(gitCommand(), ["rev-parse", "HEAD"], {
      cwd: params.sourceDir,
      logPath: join(params.logsDir, "git-rev-parse.log"),
    })
  ).stdout.trim();

  const buildEnv = {
    ...process.env,
    NODE_OPTIONS: "--max-old-space-size=6144",
  };

  await runCommand(pnpmCommand(), ["install", "--frozen-lockfile"], {
    cwd: params.sourceDir,
    env: buildEnv,
    logPath: join(params.logsDir, "pnpm-install.log"),
    timeoutMs: 45 * 60 * 1000,
  });

  await runCommand(pnpmCommand(), ["build"], {
    cwd: params.sourceDir,
    env: buildEnv,
    logPath: join(params.logsDir, "pnpm-build.log"),
    timeoutMs: 45 * 60 * 1000,
  });

  const packDir = join(outputDir, "package");
  mkdirSync(packDir, { recursive: true });
  const packJsonPath = join(packDir, "pack.json");
  const packResult = await runCommand(npmCommand(), ["pack", "--ignore-scripts", "--json", "--pack-destination", packDir], {
    cwd: params.sourceDir,
    logPath: join(params.logsDir, "npm-pack.log"),
    timeoutMs: 10 * 60 * 1000,
  });
  writeFileSync(packJsonPath, packResult.stdout, "utf8");
  const parsedPack = JSON.parse(packResult.stdout);
  const lastPack = Array.isArray(parsedPack) ? parsedPack.at(-1) : null;
  if (!lastPack?.filename) {
    throw new Error("npm pack did not report a filename.");
  }

  return {
    sourceDir: params.sourceDir,
    sourceSha,
    candidateVersion: String(lastPack.version ?? packageJson.version ?? "").trim(),
    candidateTgz: join(packDir, lastPack.filename),
  };
}

async function runFreshLane(params) {
  const lane = createLaneState("fresh");
  const cleanup = [];
  try {
    const env = buildLaneEnv(lane, params.providerConfig, params.providerSecretValue);
    await installPackage({
      spec: params.build.candidateTgz,
      env,
      cwd: lane.homeDir,
      logPath: join(params.logsDir, "fresh-install.log"),
    });
    const installed = readInstalledMetadata(lane.prefixDir);
    verifyInstalledCandidate(installed, params.build);

    await runOnboard({
      lane,
      env,
      providerConfig: params.providerConfig,
      logPath: join(params.logsDir, "fresh-onboard.log"),
    });

    const gateway = await startGateway({
      lane,
      env,
      logPath: join(params.logsDir, "fresh-gateway.log"),
    });
    cleanup.push(() => stopGateway(gateway));

    await waitForGateway({
      lane,
      env,
      logPath: join(params.logsDir, "fresh-gateway-status.log"),
    });

    await runModelsSet({
      lane,
      env,
      providerConfig: params.providerConfig,
      logPath: join(params.logsDir, "fresh-models-set.log"),
    });

    const agent = await runAgentTurn({
      lane,
      env,
      label: "fresh",
      logPath: join(params.logsDir, "fresh-agent.log"),
    });

    return {
      status: "pass",
      installedVersion: installed.version,
      installedCommit: installed.commit,
      gatewayPort: lane.gatewayPort,
      agentOutput: trimForSummary(agent.stdout),
    };
  } finally {
    await runCleanup(cleanup);
  }
}

async function runUpgradeLane(params) {
  const lane = createLaneState("upgrade");
  const cleanup = [];
  try {
    const env = buildLaneEnv(lane, params.providerConfig, params.providerSecretValue);
    await installPackage({
      spec: params.baselineSpec,
      env,
      cwd: lane.homeDir,
      logPath: join(params.logsDir, "upgrade-install-baseline.log"),
    });

    const baseline = readInstalledMetadata(lane.prefixDir);

    await runOpenClaw({
      lane,
      env,
      args: ["update", "--tag", params.candidateUrl, "--yes", "--json"],
      logPath: join(params.logsDir, "upgrade-update.log"),
      timeoutMs: 20 * 60 * 1000,
    });

    await runOpenClaw({
      lane,
      env,
      args: ["update", "status", "--json"],
      logPath: join(params.logsDir, "upgrade-update-status.log"),
      timeoutMs: 2 * 60 * 1000,
    });

    const installed = readInstalledMetadata(lane.prefixDir);
    verifyInstalledCandidate(installed, params.build);

    await runOnboard({
      lane,
      env,
      providerConfig: params.providerConfig,
      logPath: join(params.logsDir, "upgrade-onboard.log"),
    });

    const gateway = await startGateway({
      lane,
      env,
      logPath: join(params.logsDir, "upgrade-gateway.log"),
    });
    cleanup.push(() => stopGateway(gateway));

    await waitForGateway({
      lane,
      env,
      logPath: join(params.logsDir, "upgrade-gateway-status.log"),
    });

    await runModelsSet({
      lane,
      env,
      providerConfig: params.providerConfig,
      logPath: join(params.logsDir, "upgrade-models-set.log"),
    });

    const agent = await runAgentTurn({
      lane,
      env,
      label: "upgrade",
      logPath: join(params.logsDir, "upgrade-agent.log"),
    });

    return {
      status: "pass",
      baselineVersion: baseline.version,
      installedVersion: installed.version,
      installedCommit: installed.commit,
      gatewayPort: lane.gatewayPort,
      agentOutput: trimForSummary(agent.stdout),
    };
  } finally {
    await runCleanup(cleanup);
  }
}

function createLaneState(name) {
  const rootDir = mkdtempSync(join(tmpdir(), `openclaw-${name}-`));
  const prefixDir = join(rootDir, "prefix");
  const homeDir = join(rootDir, "home");
  const stateDir = join(homeDir, ".openclaw");
  const appDataDir = process.platform === "win32" ? join(homeDir, "AppData", "Roaming") : stateDir;
  mkdirSync(prefixDir, { recursive: true });
  mkdirSync(homeDir, { recursive: true });
  mkdirSync(stateDir, { recursive: true });
  mkdirSync(appDataDir, { recursive: true });
  return {
    name,
    rootDir,
    prefixDir,
    homeDir,
    stateDir,
    appDataDir,
    gatewayPort: 0,
  };
}

function buildLaneEnv(lane, providerMeta, providerSecretValue) {
  return {
    ...process.env,
    HOME: lane.homeDir,
    USERPROFILE: lane.homeDir,
    APPDATA: lane.appDataDir,
    LOCALAPPDATA: join(lane.homeDir, "AppData", "Local"),
    OPENCLAW_HOME: lane.homeDir,
    OPENCLAW_STATE_DIR: lane.stateDir,
    OPENCLAW_CONFIG_PATH: join(lane.stateDir, "openclaw.json"),
    NPM_CONFIG_PREFIX: lane.prefixDir,
    PATH: `${binDirForPrefix(lane.prefixDir)}${process.platform === "win32" ? ";" : ":"}${process.env.PATH ?? ""}`,
    [providerMeta.secretEnv]: providerSecretValue,
  };
}

async function installPackage(params) {
  await runCommand(npmCommand(), ["install", "-g", params.spec, "--no-fund", "--no-audit"], {
    cwd: params.cwd,
    env: params.env,
    logPath: params.logPath,
    timeoutMs: 20 * 60 * 1000,
  });
}

async function runOnboard(params) {
  params.lane.gatewayPort = await allocatePort();
  await runOpenClaw({
    lane: params.lane,
    env: params.env,
    args: [
      "onboard",
      "--non-interactive",
      "--mode",
      "local",
      "--auth-choice",
      params.providerConfig.authChoice,
      "--secret-input-mode",
      "ref",
      "--gateway-port",
      String(params.lane.gatewayPort),
      "--gateway-bind",
      "loopback",
      "--skip-skills",
      "--skip-health",
      "--accept-risk",
      "--json",
    ],
    logPath: params.logPath,
    timeoutMs: 10 * 60 * 1000,
  });
}

async function startGateway(params) {
  const gatewayLog = createWriteStream(params.logPath, { flags: "a" });
  const child = spawn(process.execPath, [installedEntryPath(params.lane.prefixDir), "gateway", "run", "--bind", "loopback", "--port", String(params.lane.gatewayPort), "--force"], {
    cwd: params.lane.homeDir,
    env: params.env,
    stdio: ["ignore", "pipe", "pipe"],
    windowsHide: true,
  });
  child.stdout?.pipe(gatewayLog);
  child.stderr?.pipe(gatewayLog);
  return { child, logPath: params.logPath };
}

async function waitForGateway(params) {
  const statusArgs = await resolveGatewayStatusArgs(params.lane, params.env, params.logPath);
  const deadline = Date.now() + 90_000;
  while (Date.now() < deadline) {
    const result = await runOpenClaw({
      lane: params.lane,
      env: params.env,
      args: statusArgs,
      logPath: params.logPath,
      timeoutMs: 15_000,
      check: false,
    });
    if (result.exitCode === 0) {
      return;
    }
    await sleep(2_000);
  }
  throw new Error(`Gateway did not become ready on port ${params.lane.gatewayPort}.`);
}

async function resolveGatewayStatusArgs(lane, env, logPath) {
  const help = await runOpenClaw({
    lane,
    env,
    args: ["gateway", "status", "--help"],
    logPath,
    timeoutMs: 15_000,
    check: false,
  });
  if (help.stdout.includes("--require-rpc") || help.stderr.includes("--require-rpc")) {
    return ["gateway", "status", "--deep", "--require-rpc", "--timeout", "5000"];
  }
  return ["gateway", "status", "--deep"];
}

async function runModelsSet(params) {
  await runOpenClaw({
    lane: params.lane,
    env: params.env,
    args: ["models", "set", params.providerConfig.model],
    logPath: params.logPath,
    timeoutMs: 2 * 60 * 1000,
  });
}

async function runAgentTurn(params) {
  const sessionId = `cross-os-release-check-${params.label}-${Date.now()}`;
  const result = await runOpenClaw({
    lane: params.lane,
    env: params.env,
    args: [
      "agent",
      "--agent",
      "main",
      "--session-id",
      sessionId,
      "--message",
      "Reply with exact ASCII text OK only.",
      "--json",
    ],
    logPath: params.logPath,
    timeoutMs: 10 * 60 * 1000,
  });
  if (!/\bOK\b/u.test(result.stdout)) {
    throw new Error("Agent output did not contain the expected OK marker.");
  }
  return result;
}

async function stopGateway(gateway) {
  if (!gateway?.child?.pid) {
    return;
  }
  if (process.platform === "win32") {
    await runCommand("taskkill", ["/PID", String(gateway.child.pid), "/T", "/F"], {
      logPath: gateway.logPath,
      check: false,
      timeoutMs: 30_000,
    });
    return;
  }
  gateway.child.kill("SIGTERM");
  await sleep(2_000);
  if (!gateway.child.killed) {
    gateway.child.kill("SIGKILL");
  }
}

async function runCleanup(cleanupFns) {
  for (const cleanupFn of cleanupFns.reverse()) {
    try {
      await cleanupFn();
    } catch {
      // Ignore cleanup failures so the main failure surface stays visible.
    }
  }
}

async function runOpenClaw(params) {
  return runCommand(process.execPath, [installedEntryPath(params.lane.prefixDir), ...params.args], {
    cwd: params.lane.homeDir,
    env: params.env,
    logPath: params.logPath,
    timeoutMs: params.timeoutMs,
    check: params.check ?? true,
  });
}

function readInstalledMetadata(prefixDir) {
  const packageRoot = installedPackageRoot(prefixDir);
  const packageJsonPath = join(packageRoot, "package.json");
  const buildInfoPath = join(packageRoot, "dist", "build-info.json");
  if (!existsSync(packageJsonPath)) {
    throw new Error(`Installed package manifest missing: ${packageJsonPath}`);
  }
  if (!existsSync(buildInfoPath)) {
    throw new Error(`Installed build info missing: ${buildInfoPath}`);
  }
  const packageJson = JSON.parse(readFileSync(packageJsonPath, "utf8"));
  const buildInfo = JSON.parse(readFileSync(buildInfoPath, "utf8"));
  return {
    version: String(packageJson.version ?? "").trim(),
    commit: String(buildInfo.commit ?? "").trim(),
  };
}

function verifyInstalledCandidate(installed, build) {
  if (installed.version !== build.candidateVersion) {
    throw new Error(
      `Installed version mismatch. Expected ${build.candidateVersion}, found ${installed.version || "<missing>"}.`,
    );
  }
  if (installed.commit !== build.sourceSha) {
    throw new Error(
      `Installed build commit mismatch. Expected ${build.sourceSha}, found ${installed.commit || "<missing>"}.`,
    );
  }
}

function installedPackageRoot(prefixDir) {
  return process.platform === "win32"
    ? join(prefixDir, "node_modules", "openclaw")
    : join(prefixDir, "lib", "node_modules", "openclaw");
}

function installedEntryPath(prefixDir) {
  return join(installedPackageRoot(prefixDir), "openclaw.mjs");
}

function binDirForPrefix(prefixDir) {
  return process.platform === "win32" ? prefixDir : join(prefixDir, "bin");
}

function pnpmCommand() {
  return process.platform === "win32" ? "pnpm.cmd" : "pnpm";
}

function npmCommand() {
  return process.platform === "win32" ? "npm.cmd" : "npm";
}

function gitCommand() {
  return process.platform === "win32" ? "git.exe" : "git";
}

async function runCommand(command, args, options) {
  return new Promise((resolvePromise, rejectPromise) => {
    const child = spawn(command, args, {
      cwd: options.cwd,
      env: options.env,
      stdio: ["ignore", "pipe", "pipe"],
      windowsHide: true,
    });
    const logStream = createWriteStream(options.logPath, { flags: "a" });
    let stdout = "";
    let stderr = "";
    let timedOut = false;

    const timer =
      options.timeoutMs && Number.isFinite(options.timeoutMs)
        ? setTimeout(() => {
            timedOut = true;
            child.kill(process.platform === "win32" ? undefined : "SIGKILL");
          }, options.timeoutMs)
        : null;

    child.stdout?.on("data", (chunk) => {
      const text = chunk.toString();
      stdout += text;
      logStream.write(text);
    });
    child.stderr?.on("data", (chunk) => {
      const text = chunk.toString();
      stderr += text;
      logStream.write(text);
    });

    child.on("error", (error) => {
      if (timer) {
        clearTimeout(timer);
      }
      logStream.end();
      rejectPromise(error);
    });

    child.on("close", (exitCode) => {
      if (timer) {
        clearTimeout(timer);
      }
      logStream.end();
      const result = {
        exitCode: exitCode ?? 1,
        stdout,
        stderr,
      };
      if (timedOut) {
        rejectPromise(
          new Error(`Command timed out: ${command} ${args.join(" ")}`),
        );
        return;
      }
      if ((options.check ?? true) && result.exitCode !== 0) {
        rejectPromise(
          new Error(
            `Command failed (${result.exitCode}): ${command} ${args.join(" ")}\n${trimForSummary(
              `${stdout}\n${stderr}`,
            )}`,
          ),
        );
        return;
      }
      resolvePromise(result);
    });
  });
}

async function startStaticFileServer(params) {
  mkdirSync(dirname(params.logPath), { recursive: true });
  const logStream = createWriteStream(params.logPath, { flags: "a" });
  const fileName = params.filePath.split(/[/\\]/u).at(-1);
  const fileBytes = readFileSync(params.filePath);
  const server = createServer((request, response) => {
    logStream.write(`${new Date().toISOString()} ${request.method} ${request.url}\n`);
    if (request.url !== `/${fileName}`) {
      response.statusCode = 404;
      response.end("not found");
      return;
    }
    response.statusCode = 200;
    response.setHeader("content-type", "application/octet-stream");
    response.setHeader("content-length", String(fileBytes.length));
    response.end(fileBytes);
  });
  const port = await allocatePort();
  await new Promise((resolvePromise, rejectPromise) => {
    server.once("error", rejectPromise);
    server.listen(port, "127.0.0.1", resolvePromise);
  });
  return {
    url: `http://127.0.0.1:${port}/${fileName}`,
    close: () =>
      new Promise((resolvePromise, rejectPromise) => {
        server.close((error) => {
          logStream.end();
          if (error) {
            rejectPromise(error);
            return;
          }
          resolvePromise();
        });
      }),
  };
}

function writeSummary(baseDir, summaryPayload) {
  const summaryJsonPath = join(baseDir, "summary.json");
  const summaryMarkdownPath = join(baseDir, "summary.md");
  writeFileSync(summaryJsonPath, `${JSON.stringify(summaryPayload, null, 2)}\n`, "utf8");

  const lines = [
    `## ${platformLabel()}`,
    "",
    `- Provider: \`${summaryPayload.provider}\``,
    `- Mode: \`${summaryPayload.mode}\``,
    `- Source SHA: \`${summaryPayload.sourceSha || "unknown"}\``,
    `- Candidate version: \`${summaryPayload.candidateVersion || "unknown"}\``,
    `- Baseline spec: \`${summaryPayload.baselineSpec}\``,
    summaryPayload.fresh?.status ? `- Fresh lane: \`${summaryPayload.fresh.status}\`` : "",
    summaryPayload.upgrade?.status ? `- Upgrade lane: \`${summaryPayload.upgrade.status}\`` : "",
  ].filter(Boolean);
  writeFileSync(summaryMarkdownPath, `${lines.join("\n")}\n`, "utf8");
}

function platformLabel() {
  if (process.platform === "darwin") {
    return "macOS Release Checks";
  }
  if (process.platform === "win32") {
    return "Windows Release Checks";
  }
  return "Linux Release Checks";
}

function parseArgs(argv) {
  const parsed = {};
  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (!token.startsWith("--")) {
      continue;
    }
    const key = token.slice(2);
    const next = argv[index + 1];
    if (!next || next.startsWith("--")) {
      parsed[key] = "true";
      continue;
    }
    parsed[key] = next;
    index += 1;
  }
  return parsed;
}

function requireArg(argsMap, key) {
  const value = argsMap[key]?.trim();
  if (!value) {
    throw new Error(`Missing required --${key} argument.`);
  }
  return value;
}

function trimForSummary(value) {
  const trimmed = value.trim();
  if (trimmed.length <= 600) {
    return trimmed;
  }
  return `${trimmed.slice(0, 600)}...`;
}

function formatError(error) {
  if (error instanceof Error) {
    return error.stack || error.message;
  }
  return String(error);
}

function sleep(ms) {
  return new Promise((resolvePromise) => setTimeout(resolvePromise, ms));
}

function allocatePort() {
  return new Promise((resolvePromise, rejectPromise) => {
    const server = createNetServer();
    server.listen(0, "127.0.0.1", () => {
      const address = server.address();
      server.close();
      if (!address || typeof address === "string") {
        rejectPromise(new Error("Failed to allocate a TCP port."));
        return;
      }
      resolvePromise(address.port);
    });
    server.once("error", rejectPromise);
  });
}

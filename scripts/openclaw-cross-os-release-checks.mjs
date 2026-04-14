#!/usr/bin/env node

import { createServer } from "node:http";
import { spawn } from "node:child_process";
import { chmodSync, createWriteStream, existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { createServer as createNetServer } from "node:net";

const args = parseArgs(process.argv.slice(2));
const outputDir = resolve(requireArg(args, "output-dir"));
const prepareOnly = args["prepare-only"] === "true";
const sourceDir = args["source-dir"]?.trim() ? resolve(args["source-dir"].trim()) : "";
const provider = args["provider"]?.trim() || "";
const mode = args["mode"] ?? "both";
const previousVersion = args["previous-version"]?.trim() || "";
const baselineSpec = args["baseline-spec"]?.trim() || (previousVersion ? `openclaw@${previousVersion}` : "openclaw@latest");
const providedCandidateTgz = args["candidate-tgz"]?.trim() ? resolve(args["candidate-tgz"].trim()) : "";
const providedCandidateVersion = args["candidate-version"]?.trim() || "";
const providedSourceSha = args["source-sha"]?.trim() || "";

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

if (!new Set(["fresh", "upgrade", "both"]).has(mode)) {
  throw new Error(`Unsupported mode "${mode}".`);
}

mkdirSync(outputDir, { recursive: true });
const logsDir = join(outputDir, "logs");
mkdirSync(logsDir, { recursive: true });

if (prepareOnly) {
  if (!sourceDir) {
    throw new Error("--prepare-only requires --source-dir.");
  }
  const build = await prepareCandidate({
    sourceDir,
    logsDir,
  });
  writeCandidateManifest(outputDir, build);
  process.exit(0);
}

if (!Object.hasOwn(providerConfig, provider)) {
  throw new Error(`Unsupported provider "${provider}".`);
}

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
  sourceDir,
  sourceSha: "",
  candidateVersion: "",
  candidateTgz: "",
  baselineSpec,
  fresh: { status: mode === "upgrade" ? "skipped" : "pending" },
  upgrade: { status: mode === "fresh" ? "skipped" : "pending" },
};

let overallFailed = false;

try {
  const build = sourceDir
    ? await prepareCandidate({
        sourceDir,
        logsDir,
      })
    : readProvidedCandidate({
        candidateTgz: providedCandidateTgz,
        candidateVersion: providedCandidateVersion,
        sourceSha: providedSourceSha,
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
          baselineSpec,
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
  const hasUiBuildScript = typeof packageJson.scripts?.["ui:build"] === "string";
  const controlUiIndexPath = join(params.sourceDir, "dist", "control-ui", "index.html");
  const controlUiAssetsPath = join(params.sourceDir, "dist", "control-ui", "assets");
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

  if (!hasControlUiBundle(controlUiIndexPath, controlUiAssetsPath) && hasUiBuildScript) {
    await runCommand(pnpmCommand(), ["ui:build"], {
      cwd: params.sourceDir,
      env: buildEnv,
      logPath: join(params.logsDir, "pnpm-ui-build.log"),
      timeoutMs: 30 * 60 * 1000,
    });
  }

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
    candidateFileName: String(lastPack.filename).trim(),
  };
}

function hasControlUiBundle(indexPath, assetsPath) {
  if (!existsSync(indexPath) || !existsSync(assetsPath)) {
    return false;
  }
  try {
    return readdirSync(assetsPath).length > 0;
  } catch {
    return false;
  }
}

function readProvidedCandidate(params) {
  if (!params.candidateTgz) {
    throw new Error("Missing required --candidate-tgz argument when --source-dir is not provided.");
  }
  if (!existsSync(params.candidateTgz)) {
    throw new Error(`Candidate package not found: ${params.candidateTgz}`);
  }
  if (!params.candidateVersion) {
    throw new Error("Missing required --candidate-version argument when --source-dir is not provided.");
  }
  if (!params.sourceSha) {
    throw new Error("Missing required --source-sha argument when --source-dir is not provided.");
  }
  return {
    sourceDir: "",
    sourceSha: params.sourceSha,
    candidateVersion: params.candidateVersion,
    candidateTgz: params.candidateTgz,
    candidateFileName: params.candidateTgz.split(/[/\\]/u).at(-1) ?? "",
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

    await runDashboardSmoke({
      lane,
      logPath: join(params.logsDir, "fresh-dashboard.log"),
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
      dashboardStatus: "pass",
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

    await runDashboardSmoke({
      lane,
      logPath: join(params.logsDir, "upgrade-dashboard.log"),
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
      dashboardStatus: "pass",
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
  ensureLocalNpmShim(lane);
  return {
    ...process.env,
    HOME: lane.homeDir,
    USERPROFILE: lane.homeDir,
    APPDATA: lane.appDataDir,
    LOCALAPPDATA: join(lane.homeDir, "AppData", "Local"),
    OPENCLAW_HOME: lane.homeDir,
    OPENCLAW_STATE_DIR: lane.stateDir,
    OPENCLAW_CONFIG_PATH: join(lane.stateDir, "openclaw.json"),
    OPENCLAW_DISABLE_BONJOUR: "1",
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

function ensureLocalNpmShim(lane) {
  const shimPath = npmShimPath(lane.prefixDir);
  if (existsSync(shimPath)) {
    return;
  }
  mkdirSync(dirname(shimPath), { recursive: true });
  const resolvedNpm = resolveCommandPath(npmCommand());
  if (!resolvedNpm) {
    throw new Error(`Failed to resolve ${npmCommand()} on PATH.`);
  }
  if (process.platform === "win32") {
    writeFileSync(
      shimPath,
      `@echo off\r\nset "NPM_CONFIG_PREFIX=${lane.prefixDir}"\r\n"${resolvedNpm}" %*\r\n`,
      "utf8",
    );
    return;
  }
  writeFileSync(
    shimPath,
    `#!/bin/sh\nexport NPM_CONFIG_PREFIX='${shellEscapeForSh(lane.prefixDir)}'\nexec '${shellEscapeForSh(resolvedNpm)}' "$@"\n`,
    "utf8",
  );
  chmodSync(shimPath, 0o755);
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

async function runDashboardSmoke(params) {
  const dashboardUrl = `http://127.0.0.1:${params.lane.gatewayPort}/`;
  const logStream = createWriteStream(params.logPath, { flags: "a" });
  const deadline = Date.now() + 30_000;
  let attempt = 0;
  try {
    while (Date.now() < deadline) {
      attempt += 1;
      logStream.write(`${new Date().toISOString()} attempt=${attempt} url=${dashboardUrl}\n`);
      try {
        const response = await fetch(dashboardUrl, {
          signal: AbortSignal.timeout(5_000),
        });
        const html = await response.text();
        if (
          response.ok &&
          html.includes("<title>OpenClaw Control</title>") &&
          html.includes("<openclaw-app></openclaw-app>")
        ) {
          logStream.write(`${new Date().toISOString()} dashboard-ready status=${response.status}\n`);
          return;
        }
        logStream.write(
          `${new Date().toISOString()} dashboard-not-ready status=${response.status} title=${html.includes("<title>OpenClaw Control</title>")} app=${html.includes("<openclaw-app></openclaw-app>")}\n`,
        );
      } catch (error) {
        logStream.write(`${new Date().toISOString()} dashboard-fetch-error ${formatError(error)}\n`);
      }
      await sleep(1_000);
    }
  } finally {
    logStream.end();
  }
  throw new Error(`Dashboard HTML did not become ready at ${dashboardUrl}.`);
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
    const exited = await waitForChildExit(gateway.child, 10_000);
    if (!exited) {
      gateway.child.stdout?.destroy();
      gateway.child.stderr?.destroy();
    }
    return;
  }
  if (gateway.child.exitCode !== null) {
    return;
  }
  gateway.child.kill("SIGTERM");
  const exitedAfterTerm = await waitForChildExit(gateway.child, 2_000);
  if (!exitedAfterTerm && gateway.child.exitCode === null) {
    gateway.child.kill("SIGKILL");
    await waitForChildExit(gateway.child, 5_000);
  }
}

async function waitForChildExit(child, timeoutMs) {
  if (child.exitCode !== null) {
    return true;
  }
  return new Promise((resolvePromise) => {
    let settled = false;
    const finish = (didExit) => {
      if (settled) {
        return;
      }
      settled = true;
      if (timer) {
        clearTimeout(timer);
      }
      child.off("exit", onExit);
      child.off("close", onClose);
      child.off("error", onError);
      resolvePromise(didExit);
    };
    const onExit = () => finish(true);
    const onClose = () => finish(true);
    const onError = () => finish(true);
    const timer =
      timeoutMs > 0
        ? setTimeout(() => {
            finish(false);
          }, timeoutMs)
        : null;

    child.once("exit", onExit);
    child.once("close", onClose);
    child.once("error", onError);
  });
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

function npmShimPath(prefixDir) {
  return process.platform === "win32" ? join(prefixDir, "npm.cmd") : join(prefixDir, "bin", "npm");
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
    const useWindowsShell = process.platform === "win32" && /\.(cmd|bat)$/iu.test(command);
    const child = spawn(command, args, {
      cwd: options.cwd,
      env: options.env,
      shell: useWindowsShell,
      stdio: ["ignore", "pipe", "pipe"],
      windowsHide: true,
    });
    const logStream = createWriteStream(options.logPath, { flags: "a" });
    let stdout = "";
    let stderr = "";
    let timedOut = false;
    let settled = false;

    const clearTimers = () => {
      if (timer) {
        clearTimeout(timer);
      }
      if (killWaitTimer) {
        clearTimeout(killWaitTimer);
      }
    };

    const finalize = (callback) => {
      if (settled) {
        return;
      }
      settled = true;
      clearTimers();
      logStream.end();
      callback();
    };

    const requestKill = () => {
      if (process.platform === "win32" && child.pid) {
        try {
          const killer = spawn("taskkill", ["/PID", String(child.pid), "/T", "/F"], {
            stdio: "ignore",
            windowsHide: true,
          });
          killer.on("error", () => {
            child.kill();
          });
          return;
        } catch {
          child.kill();
          return;
        }
      }
      child.kill(process.platform === "win32" ? undefined : "SIGKILL");
    };

    let killWaitTimer = null;
    const timer =
      options.timeoutMs && Number.isFinite(options.timeoutMs)
        ? setTimeout(() => {
            timedOut = true;
            logStream.write(`${new Date().toISOString()} timeout command=${command} args=${args.join(" ")}\n`);
            requestKill();
            killWaitTimer = setTimeout(() => {
              finalize(() => {
                rejectPromise(
                  new Error(`Command timed out and could not be terminated cleanly: ${command} ${args.join(" ")}`),
                );
              });
            }, 15_000);
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
      finalize(() => rejectPromise(error));
    });

    child.on("close", (exitCode) => {
      finalize(() => {
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
    summaryPayload.fresh?.dashboardStatus
      ? `- Fresh dashboard: \`${summaryPayload.fresh.dashboardStatus}\``
      : "",
    summaryPayload.upgrade?.status ? `- Upgrade lane: \`${summaryPayload.upgrade.status}\`` : "",
    summaryPayload.upgrade?.dashboardStatus
      ? `- Upgrade dashboard: \`${summaryPayload.upgrade.dashboardStatus}\``
      : "",
  ].filter(Boolean);
  writeFileSync(summaryMarkdownPath, `${lines.join("\n")}\n`, "utf8");
}

function writeCandidateManifest(baseDir, build) {
  const manifestPath = join(baseDir, "candidate.json");
  writeFileSync(
    manifestPath,
    `${JSON.stringify(
      {
        sourceSha: build.sourceSha,
        candidateVersion: build.candidateVersion,
        candidateFileName: build.candidateFileName,
      },
      null,
      2,
    )}\n`,
    "utf8",
  );
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

function resolveCommandPath(command) {
  const pathValue = process.env.PATH ?? "";
  const pathEntries = pathValue.split(process.platform === "win32" ? ";" : ":").filter(Boolean);
  const candidates =
    process.platform === "win32" && !command.toLowerCase().endsWith(".cmd")
      ? [`${command}.cmd`, `${command}.exe`, command]
      : [command];
  for (const entry of pathEntries) {
    for (const candidate of candidates) {
      const fullPath = join(entry, candidate);
      if (existsSync(fullPath)) {
        return fullPath;
      }
    }
  }
  return null;
}

function shellEscapeForSh(value) {
  return value.replace(/'/gu, `'\"'\"'`);
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

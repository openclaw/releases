#!/usr/bin/env node
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";

const PUBLIC_REPO = "openclaw/openclaw";

function usage() {
  console.log(`Usage:
  node scripts/openclaw-release-evidence-from-full-validation.mjs \\
    --full-validation-run-id 24977011361 \\
    --release-id 2026.4.24 \\
    [--release-ref v2026.4.24] \\
    [--package-spec openclaw@2026.4.24] \\
    [--notes-file /tmp/notes.md] \\
    [--output-root evidence]
`);
}

function parseArgs(argv) {
  const args = {
    fullValidationRunId: "",
    releaseId: "",
    releaseRef: "",
    packageSpec: "",
    notesFile: "",
    outputRoot: "evidence",
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--help" || arg === "-h") {
      usage();
      process.exit(0);
    }
    const next = () => {
      i += 1;
      if (i >= argv.length) throw new Error(`Missing value for ${arg}`);
      return argv[i];
    };
    switch (arg) {
      case "--full-validation-run-id":
        args.fullValidationRunId = next();
        break;
      case "--release-id":
        args.releaseId = next();
        break;
      case "--release-ref":
        args.releaseRef = next();
        break;
      case "--package-spec":
        args.packageSpec = next();
        break;
      case "--notes-file":
        args.notesFile = next();
        break;
      case "--output-root":
        args.outputRoot = next();
        break;
      default:
        throw new Error(`Unknown argument: ${arg}`);
    }
  }

  if (!/^[0-9]+$/.test(args.fullValidationRunId)) {
    throw new Error("--full-validation-run-id must be numeric");
  }
  if (!/^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(args.releaseId)) {
    throw new Error(
      "--release-id must contain only letters, numbers, dot, underscore, or dash",
    );
  }
  return args;
}

async function githubJson(pathname) {
  const token = process.env.GH_TOKEN || process.env.GITHUB_TOKEN || "";
  const headers = {
    Accept: "application/vnd.github+json",
    "User-Agent": "openclaw-release-evidence",
    "X-GitHub-Api-Version": "2022-11-28",
  };
  if (token) headers.Authorization = `Bearer ${token}`;

  const response = await fetch(`https://api.github.com${pathname}`, { headers });
  const body = await response.text();
  if (!response.ok) {
    throw new Error(
      `GitHub API ${pathname} failed: ${response.status} ${response.statusText}\n${body}`,
    );
  }
  return body ? JSON.parse(body) : null;
}

async function githubText(pathname) {
  const token = process.env.GH_TOKEN || process.env.GITHUB_TOKEN || "";
  const headers = {
    Accept: "application/vnd.github+json",
    "User-Agent": "openclaw-release-evidence",
    "X-GitHub-Api-Version": "2022-11-28",
  };
  if (token) headers.Authorization = `Bearer ${token}`;

  const response = await fetch(`https://api.github.com${pathname}`, { headers });
  const body = await response.text();
  if (response.status === 404) {
    return "";
  }
  if (!response.ok) {
    throw new Error(
      `GitHub API ${pathname} failed: ${response.status} ${response.statusText}\n${body}`,
    );
  }
  return body;
}

async function githubPaged(pathname) {
  const values = [];
  for (let page = 1; page <= 10; page += 1) {
    const separator = pathname.includes("?") ? "&" : "?";
    const payload = await githubJson(
      `${pathname}${separator}per_page=100&page=${page}`,
    );
    const pageValues = payload?.jobs ?? payload?.workflow_runs ?? [];
    values.push(...pageValues);
    if (!Array.isArray(pageValues) || pageValues.length < 100) break;
  }
  return values;
}

function collectChildRuns(logText) {
  const patterns = [
    {
      label: "normal-ci",
      workflow: "CI",
      re: /Dispatched ci\.yml:\s+https:\/\/github\.com\/openclaw\/openclaw\/actions\/runs\/([0-9]+)/,
    },
    {
      label: "release-checks",
      workflow: "OpenClaw Release Checks",
      re: /Dispatched openclaw-release-checks\.yml:\s+https:\/\/github\.com\/openclaw\/openclaw\/actions\/runs\/([0-9]+)/,
    },
    {
      label: "postpublish-telegram",
      workflow: "NPM Telegram Beta E2E",
      re: /Dispatched npm-telegram-beta-e2e\.yml:\s+https:\/\/github\.com\/openclaw\/openclaw\/actions\/runs\/([0-9]+)/,
    },
  ];

  const matches = [];
  for (const pattern of patterns) {
    const match = logText.match(pattern.re);
    if (match?.[1]) {
      matches.push({
        label: pattern.label,
        workflow: pattern.workflow,
        runId: match[1],
      });
    }
  }
  return matches;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const [owner, repo] = PUBLIC_REPO.split("/");
  const parentRun = await githubJson(
    `/repos/${owner}/${repo}/actions/runs/${args.fullValidationRunId}`,
  );
  if (parentRun.name !== "Full Release Validation") {
    throw new Error(
      `Run ${args.fullValidationRunId} is ${parentRun.name}, not Full Release Validation`,
    );
  }
  if (parentRun.status !== "completed") {
    throw new Error(
      `Full Release Validation run ${args.fullValidationRunId} is ${parentRun.status}; wait for completion before ingesting evidence`,
    );
  }

  const jobs = await githubPaged(
    `/repos/${owner}/${repo}/actions/runs/${args.fullValidationRunId}/jobs`,
  );
  const childRuns = new Map();
  for (const job of jobs) {
    const logText = await githubText(`/repos/${owner}/${repo}/actions/jobs/${job.id}/logs`);
    for (const child of collectChildRuns(logText)) {
      childRuns.set(child.label, child);
    }
  }

  const runLines = [
    `full-release-validation ${PUBLIC_REPO} ${args.fullValidationRunId} blocking`,
  ];
  for (const label of ["normal-ci", "release-checks", "postpublish-telegram"]) {
    const child = childRuns.get(label);
    if (child) {
      runLines.push(`${child.label} ${PUBLIC_REPO} ${child.runId} blocking`);
    }
  }

  const tmpDir = await fs.mkdtemp(path.join(os.tmpdir(), "openclaw-release-evidence-"));
  const runsFile = path.join(tmpDir, "runs.txt");
  const notesFile = args.notesFile || path.join(tmpDir, "notes.md");
  await fs.writeFile(runsFile, `${runLines.join("\n")}\n`);
  if (!args.notesFile) {
    const childSummary =
      [...childRuns.values()]
        .map((child) => `${child.workflow}: ${child.runId}`)
        .join("; ") || "no child runs found";
    await fs.writeFile(
      notesFile,
      `Automatically ingested from Full Release Validation ${args.fullValidationRunId}. Child runs: ${childSummary}.\n`,
    );
  }

  const script = path.join("scripts", "openclaw-release-evidence.mjs");
  const commandArgs = [
    script,
    "--release-id",
    args.releaseId,
    "--release-ref",
    args.releaseRef,
    "--package-spec",
    args.packageSpec,
    "--runs-file",
    runsFile,
    "--notes-file",
    notesFile,
    "--output-root",
    args.outputRoot,
  ];
  const result = spawnSync(process.execPath, commandArgs, {
    stdio: "inherit",
    env: process.env,
  });
  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : error);
  process.exit(1);
});

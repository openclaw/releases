#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";

const DEFAULT_PRIVATE_REPO = "openclaw/releases-private";

function usage() {
  console.log(`Usage:
  node scripts/openclaw-release-evidence.mjs \\
    --release-id 2026.4.27-beta.1 \\
    --runs-file /tmp/runs.txt \\
    [--release-ref <tag-or-sha>] \\
    [--package-spec openclaw@2026.4.27-beta.1] \\
    [--notes-file /tmp/notes.md] \\
    [--output-root evidence]

Runs file format, one run per line:
  <label> <owner/repo> <run-id> <blocking|advisory>

Example:
  full-release-validation openclaw/openclaw 24972498713 blocking
  private-cross-os openclaw/releases-private 123456789 advisory
`);
}

function parseArgs(argv) {
  const args = {
    outputRoot: "evidence",
    releaseRef: "",
    packageSpec: "",
    notesFile: "",
    releaseId: "",
    runsFile: "",
  };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--help" || arg === "-h") {
      usage();
      process.exit(0);
    }
    const next = () => {
      i += 1;
      if (i >= argv.length) {
        throw new Error(`Missing value for ${arg}`);
      }
      return argv[i];
    };
    switch (arg) {
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
      case "--runs-file":
        args.runsFile = next();
        break;
      case "--output-root":
        args.outputRoot = next();
        break;
      default:
        throw new Error(`Unknown argument: ${arg}`);
    }
  }
  if (!args.releaseId) {
    throw new Error("--release-id is required");
  }
  if (!args.runsFile) {
    throw new Error("--runs-file is required");
  }
  if (!/^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(args.releaseId)) {
    throw new Error(
      "--release-id must contain only letters, numbers, dot, underscore, or dash",
    );
  }
  return args;
}

function parseRunsFile(text) {
  return text
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => line.length > 0 && !line.startsWith("#"))
    .map((line, index) => {
      const parts = line.split(/\s+/);
      if (parts.length !== 4) {
        throw new Error(
          `Invalid runs file line ${index + 1}: expected "<label> <owner/repo> <run-id> <blocking|advisory>"`,
        );
      }
      const [label, repo, runId, role] = parts;
      if (!/^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(label)) {
        throw new Error(`Invalid label on line ${index + 1}: ${label}`);
      }
      if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repo)) {
        throw new Error(`Invalid owner/repo on line ${index + 1}: ${repo}`);
      }
      if (!/^[0-9]+$/.test(runId)) {
        throw new Error(`Invalid run id on line ${index + 1}: ${runId}`);
      }
      if (role !== "blocking" && role !== "advisory") {
        throw new Error(
          `Invalid role on line ${index + 1}: expected blocking or advisory`,
        );
      }
      return { label, repo, runId, blocking: role === "blocking" };
    });
}

async function githubJson(pathname) {
  const token = process.env.GH_TOKEN || process.env.GITHUB_TOKEN || "";
  const headers = {
    Accept: "application/vnd.github+json",
    "User-Agent": "openclaw-release-evidence",
    "X-GitHub-Api-Version": "2022-11-28",
  };
  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }
  const response = await fetch(`https://api.github.com${pathname}`, { headers });
  const body = await response.text();
  if (!response.ok) {
    throw new Error(
      `GitHub API ${pathname} failed: ${response.status} ${response.statusText}\n${body}`,
    );
  }
  return body ? JSON.parse(body) : null;
}

async function githubPaged(pathname) {
  const pages = [];
  for (let page = 1; page <= 20; page += 1) {
    const separator = pathname.includes("?") ? "&" : "?";
    const payload = await githubJson(
      `${pathname}${separator}per_page=100&page=${page}`,
    );
    const values =
      payload?.jobs ??
      payload?.artifacts ??
      payload?.workflow_runs ??
      (Array.isArray(payload) ? payload : []);
    pages.push(...values);
    if (!Array.isArray(values) || values.length < 100) {
      break;
    }
  }
  return pages;
}

function runUrl(repo, runId) {
  return `https://github.com/${repo}/actions/runs/${runId}`;
}

function jobUrl(repo, runId, jobId) {
  return `${runUrl(repo, runId)}/job/${jobId}`;
}

function normalizeRun(run, entry, jobs, artifacts) {
  const normalizedJobs = jobs.map((job) => ({
    id: job.id,
    name: job.name,
    status: job.status,
    conclusion: job.conclusion,
    startedAt: job.started_at,
    completedAt: job.completed_at,
    htmlUrl: job.html_url || jobUrl(entry.repo, entry.runId, job.id),
  }));
  const normalizedArtifacts = artifacts.map((artifact) => ({
    id: artifact.id,
    name: artifact.name,
    sizeInBytes: artifact.size_in_bytes,
    expired: artifact.expired,
    createdAt: artifact.created_at,
    expiresAt: artifact.expires_at,
    archiveDownloadUrl: artifact.archive_download_url,
  }));
  return {
    label: entry.label,
    repo: entry.repo,
    runId: Number(entry.runId),
    blocking: entry.blocking,
    status: run.status,
    conclusion: run.conclusion,
    workflowName: run.name,
    event: run.event,
    headBranch: run.head_branch,
    headSha: run.head_sha,
    path: run.path,
    createdAt: run.created_at,
    updatedAt: run.updated_at,
    runStartedAt: run.run_started_at,
    htmlUrl: run.html_url || runUrl(entry.repo, entry.runId),
    jobs: normalizedJobs,
    artifacts: normalizedArtifacts,
  };
}

function statusIcon(run) {
  if (run.status !== "completed") {
    return "running";
  }
  if (run.conclusion === "success") {
    return "pass";
  }
  if (run.conclusion === "skipped") {
    return "skipped";
  }
  return "fail";
}

function summarize(runs) {
  const summary = {
    blockingPassed: 0,
    blockingFailed: 0,
    blockingSkipped: 0,
    blockingIncomplete: 0,
    advisoryPassed: 0,
    advisoryFailed: 0,
    advisorySkipped: 0,
    advisoryIncomplete: 0,
  };
  for (const run of runs) {
    const completed = run.status === "completed";
    const passed = completed && run.conclusion === "success";
    const keyPrefix = run.blocking ? "blocking" : "advisory";
    if (passed) {
      summary[`${keyPrefix}Passed`] += 1;
    } else if (completed && run.conclusion === "skipped") {
      summary[`${keyPrefix}Skipped`] += 1;
    } else if (completed) {
      summary[`${keyPrefix}Failed`] += 1;
    } else {
      summary[`${keyPrefix}Incomplete`] += 1;
    }
  }
  return summary;
}

function renderMarkdown(evidence, notes) {
  const lines = [];
  lines.push(`# OpenClaw Release Evidence: ${evidence.release.id}`);
  lines.push("");
  lines.push(`Generated: ${evidence.generatedAt}`);
  if (evidence.release.ref) {
    lines.push(`Release ref: \`${evidence.release.ref}\``);
  }
  if (evidence.release.packageSpec) {
    lines.push(`Package spec: \`${evidence.release.packageSpec}\``);
  }
  lines.push("");
  lines.push("## Summary");
  lines.push("");
  lines.push("| Class | Passed | Failed | Skipped | Incomplete |");
  lines.push("| --- | ---: | ---: | ---: | ---: |");
  lines.push(
    `| Blocking | ${evidence.summary.blockingPassed} | ${evidence.summary.blockingFailed} | ${evidence.summary.blockingSkipped} | ${evidence.summary.blockingIncomplete} |`,
  );
  lines.push(
    `| Advisory | ${evidence.summary.advisoryPassed} | ${evidence.summary.advisoryFailed} | ${evidence.summary.advisorySkipped} | ${evidence.summary.advisoryIncomplete} |`,
  );
  lines.push("");
  lines.push("## Runs");
  lines.push("");
  lines.push("| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |");
  lines.push("| --- | --- | --- | --- | --- | --- | --- | ---: |");
  for (const run of evidence.runs) {
    const sha = run.headSha ? `\`${run.headSha.slice(0, 12)}\`` : "";
    const ref = run.headBranch ? `\`${run.headBranch}\`` : "";
    lines.push(
      `| ${statusIcon(run)} | ${run.blocking ? "blocking" : "advisory"} | \`${run.label}\` | ${run.workflowName || ""} | ${ref} | ${sha} | [${run.runId}](${run.htmlUrl}) | ${run.artifacts.length} |`,
    );
  }
  const failed = evidence.runs.filter(
    (run) => run.status === "completed" && run.conclusion !== "success",
  );
  if (failed.length > 0) {
    lines.push("");
    lines.push("## Failures");
    lines.push("");
    for (const run of failed) {
      lines.push(`- \`${run.label}\`: ${run.conclusion} - ${run.htmlUrl}`);
      for (const job of run.jobs.filter((job) => {
        return (
          job.conclusion &&
          job.conclusion !== "success" &&
          job.conclusion !== "skipped"
        );
      })) {
        lines.push(`  - ${job.name}: ${job.conclusion} - ${job.htmlUrl}`);
      }
    }
  }
  if (notes.trim()) {
    lines.push("");
    lines.push("## Notes");
    lines.push("");
    lines.push(notes.trim());
  }
  lines.push("");
  lines.push("## Storage Policy");
  lines.push("");
  lines.push(
    "This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.",
  );
  lines.push("");
  return `${lines.join("\n")}\n`;
}

async function writeJson(filePath, value) {
  await fs.writeFile(filePath, `${JSON.stringify(value, null, 2)}\n`);
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const runsText = await fs.readFile(args.runsFile, "utf8");
  const runEntries = parseRunsFile(runsText);
  const notes = args.notesFile ? await fs.readFile(args.notesFile, "utf8") : "";

  const outputDir = path.join(args.outputRoot, args.releaseId);
  await fs.mkdir(path.join(outputDir, "runs"), { recursive: true });

  const runs = [];
  for (const entry of runEntries) {
    const [owner, repoName] = entry.repo.split("/");
    const run = await githubJson(
      `/repos/${owner}/${repoName}/actions/runs/${entry.runId}`,
    );
    const jobs = await githubPaged(
      `/repos/${owner}/${repoName}/actions/runs/${entry.runId}/jobs`,
    );
    const artifacts = await githubPaged(
      `/repos/${owner}/${repoName}/actions/runs/${entry.runId}/artifacts`,
    );
    const normalized = normalizeRun(run, entry, jobs, artifacts);
    runs.push(normalized);
    await writeJson(
      path.join(outputDir, "runs", `${entry.label}.json`),
      normalized,
    );
  }

  const evidence = {
    schemaVersion: 1,
    generatedAt: new Date().toISOString(),
    generatedBy: {
      repository: process.env.GITHUB_REPOSITORY || DEFAULT_PRIVATE_REPO,
      runId: process.env.GITHUB_RUN_ID ? Number(process.env.GITHUB_RUN_ID) : null,
      workflow: process.env.GITHUB_WORKFLOW || null,
    },
    release: {
      id: args.releaseId,
      ref: args.releaseRef,
      packageSpec: args.packageSpec,
    },
    sourceRepositories: [...new Set(runs.map((run) => run.repo))].sort(),
    summary: summarize(runs),
    runs,
  };

  await writeJson(path.join(outputDir, "release-evidence.json"), evidence);
  await fs.writeFile(
    path.join(outputDir, "release-evidence.md"),
    renderMarkdown(evidence, notes),
  );

  const index = {
    releaseId: args.releaseId,
    releaseRef: args.releaseRef,
    packageSpec: args.packageSpec,
    generatedAt: evidence.generatedAt,
    summary: evidence.summary,
    markdownPath: path.posix.join(outputDir, "release-evidence.md"),
    jsonPath: path.posix.join(outputDir, "release-evidence.json"),
  };
  await writeJson(path.join(outputDir, "index.json"), index);

  console.log(`Wrote ${outputDir}/release-evidence.md`);
  console.log(`Wrote ${outputDir}/release-evidence.json`);
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : error);
  process.exit(1);
});

#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import {
  githubBinary,
  githubJson,
  githubPaged,
  resolvePublicRelease,
  resolveReleaseRef,
  validateEvidenceDocument,
} from "./openclaw-release-evidence-contract.mjs";

const DEFAULT_EVIDENCE_REPO = "openclaw/releases";

function usage() {
  console.log(`Usage:
  node scripts/openclaw-release-evidence.mjs \\
    --release-id 2026.4.27-beta.1 \\
    --runs-file /tmp/runs.txt \\
    [--release-ref <tag-or-sha>] \\
    [--package-spec openclaw@2026.4.27-beta.1] \\
    [--notes-file /tmp/notes.md] \\
    [--full-validation-source-file /tmp/full-validation-source.json] \\
    [--output-root evidence]

Runs file format, one run per line:
  <label> <owner/repo> <run-id> <blocking|advisory>

Example:
  full-release-validation openclaw/openclaw 24972498713 blocking
  release-checks openclaw/openclaw 123456789 blocking
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
    fullValidationSourceFile: "",
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
      case "--full-validation-source-file":
        args.fullValidationSourceFile = next();
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
    throw new Error("--release-id must contain only letters, numbers, dot, underscore, or dash");
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
        throw new Error(`Invalid role on line ${index + 1}: expected blocking or advisory`);
      }
      return { label, repo, runId, blocking: role === "blocking" };
    });
}

async function npmJson(pathname) {
  const response = await fetch(`https://registry.npmjs.org${pathname}`, {
    headers: {
      Accept: "application/json",
      "User-Agent": "openclaw-release-evidence",
    },
  });
  const body = await response.text();
  if (!response.ok) {
    throw new Error(
      `npm registry ${pathname} failed: ${response.status} ${response.statusText}\n${body}`,
    );
  }
  return body ? JSON.parse(body) : null;
}

function parseOpenClawPackageSpec(spec) {
  const trimmed = spec.trim();
  if (!trimmed) {
    return { provided: false, packageName: "", selector: "", exactVersion: "" };
  }
  const match = trimmed.match(/^(@?[^@\s]+(?:\/[^@\s]+)?)@(.+)$/);
  if (!match) {
    return {
      provided: true,
      packageName: "",
      selector: "",
      exactVersion: "",
      error: "package spec must include a package name and selector",
    };
  }
  const [, packageName, selector] = match;
  const exactVersion = /^\d{4}\.\d+\.\d+(?:(?:-(?:alpha|beta)\.\d+)|(?:-\d+))?$/.test(selector) ? selector : "";
  return { provided: true, packageName, selector, exactVersion };
}

async function resolveNpmPackage(packageSpec) {
  const parsed = parseOpenClawPackageSpec(packageSpec);
  if (!parsed.provided) {
    return {
      provided: false,
      status: "not-recorded",
      note: "No package spec was recorded for this evidence run; npm release matching cannot be proven from this report.",
    };
  }
  if (parsed.error) {
    return { provided: true, status: "invalid", spec: packageSpec, error: parsed.error };
  }
  if (parsed.packageName !== "openclaw") {
    return {
      provided: true,
      status: "invalid",
      spec: packageSpec,
      packageName: parsed.packageName,
      selector: parsed.selector,
      error: "only openclaw package specs are supported",
    };
  }

  try {
    const encodedName = encodeURIComponent(parsed.packageName);
    const root = await npmJson(`/${encodedName}`);
    const encodedSelector = encodeURIComponent(parsed.selector);
    const versionPayload = await npmJson(`/${encodedName}/${encodedSelector}`);
    const resolvedVersion = versionPayload?.version || "";
    const distTags = root?.["dist-tags"] || {};
    const pointingTags = Object.entries(distTags)
      .filter(([, version]) => version === resolvedVersion)
      .map(([tag]) => tag)
      .sort();
    const expectedVersionMatches = !parsed.exactVersion || parsed.exactVersion === resolvedVersion;
    return {
      provided: true,
      status: "published",
      spec: packageSpec,
      packageName: parsed.packageName,
      selector: parsed.selector,
      expectedVersion: parsed.exactVersion || "",
      resolvedVersion,
      expectedVersionMatches,
      distTags,
      pointingTags,
      tarball: versionPayload?.dist?.tarball || "",
      integrity: versionPayload?.dist?.integrity || "",
      shasum: versionPayload?.dist?.shasum || "",
      gitHead: versionPayload?.gitHead || "",
      publishedAt: root?.time?.[resolvedVersion] || "",
    };
  } catch (error) {
    return {
      provided: true,
      status: "error",
      spec: packageSpec,
      packageName: parsed.packageName,
      selector: parsed.selector,
      expectedVersion: parsed.exactVersion || "",
      error: error instanceof Error ? error.message : String(error),
    };
  }
}

function buildProvenance(
  releaseRef,
  packageSpec,
  runs,
  npmPackage,
  publicRelease,
  fullValidation,
) {
  const releaseSha = releaseRef?.resolvedSha || "";
  const npmGitHead = npmPackage?.gitHead || "";
  const npmGitHeadMatchesReleaseRef =
    Boolean(releaseSha && npmGitHead) && releaseSha === npmGitHead;
  const npmGitHeadMatchesRun = npmGitHead
    ? runs.filter((run) => run.headSha === npmGitHead).map((run) => run.label)
    : [];
  return {
    releaseRef,
    npmPackage,
    publicRelease,
    fullValidation,
    npmGitHeadMatchesReleaseRef,
    npmGitHeadMatchesRun,
    packageSpecRecorded: Boolean(packageSpec.trim()),
  };
}

function runUrl(repo, runId) {
  return `https://github.com/${repo}/actions/runs/${runId}`;
}

function jobUrl(repo, runId, jobId) {
  return `${runUrl(repo, runId)}/job/${jobId}`;
}

function durationMs(startedAt, completedAt) {
  if (!startedAt || !completedAt) {
    return null;
  }
  const started = Date.parse(startedAt);
  const completed = Date.parse(completedAt);
  if (!Number.isFinite(started) || !Number.isFinite(completed) || completed < started) {
    return null;
  }
  return completed - started;
}

function formatDuration(ms) {
  if (!Number.isFinite(ms)) {
    return "";
  }
  const totalSeconds = Math.round(ms / 1000);
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  if (hours > 0) {
    return `${hours}h ${minutes}m ${seconds}s`;
  }
  if (minutes > 0) {
    return `${minutes}m ${seconds}s`;
  }
  return `${seconds}s`;
}

function normalizeRun(run, entry, jobs, artifacts) {
  const normalizedJobs = jobs.map((job) => ({
    id: job.id,
    name: job.name,
    status: job.status,
    conclusion: job.conclusion,
    startedAt: job.started_at,
    completedAt: job.completed_at,
    durationMs: durationMs(job.started_at, job.completed_at),
    queueDurationMs: durationMs(run.created_at, job.started_at),
    htmlUrl: job.html_url || jobUrl(entry.repo, entry.runId, job.id),
  }));
  const completedJobDurationMs = normalizedJobs
    .map((job) => job.durationMs)
    .filter(Number.isFinite);
  const totalJobDurationMs = completedJobDurationMs.reduce((sum, value) => sum + value, 0);
  const completedQueueDurationMs = normalizedJobs
    .map((job) => job.queueDurationMs)
    .filter(Number.isFinite);
  const maxQueueDurationMs =
    completedQueueDurationMs.length === 0 ? null : Math.max(...completedQueueDurationMs);
  const slowestJobs = normalizedJobs
    .filter((job) => Number.isFinite(job.durationMs))
    .toSorted((a, b) => b.durationMs - a.durationMs)
    .slice(0, 10)
    .map((job) => ({
      id: job.id,
      name: job.name,
      conclusion: job.conclusion,
      durationMs: job.durationMs,
      htmlUrl: job.htmlUrl,
    }));
  const longestQueues = normalizedJobs
    .filter((job) => Number.isFinite(job.queueDurationMs))
    .toSorted((a, b) => b.queueDurationMs - a.queueDurationMs)
    .slice(0, 10)
    .map((job) => ({
      id: job.id,
      name: job.name,
      conclusion: job.conclusion,
      durationMs: job.durationMs,
      queueDurationMs: job.queueDurationMs,
      htmlUrl: job.htmlUrl,
    }));
  const normalizedArtifacts = artifacts.map((artifact) => {
    const normalized = {
      id: artifact.id,
      name: artifact.name,
      sizeInBytes: artifact.size_in_bytes,
      expired: artifact.expired,
      createdAt: artifact.created_at,
      expiresAt: artifact.expires_at,
    };
    Object.defineProperty(normalized, "archiveDownloadUrl", {
      value: artifact.archive_download_url,
      enumerable: false,
    });
    return normalized;
  });
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
    durationMs: durationMs(run.run_started_at || run.created_at, run.updated_at),
    totalJobDurationMs,
    maxQueueDurationMs,
    slowestJobs,
    longestQueues,
    htmlUrl: run.html_url || runUrl(entry.repo, entry.runId),
    jobs: normalizedJobs,
    artifacts: normalizedArtifacts,
  };
}

async function readPreviousEvidence(filePath) {
  try {
    const raw = await fs.readFile(filePath, "utf8");
    return JSON.parse(raw);
  } catch (error) {
    if (error && error.code === "ENOENT") {
      return null;
    }
    throw error;
  }
}

function attachTimingDeltas(runs, previousEvidence) {
  if (!previousEvidence?.runs || !Array.isArray(previousEvidence.runs)) {
    return runs;
  }
  const previousRunsByLabel = new Map(previousEvidence.runs.map((run) => [run.label, run]));

  return runs.map((run) => {
    const previousRun = previousRunsByLabel.get(run.label);
    if (!previousRun) {
      return run;
    }

    const previousJobsByName = new Map(
      Array.isArray(previousRun.slowestJobs)
        ? previousRun.slowestJobs.map((job) => [job.name, job])
        : [],
    );
    const slowestJobs = run.slowestJobs.map((job) => {
      const previousJob = previousJobsByName.get(job.name);
      if (!Number.isFinite(previousJob?.durationMs) || !Number.isFinite(job.durationMs)) {
        return job;
      }
      return {
        ...job,
        previousDurationMs: previousJob.durationMs,
        durationDeltaMs: job.durationMs - previousJob.durationMs,
      };
    });

    const timingDelta = {};
    if (Number.isFinite(previousRun.durationMs) && Number.isFinite(run.durationMs)) {
      timingDelta.previousDurationMs = previousRun.durationMs;
      timingDelta.durationDeltaMs = run.durationMs - previousRun.durationMs;
    }
    if (
      Number.isFinite(previousRun.totalJobDurationMs) &&
      Number.isFinite(run.totalJobDurationMs)
    ) {
      timingDelta.previousTotalJobDurationMs = previousRun.totalJobDurationMs;
      timingDelta.totalJobDurationDeltaMs = run.totalJobDurationMs - previousRun.totalJobDurationMs;
    }

    return {
      ...run,
      timingDelta,
      slowestJobs,
    };
  });
}

function formatDurationDelta(ms) {
  if (!Number.isFinite(ms) || ms === 0) {
    return "0s";
  }
  const prefix = ms > 0 ? "+" : "-";
  return `${prefix}${formatDuration(Math.abs(ms))}`;
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

function isPerformanceRun(run) {
  return run.label === "product-performance" || run.workflowName === "OpenClaw Performance";
}

function formatMetric(valueToFormat, unit = "") {
  if (valueToFormat === null || valueToFormat === undefined || Number.isNaN(valueToFormat)) {
    return "";
  }
  const numeric = Number(valueToFormat);
  const rendered = Number.isFinite(numeric)
    ? numeric.toLocaleString("en-US", { maximumFractionDigits: numeric >= 100 ? 0 : 1 })
    : String(valueToFormat);
  return unit ? `${rendered} ${unit}` : rendered;
}

function metricValue(metric, field = "p95") {
  if (!metric) {
    return "";
  }
  const value = metric[field] ?? metric.median ?? metric.max ?? metric.mean;
  return formatMetric(value, metric.unit || "");
}

async function walkFiles(dir) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const child = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await walkFiles(child)));
    } else if (entry.isFile()) {
      files.push(child);
    }
  }
  return files;
}

async function readJsonFile(filePath) {
  return JSON.parse(await fs.readFile(filePath, "utf8"));
}

function laneFromArtifactName(name, runId) {
  const prefix = "openclaw-performance-";
  const suffix = `-${runId}`;
  if (!name.startsWith(prefix)) {
    return "";
  }
  const withoutPrefix = name.slice(prefix.length);
  const suffixIndex = withoutPrefix.indexOf(suffix);
  return suffixIndex === -1 ? withoutPrefix : withoutPrefix.slice(0, suffixIndex);
}

function summarizeKovaReport(report) {
  const groups = Array.isArray(report.performance?.groups) ? report.performance.groups : [];
  return {
    runId: report.runId || "",
    generatedAt: report.generatedAt || "",
    target: report.target || "",
    profile: report.profile || "",
    repeat: report.performance?.repeat ?? null,
    statuses: report.summary?.statuses || {},
    groups: groups.map((group) => ({
      key: group.key || "",
      scenario: group.scenario || "",
      state: group.state || "",
      title: group.title || "",
      sampleCount: group.sampleCount ?? null,
      statuses: group.statuses || {},
      metrics: {
        timeToHealthReadyMs: group.metrics?.timeToHealthReadyMs || null,
        timeToListeningMs: group.metrics?.timeToListeningMs || null,
        healthP95Ms: group.metrics?.healthP95Ms || null,
        peakRssMb: group.metrics?.peakRssMb || null,
        resourcePeakGatewayRssMb: group.metrics?.resourcePeakGatewayRssMb || null,
        cpuPercentMax: group.metrics?.cpuPercentMax || null,
        openclawEventLoopMaxMs: group.metrics?.openclawEventLoopMaxMs || null,
        agentTurnP95Ms: group.metrics?.agentTurnP95Ms || null,
        coldAgentTurnMs: group.metrics?.coldAgentTurnMs || null,
        warmAgentTurnMs: group.metrics?.warmAgentTurnMs || null,
        agentPreProviderP95Ms: group.metrics?.agentPreProviderP95Ms || null,
        agentProviderFinalP95Ms: group.metrics?.agentProviderFinalP95Ms || null,
        agentCleanupP95Ms: group.metrics?.agentCleanupP95Ms || null,
        runtimeDepsStagingMs: group.metrics?.runtimeDepsStagingMs || null,
      },
    })),
  };
}

function summarizeGatewayStartup(payload) {
  const results = Array.isArray(payload.results) ? payload.results : [];
  return {
    generatedAt: payload.generatedAt || "",
    cases: results.map((result) => ({
      id: result.id || "",
      name: result.name || "",
      sampleCount: Array.isArray(result.samples) ? result.samples.length : null,
      readyzMs: result.summary?.readyzMs || null,
      healthzMs: result.summary?.healthzMs || null,
      httpListenLogMs: result.summary?.httpListenLogMs || null,
      gatewayReadyLogMs: result.summary?.gatewayReadyLogMs || null,
      firstOutputMs: result.summary?.firstOutputMs || null,
      maxRssMb: result.summary?.maxRssMb || null,
      cpuCoreRatio: result.summary?.cpuCoreRatio || null,
    })),
  };
}

function summarizeCliStartup(payload) {
  return {
    node: payload.node || "",
    runs: payload.runs ?? null,
    cases: (payload.primary?.cases || []).map((testCase) => ({
      id: testCase.id || "",
      name: testCase.name || "",
      sampleCount: testCase.summary?.sampleCount ?? null,
      durationMs: testCase.summary?.durationMs || null,
      firstOutputMs: testCase.summary?.firstOutputMs || null,
      maxRssMb: testCase.summary?.maxRssMb || null,
      exitSummary: testCase.summary?.exitSummary || "",
    })),
  };
}

async function extractPerformanceArtifact(run, artifact) {
  const lane = laneFromArtifactName(artifact.name, run.runId);
  if (!lane || lane.includes("deep-profile")) {
    return null;
  }
  const tmpDir = await fs.mkdtemp(path.join(os.tmpdir(), "openclaw-performance-artifact-"));
  try {
    const zipPath = path.join(tmpDir, "artifact.zip");
    await fs.writeFile(zipPath, await githubBinary(artifact.archiveDownloadUrl));
    const extractDir = path.join(tmpDir, "extract");
    await fs.mkdir(extractDir);
    const unzip = spawnSync("unzip", ["-q", zipPath, "-d", extractDir], {
      encoding: "utf8",
    });
    if (unzip.status !== 0) {
      throw new Error(`unzip failed for ${artifact.name}: ${unzip.stderr || unzip.stdout}`);
    }

    const files = await walkFiles(extractDir);
    const reportPath = files.find((file) => {
      if (!file.endsWith(".json") || !file.includes(`${path.sep}kova${path.sep}reports${path.sep}`)) {
        return false;
      }
      return !file.endsWith(`${path.sep}bundle.json`);
    });
    const gatewayPath = files.find((file) =>
      file.endsWith(`${path.sep}gateway-cpu${path.sep}gateway-startup-bench.json`),
    );
    const cliPath = files.find((file) => file.endsWith(`${path.sep}cli-startup.json`));
    const sourceSummaryPath = files.find((file) =>
      file.endsWith(`${path.sep}gateway-cpu${path.sep}summary.json`),
    );

    const kova = reportPath ? summarizeKovaReport(await readJsonFile(reportPath)) : null;
    const gatewayStartup = gatewayPath
      ? summarizeGatewayStartup(await readJsonFile(gatewayPath))
      : null;
    const cliStartup = cliPath ? summarizeCliStartup(await readJsonFile(cliPath)) : null;
    const sourceSummary = sourceSummaryPath ? await readJsonFile(sourceSummaryPath) : null;

    return {
      lane,
      artifact: {
        id: artifact.id,
        name: artifact.name,
        sizeInBytes: artifact.sizeInBytes,
        expiresAt: artifact.expiresAt,
      },
      kova,
      source: {
        gatewayStartup,
        cliStartup,
        observations: sourceSummary?.observations || [],
      },
    };
  } finally {
    await fs.rm(tmpDir, { recursive: true, force: true });
  }
}

async function collectPerformanceMetrics(runs) {
  const performanceRuns = runs.filter(isPerformanceRun);
  const reports = [];
  for (const run of performanceRuns) {
    const laneReports = [];
    for (const artifact of run.artifacts) {
      if (!artifact.name.startsWith("openclaw-performance-") || artifact.expired) {
        continue;
      }
      try {
        const report = await extractPerformanceArtifact(run, artifact);
        if (report) {
          laneReports.push(report);
        }
      } catch (error) {
        laneReports.push({
          lane: laneFromArtifactName(artifact.name, run.runId) || artifact.name,
          artifact: {
            id: artifact.id,
            name: artifact.name,
            sizeInBytes: artifact.sizeInBytes,
            expiresAt: artifact.expiresAt,
          },
          error: error instanceof Error ? error.message : String(error),
        });
      }
    }
    reports.push({
      label: run.label,
      runId: run.runId,
      htmlUrl: run.htmlUrl,
      headSha: run.headSha,
      conclusion: run.conclusion,
      lanes: laneReports.toSorted((a, b) => a.lane.localeCompare(b.lane)),
    });
  }
  return reports;
}

function renderPerformanceMetrics(performance) {
  if (!Array.isArray(performance) || performance.length === 0) {
    return [];
  }

  const lines = [];
  lines.push("");
  lines.push("## Performance Metrics");
  lines.push("");
  for (const run of performance) {
    lines.push(`Run: [${run.runId}](${run.htmlUrl})`);
    lines.push("");
    for (const lane of run.lanes) {
      lines.push(`### ${lane.lane}`);
      lines.push("");
      if (lane.error) {
        lines.push(`- artifact parse error: ${lane.error.replace(/\s+/g, " ").trim()}`);
        lines.push("");
        continue;
      }

      if (lane.kova?.groups?.length) {
        lines.push("Kova summary:");
        lines.push("");
        lines.push("| Scenario | State | Samples | Health ready | Listen | Agent p95 | Cold | Warm | RSS | CPU |");
        lines.push("| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |");
        for (const group of lane.kova.groups) {
          const metrics = group.metrics || {};
          lines.push(
            `| ${group.scenario} | ${group.state} | ${group.sampleCount ?? ""} | ${metricValue(metrics.timeToHealthReadyMs)} | ${metricValue(metrics.timeToListeningMs)} | ${metricValue(metrics.agentTurnP95Ms)} | ${metricValue(metrics.coldAgentTurnMs)} | ${metricValue(metrics.warmAgentTurnMs)} | ${metricValue(metrics.peakRssMb)} | ${metricValue(metrics.cpuPercentMax)} |`,
          );
        }
        lines.push("");
      }

      const startupCases = lane.source?.gatewayStartup?.cases || [];
      if (startupCases.length) {
        lines.push("Gateway startup:");
        lines.push("");
        lines.push("| Case | Samples | readyz p50 | readyz p95 | health p50 | listen p50 | ready log p50 | RSS p95 | CPU core p95 |");
        lines.push("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |");
        for (const testCase of startupCases) {
          lines.push(
            `| ${testCase.id} | ${testCase.sampleCount ?? ""} | ${formatMetric(testCase.readyzMs?.p50, "ms")} | ${formatMetric(testCase.readyzMs?.p95, "ms")} | ${formatMetric(testCase.healthzMs?.p50, "ms")} | ${formatMetric(testCase.httpListenLogMs?.p50, "ms")} | ${formatMetric(testCase.gatewayReadyLogMs?.p50, "ms")} | ${formatMetric(testCase.maxRssMb?.p95, "MB")} | ${formatMetric(testCase.cpuCoreRatio?.p95, "cores")} |`,
          );
        }
        lines.push("");
      }

      const cliCases = lane.source?.cliStartup?.cases || [];
      if (cliCases.length) {
        lines.push("CLI startup:");
        lines.push("");
        lines.push("| Case | Samples | duration p50 | duration p95 | first output p50 | RSS p95 | Exit |");
        lines.push("| --- | ---: | ---: | ---: | ---: | ---: | --- |");
        for (const testCase of cliCases) {
          lines.push(
            `| ${testCase.id} | ${testCase.sampleCount ?? ""} | ${formatMetric(testCase.durationMs?.p50, "ms")} | ${formatMetric(testCase.durationMs?.p95, "ms")} | ${formatMetric(testCase.firstOutputMs?.p50, "ms")} | ${formatMetric(testCase.maxRssMb?.p95, "MB")} | ${testCase.exitSummary} |`,
          );
        }
        lines.push("");
      }
    }
  }
  return lines;
}

function renderMarkdown(evidence, notes) {
  const lines = [];
  lines.push(`# OpenClaw Release Evidence: ${evidence.release.id}`);
  lines.push("");
  lines.push(`Generated: ${evidence.generatedAt}`);
  lines.push("");
  lines.push("## Provenance");
  lines.push("");
  lines.push("| Field | Value |");
  lines.push("| --- | --- |");
  lines.push(`| Evidence id | \`${evidence.release.id}\` |`);
  lines.push(
    `| Release ref input | ${evidence.release.ref ? `\`${evidence.release.ref}\`` : "not recorded"} |`,
  );
  const releaseRef = evidence.provenance.releaseRef;
  lines.push(`| Release ref status | ${releaseRef.status || ""} |`);
  lines.push(`| Release ref kind | ${releaseRef.kind ? `\`${releaseRef.kind}\`` : "unknown"} |`);
  lines.push(`| Release ref name | ${releaseRef.name ? `\`${releaseRef.name}\`` : "unknown"} |`);
  lines.push(
    `| Release ref SHA | ${releaseRef.resolvedSha ? `\`${releaseRef.resolvedSha}\`` : "not resolved"} |`,
  );
  lines.push(
    `| Runs at release SHA | ${releaseRef.matchingRunLabels?.length ? releaseRef.matchingRunLabels.map((label) => `\`${label}\``).join(", ") : "none"} |`,
  );
  const npmPackage = evidence.provenance.npmPackage;
  lines.push(
    `| Package spec | ${evidence.release.packageSpec ? `\`${evidence.release.packageSpec}\`` : "not recorded"} |`,
  );
  lines.push(`| npm status | ${npmPackage.status || ""} |`);
  if (npmPackage.note) {
    lines.push(`| npm note | ${npmPackage.note} |`);
  }
  if (npmPackage.error) {
    lines.push(`| npm error | ${npmPackage.error.replace(/\s+/g, " ").trim()} |`);
  }
  if (npmPackage.resolvedVersion) {
    lines.push(`| npm resolved version | \`${npmPackage.resolvedVersion}\` |`);
  }
  if (npmPackage.expectedVersion) {
    lines.push(
      `| npm expected version match | ${npmPackage.expectedVersionMatches ? "yes" : "no"} |`,
    );
  }
  if (npmPackage.pointingTags?.length) {
    lines.push(
      `| npm dist-tags pointing here | ${npmPackage.pointingTags.map((tag) => `\`${tag}\``).join(", ")} |`,
    );
  }
  if (npmPackage.gitHead) {
    lines.push(`| npm gitHead | \`${npmPackage.gitHead}\` |`);
    lines.push(
      `| npm gitHead matches release ref | ${evidence.provenance.npmGitHeadMatchesReleaseRef ? "yes" : "no"} |`,
    );
    lines.push(
      `| Runs at npm gitHead | ${evidence.provenance.npmGitHeadMatchesRun.length ? evidence.provenance.npmGitHeadMatchesRun.map((label) => `\`${label}\``).join(", ") : "none"} |`,
    );
  } else if (npmPackage.status === "published") {
    lines.push("| npm gitHead | not recorded in npm metadata |");
  }
  if (npmPackage.publishedAt) {
    lines.push(`| npm published at | ${npmPackage.publishedAt} |`);
  }
  if (npmPackage.tarball) {
    lines.push(`| npm tarball | ${npmPackage.tarball} |`);
  }
  const publicRelease = evidence.provenance.publicRelease;
  lines.push(`| Public release status | ${publicRelease.status || ""} |`);
  if (publicRelease.htmlUrl) {
    lines.push(`| Public release | ${publicRelease.htmlUrl} |`);
  }
  if (publicRelease.publishedAt) {
    lines.push(`| Public release published at | ${publicRelease.publishedAt} |`);
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
  lines.push(
    "| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |",
  );
  lines.push("| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |");
  for (const run of evidence.runs) {
    const sha = run.headSha ? `\`${run.headSha.slice(0, 12)}\`` : "";
    const ref = run.headBranch ? `\`${run.headBranch}\`` : "";
    const durationDelta = run.timingDelta?.durationDeltaMs;
    const jobTimeDelta = run.timingDelta?.totalJobDurationDeltaMs;
    lines.push(
      `| ${statusIcon(run)} | ${run.blocking ? "blocking" : "advisory"} | \`${run.label}\` | ${run.workflowName || ""} | ${ref} | ${sha} | ${formatDuration(run.durationMs)}${Number.isFinite(durationDelta) ? ` (${formatDurationDelta(durationDelta)})` : ""} | ${formatDuration(run.totalJobDurationMs)}${Number.isFinite(jobTimeDelta) ? ` (${formatDurationDelta(jobTimeDelta)})` : ""} | ${formatDuration(run.maxQueueDurationMs)} | [${run.runId}](${run.htmlUrl}) | ${run.artifacts.length} |`,
    );
  }
  const slowestJobs = evidence.runs
    .flatMap((run) =>
      run.slowestJobs.map((job) => ({
        ...job,
        runLabel: run.label,
        runId: run.runId,
      })),
    )
    .toSorted((a, b) => b.durationMs - a.durationMs)
    .slice(0, 15);
  if (slowestJobs.length > 0) {
    lines.push("");
    lines.push("## Slowest Jobs");
    lines.push("");
    lines.push("| Duration | Run | Job | Result | Link |");
    lines.push("| ---: | --- | --- | --- | --- |");
    for (const job of slowestJobs) {
      lines.push(
        `| ${formatDuration(job.durationMs)} | \`${job.runLabel}\` | ${job.name} | ${job.conclusion || ""} | [job](${job.htmlUrl}) |`,
      );
    }
  }
  const longestQueues = evidence.runs
    .flatMap((run) =>
      (run.longestQueues ?? []).map((job) => ({
        ...job,
        runLabel: run.label,
        runId: run.runId,
      })),
    )
    .toSorted((a, b) => b.queueDurationMs - a.queueDurationMs)
    .slice(0, 15);
  if (longestQueues.length > 0) {
    lines.push("");
    lines.push("## Longest Queues");
    lines.push("");
    lines.push("| Queue | Duration | Run | Job | Result | Link |");
    lines.push("| ---: | ---: | --- | --- | --- | --- |");
    for (const job of longestQueues) {
      lines.push(
        `| ${formatDuration(job.queueDurationMs)} | ${formatDuration(job.durationMs)} | \`${job.runLabel}\` | ${job.name} | ${job.conclusion || ""} | [job](${job.htmlUrl}) |`,
      );
    }
  }
  const timingDeltas = evidence.runs
    .filter((run) => Number.isFinite(run.timingDelta?.durationDeltaMs))
    .toSorted(
      (a, b) => Math.abs(b.timingDelta.durationDeltaMs) - Math.abs(a.timingDelta.durationDeltaMs),
    );
  if (timingDeltas.length > 0) {
    lines.push("");
    lines.push("## Timing Changes");
    lines.push("");
    lines.push("| Run | Previous | Current | Delta | Job Time Delta |");
    lines.push("| --- | ---: | ---: | ---: | ---: |");
    for (const run of timingDeltas) {
      lines.push(
        `| \`${run.label}\` | ${formatDuration(run.timingDelta.previousDurationMs)} | ${formatDuration(run.durationMs)} | ${formatDurationDelta(run.timingDelta.durationDeltaMs)} | ${Number.isFinite(run.timingDelta.totalJobDurationDeltaMs) ? formatDurationDelta(run.timingDelta.totalJobDurationDeltaMs) : ""} |`,
      );
    }
  }
  lines.push(...renderPerformanceMetrics(evidence.performance));
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
        return job.conclusion && job.conclusion !== "success" && job.conclusion !== "skipped";
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
  const fullValidation = args.fullValidationSourceFile
    ? JSON.parse(await fs.readFile(args.fullValidationSourceFile, "utf8"))
    : null;

  const outputDir = path.join(args.outputRoot, args.releaseId);
  const runsDir = path.join(outputDir, "runs");
  await fs.mkdir(outputDir, { recursive: true });
  const previousEvidence = await readPreviousEvidence(
    path.join(outputDir, "release-evidence.json"),
  );

  const runs = [];
  for (const entry of runEntries) {
    const [owner, repoName] = entry.repo.split("/");
    const run = await githubJson(`/repos/${owner}/${repoName}/actions/runs/${entry.runId}`);
    const jobs = await githubPaged(
      `/repos/${owner}/${repoName}/actions/runs/${entry.runId}/jobs`,
      "jobs",
    );
    const artifacts = await githubPaged(
      `/repos/${owner}/${repoName}/actions/runs/${entry.runId}/artifacts`,
      "artifacts",
    );
    const normalized = normalizeRun(run, entry, jobs, artifacts);
    runs.push(normalized);
  }
  const runsWithDeltas = attachTimingDeltas(runs, previousEvidence);
  await fs.rm(runsDir, { recursive: true, force: true });
  await fs.mkdir(runsDir);
  for (const run of runsWithDeltas) {
    await writeJson(path.join(runsDir, `${run.label}.json`), run);
  }

  const evidence = {
    schemaVersion: 1,
    generatedAt: new Date().toISOString(),
    generatedBy: {
      repository: process.env.GITHUB_REPOSITORY || DEFAULT_EVIDENCE_REPO,
      runId: process.env.GITHUB_RUN_ID ? Number(process.env.GITHUB_RUN_ID) : null,
      workflow: process.env.GITHUB_WORKFLOW || null,
    },
    release: {
      id: args.releaseId,
      ref: args.releaseRef,
      packageSpec: args.packageSpec,
    },
    provenance: null,
    sourceRepositories: [...new Set(runsWithDeltas.map((run) => run.repo))].sort(),
    summary: summarize(runsWithDeltas),
    runs: runsWithDeltas,
  };
  const [npmPackage, releaseRef, publicRelease] = await Promise.all([
    resolveNpmPackage(args.packageSpec),
    resolveReleaseRef(args.releaseRef, runs),
    resolvePublicRelease(args.releaseRef),
  ]);
  evidence.provenance = buildProvenance(
    releaseRef,
    args.packageSpec,
    runs,
    npmPackage,
    publicRelease,
    fullValidation,
  );
  evidence.performance = await collectPerformanceMetrics(runsWithDeltas);
  validateEvidenceDocument(evidence, {
    releaseId: args.releaseId,
    releaseRef: args.releaseRef,
    packageSpec: args.packageSpec,
  }, { requireFullValidation: Boolean(fullValidation) });

  await writeJson(path.join(outputDir, "release-evidence.json"), evidence);
  await fs.writeFile(path.join(outputDir, "release-evidence.md"), renderMarkdown(evidence, notes));

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

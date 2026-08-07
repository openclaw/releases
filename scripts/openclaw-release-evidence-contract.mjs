#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
export const PUBLIC_REPO = "openclaw/openclaw";
const WORKFLOW = "Full Release Validation";
const WORKFLOW_PATH = ".github/workflows/full-release-validation.yml";
const SHA = /^[a-f0-9]{40}$/u;
const RUN_ID = /^[1-9][0-9]*$/u;
const VERSION =
  /^[0-9]{4}\.[0-9]+\.[0-9]+(?:(?:-(?:alpha|beta)\.[1-9][0-9]*)|(?:-[1-9][0-9]*))?$/u;
function headers() {
  const token = process.env.GH_TOKEN || process.env.GITHUB_TOKEN || "";
  return {
    Accept: "application/vnd.github+json",
    "User-Agent": "openclaw-release-evidence",
    "X-GitHub-Api-Version": "2022-11-28",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
  };
}
async function request(pathname, { binary = false, fetchImpl = fetch } = {}) {
  const url = pathname.startsWith("https://") ? pathname : `https://api.github.com${pathname}`;
  const response = await fetchImpl(url, { headers: headers() });
  const body = binary ? Buffer.from(await response.arrayBuffer()) : await response.text();
  if (!response.ok) {
    throw new Error(
      `GitHub API ${pathname} failed: ${response.status} ${response.statusText}${
        binary ? "" : `\n${body}`
      }`,
    );
  }
  return body;
}
export async function githubJson(pathname, options) {
  const body = await request(pathname, options);
  return body ? JSON.parse(body) : null;
}
async function githubJsonOrNull(pathname) {
  try {
    return await githubJson(pathname);
  } catch (error) {
    if (error instanceof Error && error.message.includes("failed: 404 ")) {
      return null;
    }
    throw error;
  }
}
export async function githubBinary(url) {
  return request(url, { binary: true });
}
export function workflowRunPath(repository, workflowRunId, runAttempt) {
  const normalizedRunId = runId(workflowRunId, "workflow run id");
  if (runAttempt === undefined || runAttempt === null || runAttempt === "") {
    return `/repos/${repository}/actions/runs/${normalizedRunId}`;
  }
  return `${workflowRunPath(repository, normalizedRunId)}/attempts/${runId(
    runAttempt,
    "workflow run attempt",
  )}`;
}
export function workflowRunJobsPath(repository, workflowRunId, runAttempt) {
  return `${workflowRunPath(repository, workflowRunId, runAttempt)}/jobs`;
}
export async function githubPaged(
  pathname,
  key,
  { fetchImpl = fetch, maxPages = 20 } = {},
) {
  const all = [];
  let total;
  for (let page = 1; page <= maxPages; page += 1) {
    const separator = pathname.includes("?") ? "&" : "?";
    const payload = await githubJson(
      `${pathname}${separator}per_page=100&page=${page}`,
      { fetchImpl },
    );
    const values = payload?.[key];
    if (!Array.isArray(values)) {
      throw new Error(`GitHub pagination payload ${pathname} is malformed`);
    }
    if (Number.isInteger(payload.total_count)) {
      total ??= payload.total_count;
      if (total !== payload.total_count) {
        throw new Error(`GitHub pagination total changed while reading ${pathname}`);
      }
    }
    all.push(...values);
    if (values.length < 100) {
      if (total !== undefined && all.length !== total) {
        throw new Error(`GitHub pagination for ${pathname} is incomplete: read ${all.length} of ${total}`);
      }
      return all;
    }
  }
  throw new Error(`GitHub pagination for ${pathname} exceeded ${maxPages} pages`);
}
export function validateReleaseIdentity({ releaseId, releaseRef, packageSpec }) {
  if (!VERSION.test(releaseId)) {
    throw new Error(`Release id must be an exact OpenClaw version: ${releaseId || "<missing>"}`);
  }
  if (packageSpec !== `openclaw@${releaseId}`) {
    throw new Error(`Package spec must be exact: expected openclaw@${releaseId}`);
  }
  if (!releaseRef?.trim() || releaseRef !== releaseRef.trim()) throw new Error("Release ref is invalid");
  const tag = releaseRef.replace(/^refs\/tags\//u, "");
  if (tag !== `v${releaseId}` && !SHA.test(releaseRef)) {
    throw new Error(`Release ref ${releaseRef} does not match release id ${releaseId}`);
  }
  return { releaseId, releaseRef, packageSpec };
}
async function resolvedObject(object) {
  if (object?.type !== "tag") {
    return { sha: object?.sha || "", type: object?.type || "" };
  }
  const tag = await githubJsonOrNull(`/repos/${PUBLIC_REPO}/git/tags/${object.sha}`);
  return { sha: tag?.object?.sha || object.sha, type: tag?.object?.type || "tag", tagSha: object.sha };
}
export async function resolveReleaseRef(releaseRef, runs = []) {
  const input = releaseRef.trim();
  if (SHA.test(input)) {
    const commit = await githubJsonOrNull(`/repos/${PUBLIC_REPO}/commits/${input}`);
    return {
      input, kind: "sha", name: input,
      status: commit ? "resolved" : "unverified-sha",
      resolvedSha: commit?.sha || input,
      matchingRunLabels: runs.filter((run) => run.headSha === input).map((run) => run.label),
    };
  }
  const name = input.replace(/^refs\/tags\//u, "");
  if (!name.startsWith("v")) {
    return { input, status: "not-found", matchingRunLabels: [] };
  }
  const ref = await githubJsonOrNull(`/repos/${PUBLIC_REPO}/git/ref/tags/${name}`);
  if (!ref) {
    return { input, status: "not-found", matchingRunLabels: [] };
  }
  const object = await resolvedObject(ref.object);
  return {
    input, kind: "tag", name, status: "resolved", ref: ref.ref || "",
    resolvedSha: object.sha, objectType: object.type, tagObjectSha: object.tagSha || "",
    matchingRunLabels: runs.filter((run) => run.headSha === object.sha).map((run) => run.label),
  };
}
export async function resolvePublicRelease(releaseRef) {
  const tag = releaseRef.replace(/^refs\/tags\//u, "");
  if (!tag.startsWith("v")) {
    return { status: "not-applicable", tag: "" };
  }
  let release;
  try {
    release = await githubJsonOrNull(`/repos/${PUBLIC_REPO}/releases/tags/${tag}`);
  } catch (error) {
    return { status: "error", tag, error: error instanceof Error ? error.message : String(error) };
  }
  return release
    ? {
        status: release.draft ? "draft" : "published", id: release.id,
        tag: release.tag_name,
        draft: Boolean(release.draft), prerelease: Boolean(release.prerelease),
        publishedAt: release.published_at || "", htmlUrl: release.html_url || "",
        assetCount: release.assets?.length ?? 0,
      }
    : { status: "not-found", tag };
}
function runId(value, label, optional = false) {
  const normalized = String(value ?? "");
  if (optional && !normalized) {
    return "";
  }
  if (!RUN_ID.test(normalized)) {
    throw new Error(`${label} is invalid`);
  }
  return normalized;
}
export function selectFullValidationArtifact(artifacts, parent) {
  const name = `full-release-validation-${parent.id}-${parent.run_attempt}`;
  const matches = artifacts.filter((artifact) => artifact.name === name);
  if (matches.length !== 1) {
    throw new Error(`Expected exactly one ${name} artifact, found ${matches.length}`);
  }
  const artifact = matches[0];
  if (artifact.expired) {
    throw new Error(`Full release validation artifact ${name} is expired`);
  }
  if (
    !RUN_ID.test(String(artifact.id ?? "")) ||
    artifact.workflow_run?.id !== parent.id ||
    artifact.workflow_run?.head_sha !== parent.head_sha ||
    artifact.workflow_run?.head_branch !== parent.head_branch ||
    !/^sha256:[a-f0-9]{64}$/u.test(artifact.digest ?? "") ||
    !artifact.archive_download_url
  ) {
    throw new Error(`Full release validation artifact ${name} identity is invalid`);
  }
  return artifact;
}
export function validateFullValidationManifest(value, parent) {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    throw new Error("Full release validation manifest must be an object");
  }
  for (const [key, expected] of Object.entries({
    version: "3",
    workflowName: WORKFLOW,
    runId: String(parent.id),
    runAttempt: String(parent.run_attempt),
    workflowRef: parent.head_branch,
    workflowSha: parent.head_sha,
    workflowFullRef: `refs/heads/${parent.head_branch}`,
    workflowRefType: "branch",
  })) {
    if (String(value[key] ?? "") !== expected) {
      throw new Error(`Full release validation manifest ${key} mismatch`);
    }
  }
  if (!SHA.test(value.targetSha ?? "")) {
    throw new Error("Full release validation manifest target SHA is invalid");
  }
  if (typeof value.childRuns?.productPerformance?.blocking !== "boolean") {
    throw new Error("Full release validation performance blocking flag is invalid");
  }
  const childRuns = {
    normalCi: runId(value.childRuns?.normalCi, "normal CI run id", true),
    pluginPrerelease: runId(value.childRuns?.pluginPrerelease, "plugin prerelease run id", true),
    releaseChecks: runId(value.childRuns?.releaseChecks, "release checks run id", true),
    npmTelegram: runId(value.childRuns?.npmTelegram, "npm Telegram run id", true),
    productPerformance: {
      runId: runId(value.childRuns?.productPerformance?.runId, "performance run id", true),
      blocking: value.childRuns.productPerformance.blocking,
      conclusion: String(value.childRuns?.productPerformance?.conclusion ?? ""),
    },
  };
  let evidenceReuse = null;
  if (value.evidenceReuse !== undefined) {
    const reuse = value.evidenceReuse;
    if (
      !["exact-target-full-validation-v1", "changelog-only-release-v1"].includes(reuse?.policy) ||
      !SHA.test(reuse?.evidenceSha ?? "") ||
      !Array.isArray(reuse?.changedPaths) ||
      reuse.changedPaths.some((entry) => typeof entry !== "string" || !entry) ||
      new Set(reuse.changedPaths).size !== reuse.changedPaths.length
    ) {
      throw new Error("Full release validation manifest evidence reuse is invalid");
    }
    evidenceReuse = {
      policy: reuse.policy, runId: runId(reuse.runId, "evidence reuse root run id"),
      selectedRunId: runId(reuse.selectedRunId, "evidence reuse selected run id"),
      evidenceSha: reuse.evidenceSha, changedPaths: reuse.changedPaths,
    };
  }
  return { ...value, version: 3, runId: String(value.runId), runAttempt: Number(value.runAttempt), childRuns, evidenceReuse };
}
async function readManifest(artifact) {
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), "openclaw-release-manifest-"));
  const zip = path.join(dir, "manifest.zip");
  try {
    const archive = await githubBinary(artifact.archive_download_url);
    if (`sha256:${createHash("sha256").update(archive).digest("hex")}` !== artifact.digest) {
      throw new Error("Full validation artifact digest does not match");
    }
    await fs.writeFile(zip, archive);
    const listing = spawnSync("unzip", ["-Z1", zip], { encoding: "utf8" });
    const entries = listing.stdout?.split(/\r?\n/u).filter(Boolean) ?? [];
    if (listing.status !== 0 || entries.filter((entry) => entry === "full-release-validation-manifest.json").length !== 1) {
      throw new Error("Full validation artifact must contain one root manifest");
    }
    const output = spawnSync("unzip", ["-p", zip, "full-release-validation-manifest.json"], {
      encoding: "utf8",
      maxBuffer: 2 * 1024 * 1024,
    });
    if (output.status !== 0) {
      throw new Error(`Could not read full validation manifest: ${output.stderr.trim()}`);
    }
    try {
      return JSON.parse(output.stdout);
    } catch {
      throw new Error("Full release validation manifest is malformed JSON");
    }
  } finally {
    await fs.rm(dir, { recursive: true, force: true });
  }
}
export async function loadFullValidationSource(input) {
  validateReleaseIdentity(input);
  const parent = await githubJson(
    workflowRunPath(PUBLIC_REPO, input.fullValidationRunId, input.fullValidationRunAttempt),
  );
  if (
    String(parent.id) !== String(input.fullValidationRunId) ||
    (input.fullValidationRunAttempt &&
      String(parent.run_attempt) !== String(input.fullValidationRunAttempt)) ||
    parent.name !== WORKFLOW ||
    parent.path?.split("@", 1)[0] !== WORKFLOW_PATH ||
    parent.event !== "workflow_dispatch" ||
    parent.status !== "completed" ||
    parent.conclusion !== "success" ||
    !Number.isInteger(parent.run_attempt) ||
    parent.run_attempt < 1 ||
    Number.isNaN(Date.parse(parent.updated_at ?? "")) ||
    !SHA.test(parent.head_sha ?? "")
  ) {
    throw new Error(`Full release validation run ${input.fullValidationRunId} is not successful`);
  }
  const artifacts = await githubPaged(
    `/repos/${PUBLIC_REPO}/actions/runs/${input.fullValidationRunId}/artifacts`,
    "artifacts",
  );
  const artifact = selectFullValidationArtifact(artifacts, parent);
  const manifest = validateFullValidationManifest(await readManifest(artifact), parent);
  if (
    parent.head_branch !== "main" &&
    !new RegExp(`^release-ci/${parent.head_sha.slice(0, 12)}-[1-9][0-9]*$`, "u").test(parent.head_branch ?? "")
  ) {
    throw new Error(`Full validation workflow branch ${parent.head_branch} is untrusted`);
  }
  const comparison = await githubJson(`/repos/${PUBLIC_REPO}/compare/${manifest.workflowSha}...main`);
  if (!["ahead", "identical"].includes(comparison?.status) || comparison?.merge_base_commit?.sha !== manifest.workflowSha) {
    throw new Error(`Full validation workflow SHA ${manifest.workflowSha} is not on current main`);
  }
  const resolvedRef = await resolveReleaseRef(input.releaseRef);
  if (resolvedRef.status !== "resolved" || resolvedRef.resolvedSha !== manifest.targetSha) {
    throw new Error(`Release ref ${input.releaseRef} does not resolve to validation target ${manifest.targetSha}`);
  }
  return {
    parentRun: {
      repo: PUBLIC_REPO, runId: String(parent.id), runAttempt: parent.run_attempt,
      workflowName: parent.name, workflowPath: parent.path,
      workflowRef: parent.head_branch, workflowSha: parent.head_sha,
      status: parent.status, conclusion: parent.conclusion, updatedAt: parent.updated_at,
      htmlUrl: parent.html_url,
    },
    artifact: {
      id: String(artifact.id), name: artifact.name, digest: artifact.digest,
      sizeInBytes: artifact.size_in_bytes, expiresAt: artifact.expires_at,
    },
    manifest,
    releaseIdentity: {
      releaseId: input.releaseId, releaseRef: input.releaseRef, packageSpec: input.packageSpec,
      resolvedSha: resolvedRef.resolvedSha,
    },
  };
}
export function fullValidationRunEntries(source) {
  const child = source.manifest.childRuns;
  const entries = [
    { label: "full-release-validation", runId: source.parentRun.runId, blocking: false,
      runAttempt: source.parentRun.runAttempt, headSha: source.parentRun.workflowSha,
      updatedAt: source.parentRun.updatedAt, workflowPath: WORKFLOW_PATH },
    // Manifest v3 only qualifies the parent attempt. Child attempt pinning needs an
    // additive upstream protocol field; do not infer it from mutable run state here.
    { label: "normal-ci", runId: child.normalCi, blocking: true, workflowPath: ".github/workflows/ci.yml" },
    { label: "plugin-prerelease", runId: child.pluginPrerelease, blocking: true,
      workflowPath: ".github/workflows/plugin-prerelease.yml" },
    { label: "release-checks", runId: child.releaseChecks, blocking: true,
      workflowPath: ".github/workflows/openclaw-release-checks.yml" },
    { label: "postpublish-telegram", runId: child.npmTelegram, blocking: true,
      workflowPath: ".github/workflows/npm-telegram-beta-e2e.yml" },
    { label: "product-performance", runId: child.productPerformance.runId,
      blocking: child.productPerformance.blocking,
      workflowPath: ".github/workflows/openclaw-performance.yml" },
  ]
    .filter((entry) => entry.runId)
    .map((entry) => ({ ...entry, repo: PUBLIC_REPO }));
  if (entries.length === 1) {
    entries[0].blocking = true;
  }
  return entries;
}
export function validateEvidenceDocument(value, expected, { requireFullValidation = false } = {}) {
  validateReleaseIdentity(expected);
  const schemaVersion = value?.schemaVersion ?? 1;
  if (schemaVersion !== 1 && schemaVersion !== 2) {
    throw new Error("Release evidence schema version is unsupported");
  }
  const requiresRunAttempt = schemaVersion >= 2;
  const runs = value?.runs;
  if (
    value?.release?.id !== expected.releaseId ||
    value?.release?.ref !== expected.releaseRef ||
    value?.release?.packageSpec !== expected.packageSpec ||
    value.provenance?.releaseRef?.status !== "resolved" ||
    !SHA.test(value.provenance.releaseRef.resolvedSha ?? "") ||
    !Array.isArray(runs) ||
    runs.length === 0 ||
    runs.some((run) =>
      !run || typeof run.label !== "string" || !run.label ||
      typeof run.repo !== "string" || !run.repo.includes("/") ||
      !RUN_ID.test(String(run.runId ?? "")) ||
      (requiresRunAttempt && !RUN_ID.test(String(run.runAttempt ?? ""))) ||
      typeof run.blocking !== "boolean") ||
    new Set(runs.map((run) => run.label)).size !== runs.length
  ) {
    throw new Error("Release evidence identity does not match");
  }
  const source = value.provenance?.fullValidation;
  if (requireFullValidation && !source) {
    throw new Error("Full validation evidence provenance is required");
  }
  if (
    source &&
    (source.releaseIdentity?.releaseId !== expected.releaseId ||
      source.releaseIdentity?.releaseRef !== expected.releaseRef ||
      source.releaseIdentity?.packageSpec !== expected.packageSpec ||
      source.releaseIdentity?.resolvedSha !== source.manifest?.targetSha ||
      source.parentRun?.runId !== source.manifest?.runId ||
      source.parentRun?.runAttempt !== source.manifest?.runAttempt ||
      source.parentRun?.workflowSha !== source.manifest?.workflowSha ||
      value.provenance?.releaseRef?.resolvedSha !== source.manifest?.targetSha)
  ) {
    throw new Error("Full validation evidence provenance is inconsistent");
  }
  if (source) {
    const manifest = validateFullValidationManifest(source.manifest, {
      id: Number(source.parentRun.runId), run_attempt: source.parentRun.runAttempt,
      head_branch: source.parentRun.workflowRef, head_sha: source.parentRun.workflowSha,
    });
    const expectedRuns = fullValidationRunEntries({ ...source, manifest });
    if (
      expectedRuns.length !== runs.length ||
      expectedRuns.some((entry) => !runs.some((run) =>
        run.label === entry.label && String(run.runId) === entry.runId &&
        (!requiresRunAttempt ||
          entry.runAttempt === undefined ||
          run.runAttempt === entry.runAttempt) &&
        (entry.headSha === undefined || run.headSha === entry.headSha) &&
        (entry.updatedAt === undefined || run.updatedAt === entry.updatedAt) &&
        run.repo === entry.repo && run.blocking === entry.blocking &&
        run.path?.split("@", 1)[0] === entry.workflowPath &&
        run.status === "completed" && run.conclusion === "success"))
    ) {
      throw new Error("Full validation evidence runs are inconsistent");
    }
  }
  return value;
}
export function classifyFullValidationUpdate(previousEvidence, source, expected) {
  const previousSource = previousEvidence?.provenance?.fullValidation;
  if (!previousSource) {
    return "update";
  }
  const previousRunId = String(previousSource.parentRun?.runId ?? "");
  const currentRunId = String(source.parentRun?.runId ?? "");
  if (previousRunId !== currentRunId) {
    return "update";
  }
  const previousAttempt = Number(previousSource.parentRun?.runAttempt);
  const currentAttempt = Number(source.parentRun?.runAttempt);
  if (!Number.isSafeInteger(previousAttempt) || previousAttempt < 1) {
    return "update";
  }
  if (!Number.isSafeInteger(currentAttempt) || currentAttempt < 1) {
    throw new Error("Full validation source attempt is invalid");
  }
  if (previousAttempt > currentAttempt) {
    throw new Error(
      `Refusing to replace Full Release Validation ${currentRunId} attempt ${previousAttempt} with stale attempt ${currentAttempt}`,
    );
  }
  if (previousAttempt === currentAttempt) {
    if (previousEvidence.schemaVersion !== 2) {
      return "update";
    }
    if (
      previousSource.parentRun?.workflowSha !== source.parentRun?.workflowSha ||
      previousSource.parentRun?.updatedAt !== source.parentRun?.updatedAt
    ) {
      throw new Error(
        `Full Release Validation ${currentRunId} attempt ${currentAttempt} identity changed`,
      );
    }
    try {
      validateEvidenceDocument(previousEvidence, expected, { requireFullValidation: true });
      return "duplicate";
    } catch {
      return "update";
    }
  }
  return "update";
}
async function cli() {
  if (process.argv[2] !== "verify-evidence") {
    throw new Error("Usage: openclaw-release-evidence-contract.mjs verify-evidence <file>");
  }
  const [file, releaseId, releaseRef, packageSpec, mode] = process.argv.slice(3);
  validateEvidenceDocument(JSON.parse(await fs.readFile(file, "utf8")),
    { releaseId, releaseRef, packageSpec },
    { requireFullValidation: mode === "--require-full-validation" });
  console.log(`Verified ${file}`);
}
if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  cli().catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exit(1);
  });
}

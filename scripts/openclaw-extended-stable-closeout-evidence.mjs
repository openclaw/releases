#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const PUBLIC_REPO = "openclaw/openclaw";
const CLOSEOUT_WORKFLOW_NAME = "OpenClaw NPM Extended-Stable Closeout";
const CLOSEOUT_WORKFLOW_PATH = ".github/workflows/openclaw-npm-extended-stable-closeout.yml";
const SNAPSHOT_FILE = "extended-stable-registry-snapshot.json";
const MAX_SNAPSHOT_BYTES = 128 * 1024;

function usage() {
  console.log(`Usage:
  node scripts/openclaw-extended-stable-closeout-evidence.mjs \\
    --release-id 2026.6.33 \\
    --release-ref v2026.6.33 \\
    --package-spec openclaw@2026.6.33 \\
    --closeout-run-id 123 \\
    --closeout-run-attempt 1 \\
    --artifact-name extended-stable-registry-snapshot-v2026.6.33 \\
    --artifact-digest sha256:<64-hex-digits> \\
    --artifact-dir /tmp/downloaded-artifact \\
    --plugin-run-id 120 \\
    --core-run-id 121 \\
    --full-validation-run-id 122 \\
    [--output-root evidence]
`);
}

function requiredValue(argv, index, flag) {
  if (index + 1 >= argv.length || argv[index + 1].startsWith("--")) {
    throw new Error(`Missing value for ${flag}`);
  }
  return argv[index + 1];
}

function parseArgs(argv) {
  const args = {
    outputRoot: "evidence",
    releaseId: "",
    releaseRef: "",
    packageSpec: "",
    closeoutRunId: "",
    closeoutRunAttempt: "",
    artifactName: "",
    artifactDigest: "",
    artifactDir: "",
    pluginRunId: "",
    coreRunId: "",
    fullValidationRunId: "",
  };
  const flags = {
    "--output-root": "outputRoot",
    "--release-id": "releaseId",
    "--release-ref": "releaseRef",
    "--package-spec": "packageSpec",
    "--closeout-run-id": "closeoutRunId",
    "--closeout-run-attempt": "closeoutRunAttempt",
    "--artifact-name": "artifactName",
    "--artifact-digest": "artifactDigest",
    "--artifact-dir": "artifactDir",
    "--plugin-run-id": "pluginRunId",
    "--core-run-id": "coreRunId",
    "--full-validation-run-id": "fullValidationRunId",
  };
  for (let index = 0; index < argv.length; index += 1) {
    const flag = argv[index];
    if (flag === "--help" || flag === "-h") {
      usage();
      process.exit(0);
    }
    const key = flags[flag];
    if (!key) {
      throw new Error(`Unknown argument: ${flag}`);
    }
    args[key] = requiredValue(argv, index, flag);
    index += 1;
  }
  for (const [key, value] of Object.entries(args)) {
    if (key !== "outputRoot" && !value) {
      throw new Error(`--${key.replace(/[A-Z]/g, (letter) => `-${letter.toLowerCase()}`)} is required`);
    }
  }
  if (!/^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(args.releaseId)) {
    throw new Error("--release-id must contain only letters, numbers, dot, underscore, or dash");
  }
  for (const key of ["closeoutRunId", "closeoutRunAttempt", "pluginRunId", "coreRunId", "fullValidationRunId"]) {
    if (!/^[1-9][0-9]*$/.test(args[key])) {
      throw new Error(`${key} must be a positive integer`);
    }
  }
  return args;
}

function normalizeDigest(value) {
  const digest = value.toLowerCase();
  return digest.startsWith("sha256:") ? digest : `sha256:${digest}`;
}

function requireSha256Digest(value, label) {
  const digest = normalizeDigest(value);
  if (!/^sha256:[0-9a-f]{64}$/.test(digest)) {
    throw new Error(`${label} must be a SHA-256 digest`);
  }
  return digest;
}

function assertExactKeys(value, keys, label) {
  const actual = Object.keys(value).sort();
  const expected = [...keys].sort();
  if (JSON.stringify(actual) !== JSON.stringify(expected)) {
    throw new Error(`${label} must contain exactly: ${expected.join(", ")}`);
  }
}

function parseFinalVersion(value, label) {
  const match = /^(\d{4})\.([1-9]|1[0-2])\.([1-9]\d*)$/.exec(value);
  if (!match) {
    throw new Error(`${label} must be an exact YYYY.M.PATCH version`);
  }
  const patch = Number(match[3]);
  if (!Number.isSafeInteger(patch)) {
    throw new Error(`${label} patch must be a positive safe integer`);
  }
  return { year: Number(match[1]), month: Number(match[2]), patch };
}

function validateLatest(value) {
  const match = /^(\d{4})\.([1-9]|1[0-2])\.([1-9]\d*)(?:-([1-9]\d*))?$/.exec(value);
  if (!match) {
    throw new Error("snapshot latest must be a stable final or numeric correction release");
  }
  const month = Number(match[2]);
  const patch = Number(match[3]);
  const correction = match[4] === undefined ? undefined : Number(match[4]);
  if (
    !Number.isSafeInteger(patch) ||
    patch >= 33 ||
    (correction !== undefined && !Number.isSafeInteger(correction))
  ) {
    throw new Error("snapshot latest must have a valid month and base patch below 33");
  }
  return { year: Number(match[1]), month, patch };
}

function validatePackageEntries(entries, expectedNames, version, label) {
  if (!Array.isArray(entries)) {
    throw new Error(`snapshot ${label} must be an array`);
  }
  const names = entries.map((entry, index) => {
    if (!entry || typeof entry !== "object" || Array.isArray(entry)) {
      throw new Error(`snapshot ${label}[${index}] must be an object`);
    }
    assertExactKeys(entry, ["packageName", "exact", "extendedStable"], `snapshot ${label}[${index}]`);
    if (
      typeof entry.packageName !== "string" ||
      !/^(@[a-z0-9._-]+\/[a-z0-9._-]+|[a-z0-9._-]+)$/.test(entry.packageName)
    ) {
      throw new Error(`snapshot ${label}[${index}] has an invalid packageName`);
    }
    if (entry.exact !== version || entry.extendedStable !== version) {
      throw new Error(`snapshot ${label}[${index}] does not resolve to ${version}`);
    }
    return entry.packageName;
  });
  if (new Set(names).size !== names.length) {
    throw new Error(`snapshot ${label} contains duplicate package names`);
  }
  if (JSON.stringify(names) !== JSON.stringify([...names].sort())) {
    throw new Error(`snapshot ${label} must be sorted by packageName`);
  }
  if (expectedNames && JSON.stringify(names) !== JSON.stringify([...expectedNames].sort())) {
    throw new Error(`snapshot ${label} must contain exactly ${expectedNames.join(" and ")}`);
  }
  return names;
}

export function validateSnapshotBuffer(buffer, context) {
  if (buffer.byteLength > MAX_SNAPSHOT_BYTES) {
    throw new Error(`snapshot exceeds ${MAX_SNAPSHOT_BYTES} bytes`);
  }
  let snapshot;
  try {
    snapshot = JSON.parse(buffer.toString("utf8"));
  } catch (error) {
    throw new Error(`snapshot is not valid JSON: ${error instanceof Error ? error.message : error}`);
  }
  if (!snapshot || typeof snapshot !== "object" || Array.isArray(snapshot)) {
    throw new Error("snapshot must be a JSON object");
  }
  assertExactKeys(snapshot, ["schemaVersion", "version", "corePackages", "latest", "plugins"], "snapshot");
  if (snapshot.schemaVersion !== 1) {
    throw new Error("snapshot schemaVersion must be 1");
  }
  const extendedStable = parseFinalVersion(snapshot.version, "snapshot version");
  if (extendedStable.patch < 33) {
    throw new Error("snapshot version patch must be at least 33");
  }
  const expectedRef = `v${snapshot.version}`;
  if (context.releaseId !== snapshot.version) {
    throw new Error(`release id must be ${snapshot.version}`);
  }
  const normalizedRef = context.releaseRef.replace(/^refs\/tags\//, "");
  if (normalizedRef !== expectedRef) {
    throw new Error(`release ref must be ${expectedRef}`);
  }
  if (context.packageSpec !== `openclaw@${snapshot.version}`) {
    throw new Error(`package spec must be openclaw@${snapshot.version}`);
  }
  if (context.artifactName !== `extended-stable-registry-snapshot-${expectedRef}`) {
    throw new Error(`artifact name must be extended-stable-registry-snapshot-${expectedRef}`);
  }
  const latest = validateLatest(snapshot.latest);
  if (
    latest.year < extendedStable.year ||
    (latest.year === extendedStable.year && latest.month <= extendedStable.month)
  ) {
    throw new Error("snapshot latest must be from a later calendar month than extended-stable");
  }
  validatePackageEntries(snapshot.corePackages, ["@openclaw/ai", "openclaw"], snapshot.version, "corePackages");
  const plugins = validatePackageEntries(snapshot.plugins, null, snapshot.version, "plugins");
  if (plugins.length === 0) {
    throw new Error("snapshot plugins must contain at least one package");
  }
  return snapshot;
}

export function validateCloseoutRun(run, context) {
  if (run.name !== CLOSEOUT_WORKFLOW_NAME) {
    throw new Error(`closeout run workflow must be ${CLOSEOUT_WORKFLOW_NAME}`);
  }
  if (run.path !== CLOSEOUT_WORKFLOW_PATH) {
    throw new Error(`closeout run path must be ${CLOSEOUT_WORKFLOW_PATH}`);
  }
  if (run.event !== "workflow_dispatch" || run.status !== "completed" || run.conclusion !== "success") {
    throw new Error("closeout run must be a completed successful workflow_dispatch run");
  }
  if (Number(run.run_attempt) !== Number(context.closeoutRunAttempt)) {
    throw new Error("closeout run attempt does not match the requested attempt");
  }
  if (Number(run.run_attempt) !== 1) {
    throw new Error("closeout evidence requires a first-attempt run; dispatch a fresh closeout run instead of rerunning");
  }
  if (run.head_sha !== context.releaseSha) {
    throw new Error("closeout run SHA does not match the release ref");
  }
  const expectedBranch = canonicalBranchForReleaseRef(context.releaseRef);
  if (run.head_branch !== expectedBranch) {
    throw new Error(`closeout run branch must be ${expectedBranch}`);
  }
}

function canonicalBranchForReleaseRef(releaseRef) {
  const tag = releaseRef.replace(/^refs\/tags\//, "");
  const version = parseFinalVersion(tag.replace(/^v/, ""), "release ref");
  return `extended-stable/${version.year}.${version.month}.33`;
}

export function validateRelatedRun(run, context) {
  const workflowNames = {
    plugin: "Plugin NPM Release",
    core: "OpenClaw NPM Release",
    validation: "Full Release Validation",
  };
  const workflowPaths = {
    plugin: ".github/workflows/plugin-npm-release.yml",
    core: ".github/workflows/openclaw-npm-release.yml",
    validation: ".github/workflows/full-release-validation.yml",
  };
  const workflowName = workflowNames[context.kind];
  if (!workflowName) {
    throw new Error(`unsupported related run kind: ${context.kind}`);
  }
  if (Number(run.id) !== Number(context.runId)) {
    throw new Error(`related ${context.kind} run id does not match the requested run`);
  }
  if (run.name !== workflowName) {
    throw new Error(`related ${context.kind} run workflow must be ${workflowName}`);
  }
  if (run.path !== workflowPaths[context.kind]) {
    throw new Error(`related ${context.kind} run path must be ${workflowPaths[context.kind]}`);
  }
  if (
    context.kind === "plugin" &&
    run.display_title !== `Plugin NPM Release [extended-stable] ${context.releaseSha}`
  ) {
    throw new Error("related plugin run display title does not match extended-stable and the release SHA");
  }
  if (run.event !== "workflow_dispatch" || run.status !== "completed") {
    throw new Error(`related ${context.kind} run must be a completed workflow_dispatch run`);
  }
  const allowedConclusions = context.kind === "core" ? new Set(["success", "failure"]) : new Set(["success"]);
  if (!allowedConclusions.has(run.conclusion)) {
    throw new Error(`related ${context.kind} run has disallowed conclusion ${run.conclusion ?? "<missing>"}`);
  }
  const expectedBranch = canonicalBranchForReleaseRef(context.releaseRef);
  if (run.head_branch !== expectedBranch || run.head_sha !== context.releaseSha) {
    throw new Error(`related ${context.kind} run does not match branch ${expectedBranch} and the release SHA`);
  }
}

export function validateFailedCoreRunJobs(jobs) {
  if (!Array.isArray(jobs) || jobs.length === 0) {
    throw new Error("failed core run validation requires its complete job list");
  }
  const allowedNonFailure = new Set(["success", "skipped"]);
  const failingJobs = jobs.filter((job) => job.conclusion === "failure");
  const publishJobs = jobs.filter((job) =>
    Array.isArray(job.steps) && job.steps.some((step) => step.name === "Publish"),
  );
  if (failingJobs.length !== 1 || publishJobs.length !== 1 || failingJobs[0] !== publishJobs[0]) {
    throw new Error("failed core run must contain exactly one failed publish job");
  }
  for (const job of jobs) {
    if (job !== publishJobs[0] && !allowedNonFailure.has(job.conclusion)) {
      throw new Error("every non-publish core job must be successful or skipped");
    }
  }
  const steps = jobs.flatMap((job) => (Array.isArray(job.steps) ? job.steps : []));
  const publishSteps = steps.filter((step) => step.name === "Publish");
  const readbackSteps = steps.filter(
    (step) => step.name === "Verify extended-stable registry readback",
  );
  if (
    publishSteps.length !== 1 ||
    publishSteps[0].conclusion !== "success" ||
    readbackSteps.length !== 1 ||
    readbackSteps[0].conclusion !== "failure"
  ) {
    throw new Error("failed core run requires publish success and one registry readback failure");
  }
  for (const step of steps) {
    if (step !== readbackSteps[0] && !allowedNonFailure.has(step.conclusion)) {
      throw new Error("every other core run step must be successful or skipped");
    }
  }
}

export function selectArtifact(artifacts, context) {
  const matches = artifacts.filter((artifact) => artifact.name === context.artifactName);
  if (matches.length !== 1) {
    throw new Error(`expected exactly one artifact named ${context.artifactName}`);
  }
  const artifact = matches[0];
  if (artifact.expired) {
    throw new Error("closeout snapshot artifact has expired");
  }
  if (
    requireSha256Digest(artifact.digest || "", "GitHub artifact digest") !==
    requireSha256Digest(context.artifactDigest, "requested artifact digest")
  ) {
    throw new Error("closeout snapshot artifact digest does not match GitHub metadata");
  }
  return artifact;
}

async function githubJson(pathname) {
  const token = process.env.GH_TOKEN || process.env.GITHUB_TOKEN || "";
  if (!token) {
    throw new Error("GH_TOKEN is required to verify closeout evidence");
  }
  const response = await fetch(`https://api.github.com${pathname}`, {
    headers: {
      Accept: "application/vnd.github+json",
      Authorization: `Bearer ${token}`,
      "User-Agent": "openclaw-extended-stable-closeout-evidence",
      "X-GitHub-Api-Version": "2022-11-28",
    },
  });
  const body = await response.text();
  if (!response.ok) {
    throw new Error(`GitHub API ${pathname} failed: ${response.status} ${response.statusText}\n${body}`);
  }
  return body ? JSON.parse(body) : null;
}

async function resolveReleaseSha(releaseRef) {
  const tag = releaseRef.replace(/^refs\/tags\//, "");
  if (!/^v\d{4}\.\d{1,2}\.\d+$/.test(tag)) {
    throw new Error("release ref must be an exact vYYYY.M.PATCH tag");
  }
  const ref = await githubJson(`/repos/${PUBLIC_REPO}/git/ref/tags/${encodeURIComponent(tag)}`);
  let object = ref?.object;
  if (object?.type === "tag") {
    const annotated = await githubJson(`/repos/${PUBLIC_REPO}/git/tags/${object.sha}`);
    object = annotated?.object;
  }
  if (!object?.sha || object.type !== "commit") {
    throw new Error(`release ref ${tag} does not resolve to a commit`);
  }
  return object.sha;
}

async function listFiles(root) {
  const entries = await fs.readdir(root, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const absolute = path.join(root, entry.name);
    if (entry.isSymbolicLink()) {
      throw new Error("artifact directory must not contain symbolic links");
    }
    if (entry.isDirectory()) {
      files.push(...(await listFiles(absolute)));
    } else if (entry.isFile()) {
      files.push(absolute);
    }
  }
  return files;
}

async function readSnapshotArtifact(artifactDir) {
  const files = await listFiles(artifactDir);
  if (files.length !== 1 || path.basename(files[0]) !== SNAPSHOT_FILE) {
    throw new Error(`artifact must contain exactly one file named ${SNAPSHOT_FILE}`);
  }
  return fs.readFile(files[0]);
}

function closeoutMetadata(args, run, artifact, snapshot) {
  const runUrl = `https://github.com/${PUBLIC_REPO}/actions/runs/${args.closeoutRunId}/attempts/${args.closeoutRunAttempt}`;
  return {
    version: snapshot.version,
    closeoutRun: {
      id: Number(args.closeoutRunId),
      attempt: Number(args.closeoutRunAttempt),
      url: run.html_url || runUrl,
    },
    artifact: {
      id: Number(artifact.id),
      name: artifact.name,
      digest: requireSha256Digest(args.artifactDigest, "artifact digest"),
    },
    relatedRuns: {
      pluginNpm: Number(args.pluginRunId),
      coreNpm: Number(args.coreRunId),
      fullReleaseValidation: Number(args.fullValidationRunId),
    },
  };
}

function renderMarkdownSection(metadata) {
  const runLink = (id) => `https://github.com/${PUBLIC_REPO}/actions/runs/${id}`;
  return [
    "<!-- extended-stable-closeout:start -->",
    "## Extended-Stable npm Closeout",
    "",
    `- Registry snapshot: [\`${SNAPSHOT_FILE}\`](./${SNAPSHOT_FILE})`,
    `- Closeout run: [${metadata.closeoutRun.id} attempt ${metadata.closeoutRun.attempt}](${metadata.closeoutRun.url})`,
    `- Plugin npm run: [${metadata.relatedRuns.pluginNpm}](${runLink(metadata.relatedRuns.pluginNpm)})`,
    `- Core npm run: [${metadata.relatedRuns.coreNpm}](${runLink(metadata.relatedRuns.coreNpm)})`,
    `- Full Release Validation run: [${metadata.relatedRuns.fullReleaseValidation}](${runLink(metadata.relatedRuns.fullReleaseValidation)})`,
    `- Snapshot artifact: \`${metadata.artifact.name}\` (\`${metadata.artifact.digest}\`)`,
    "<!-- extended-stable-closeout:end -->",
    "",
  ].join("\n");
}

function expectedIndexMetadata(metadata, releaseId) {
  return {
    ...metadata,
    snapshotPath: path.posix.join("evidence", releaseId, SNAPSHOT_FILE),
  };
}

function valuesEqual(left, right) {
  return JSON.stringify(left) === JSON.stringify(right);
}

function inspectMarkdownSection(markdown, expectedSection) {
  const start = "<!-- extended-stable-closeout:start -->";
  const end = "<!-- extended-stable-closeout:end -->";
  const startIndex = markdown.indexOf(start);
  const endIndex = markdown.indexOf(end);
  if (startIndex === -1 && endIndex === -1) {
    return "missing";
  }
  if (startIndex === -1 || endIndex === -1 || endIndex < startIndex) {
    throw new Error("release evidence markdown contains malformed extended-stable closeout metadata");
  }
  const afterEnd = endIndex + end.length;
  if (markdown.indexOf(start, startIndex + start.length) !== -1 || markdown.indexOf(end, afterEnd) !== -1) {
    throw new Error("release evidence markdown contains duplicate extended-stable closeout metadata");
  }
  if (markdown.slice(startIndex, afterEnd).trim() !== expectedSection.trim()) {
    throw new Error("release evidence markdown contains conflicting extended-stable closeout metadata");
  }
  return "present";
}

async function readJson(filePath) {
  return JSON.parse(await fs.readFile(filePath, "utf8"));
}

export async function persistSidecar({ outputRoot, releaseId, snapshot, metadata }) {
  const outputDir = path.join(outputRoot, releaseId);
  const sidecarPath = path.join(outputDir, SNAPSHOT_FILE);
  const indexPath = path.join(outputDir, "index.json");
  const markdownPath = path.join(outputDir, "release-evidence.md");
  const evidencePath = path.join(outputDir, "release-evidence.json");
  const [index, markdown] = await Promise.all([
    readJson(indexPath),
    fs.readFile(markdownPath, "utf8"),
    fs.access(evidencePath),
  ]);
  const canonical = `${JSON.stringify(snapshot, null, 2)}\n`;
  const nextCloseoutMetadata = expectedIndexMetadata(metadata, releaseId);
  const markdownSection = renderMarkdownSection(metadata);
  let sidecarExists = false;
  try {
    const existing = await fs.readFile(sidecarPath, "utf8");
    if (existing !== canonical) {
      throw new Error(`conflicting immutable sidecar already exists at ${sidecarPath}`);
    }
    sidecarExists = true;
  } catch (error) {
    if (error?.code !== "ENOENT") {
      throw error;
    }
  }

  if (
    index.extendedStableCloseout &&
    !valuesEqual(index.extendedStableCloseout, nextCloseoutMetadata)
  ) {
    throw new Error("index contains conflicting extended-stable closeout metadata");
  }
  const markdownState = inspectMarkdownSection(markdown, markdownSection);
  if (!sidecarExists && (index.extendedStableCloseout || markdownState === "present")) {
    throw new Error("closeout metadata exists without its immutable sidecar");
  }
  const indexComplete = Boolean(index.extendedStableCloseout);
  const markdownComplete = markdownState === "present";
  if (sidecarExists && indexComplete && markdownComplete) {
    return { status: "unchanged", sidecarPath };
  }
  const nextIndex = {
    ...index,
    extendedStableCloseout: nextCloseoutMetadata,
  };
  const nextMarkdown = markdownComplete ? markdown : `${markdown.trimEnd()}\n\n${markdownSection}`;

  if (!sidecarExists) {
    await fs.writeFile(sidecarPath, canonical, { flag: "wx" });
  }
  if (!indexComplete) {
    await fs.writeFile(indexPath, `${JSON.stringify(nextIndex, null, 2)}\n`);
  }
  if (!markdownComplete) {
    await fs.writeFile(markdownPath, nextMarkdown);
  }
  return { status: sidecarExists ? "recovered" : "written", sidecarPath };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const releaseSha = await resolveReleaseSha(args.releaseRef);
  const run = await githubJson(`/repos/${PUBLIC_REPO}/actions/runs/${args.closeoutRunId}`);
  validateCloseoutRun(run, { ...args, releaseSha });
  const artifactPayload = await githubJson(
    `/repos/${PUBLIC_REPO}/actions/runs/${args.closeoutRunId}/artifacts?per_page=100`,
  );
  const artifact = selectArtifact(artifactPayload?.artifacts || [], args);
  const relatedRunRequests = [
    ["plugin", args.pluginRunId],
    ["core", args.coreRunId],
    ["validation", args.fullValidationRunId],
  ];
  const relatedRuns = await Promise.all(
    relatedRunRequests.map(([, runId]) =>
      githubJson(`/repos/${PUBLIC_REPO}/actions/runs/${runId}`),
    ),
  );
  for (let index = 0; index < relatedRunRequests.length; index += 1) {
    const [kind, runId] = relatedRunRequests[index];
    validateRelatedRun(relatedRuns[index], {
      kind,
      runId,
      releaseRef: args.releaseRef,
      releaseSha,
    });
  }
  const coreRun = relatedRuns[1];
  if (coreRun.conclusion === "failure") {
    const jobsPayload = await githubJson(
      `/repos/${PUBLIC_REPO}/actions/runs/${args.coreRunId}/jobs?filter=latest&per_page=100`,
    );
    if (jobsPayload?.total_count !== jobsPayload?.jobs?.length) {
      throw new Error("failed core run job list is incomplete");
    }
    validateFailedCoreRunJobs(jobsPayload?.jobs || []);
  }
  const snapshotBuffer = await readSnapshotArtifact(args.artifactDir);
  const snapshot = validateSnapshotBuffer(snapshotBuffer, args);
  const metadata = closeoutMetadata(args, run, artifact, snapshot);
  const result = await persistSidecar({
    outputRoot: args.outputRoot,
    releaseId: args.releaseId,
    snapshot,
    metadata,
  });
  const verb =
    result.status === "written"
      ? "Wrote"
      : result.status === "recovered"
        ? "Recovered"
        : "Verified unchanged";
  console.log(`${verb} ${result.sidecarPath}`);
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exit(1);
  });
}

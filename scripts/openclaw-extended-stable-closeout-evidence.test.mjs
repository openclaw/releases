import assert from "node:assert/strict";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

import {
  persistSidecar,
  selectArtifact,
  validateCloseoutRun,
  validateFailedCoreRunJobs,
  validateRelatedRun,
  validateSnapshotBuffer,
} from "./openclaw-extended-stable-closeout-evidence.mjs";

function validSnapshot() {
  return {
    schemaVersion: 1,
    version: "2026.6.33",
    corePackages: [
      { packageName: "@openclaw/ai", exact: "2026.6.33", extendedStable: "2026.6.33" },
      { packageName: "openclaw", exact: "2026.6.33", extendedStable: "2026.6.33" },
    ],
    latest: "2026.7.4-1",
    plugins: [
      { packageName: "@openclaw/discord", exact: "2026.6.33", extendedStable: "2026.6.33" },
      { packageName: "@openclaw/slack", exact: "2026.6.33", extendedStable: "2026.6.33" },
    ],
  };
}

const snapshotContext = {
  releaseId: "2026.6.33",
  releaseRef: "v2026.6.33",
  packageSpec: "openclaw@2026.6.33",
  artifactName: "extended-stable-registry-snapshot-v2026.6.33",
};

function snapshotBuffer(value = validSnapshot()) {
  return Buffer.from(JSON.stringify(value));
}

test("accepts the compact sorted registry snapshot", () => {
  assert.deepEqual(validateSnapshotBuffer(snapshotBuffer(), snapshotContext), validSnapshot());
});

test("rejects snapshot identity mismatches", () => {
  assert.throws(
    () => validateSnapshotBuffer(snapshotBuffer(), { ...snapshotContext, releaseId: "release-2026.6.33" }),
    /release id must be/,
  );
  assert.throws(
    () => validateSnapshotBuffer(snapshotBuffer(), { ...snapshotContext, releaseRef: "v2026.6.34" }),
    /release ref must be/,
  );
  assert.throws(
    () => validateSnapshotBuffer(snapshotBuffer(), { ...snapshotContext, packageSpec: "openclaw@2026.6.34" }),
    /package spec must be/,
  );
  assert.throws(
    () => validateSnapshotBuffer(snapshotBuffer(), { ...snapshotContext, artifactName: "wrong" }),
    /artifact name must be/,
  );
});

test("rejects malformed, oversized, and semantically incomplete snapshots", () => {
  assert.throws(() => validateSnapshotBuffer(Buffer.from("{"), snapshotContext), /not valid JSON/);
  assert.throws(
    () => validateSnapshotBuffer(Buffer.alloc(128 * 1024 + 1, 32), snapshotContext),
    /exceeds 131072 bytes/,
  );
  const extra = { ...validSnapshot(), unexpected: true };
  assert.throws(() => validateSnapshotBuffer(snapshotBuffer(extra), snapshotContext), /must contain exactly/);
  const unsorted = validSnapshot();
  unsorted.plugins.reverse();
  assert.throws(() => validateSnapshotBuffer(snapshotBuffer(unsorted), snapshotContext), /must be sorted/);
  const emptyPlugins = { ...validSnapshot(), plugins: [] };
  assert.throws(() => validateSnapshotBuffer(snapshotBuffer(emptyPlugins), snapshotContext), /at least one/);
});

test("rejects extended-stable and latest versions outside the monthly contract", () => {
  const early = { ...validSnapshot(), version: "2026.6.32" };
  early.corePackages = early.corePackages.map((entry) => ({
    ...entry,
    exact: "2026.6.32",
    extendedStable: "2026.6.32",
  }));
  early.plugins = early.plugins.map((entry) => ({
    ...entry,
    exact: "2026.6.32",
    extendedStable: "2026.6.32",
  }));
  assert.throws(
    () =>
      validateSnapshotBuffer(snapshotBuffer(early), {
        releaseId: "2026.6.32",
        releaseRef: "v2026.6.32",
        packageSpec: "openclaw@2026.6.32",
        artifactName: "extended-stable-registry-snapshot-v2026.6.32",
      }),
    /patch must be at least 33/,
  );
  const sameMonth = { ...validSnapshot(), latest: "2026.6.4" };
  assert.throws(
    () => validateSnapshotBuffer(snapshotBuffer(sameMonth), snapshotContext),
    /later calendar month/,
  );
  const latePatch = { ...validSnapshot(), latest: "2026.7.33" };
  assert.throws(
    () => validateSnapshotBuffer(snapshotBuffer(latePatch), snapshotContext),
    /base patch below 33/,
  );
  for (const version of ["2026.06.33", "2026.6.0", `2026.6.${Number.MAX_SAFE_INTEGER}0`]) {
    const invalid = { ...validSnapshot(), version };
    assert.throws(
      () =>
        validateSnapshotBuffer(snapshotBuffer(invalid), {
          releaseId: version,
          releaseRef: `v${version}`,
          packageSpec: `openclaw@${version}`,
          artifactName: `extended-stable-registry-snapshot-v${version}`,
        }),
      /exact YYYY\.M\.PATCH|positive safe integer/,
    );
  }
  for (const latest of ["2026.07.2", "2026.7.0", "2026.7.2-0", `2026.7.${Number.MAX_SAFE_INTEGER}0`]) {
    assert.throws(
      () => validateSnapshotBuffer(snapshotBuffer({ ...validSnapshot(), latest }), snapshotContext),
      /stable final|positive safe integer|base patch below 33/,
    );
  }
});

test("validates exact closeout workflow identity", () => {
  const run = {
    name: "OpenClaw NPM Extended-Stable Closeout",
    path: ".github/workflows/openclaw-npm-extended-stable-closeout.yml",
    event: "workflow_dispatch",
    status: "completed",
    conclusion: "success",
    run_attempt: 1,
    head_sha: "a".repeat(40),
    head_branch: "extended-stable/2026.6.33",
  };
  const context = {
    releaseRef: "v2026.6.33",
    releaseSha: "a".repeat(40),
    closeoutRunAttempt: "1",
  };
  assert.doesNotThrow(() => validateCloseoutRun(run, context));
  assert.throws(
    () => validateCloseoutRun({ ...run, path: `${run.path}@refs/heads/main` }, context),
    /run path must be/,
  );
  assert.throws(
    () =>
      validateCloseoutRun(
        { ...run, run_attempt: 2 },
        { ...context, closeoutRunAttempt: "2" },
      ),
    /requires a first-attempt run/,
  );
  assert.throws(() => validateCloseoutRun({ ...run, event: "push" }, context), /workflow_dispatch/);
  assert.throws(
    () => validateCloseoutRun({ ...run, head_sha: "b".repeat(40) }, context),
    /SHA does not match/,
  );
  assert.throws(
    () => validateCloseoutRun({ ...run, head_branch: "main" }, context),
    /branch must be extended-stable\/2026\.6\.33/,
  );
});

test("binds related release runs to the exact workflow, branch, and SHA", () => {
  const context = {
    runId: "101",
    releaseRef: "v2026.6.33",
    releaseSha: "a".repeat(40),
  };
  const baseRun = {
    id: 101,
    event: "workflow_dispatch",
    status: "completed",
    conclusion: "success",
    head_branch: "extended-stable/2026.6.33",
    head_sha: "a".repeat(40),
  };
  const pluginRun = {
    ...baseRun,
    name: "Plugin NPM Release",
    path: ".github/workflows/plugin-npm-release.yml",
    display_title: `Plugin NPM Release [extended-stable] ${context.releaseSha}`,
  };
  const validationRun = {
    ...baseRun,
    name: "Full Release Validation",
    path: ".github/workflows/full-release-validation.yml",
  };
  const coreRun = {
    ...baseRun,
    name: "OpenClaw NPM Release",
    path: ".github/workflows/openclaw-npm-release.yml",
  };
  assert.doesNotThrow(() =>
    validateRelatedRun(pluginRun, { ...context, kind: "plugin" }),
  );
  assert.doesNotThrow(() =>
    validateRelatedRun(validationRun, { ...context, kind: "validation" }),
  );
  assert.doesNotThrow(() =>
    validateRelatedRun({ ...coreRun, conclusion: "failure" }, { ...context, kind: "core" }),
  );
  assert.throws(
    () => validateRelatedRun({ ...pluginRun, conclusion: "failure" }, { ...context, kind: "plugin" }),
    /disallowed conclusion/,
  );
  assert.throws(
    () => validateRelatedRun({ ...coreRun, head_branch: "main" }, { ...context, kind: "core" }),
    /does not match branch/,
  );
  assert.throws(
    () => validateRelatedRun({ ...coreRun, id: 102 }, { ...context, kind: "core" }),
    /run id does not match/,
  );
  assert.throws(
    () =>
      validateRelatedRun(
        { ...validationRun, head_sha: "b".repeat(40) },
        { ...context, kind: "validation" },
      ),
    /does not match branch/,
  );
  assert.throws(
    () => validateRelatedRun({ ...coreRun, path: pluginRun.path }, { ...context, kind: "core" }),
    /run path must be/,
  );
  assert.throws(
    () =>
      validateRelatedRun(
        { ...pluginRun, display_title: "Plugin NPM Release" },
        { ...context, kind: "plugin" },
      ),
    /display title does not match/,
  );
});

test("accepts only the bounded failed core publication shape", () => {
  const bounded = [
    {
      name: "preflight_openclaw_npm",
      conclusion: "skipped",
      steps: [],
    },
    {
      name: "publish_openclaw_npm",
      conclusion: "failure",
      steps: [
        { name: "Checkout", conclusion: "success" },
        { name: "Publish", conclusion: "success" },
        { name: "Verify extended-stable registry readback", conclusion: "failure" },
        { name: "Summarize extended-stable npm publication", conclusion: "success" },
        { name: "Post Setup", conclusion: "skipped" },
      ],
    },
  ];
  assert.doesNotThrow(() => validateFailedCoreRunJobs(bounded));
  assert.throws(
    () =>
      validateFailedCoreRunJobs([
        ...bounded,
        { name: "unexpected", conclusion: "timed_out", steps: [] },
      ]),
    /exactly one failed publish job|successful or skipped/,
  );
  assert.throws(
    () =>
      validateFailedCoreRunJobs([
        {
          ...bounded[1],
          steps: [
            { name: "Publish", conclusion: "success" },
            { name: "Verify extended-stable registry readback", conclusion: "failure" },
            { name: "Unrelated", conclusion: "cancelled" },
          ],
        },
      ]),
    /every other core run step/,
  );
  assert.throws(
    () =>
      validateFailedCoreRunJobs([
        {
          ...bounded[1],
          steps: [
            { name: "Publish", conclusion: "failure" },
            { name: "Verify extended-stable registry readback", conclusion: "failure" },
          ],
        },
      ]),
    /publish success/,
  );
});

test("requires one unexpired artifact with the exact GitHub digest", () => {
  const context = {
    artifactName: snapshotContext.artifactName,
    artifactDigest: `sha256:${"a".repeat(64)}`,
  };
  const artifact = {
    id: 42,
    name: snapshotContext.artifactName,
    digest: `sha256:${"a".repeat(64)}`,
    expired: false,
  };
  assert.equal(selectArtifact([artifact], context), artifact);
  assert.throws(
    () => selectArtifact([{ ...artifact, digest: `sha256:${"b".repeat(64)}` }], context),
    /digest does not match/,
  );
  assert.throws(() => selectArtifact([{ ...artifact, expired: true }], context), /expired/);
});

async function fixture() {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), "openclaw-closeout-evidence-"));
  const releaseId = "release-2026.6.33";
  const dir = path.join(root, releaseId);
  await fs.mkdir(path.join(dir, "runs"), { recursive: true });
  const evidence = { schemaVersion: 1, runs: [{ id: 1 }] };
  const index = { releaseId, markdownPath: `evidence/${releaseId}/release-evidence.md` };
  const markdown = "# Existing release evidence\n\nExisting Full Validation proof.\n";
  const runFile = '{"preserve":true}\n';
  await Promise.all([
    fs.writeFile(path.join(dir, "release-evidence.json"), `${JSON.stringify(evidence)}\n`),
    fs.writeFile(path.join(dir, "index.json"), `${JSON.stringify(index)}\n`),
    fs.writeFile(path.join(dir, "release-evidence.md"), markdown),
    fs.writeFile(path.join(dir, "runs", "full-release-validation.json"), runFile),
  ]);
  return { root, releaseId, dir, evidence, runFile };
}

function metadata(overrides = {}) {
  return {
    version: "2026.6.33",
    closeoutRun: { id: 100, attempt: 1, url: "https://github.com/openclaw/openclaw/actions/runs/100" },
    artifact: {
      id: 200,
      name: snapshotContext.artifactName,
      digest: `sha256:${"a".repeat(64)}`,
    },
    relatedRuns: { pluginNpm: 97, coreNpm: 98, fullReleaseValidation: 99 },
    ...overrides,
  };
}

test("writes an immutable sidecar and preserves existing Full Validation evidence", async () => {
  const state = await fixture();
  const result = await persistSidecar({
    outputRoot: state.root,
    releaseId: state.releaseId,
    snapshot: validSnapshot(),
    metadata: metadata(),
  });
  assert.equal(result.status, "written");
  assert.deepEqual(
    JSON.parse(await fs.readFile(path.join(state.dir, "extended-stable-registry-snapshot.json"), "utf8")),
    validSnapshot(),
  );
  assert.deepEqual(
    JSON.parse(await fs.readFile(path.join(state.dir, "release-evidence.json"), "utf8")),
    state.evidence,
  );
  assert.equal(
    await fs.readFile(path.join(state.dir, "runs", "full-release-validation.json"), "utf8"),
    state.runFile,
  );
  const index = JSON.parse(await fs.readFile(path.join(state.dir, "index.json"), "utf8"));
  assert.equal(
    index.extendedStableCloseout.snapshotPath,
    `evidence/${state.releaseId}/extended-stable-registry-snapshot.json`,
  );
  const markdown = await fs.readFile(path.join(state.dir, "release-evidence.md"), "utf8");
  assert.match(markdown, /Existing Full Validation proof/);
  assert.match(markdown, /Extended-Stable npm Closeout/);
});

test("identical replay is a no-op", async () => {
  const state = await fixture();
  const input = {
    outputRoot: state.root,
    releaseId: state.releaseId,
    snapshot: validSnapshot(),
    metadata: metadata(),
  };
  await persistSidecar(input);
  const indexBefore = await fs.readFile(path.join(state.dir, "index.json"), "utf8");
  const markdownBefore = await fs.readFile(path.join(state.dir, "release-evidence.md"), "utf8");
  const result = await persistSidecar(input);
  assert.equal(result.status, "unchanged");
  assert.equal(await fs.readFile(path.join(state.dir, "index.json"), "utf8"), indexBefore);
  assert.equal(await fs.readFile(path.join(state.dir, "release-evidence.md"), "utf8"), markdownBefore);
});

test("identical replay completes metadata after a sidecar-first partial write", async () => {
  const state = await fixture();
  await fs.writeFile(
    path.join(state.dir, "extended-stable-registry-snapshot.json"),
    `${JSON.stringify(validSnapshot(), null, 2)}\n`,
    { flag: "wx" },
  );
  const result = await persistSidecar({
    outputRoot: state.root,
    releaseId: state.releaseId,
    snapshot: validSnapshot(),
    metadata: metadata(),
  });
  assert.equal(result.status, "recovered");
  const index = JSON.parse(await fs.readFile(path.join(state.dir, "index.json"), "utf8"));
  assert.equal(index.extendedStableCloseout.closeoutRun.id, 100);
  assert.match(
    await fs.readFile(path.join(state.dir, "release-evidence.md"), "utf8"),
    /Extended-Stable npm Closeout/,
  );
  assert.deepEqual(
    JSON.parse(await fs.readFile(path.join(state.dir, "release-evidence.json"), "utf8")),
    state.evidence,
  );
  assert.equal(
    await fs.readFile(path.join(state.dir, "runs", "full-release-validation.json"), "utf8"),
    state.runFile,
  );
});

test("identical replay rejects conflicting index metadata without changing evidence", async () => {
  const state = await fixture();
  const input = {
    outputRoot: state.root,
    releaseId: state.releaseId,
    snapshot: validSnapshot(),
    metadata: metadata(),
  };
  await persistSidecar(input);
  const indexPath = path.join(state.dir, "index.json");
  const index = JSON.parse(await fs.readFile(indexPath, "utf8"));
  index.extendedStableCloseout.closeoutRun.id = 999;
  await fs.writeFile(indexPath, `${JSON.stringify(index, null, 2)}\n`);
  const before = await Promise.all([
    fs.readFile(indexPath, "utf8"),
    fs.readFile(path.join(state.dir, "release-evidence.md"), "utf8"),
    fs.readFile(path.join(state.dir, "release-evidence.json"), "utf8"),
  ]);
  await assert.rejects(persistSidecar(input), /index contains conflicting/);
  assert.deepEqual(
    await Promise.all([
      fs.readFile(indexPath, "utf8"),
      fs.readFile(path.join(state.dir, "release-evidence.md"), "utf8"),
      fs.readFile(path.join(state.dir, "release-evidence.json"), "utf8"),
    ]),
    before,
  );
});

test("conflicting replay fails without changing existing evidence", async () => {
  const state = await fixture();
  await persistSidecar({
    outputRoot: state.root,
    releaseId: state.releaseId,
    snapshot: validSnapshot(),
    metadata: metadata(),
  });
  const before = await Promise.all([
    fs.readFile(path.join(state.dir, "release-evidence.json"), "utf8"),
    fs.readFile(path.join(state.dir, "index.json"), "utf8"),
    fs.readFile(path.join(state.dir, "release-evidence.md"), "utf8"),
  ]);
  const conflicting = { ...validSnapshot(), latest: "2026.7.5" };
  await assert.rejects(
    persistSidecar({
      outputRoot: state.root,
      releaseId: state.releaseId,
      snapshot: conflicting,
      metadata: metadata(),
    }),
    /conflicting immutable sidecar/,
  );
  assert.deepEqual(
    await Promise.all([
      fs.readFile(path.join(state.dir, "release-evidence.json"), "utf8"),
      fs.readFile(path.join(state.dir, "index.json"), "utf8"),
      fs.readFile(path.join(state.dir, "release-evidence.md"), "utf8"),
    ]),
    before,
  );
});

test("workflow preserves generic evidence as the default and keeps closeout non-mutating", async () => {
  const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
  const workflow = await fs.readFile(
    path.join(root, ".github", "workflows", "openclaw-release-evidence.yml"),
    "utf8",
  );
  const closeoutScript = await fs.readFile(
    path.join(root, "scripts", "openclaw-extended-stable-closeout-evidence.mjs"),
    "utf8",
  );
  assert.match(workflow, /default: generic/);
  assert.match(workflow, /write_evidence:\n\s+if: inputs\.mode == 'generic'/);
  assert.match(workflow, /node scripts\/openclaw-release-evidence\.mjs/);
  assert.match(workflow, /write_extended_stable_closeout:\n\s+if: inputs\.mode == 'extended-stable-closeout'/);
  assert.match(
    workflow,
    /write_extended_stable_closeout:[\s\S]*?permissions:\n\s+actions: read\n\s+contents: read/,
  );
  assert.match(workflow, /closeout_run_attempt must be 1/);
  assert.doesNotMatch(`${workflow}\n${closeoutScript}`, /npm\s+(?:publish|dist-tag)/);
});

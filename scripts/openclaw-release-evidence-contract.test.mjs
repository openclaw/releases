import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";
import {
  classifyFullValidationUpdate,
  fullValidationRunEntries,
  githubPaged,
  selectFullValidationArtifact,
  validateEvidenceDocument,
  validateFullValidationManifest,
  validateReleaseIdentity,
  workflowRunJobsPath,
  workflowRunPath,
} from "./openclaw-release-evidence-contract.mjs";

const parentRun = {
  id: 30714067986,
  run_attempt: 1,
  head_branch: "release-ci/ebf121af6ab5-1785611218973",
  head_sha: "ebf121af6ab5036beda157722467ef5065ba58c3",
  updated_at: "2026-08-06T08:00:00Z",
};

const artifact = {
  id: 8822791237,
  name: "full-release-validation-30714067986-1",
  expired: false,
  digest: "sha256:4d46946273bb4645e6b7835d8e237bc350d2af8c40863b8381feeb2f1932f24c",
  archive_download_url: "https://api.github.test/artifacts/8822791237/zip",
  workflow_run: {
    id: parentRun.id,
    head_branch: parentRun.head_branch,
    head_sha: parentRun.head_sha,
  },
};

const manifest = {
  version: 3,
  workflowName: "Full Release Validation",
  runId: String(parentRun.id),
  runAttempt: String(parentRun.run_attempt),
  workflowRef: parentRun.head_branch,
  workflowSha: parentRun.head_sha,
  workflowFullRef: `refs/heads/${parentRun.head_branch}`,
  workflowRefType: "branch",
  targetRef: "dabe1915362e20c25704af91612a32a8f4c96e83",
  targetSha: "dabe1915362e20c25704af91612a32a8f4c96e83",
  releaseProfile: "beta",
  rerunGroup: "all",
  runReleaseSoak: "false",
  validationInputs: {},
  controls: { performanceBlocking: false },
  childRuns: {
    normalCi: "30709953877",
    pluginPrerelease: "30710364914",
    releaseChecks: "30710361061",
    npmTelegram: "",
    productPerformance: {
      runId: "30709954610",
      conclusion: "success",
      blocking: false,
    },
  },
  evidenceReuse: {
    policy: "changelog-only-release-v1",
    runId: "30709839350",
    selectedRunId: "30709839350",
    evidenceSha: "02d06caeb0febe7ec3c0df1454b85c38f3fb27d1",
    changedPaths: ["CHANGELOG.md"],
  },
};
const releaseIdentity = {
  releaseId: "2026.7.2-beta.7",
  releaseRef: "v2026.7.2-beta.7",
  packageSpec: "openclaw@2026.7.2-beta.7",
  resolvedSha: manifest.targetSha,
};

function persistedEvidence() {
  const evidence = {
    schemaVersion: 2,
    release: {
      id: releaseIdentity.releaseId,
      ref: releaseIdentity.releaseRef,
      packageSpec: releaseIdentity.packageSpec,
    },
    provenance: {
      releaseRef: { status: "resolved", resolvedSha: manifest.targetSha },
      fullValidation: {
        releaseIdentity,
        parentRun: {
          runId: String(parentRun.id),
          runAttempt: parentRun.run_attempt,
          workflowRef: parentRun.head_branch,
          workflowSha: parentRun.head_sha,
          updatedAt: parentRun.updated_at,
        },
        manifest: validateFullValidationManifest(manifest, parentRun),
      },
    },
    runs: [],
  };
  evidence.runs = fullValidationRunEntries(evidence.provenance.fullValidation).map((entry) => ({
    ...entry,
    runId: Number(entry.runId),
    runAttempt: entry.runAttempt ?? 1,
    path: `${entry.workflowPath}@refs/heads/main`,
    status: "completed",
    conclusion: "success",
  }));
  return evidence;
}

test("requires an exact package spec bound to the release id", () => {
  assert.equal(validateReleaseIdentity(releaseIdentity).releaseRef, releaseIdentity.releaseRef);
  assert.throws(
    () =>
      validateReleaseIdentity({
        releaseId: "2026.7.2-beta.7",
        releaseRef: "v2026.7.2-beta.7",
        packageSpec: "openclaw@beta",
      }),
    /Package spec must be exact/u,
  );
  for (const releaseRef of [" v2026.7.2-beta.7", "main", "v2026.7.2-beta.8"]) {
    assert.throws(
      () => validateReleaseIdentity({
        releaseId: "2026.7.2-beta.7",
        releaseRef,
        packageSpec: "openclaw@2026.7.2-beta.7",
      }),
      /Release ref/u,
    );
  }
});

test("selects one live attempt-qualified artifact", () => {
  assert.equal(selectFullValidationArtifact([artifact], parentRun), artifact);
  assert.throws(() => selectFullValidationArtifact([], parentRun), /Expected exactly one/u);
  assert.throws(() => selectFullValidationArtifact([artifact, { ...artifact }], parentRun), /found 2/u);
  assert.throws(() => selectFullValidationArtifact([{ ...artifact, expired: true }], parentRun), /expired/u);
  assert.throws(
    () =>
      selectFullValidationArtifact(
        [{ ...artifact, workflow_run: { ...artifact.workflow_run, head_sha: "0".repeat(40) } }],
        parentRun,
      ),
    /identity is invalid/u,
  );
});

test("builds exact-attempt workflow run and job API paths", () => {
  assert.equal(
    workflowRunPath("openclaw/openclaw", parentRun.id, parentRun.run_attempt),
    `/repos/openclaw/openclaw/actions/runs/${parentRun.id}/attempts/${parentRun.run_attempt}`,
  );
  assert.equal(
    workflowRunJobsPath("openclaw/openclaw", parentRun.id, parentRun.run_attempt),
    `/repos/openclaw/openclaw/actions/runs/${parentRun.id}/attempts/${parentRun.run_attempt}/jobs`,
  );
  assert.equal(
    workflowRunPath("other/repository", parentRun.id),
    `/repos/other/repository/actions/runs/${parentRun.id}`,
  );
  assert.equal(
    workflowRunJobsPath("other/repository", parentRun.id, 2),
    `/repos/other/repository/actions/runs/${parentRun.id}/attempts/2/jobs`,
  );
  assert.equal(
    workflowRunPath("openclaw/openclaw", parentRun.id),
    `/repos/openclaw/openclaw/actions/runs/${parentRun.id}`,
  );
});

test("validates parent, workflow, target, children, and reuse provenance", () => {
  const normalized = validateFullValidationManifest(manifest, parentRun);
  assert.equal(normalized.targetSha, manifest.targetSha);
  assert.equal(normalized.childRuns.releaseChecks, "30710361061");
  assert.deepEqual(normalized.evidenceReuse.changedPaths, ["CHANGELOG.md"]);
  assert.throws(
    () => validateFullValidationManifest({ ...manifest, runAttempt: "2" }, parentRun),
    /runAttempt mismatch/u,
  );
  assert.throws(
    () =>
      validateFullValidationManifest(
        {
          ...manifest,
          evidenceReuse: { ...manifest.evidenceReuse, changedPaths: ["CHANGELOG.md", "CHANGELOG.md"] },
        },
        parentRun,
      ),
    /evidence reuse is invalid/u,
  );
  assert.throws(
    () =>
      validateFullValidationManifest({
        ...manifest,
        childRuns: {
          ...manifest.childRuns,
          productPerformance: { ...manifest.childRuns.productPerformance, blocking: "false" },
        },
      }, parentRun),
    /performance blocking flag/u,
  );
});

test("rejects incomplete GitHub pagination", async () => {
  const fetchImpl = async (url) => {
    const page = Number(new URL(url).searchParams.get("page"));
    const jobs = page === 1 ? Array.from({ length: 100 }, (_, index) => ({ id: index })) : [];
    return new Response(JSON.stringify({ total_count: 101, jobs }), {
      status: 200,
      headers: { "content-type": "application/json" },
    });
  };
  await assert.rejects(
    githubPaged("/repos/openclaw/openclaw/actions/runs/1/jobs", "jobs", {
      fetchImpl,
    }),
    /incomplete: read 100 of 101/u,
  );
});

test("revalidates the persisted full-validation evidence identity", () => {
  const evidence = persistedEvidence();
  assert.equal(
    validateEvidenceDocument(evidence, releaseIdentity, { requireFullValidation: true }),
    evidence,
  );
  assert.throws(
    () =>
      validateEvidenceDocument(
        {
          ...evidence,
          provenance: {
            ...evidence.provenance,
            releaseRef: { status: "resolved", resolvedSha: "0".repeat(40) },
          },
        },
        releaseIdentity,
        { requireFullValidation: true },
      ),
    /provenance is inconsistent/u,
  );
  assert.throws(
    () =>
      validateEvidenceDocument(
        { ...evidence, provenance: { ...evidence.provenance, fullValidation: null } },
        releaseIdentity,
        { requireFullValidation: true },
      ),
    /provenance is required/u,
  );
  assert.throws(
    () =>
      validateEvidenceDocument(
        { ...evidence, runs: [{ ...evidence.runs[0], runId: 1 }] },
        releaseIdentity,
        { requireFullValidation: true },
      ),
    /runs are inconsistent/u,
  );
  assert.equal(
    validateEvidenceDocument(
      {
        ...evidence,
        schemaVersion: 1,
        runs: evidence.runs.map(({ runAttempt: _runAttempt, ...run }) => run),
      },
      releaseIdentity,
      { requireFullValidation: true },
    ).schemaVersion,
    1,
  );
});

test("deduplicates an exact attempt and rejects attempt rollback", () => {
  const evidence = persistedEvidence();
  const source = evidence.provenance.fullValidation;
  assert.equal(
    classifyFullValidationUpdate(evidence, source, releaseIdentity),
    "duplicate",
  );
  assert.equal(
    classifyFullValidationUpdate(
      {
        ...evidence,
        schemaVersion: 1,
        provenance: {
          ...evidence.provenance,
          fullValidation: {
            ...source,
            parentRun: {
              runId: source.parentRun.runId,
              runAttempt: source.parentRun.runAttempt,
              workflowRef: source.parentRun.workflowRef,
              workflowSha: source.parentRun.workflowSha,
            },
          },
        },
        runs: evidence.runs.map(({ runAttempt: _runAttempt, ...run }) => run),
      },
      source,
      releaseIdentity,
    ),
    "update",
  );
  assert.equal(
    classifyFullValidationUpdate(
      evidence,
      {
        ...source,
        parentRun: { ...source.parentRun, runAttempt: parentRun.run_attempt + 1 },
        manifest: { ...source.manifest, runAttempt: parentRun.run_attempt + 1 },
      },
      releaseIdentity,
    ),
    "update",
  );
  assert.throws(
    () =>
      classifyFullValidationUpdate(
        {
          ...evidence,
          provenance: {
            ...evidence.provenance,
            fullValidation: {
              ...source,
              parentRun: { ...source.parentRun, runAttempt: parentRun.run_attempt + 1 },
            },
          },
        },
        source,
        releaseIdentity,
      ),
    /stale attempt/u,
  );
});

test("release evidence workflows pin actions and verify the published tree", () => {
  for (const path of [
    "../.github/workflows/openclaw-release-evidence.yml",
    "../.github/workflows/openclaw-release-evidence-from-full-validation.yml",
  ]) {
    const workflow = readFileSync(new URL(path, import.meta.url), "utf8");
    for (const match of workflow.matchAll(/uses:\s+actions\/[^@\s]+@([^\s]+)/gu)) {
      assert.match(match[1], /^[0-9a-f]{40}$/u);
    }
    const verifies = [...workflow.matchAll(/verify-evidence/gu)].map((match) => match.index);
    assert.equal(verifies.length, 2);
    assert.ok(verifies[0] < workflow.indexOf('git add "${evidence_path}"'));
    assert.ok(verifies[1] > workflow.indexOf('git show "origin/main:${evidence_path}'));
    assert.match(workflow, /group: openclaw-release-evidence-\$\{/u);
    assert.match(workflow, /if: github\.ref == 'refs\/heads\/main'/u);
    assert.match(workflow, /environment: release-evidence/u);
    if (path.includes("from-full-validation")) {
      assert.match(workflow, /full_validation_run_attempt/u);
      assert.match(
        workflow,
        /repository_dispatch requires a positive full_validation_run_attempt/u,
      );
      assert.match(workflow, /--full-validation-run-attempt/u);
    }
    assert.match(workflow, /generated_tree="\$\(git write-tree\)"[\s\S]*git rev-parse "HEAD:\$\{evidence_path\}"/u);
    assert.match(workflow, /git rev-parse "origin\/main:\$\{evidence_path\}"/u);
  }
});

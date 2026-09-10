import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { chmodSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { delimiter, dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";
import { betaFloorTarget } from "../scripts/release-npm-beta-floor.mjs";

const SCRIPT = fileURLToPath(new URL("../scripts/release-npm-beta-floor.mjs", import.meta.url));

for (const [label, beta, expected] of [
  ["missing", undefined, "2026.9.3"],
  ["older same-train prerelease", "2026.9.3-beta.1", "2026.9.3"],
  ["older final", "2026.9.1", "2026.9.3"],
  ["equal", "2026.9.3", undefined],
  ["newer next-train prerelease", "2026.9.4-beta.1", undefined],
]) {
  test(label, () => {
    const tags = Object.freeze({
      latest: "2026.9.3",
      beta,
      alpha: "2026.9.5-alpha.1",
      "extended-stable": "2026.8.33",
    });
    assert.equal(betaFloorTarget(tags), expected);
  });
}

test("compares prerelease identifiers numerically and ignores build metadata", () => {
  assert.equal(
    betaFloorTarget({ latest: "2026.9.3-beta.10", beta: "2026.9.3-beta.9" }),
    "2026.9.3-beta.10",
  );
  assert.equal(betaFloorTarget({ latest: "2026.9.3+one", beta: "2026.9.3+two" }), undefined);
});

test("rejects malformed versions and skips packages with no latest", () => {
  assert.throws(
    () => betaFloorTarget({ latest: "2026.9.3", beta: "broken" }),
    /Invalid npm version/,
  );
  assert.throws(
    () => betaFloorTarget({ latest: "2026.9.3", beta: "2026.9.3-beta.01" }),
    /Invalid npm prerelease/,
  );
  assert.equal(betaFloorTarget({ beta: "2026.9.4-beta.1" }), undefined);
});

// Fake npm on PATH: serves dist-tags from a JSON state file in the npm 11 object
// shape or the npm 12 one-element array shape, records every invocation, and
// mutates state on `dist-tag add` unless the package is listed as failing or stale,
// and can serve a fixed number of stale reads after a mutation before converging.
const FAKE_NPM = `#!/usr/bin/env node
const fs = require("node:fs");
const state = JSON.parse(fs.readFileSync(process.env.FAKE_NPM_STATE, "utf8"));
const args = process.argv.slice(2);
fs.appendFileSync(process.env.FAKE_NPM_CALLS, args.join(" ") + "\\n");
if (args[0] === "view" && args[2] === "dist-tags" && args.includes("--json")) {
  let tags = state.registry[args[1]];
  const stale = (state.stale || {})[args[1]];
  if (stale && stale.remaining > 0) {
    stale.remaining -= 1;
    fs.writeFileSync(process.env.FAKE_NPM_STATE, JSON.stringify(state));
    tags = stale.tags;
  }
  if (!tags) {
    process.stdout.write(JSON.stringify({ error: { code: "E404", summary: "Not Found" } }));
    process.exit(1);
  }
  process.stdout.write(JSON.stringify(state.shape === "array" ? [tags] : tags));
  process.exit(0);
}
if (args[0] === "dist-tag" && args[1] === "add" && args[3] === "beta") {
  const at = args[2].lastIndexOf("@");
  const name = args[2].slice(0, at);
  if ((state.failAdd || []).includes(name)) {
    process.stderr.write("npm error code E403\\n");
    process.exit(1);
  }
  if (!(state.staleReadback || []).includes(name)) {
    if (state.staleReads) {
      state.stale = { ...(state.stale || {}), [name]: { remaining: state.staleReads, tags: { ...state.registry[name] } } };
    }
    state.registry[name].beta = args[2].slice(at + 1);
    fs.writeFileSync(process.env.FAKE_NPM_STATE, JSON.stringify(state));
  }
  process.exit(0);
}
process.stderr.write("unexpected npm invocation\\n");
process.exit(2);
`;

// Official inventory fixture: a bundledDist:false plugin, a plugin without the
// bundledDist key, a deferred (bundledDist:true) plugin, a core-only extension,
// and a directory without a manifest.
const OFFICIAL_MANIFESTS = {
  alpha: {},
  bravo: { openclaw: { release: { publishToNpm: true } } },
  deferred: { openclaw: { release: { publishToNpm: true }, build: { bundledDist: true } } },
  internal: { openclaw: {} },
  "no-manifest": null,
};

function runFloor({
  registry,
  shape = "object",
  failAdd,
  staleReadback,
  staleReads,
  manifests = OFFICIAL_MANIFESTS,
}) {
  const root = mkdtempSync(join(tmpdir(), "beta-floor-"));
  try {
    const bin = join(root, "bin");
    mkdirSync(bin);
    writeFileSync(join(bin, "npm"), FAKE_NPM);
    chmodSync(join(bin, "npm"), 0o755);
    const source = join(root, "source");
    for (const [name, extra] of Object.entries(manifests)) {
      const dir = join(source, "extensions", name);
      mkdirSync(dir, { recursive: true });
      if (extra === null) continue;
      writeFileSync(
        join(dir, "package.json"),
        JSON.stringify({
          name: `@openclaw/${name}`,
          version: "2026.9.3",
          openclaw: { release: { publishToNpm: true }, build: { bundledDist: false } },
          ...extra,
        }),
      );
    }
    const statePath = join(root, "state.json");
    writeFileSync(statePath, JSON.stringify({ registry, shape, failAdd, staleReadback, staleReads }));
    const callsPath = join(root, "calls.log");
    writeFileSync(callsPath, "");
    const result = { code: 0, stdout: "", stderr: "" };
    try {
      result.stdout = execFileSync(process.execPath, [SCRIPT, source], {
        encoding: "utf8",
        stdio: ["ignore", "pipe", "pipe"],
        env: {
          ...process.env,
          PATH: [bin, dirname(process.execPath), process.env.PATH].join(delimiter),
          FAKE_NPM_STATE: statePath,
          FAKE_NPM_CALLS: callsPath,
        },
      });
    } catch (error) {
      Object.assign(result, { code: error.status, stdout: error.stdout, stderr: error.stderr });
    }
    result.registry = JSON.parse(readFileSync(statePath, "utf8")).registry;
    result.calls = readFileSync(callsPath, "utf8").trim().split("\n").filter(Boolean);
    return result;
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
}

for (const shape of ["object", "array"]) {
  test(`advances only lagging betas across core and published plugins (npm ${shape} output)`, () => {
    const result = runFloor({
      shape,
      registry: {
        openclaw: { latest: "2026.9.3", beta: "2026.9.1" },
        "@openclaw/alpha": { latest: "2026.9.3", beta: "2026.9.4-beta.1" },
      },
    });
    assert.equal(result.code, 0, result.stderr);
    assert.equal(result.registry.openclaw.beta, "2026.9.3");
    assert.equal(result.registry["@openclaw/alpha"].beta, "2026.9.4-beta.1");
    assert.deepEqual(
      result.calls.filter((call) => call.startsWith("dist-tag ")),
      ["dist-tag add openclaw@2026.9.3 beta"],
    );
    assert.deepEqual(
      result.calls.filter((call) => /deferred|internal|no-manifest/.test(call)),
      [],
    );
    for (const line of [
      "@openclaw/alpha: beta=2026.9.4-beta.1 >= latest=2026.9.3; unchanged",
      "@openclaw/bravo: no published latest; skipped",
      "openclaw: beta 2026.9.1 -> 2026.9.3",
    ]) {
      assert.match(result.stdout, new RegExp(`^${line.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}$`, "m"));
    }
  });
}

test("keeps checking every package and reports all failures together", () => {
  const result = runFloor({
    failAdd: ["@openclaw/alpha"],
    registry: {
      openclaw: { beta: "2026.9.1" },
      "@openclaw/alpha": { latest: "2026.9.3", beta: "2026.9.1" },
    },
  });
  assert.equal(result.code, 1);
  assert.match(result.stderr, /^@openclaw\/alpha: /m);
  assert.match(result.stderr, /^openclaw: npm latest is missing\.$/m);
  assert.match(result.stdout, /^@openclaw\/bravo: no published latest; skipped$/m);
  assert.equal(result.registry["@openclaw/alpha"].beta, "2026.9.1");
});

test("waits for a lagging registry read to converge after the mutation", () => {
  const result = runFloor({
    staleReads: 2,
    registry: {
      openclaw: { latest: "2026.9.3", beta: "2026.9.1" },
      "@openclaw/alpha": { latest: "2026.9.3", beta: "2026.9.3" },
    },
  });
  assert.equal(result.code, 0, result.stderr);
  assert.equal(result.registry.openclaw.beta, "2026.9.3");
  assert.match(result.stdout, /^openclaw: beta 2026.9.1 -> 2026.9.3$/m);
  assert.equal(
    result.calls.filter((call) => call === "view openclaw dist-tags --json --prefer-online").length,
    4,
  );
});

test("fails when the registry does not converge after the mutation", () => {
  const result = runFloor({
    staleReadback: ["openclaw"],
    registry: {
      openclaw: { latest: "2026.9.3", beta: "2026.9.1" },
      "@openclaw/alpha": { latest: "2026.9.3", beta: "2026.9.3" },
    },
  });
  assert.equal(result.code, 1);
  assert.match(result.stderr, /^openclaw: beta floor did not converge after mutation\.$/m);
  assert.ok(result.calls.includes("dist-tag add openclaw@2026.9.3 beta"));
  assert.equal(
    result.calls.filter((call) => call === "view openclaw dist-tags --json --prefer-online").length,
    11,
  );
});

test("rejects an invalid publishable manifest before touching the registry", () => {
  const result = runFloor({
    manifests: { alpha: { private: true } },
    registry: { openclaw: { latest: "2026.9.3", beta: "2026.9.3" } },
  });
  assert.equal(result.code, 1);
  assert.match(result.stderr, /^Invalid publishable plugin manifest: alpha$/m);
  assert.deepEqual(result.calls, []);
});

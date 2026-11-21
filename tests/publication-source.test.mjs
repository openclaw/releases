import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { chmodSync, mkdtempSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { assessPublication, PUBLICATION_CONTEXT, requireStrictGate, validateMergeAdmission, validateSource } from "../scripts/publication-source.mjs";

const root = mkdtempSync(join(tmpdir(), "publication-source-"));
const git = (...args) => execFileSync("git", args, { cwd: root, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] }).trim();
git("init", "--initial-branch=main");
git("config", "user.name", "Fixture");
git("config", "user.email", "fixture@example.invalid");
git("config", "commit.gpgsign", "false");
mkdirSync(join(root, "evidence", "2026.11.1"), { recursive: true });
writeFileSync(join(root, "evidence/2026.11.1/release-evidence.json"), '{"before":true}\n');
writeFileSync(join(root, "outside.json"), '{"retained":true}\n');
git("add", ".");
git("commit", "-m", "Base");
const base = git("rev-parse", "HEAD");
writeFileSync(join(root, "evidence/2026.11.1/release-evidence.json"), '{"after":true}\n');
git("add", ".");
git("commit", "-m", "Candidate");
const head = git("rev-parse", "HEAD");
const tree = (ref) => ({ truncated: false, tree: git("ls-tree", "-r", "-t", ref).split("\n").map((line) => {
  const [metadata, path] = line.split("\t");
  const [mode, type, sha] = metadata.split(" ");
  return { mode, type, sha, path };
}) });
const key = createHash("sha1").update("blob 9\0" + "2026.11.1").digest("hex");
const branch = `automation/release-evidence/${key}-${git("rev-parse", "HEAD:evidence/2026.11.1")}-${base}`;
const fixture = () => ({ repository: "example/releases", expectedHead: head, main: base,
  pull: { state: "open", head: { sha: head, ref: branch, repo: { full_name: "example/releases" } },
    base: { ref: "main", sha: base, repo: { full_name: "example/releases" } } },
  commit: { sha: head, parents: [{ sha: base }] }, baseTree: tree(base), headTree: tree(head) });
test.after(() => rmSync(root, { recursive: true, force: true }));

test("accepts exact same-repository candidate from current base", () => {
  assert.equal(assessPublication(fixture()).sourceBase, base);
});

for (const [name, mutate, error] of [
  ["changed event head", (f) => { f.expectedHead = "a".repeat(40); }, /head changed/],
  ["closed PR", (f) => { f.pull.state = "closed"; }, /closed/],
  ["fork reserved branch", (f) => { f.pull.head.repo.full_name = "outsider/releases"; }, /belong/],
  ["malformed reserved branch", (f) => { f.pull.head.ref = "automation/release-evidence/custom"; }, /Invalid reserved/],
  ["base advance", (f) => { f.main = "b".repeat(40); }, /no longer current/],
  ["multiple parents", (f) => { f.commit.parents.push({ sha: base }); }, /one parent/],
  ["wrong recorded parent", (f) => { f.commit.parents[0].sha = "c".repeat(40); }, /one parent/],
  ["truncated tree", (f) => { f.headTree.truncated = true; }, /Incomplete/],
  ["wrong release key", (f) => { f.pull.head.ref = branch.replace(key, "d".repeat(40)); }, /Release ID/],
  ["wrong subtree", (f) => { f.headTree.tree.find((e) => e.path === "evidence/2026.11.1").sha = "e".repeat(40); }, /subtree/],
  ["outside deletion hidden by rename", (f) => {
    f.headTree.tree = f.headTree.tree.filter((e) => e.path !== "outside.json");
    f.headTree.tree.push({ path: "evidence/2026.11.1/moved.json", mode: "100644", type: "blob", sha: "f".repeat(40) });
  }, /outside/],
]) {
  test(`rejects ${name}`, () => { const f = fixture(); mutate(f); assert.throws(() => assessPublication(f), error); });
}

test("neutral admission reads only current PR identity for any branch", () => {
  for (const ref of ["fix/readme", branch, "automation/release-evidence/invalid"]) {
    const f = fixture(); f.pull.head.ref = ref; f.pull.head.repo.full_name = "fork/releases";
    const api = (path) => { assert.equal(path, "repos/example/releases/pulls/1"); return f.pull; };
    assert.equal(validateMergeAdmission(api, "example/releases", 1, head).description, "Current open pull request targeting main");
  }
});

function gateApi(change = () => {}) {
  const values = {
    "apps/github-actions": { id: 15368 },
    "repos/example/releases/rules/branches/main?per_page=100": [
      { type: "non_fast_forward", ruleset_id: 1 },
      { type: "required_status_checks", ruleset_id: 1, parameters: {
        strict_required_status_checks_policy: true,
        required_status_checks: [{ context: PUBLICATION_CONTEXT, integration_id: 15368 }],
      } },
    ],
    "repos/example/releases/rulesets/1?includes_parents=true": { enforcement: "active", bypass_actors: [] },
  };
  change(values);
  return (path) => { assert.ok(Object.hasOwn(values, path), path); return values[path]; };
}

test("requires the active strict Actions-bound context with no bypass", () => {
  requireStrictGate(gateApi(), "example/releases");
});
test("accepts documented redaction after administrator-owned activation", () => {
  requireStrictGate(gateApi((v) => {
    delete v["repos/example/releases/rulesets/1?includes_parents=true"].bypass_actors;
  }), "example/releases");
  requireStrictGate(gateApi((v) => {
    v["repos/example/releases/rulesets/1?includes_parents=true"].current_user_can_bypass = "never";
  }), "example/releases");
});
for (const [name, change] of [
  ["missing context", (v) => { v["repos/example/releases/rules/branches/main?per_page=100"] = []; }],
  ["non-strict context", (v) => { v["repos/example/releases/rules/branches/main?per_page=100"][1].parameters.strict_required_status_checks_policy = false; }],
  ["wrong app", (v) => { v["apps/github-actions"].id = 42; }],
  ["bypass", (v) => { v["repos/example/releases/rulesets/1?includes_parents=true"].bypass_actors = [{}]; }],
  ["malformed exposed bypass policy", (v) => { v["repos/example/releases/rulesets/1?includes_parents=true"].bypass_actors = null; }],
  ["current user bypass", (v) => { v["repos/example/releases/rulesets/1?includes_parents=true"].current_user_can_bypass = "always"; }],
  ["missing non-fast-forward rule", (v) => { v["repos/example/releases/rules/branches/main?per_page=100"].shift(); }],
  ["inactive rule", (v) => { v["repos/example/releases/rulesets/1?includes_parents=true"].enforcement = "disabled"; }],
]) {
  test(`refuses auto-merge for ${name}`, () => assert.throws(() => requireStrictGate(gateApi(change), "example/releases")));
}

test("re-reads the PR after metadata inspection before attesting", () => {
  const f = fixture(); let reads = 0;
  const api = (path) => {
    if (path.includes("/pulls/")) { const pull = structuredClone(f.pull); if (++reads > 1) pull.head.sha = "a".repeat(40); return pull; }
    if (path.endsWith("/git/ref/heads/main")) return { object: { sha: base } };
    if (path.endsWith(`/git/commits/${head}`)) return { ...f.commit, tree: { sha: "head-tree" } };
    if (path.endsWith(`/git/commits/${base}`)) return { tree: { sha: "base-tree" } };
    if (path.includes("head-tree")) return f.headTree;
    if (path.includes("base-tree")) return f.baseTree;
    return gateApi()(path);
  };
  assert.throws(() => validateSource(api, "example/releases", 1, head), /PR changed/);
});

test("obsolete PR events write no status; current events write only neutral admission", () => {
  const bin = join(root, "bin"); mkdirSync(bin);
  const cli = new URL("../scripts/publication-source.mjs", import.meta.url);
  const eventPath = join(root, "event.json"), pullPath = join(root, "pull.json"), callsPath = join(root, "calls.jsonl");
  writeFileSync(eventPath, JSON.stringify({ number: 1, pull_request: { head: { sha: head } } }));
  writeFileSync(join(bin, "gh"), `#!${process.execPath}\nconst fs = require("node:fs");
fs.appendFileSync(process.env.CALLS, JSON.stringify(process.argv.slice(2)) + "\\n");
console.log(process.argv[3].includes("/pulls/") ? fs.readFileSync(process.env.PULL, "utf8") : "{}");\n`);
  chmodSync(join(bin, "gh"), 0o755);
  for (const change of [
    (p) => { p.state = "closed"; },
    (p) => { p.head.sha = "a".repeat(40); },
    (p) => { p.base.ref = "other"; },
    (p) => { p.base.repo.full_name = "other/releases"; },
    () => {},
  ]) {
    const pull = fixture().pull; change(pull);
    writeFileSync(pullPath, JSON.stringify(pull)); writeFileSync(callsPath, "");
    execFileSync(process.execPath, [cli.pathname], { env: { ...process.env, PATH: `${bin}:${process.env.PATH}`,
      GITHUB_REPOSITORY: "example/releases", GITHUB_EVENT_PATH: eventPath, PULL: pullPath, CALLS: callsPath }, stdio: "pipe" });
    const calls = readFileSync(callsPath, "utf8").trim().split("\n").map(JSON.parse);
    const current = pull.state === "open" && pull.head.sha === head && pull.base.ref === "main" && pull.base.repo.full_name === "example/releases";
    assert.equal(calls.length, current ? 2 : 1);
    if (current) {
      assert.equal(calls[1][1], `repos/example/releases/statuses/${head}`);
      assert.ok(calls[1].includes(`context=${PUBLICATION_CONTEXT}`));
      assert.ok(calls[1].includes("state=success"));
    }
  }
});

test("PR target workflow executes only its trusted workflow revision", () => {
  const workflow = readFileSync(new URL("../.github/workflows/publication-source.yml", import.meta.url), "utf8");
  assert.match(workflow, /pull_request_target:/);
  assert.match(workflow, /ref: \$\{\{ github.workflow_sha \}\}/);
  assert.doesNotMatch(workflow, /pull_request.head|refs\/pull|npm |pnpm /);
  assert.doesNotMatch(workflow, /name: Publication merge admission/);
});

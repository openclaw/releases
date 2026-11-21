import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { pathToFileURL } from "node:url";

export const PUBLICATION_CONTEXT = "Publication merge admission";
const PREFIX = "automation/release-evidence/";

function requireCondition(value, message) {
  if (!value) throw new Error(message);
}

export function assessPublication({ repository, expectedHead, pull, main, commit, baseTree, headTree }) {
  requireCondition(pull.state === "open" && pull.head.sha === expectedHead, "PR closed or its head changed");
  requireCondition(pull.base.ref === "main" && pull.base.repo.full_name === repository, "Unexpected PR target");
  requireCondition(pull.head.repo?.full_name === repository, "Reserved publication branch must belong to this repository");
  const match = /^automation\/release-evidence\/([a-f0-9]{40})-([a-f0-9]{40})-([a-f0-9]{40})$/.exec(pull.head.ref);
  requireCondition(match, "Invalid reserved publication branch");
  const [, releaseKey, evidenceTree, sourceBase] = match;
  requireCondition(commit.sha === expectedHead && commit.parents.length === 1 && commit.parents[0].sha === sourceBase,
    "Publication must have one parent matching its recorded base");
  requireCondition(main === sourceBase && pull.base.sha === main, "Publication source base is no longer current");
  requireCondition(baseTree.truncated === false && headTree.truncated === false, "Incomplete Git tree response");
  const entries = (tree) => new Map(tree.tree.filter((entry) => entry.type !== "tree")
    .map((entry) => [entry.path, `${entry.mode}:${entry.type}:${entry.sha}`]));
  const before = entries(baseTree);
  const after = entries(headTree);
  // Compare path entries directly: rename detection must not hide an outside deletion.
  const changed = [...new Set([...before.keys(), ...after.keys()])].filter((path) => before.get(path) !== after.get(path));
  requireCondition(changed.length > 0, "Publication has no changed evidence");
  const directory = /^evidence\/([A-Za-z0-9][A-Za-z0-9._-]*)\//.exec(changed[0]);
  requireCondition(directory, "Publication changes a path outside release evidence");
  const releaseId = directory[1];
  const prefix = `evidence/${releaseId}/`;
  requireCondition(changed.every((path) => path.startsWith(prefix)), "Publication changes paths outside one release");
  const key = createHash("sha1").update(`blob ${Buffer.byteLength(releaseId)}\0${releaseId}`).digest("hex");
  requireCondition(key === releaseKey, "Release ID does not match the reserved branch");
  requireCondition(headTree.tree.some((entry) => entry.path === prefix.slice(0, -1) && entry.type === "tree" && entry.sha === evidenceTree),
    "Evidence subtree does not match the reserved branch");
  requireCondition(headTree.tree.some((entry) => entry.path === `${prefix}release-evidence.json` && entry.type === "blob"),
    "Release evidence record is missing");
  return { description: "Publication is based on current main", generated: true, sourceBase };
}

export function requireStrictGate(api, repository) {
  const rules = api(`repos/${repository}/rules/branches/main?per_page=100`);
  requireCondition(Array.isArray(rules) && rules.length < 100, "Effective branch rules are incomplete");
  const app = api("apps/github-actions");
  requireCondition(Number.isInteger(app.id), "GitHub Actions identity is unavailable");
  const strict = rules.filter((rule) => rule.type === "required_status_checks" &&
    rule.parameters?.strict_required_status_checks_policy === true &&
    rule.parameters.required_status_checks.some((check) => check.context === PUBLICATION_CONTEXT && check.integration_id === app.id));
  const nonFastForward = rules.filter((rule) => rule.type === "non_fast_forward");
  requireCondition(strict.length > 0 && nonFastForward.length > 0,
    "Required strict Publication merge admission gate is not active; PR retained");
  for (const id of new Set([...strict, ...nonFastForward].map((rule) => rule.ruleset_id))) {
    requireCondition(Number.isInteger(id), "Effective rule has no source ruleset");
    const ruleset = api(`repos/${repository}/rulesets/${id}?includes_parents=true`);
    requireCondition(ruleset.enforcement === "active", "Publication ruleset is inactive");
    // GitHub redacts bypass actors without ruleset-write access. Activation owns
    // that proof; runtime still rejects an exposed bypass without admin credentials.
    if (Object.hasOwn(ruleset, "bypass_actors")) {
      requireCondition(Array.isArray(ruleset.bypass_actors) && ruleset.bypass_actors.length === 0,
        "Publication ruleset permits bypass");
    }
    if (Object.hasOwn(ruleset, "current_user_can_bypass")) {
      requireCondition(ruleset.current_user_can_bypass === "never", "Current publisher can bypass the ruleset");
    }
  }
}

export function validateSource(api, repository, number, expectedHead) {
  const pull = api(`repos/${repository}/pulls/${number}`);
  let inputs = { repository, expectedHead, pull };
  if (pull.head.ref.startsWith(PREFIX)) {
    const main = api(`repos/${repository}/git/ref/heads/main`).object.sha;
    const commit = api(`repos/${repository}/git/commits/${expectedHead}`);
    const base = api(`repos/${repository}/git/commits/${main}`);
    inputs = { ...inputs, main, commit,
      baseTree: api(`repos/${repository}/git/trees/${base.tree.sha}?recursive=1`),
      headTree: api(`repos/${repository}/git/trees/${commit.tree.sha}?recursive=1`) };
  }
  const result = assessPublication(inputs);
  requireStrictGate(api, repository);
  const refreshed = api(`repos/${repository}/pulls/${number}`);
  requireCondition(refreshed.state === "open" && refreshed.head.sha === expectedHead && refreshed.base.ref === "main" &&
    refreshed.base.repo.full_name === repository, "PR changed during source validation");
  if (result.generated) {
    requireCondition(api(`repos/${repository}/git/ref/heads/main`).object.sha === result.sourceBase,
      "Main changed during source validation");
  }
  return result;
}

export function validateMergeAdmission(api, repository, number, expectedHead) {
  const pull = api(`repos/${repository}/pulls/${number}`);
  if (pull.state !== "open" || pull.head.sha !== expectedHead || pull.base.ref !== "main" ||
      pull.base.repo.full_name !== repository) return null;
  return { description: "Current open pull request targeting main" };
}

function api(path, fields) {
  const args = ["api", path];
  if (fields) {
    args.push("--method", "POST");
    for (const [key, value] of Object.entries(fields)) args.push("-f", `${key}=${value}`);
  }
  return JSON.parse(execFileSync("gh", args, { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] }));
}

function main() {
  const publisher = process.argv[2] === "--publisher";
  const event = publisher ? null : JSON.parse(readFileSync(process.env.GITHUB_EVENT_PATH, "utf8"));
  const repository = process.env.GITHUB_REPOSITORY;
  const number = publisher ? process.argv[3] : event.number;
  const expectedHead = publisher ? process.argv[4] : event.pull_request.head.sha;
  requireCondition(/^[\w.-]+\/[\w.-]+$/.test(repository) && /^[1-9][0-9]*$/.test(String(number)) && /^[a-f0-9]{40}$/.test(expectedHead),
    "Invalid publication event identity");
  const status = { context: PUBLICATION_CONTEXT,
    target_url: `${process.env.GITHUB_SERVER_URL || "https://github.com"}/${repository}/actions/runs/${process.env.GITHUB_RUN_ID}` };
  // The privileged PR event path admits only a current PR; payload policy stays
  // in the publisher. Obsolete events must not overwrite a newer head's status.
  const result = publisher ? validateSource(api, repository, number, expectedHead) :
    validateMergeAdmission(api, repository, number, expectedHead);
  if (!result) {
    console.log("Obsolete pull request event; no status written.");
    return;
  }
  api(`repos/${repository}/statuses/${expectedHead}`, { ...status, state: "success",
    description: "Current open pull request targeting main" });
  console.log(result.description);
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try { main(); } catch (error) { console.error(error.message); process.exitCode = 1; }
}

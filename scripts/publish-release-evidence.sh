#!/usr/bin/env bash
set -euo pipefail

fail() { echo "::error::$*" >&2; exit 1; }
if [[ ! "${RELEASE_ID:-}" =~ ^[A-Za-z0-9][A-Za-z0-9._-]*$ ]]; then
  fail "RELEASE_ID must be a release evidence directory name."
fi
[[ "${EVIDENCE_APP_BOT:-}" =~ ^[A-Za-z0-9-]+\[bot\]$ ]] || fail "EVIDENCE_APP_BOT must identify the evidence GitHub App."
repository="openclaw/releases"
evidence_path="evidence/${RELEASE_ID}"
[[ -f "${evidence_path}/release-evidence.json" ]] || fail "Generated release-evidence.json is missing."
git diff --cached --quiet || fail "The index contains unrelated staged work."
git config user.name "openclaw-release-bot"
git config user.email "release-bot@openclaw.ai"
git add -A -- "$evidence_path"
generated_tree="$(git write-tree)"
expected_tree="$(git rev-parse "${generated_tree}:${evidence_path}")"
changed=1
git diff --cached --quiet && changed=0

report() {
  echo "$1"
  if [[ -n "${GITHUB_STEP_SUMMARY:-}" ]]; then
    printf '\n%s\n' "$1" >> "$GITHUB_STEP_SUMMARY"
  fi
}
main_matches() {
  [[ "$(git rev-parse "origin/main:${evidence_path}" 2>/dev/null || true)" == "$expected_tree" ]]
}
git fetch origin main
if main_matches; then
  report "Verified exact evidence directory already on origin/main: ${evidence_path}"
  exit 0
fi
[[ "$changed" == 1 ]] || fail "Remote evidence directory differs from the unchanged local record; regenerate from current main."
git commit -m "Evidence: record ${RELEASE_ID}"
if ! git rebase origin/main; then
  git rebase --abort
  fail "Evidence conflicts with main; regenerate from current main."
fi
[[ "$(git rev-parse "HEAD:${evidence_path}")" == "$expected_tree" ]] || fail "Rebase changed the generated evidence directory; regenerate from current main."

# Content-addressed branches are immutable. Never adopt an orphan or force-push.
branch="evidence/${RELEASE_ID}/${expected_tree}"
list_prs() {
  gh api --method GET "repos/${repository}/pulls" -f state=all -f base=main -f "head=openclaw:${branch}"
}
check_branch() {
  [[ "$(git rev-parse "${1}:${evidence_path}")" == "$expected_tree" ]] || fail "Remote evidence branch differs from the generated directory."
  local path changed_paths
  # Renames must expose both sides, including deletions in another release.
  changed_paths="$(git diff --no-renames --name-only "origin/main...${1}")"
  while IFS= read -r path; do
    [[ -z "$path" ]] && continue
    [[ "$path" == "$evidence_path/"* ]] || fail "Evidence branch contains unrelated changes."
  done <<< "$changed_paths"
}
existing="$(git ls-remote --heads origin "refs/heads/${branch}")"
if [[ -n "$existing" ]]; then
  git fetch origin "refs/heads/${branch}"
  published_sha="$(git rev-parse FETCH_HEAD)"
  check_branch "$published_sha"
  prs="$(list_prs)"
  [[ "$(jq 'length' <<< "$prs")" == 1 ]] || fail "Existing evidence branch has no unique PR; inspect and recover it manually."
else
  check_branch HEAD
  published_sha="$(git rev-parse HEAD)"
  if ! git push origin "HEAD:refs/heads/${branch}"; then
    # A failed response can follow an accepted push. Reconcile, never replay it.
    observed="$(git ls-remote --heads origin "refs/heads/${branch}")"
    [[ "${observed%%[[:space:]]*}" == "$published_sha" ]] || fail "Evidence branch push was not confirmed; inspect before retrying."
  fi
  prs="$(list_prs)"
fi

# Check the actual merge result against fresh main, including clean additions in
# this directory. A PR is a proposal, not proof that its bytes reached the ledger.
git fetch origin main
if main_matches; then
  report "Verified exact evidence directory already on origin/main: ${evidence_path}"
  exit 0
fi
if ! merge_output="$(git merge-tree --write-tree origin/main "$published_sha")"; then
  fail "Evidence conflicts with current main; regenerate from current main."
fi
merge_tree="${merge_output%%$'\n'*}"
[[ "$(git rev-parse "${merge_tree}:${evidence_path}")" == "$expected_tree" ]] || fail "Current main changes the generated evidence directory; regenerate from current main."

if [[ "$(jq 'length' <<< "$prs")" == 0 ]]; then
  body="Evidence-only update for ${RELEASE_ID}. Generated directory tree: ${expected_tree}. This record is not in the main ledger until this PR is merged through the repository's normal checks and reviews."
  if ! gh api --method POST "repos/${repository}/pulls" -f base=main -f "head=${branch}" \
      -f "title=Evidence: record ${RELEASE_ID}" -f "body=${body}" > /dev/null; then
    echo "PR creation response failed; reconciling the existing request." >&2
  fi
  # Reconcile successful and ambiguous creates identically; never POST twice.
  prs="$(list_prs)"
fi
[[ "$(jq 'length' <<< "$prs")" == 1 ]] || fail "Evidence PR creation is unconfirmed; inspect the branch before retrying."
jq -e --arg bot "$EVIDENCE_APP_BOT" --arg branch "$branch" --arg sha "$published_sha" --arg repo "$repository" '
  .[0] | .user.login == $bot and .head.ref == $branch and .head.sha == $sha
  and .head.repo.full_name == $repo and .base.ref == "main" and .base.repo.full_name == $repo
  and .state == "open"
' <<< "$prs" > /dev/null || fail "Evidence PR is closed or has unexpected ownership, source, or target; inspect it manually."
url="$(jq -r '.[0].html_url' <<< "$prs")"
report "Evidence PR pending normal checks, review, and merge (not yet in main): ${url}"

#!/usr/bin/env bash
set -euo pipefail

if [[ ! "${RELEASE_ID:-}" =~ ^[A-Za-z0-9][A-Za-z0-9._-]*$ ]]; then
  echo "::error::RELEASE_ID must be a release evidence directory name."
  exit 1
fi
evidence_path="evidence/${RELEASE_ID}"
if [[ ! -f "${evidence_path}/release-evidence.json" ]]; then
  echo "::error::Generated release-evidence.json is missing."
  exit 1
fi

git config user.name "openclaw-release-bot"
git config user.email "release-bot@openclaw.ai"
git add -- "$evidence_path"
generated_tree="$(git write-tree)"
expected_tree="$(git rev-parse "${generated_tree}:${evidence_path}")"
git fetch origin main
baseline_tree="$(git rev-parse "origin/main:${evidence_path}" 2>/dev/null || true)"

if git diff --cached --quiet; then
  echo "No evidence changes to commit; verifying remote evidence."
else
  git commit -m "Evidence: record ${RELEASE_ID}"
  if ! git rebase origin/main; then
    git rebase --abort
    echo "::error::Evidence conflicts with main; regenerate from current main."
    exit 1
  fi
fi

# An unrelated file in this directory can merge cleanly and still change the proof.
if [[ "$(git rev-parse "HEAD:${evidence_path}")" != "$expected_tree" ]]; then
  echo "::error::Rebase changed the generated evidence directory; regenerate from current main."
  exit 1
fi
git fetch origin main
if git merge-base --is-ancestor HEAD origin/main; then
  # An unchanged record is successful only against the fresh remote tree.
  [[ "$(git rev-parse "origin/main:${evidence_path}")" == "$expected_tree" ]] || {
    echo "::error::Remote evidence directory differs from the generated files."
    exit 1
  }
  echo "Verified exact evidence directory on origin/main: ${evidence_path}"
  exit 0
fi

[[ "$(git rev-parse "origin/main:${evidence_path}" 2>/dev/null || true)" == "$baseline_tree" ]] || {
  echo "::error::Remote evidence directory changed; regenerate from current main."
  exit 1
}
release_key="$(printf '%s' "$RELEASE_ID" | git hash-object --stdin)"
branch_prefix="automation/release-evidence/${release_key}-"
publication_base="$(git rev-parse origin/main)"
branch="${branch_prefix}${expected_tree}-${publication_base}"
repo="${GITHUB_REPOSITORY:-$(gh repo view --json nameWithOwner --jq .nameWithOwner)}"
# A new generation must not abandon a pending or closed-unmerged predecessor.
# Including the base commit permits A -> B -> A after each prior PR has merged.
release_refs="$(git ls-remote --heads origin "refs/heads/${branch_prefix}*")"
while read -r prior_head prior_ref; do
  [[ -z "$prior_ref" || "$prior_ref" == "refs/heads/$branch" ]] && continue
  prior_branch="${prior_ref#refs/heads/}"
  merged="$(gh pr list --base main --head "$prior_branch" --state all --json isCrossRepository,headRefOid,state \
    --jq "[.[] | select(.isCrossRepository == false and .headRefOid == \"$prior_head\")] | any(.state == \"MERGED\")")"
  [[ "$merged" == true ]] || {
    echo "::error::Earlier evidence candidate is not confirmed merged; inspect https://github.com/$repo/compare/main...$prior_branch before publishing another generation."
    exit 1
  }
done <<< "$release_refs"
remote_head=""
lookup_status=0
remote_ref="$(git ls-remote --exit-code --heads origin "refs/heads/$branch")" || lookup_status=$?
if [[ "$lookup_status" == 0 ]]; then
  remote_head="${remote_ref%%[[:space:]]*}"
  git fetch origin "$remote_head"
  # Never replace pending evidence. A retry may reuse only the same owned payload.
  [[ "$(git rev-parse "${remote_head}:${evidence_path}")" == "$expected_tree" ]] || {
    echo "::error::Pending evidence branch differs; inspect $branch before retrying."
    exit 1
  }
elif [[ "$lookup_status" == 2 ]]; then
  remote_head="$(git rev-parse HEAD)"
else
  echo "::error::Could not inspect the release evidence branch."
  exit 1
fi
while IFS= read -r changed_path; do
  [[ "$changed_path" == "$evidence_path/"* ]] || {
    echo "::error::Evidence branch changes a path outside ${evidence_path}."
    exit 1
  }
done < <(git diff --no-renames --name-only "origin/main...$remote_head")
[[ "$(git show -s --format=%P "$remote_head")" == "$publication_base" ]] || {
  echo "::error::Evidence candidate must have one parent at current main; regenerate."
  exit 1
}
if [[ "$lookup_status" == 2 ]]; then
  # The empty lease admits creation only; it cannot overwrite an existing branch.
  git push --force-with-lease="refs/heads/$branch:" origin "HEAD:refs/heads/$branch"
fi

find_pr() {
  gh pr list --base main --head "$branch" --state all --json number,isCrossRepository,headRefOid \
    --jq "[.[] | select(.isCrossRepository == false and .headRefOid == \"$remote_head\")] | .[0].number // empty"
}
candidate_url="https://github.com/$repo/compare/main...$branch?expand=1"
echo "Evidence candidate: $candidate_url"
pr_number="$(find_pr)"
if [[ -z "$pr_number" ]]; then
  pr_body="$(mktemp)"
  trap 'rm -f "$pr_body"' EXIT
  printf 'Record validated release evidence for `%s`.\n\nExpected evidence tree: `%s`.\n' "$RELEASE_ID" "$expected_tree" > "$pr_body"
  if ! gh pr create --base main --head "$branch" --title "Evidence: record ${RELEASE_ID}" --body-file "$pr_body"; then
    echo "PR creation did not confirm success; checking for the published PR."
  fi
  pr_number="$(find_pr)" || {
    echo "::error::PR creation outcome is unknown; inspect $candidate_url before retrying."
    exit 1
  }
fi
[[ -n "$pr_number" ]] || {
  echo "::error::No evidence PR confirmed; inspect $candidate_url before retrying."
  exit 1
}
echo "Evidence PR: https://github.com/$repo/pull/$pr_number"
# Attest before waiting: a required status starts out missing and blocks readiness.
# Missing or bypassable policy retains this PR instead of auto-merging it.
node scripts/publication-source.mjs --publisher "$pr_number" "$remote_head"

merge_requested=0
merged_sha=""
for attempt in {1..30}; do
  record="$(gh pr view "$pr_number" --json headRefOid,state,mergeStateStatus,mergeCommit --jq '[.headRefOid, .state, .mergeStateStatus, (.mergeCommit.oid // "")] | @tsv')"
  IFS=$'\t' read -r head state merge_state merged_sha <<< "$record"
  [[ "$head" == "$remote_head" ]] || { echo "::error::Evidence PR head changed; publication unconfirmed."; exit 1; }
  if [[ "$state" == MERGED ]]; then break; fi
  [[ "$state" == OPEN && "$merge_state" != DIRTY ]] || {
    echo "::error::Evidence PR cannot merge: https://github.com/$repo/pull/$pr_number ($state, $merge_state)."
    exit 1
  }
  if [[ "$merge_state" == CLEAN && "$merge_requested" == 0 ]]; then
    git fetch origin main
    [[ "$(git rev-parse "origin/main:${evidence_path}" 2>/dev/null || true)" == "$baseline_tree" ]] || {
      echo "::error::Remote evidence directory changed; regenerate from current main."
      exit 1
    }
    # Strict server-side checks close the race after the last client read.
    merge_requested=1
    if ! gh pr merge "$pr_number" --squash --match-head-commit "$remote_head"; then
      echo "Merge request did not confirm success; checking the actual PR outcome."
    fi
  fi
  sleep 10
done
[[ "$state" == MERGED && "$merged_sha" =~ ^[0-9a-f]{40}$ ]] || {
  echo "::error::Evidence PR is not merged: https://github.com/$repo/pull/$pr_number; branch $branch remains available."
  exit 1
}

# A successful request or queued merge is not a publication receipt.
git fetch origin main "$merged_sha"
git merge-base --is-ancestor "$merged_sha" origin/main
[[ "$(git show -s --format=%P "$merged_sha")" == "$publication_base" ]] || {
  echo "::error::Squash merge parent differs from the validated publication base."
  exit 1
}
if [[ "$(git rev-parse "${merged_sha}:${evidence_path}")" != "$expected_tree" ||
      "$(git rev-parse "origin/main:${evidence_path}")" != "$expected_tree" ]]; then
  echo "::error::Merged evidence directory differs from the generated files."
  exit 1
fi
echo "Verified merged evidence PR $pr_number at $merged_sha."
echo "Verified exact evidence directory on origin/main: ${evidence_path}"

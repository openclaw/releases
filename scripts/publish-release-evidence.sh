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

if git diff --cached --quiet; then
  echo "No evidence changes to commit; verifying remote evidence."
else
  git commit -m "Evidence: record ${RELEASE_ID}"
  pushed=0
  for attempt in 1 2 3 4 5; do
    git fetch origin main
    if ! git rebase origin/main; then
      git rebase --abort
      echo "::error::Evidence conflicts with main; regenerate from current main."
      exit 1
    fi
    # An unrelated file in this directory can merge cleanly and still change the proof.
    if [[ "$(git rev-parse "HEAD:${evidence_path}")" != "$expected_tree" ]]; then
      echo "::error::Rebase changed the generated evidence directory; regenerate from current main."
      exit 1
    fi
    if git push origin HEAD:main; then
      pushed=1
      break
    fi
    sleep $((attempt * 5))
  done
  if [[ "$pushed" != "1" ]]; then
    echo "::error::Could not push evidence to main after retries."
    exit 1
  fi
fi

# Verify even a no-op against fresh remote state, not the checkout's old snapshot.
git fetch origin main
git merge-base --is-ancestor HEAD origin/main || {
  echo "::error::Published evidence commit is not reachable from origin/main."
  exit 1
}
if [[ "$(git rev-parse "origin/main:${evidence_path}")" != "$expected_tree" ]]; then
  echo "::error::Remote evidence directory differs from the generated files."
  exit 1
fi
echo "Verified exact evidence directory on origin/main: ${evidence_path}"

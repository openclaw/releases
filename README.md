# OpenClaw Releases

![OpenClaw Releases banner](docs/assets/readme-banner.jpg)

Release automation and evidence ledger for OpenClaw.

The source of truth stays in `openclaw/openclaw`:

- source code
- git tags
- GitHub releases
- npm publish workflow
- `appcast.xml` on `main`

This repo keeps release packaging, macOS publication support, npm dist-tag
maintenance, and durable release evidence separate from the product source repo.

## Workflows

- `.github/workflows/openclaw-macos-validate.yml` runs the release-blocking macOS
  Swift test lane for an existing OpenClaw tag.
- `.github/workflows/openclaw-macos-publish.yml` prepares and promotes signed
  macOS release artifacts for an existing OpenClaw tag.
- `.github/workflows/openclaw-npm-dist-tags.yml` reconciles npm dist-tags after
  package publication.
- `.github/workflows/openclaw-release-evidence.yml` records manually supplied
  release proof runs and can attach a verified extended-stable npm registry
  snapshot as an immutable sidecar.
- `.github/workflows/openclaw-release-evidence-from-full-validation.yml` ingests
  child runs from the public `Full Release Validation` workflow.

The macOS publish workflow builds from public `openclaw/openclaw` tags and uses
the public repo's packaging scripts. Real publish runs promote previously
prepared artifacts rather than rebuilding during the final upload step.

## Release Approval

The `mac-release` environment is the macOS equivalent of the public repo's
`npm-release` environment:

- real macOS preflight and promotion jobs must use `mac-release`
- `mac-release` requires approval from `openclaw-release-managers`
- real publish runs must be dispatched from this repo's `main` branch
- read-only maintainers can inspect the run; dispatch and approval stay with
  the configured release-manager reviewers, matching npm release policy

Keep the environment's required-reviewer rule, enabled self-review prevention,
main-branch policy, and disabled administrator bypass aligned with the macOS
release policy. Do not move signing or promotion secrets into repository-level
secrets.

## Release Evidence

The evidence workflows write release summaries under `evidence/<release-id>/`.
Each evidence directory contains:

- `release-evidence.md`
- `release-evidence.json`
- `index.json`
- `runs/<label>.json`
- `extended-stable-registry-snapshot.json` after an extended-stable npm closeout

Evidence records include release ref provenance, npm package metadata, run URLs,
workflow names, refs, SHAs, pass/fail state, timing summaries, artifact names,
artifact sizes, and selected release performance summaries.

Evidence records do not store raw logs, provider payloads, live-channel
transcripts, signing material, credentials, environment dumps, or downloaded
release artifacts.

### Manual Evidence

Manual evidence input format:

```text
<label> <owner/repo> <run-id> <blocking|advisory>
```

Example:

```text
full-release-validation openclaw/openclaw 24972498713 advisory
normal-ci openclaw/openclaw 24972500000 blocking
release-checks openclaw/openclaw 24972511111 blocking
```

Recommended labels:

```text
full-release-validation
normal-ci
release-checks
plugin-prerelease
product-performance
macos-validate
macos-preflight
macos-publish
npm-dist-tags
```

Mark a run as `blocking` when a release should not proceed without it passing.
Mark a run as `advisory` when it informed the release decision but should not
fail the release by itself.

### Full Validation Ingest

`OpenClaw Release Evidence From Full Validation` takes a completed
`openclaw/openclaw` full-validation run id, reads that parent run's logs,
extracts child run ids, and writes the same evidence directory shape.

Manual ingest example:

```bash
gh workflow run openclaw-release-evidence-from-full-validation.yml \
  --repo openclaw/releases \
  --ref main \
  -f full_validation_run_id=24977011361 \
  -f release_id=2026.4.24 \
  -f release_ref=v2026.4.24 \
  -f package_spec=openclaw@2026.4.24
```

### Extended-Stable npm Closeout

After the read-only closeout workflow in `openclaw/openclaw` succeeds, attach
its compact registry snapshot to an existing evidence directory:

```bash
CLOSEOUT_RUN_ID=123456789
ARTIFACT_NAME=extended-stable-registry-snapshot-v2026.6.33

CLOSEOUT_RUN_ATTEMPT="$(
  gh api "repos/openclaw/openclaw/actions/runs/${CLOSEOUT_RUN_ID}" --jq .run_attempt
)"
CLOSEOUT_ARTIFACT_DIGEST="$(
  gh api --paginate --slurp \
    "repos/openclaw/openclaw/actions/runs/${CLOSEOUT_RUN_ID}/artifacts?per_page=100" |
    jq -er --arg name "$ARTIFACT_NAME" '
      [.[].artifacts[] | select(.name == $name and .expired == false)] as $matches |
      if ($matches | length) == 1
      then $matches[0].digest
      else error("expected one unexpired artifact named " + $name)
      end
    '
)

gh workflow run openclaw-release-evidence.yml \
  --repo openclaw/releases \
  --ref main \
  -f mode=extended-stable-closeout \
  -f release_id=2026.6.33 \
  -f release_ref=v2026.6.33 \
  -f package_spec=openclaw@2026.6.33 \
  -f closeout_run_id="$CLOSEOUT_RUN_ID" \
  -f closeout_run_attempt="$CLOSEOUT_RUN_ATTEMPT" \
  -f closeout_artifact_name="$ARTIFACT_NAME" \
  -f closeout_artifact_digest="$CLOSEOUT_ARTIFACT_DIGEST" \
  -f plugin_npm_run_id=123456780 \
  -f core_npm_run_id=123456781 \
  -f full_release_validation_run_id=123456782
```

The target evidence directory must already contain `release-evidence.json`,
`release-evidence.md`, and `index.json`. This evidence-only mode has no npm
publish or selector-mutation authority. It verifies the closeout and related
runs against the canonical `extended-stable/YYYY.M.33` branch and release SHA,
then verifies the exact GitHub artifact digest before writing the sidecar. The
digest above is the GitHub artifact digest, not a digest calculated from the
extracted JSON file.

The closeout run must be on attempt `1`. GitHub's artifact download action is
run-id scoped rather than attempt scoped, so a rerun could make a name-based
download ambiguous. If closeout needs another attempt, dispatch a fresh
closeout workflow run and use its new run id instead of rerunning the old run.

The `release_id` must equal the exact `YYYY.M.PATCH` snapshot version. The mode
adds links to the existing `index.json` and `release-evidence.md`; it does not
regenerate or replace recorded Full Release Validation evidence. Replaying the
same snapshot is a no-op, while a different snapshot for the same release id
fails without overwrite.

## Storage Policy

Store only release summaries, normalized run metadata, artifact metadata, timing
summaries, package specs, and short release-manager notes here.

Do not commit:

- raw logs
- provider prompts or responses
- Matrix, Telegram, Discord, or other live-channel transcripts
- signing material, certificates, notarization credentials, or Sparkle keys
- token-bearing npm, GitHub, Apple, channel, or provider config
- downloaded release artifacts, `.zip`, `.dmg`, `.tgz`, or dSYM payloads
- secret-bearing environment dumps

Raw logs and bulky proof artifacts belong in GitHub Actions retention, external
artifact storage, or the public GitHub release when they are intended for users.

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
  release proof runs.
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

The evidence writer jobs use the `release-evidence` environment. It requires
approval from `openclaw-release-managers`, permits deployments only from
`main`, prevents self-review, and keeps administrator bypass disabled. Keep the
environment free of secrets and variables; its approval gates durable evidence
publication only and must not turn a pending publication into a failed upstream
validation result.

## Release Evidence

The evidence workflows write release summaries under `evidence/<release-id>/`.
Each evidence directory contains:

- `release-evidence.md`
- `release-evidence.json`
- `index.json`
- `runs/<label>.json`

Evidence records include release ref provenance, current npm and public GitHub
release state, run URLs, workflow names, refs, SHAs, pass/fail state, timing
summaries, artifact names, artifact sizes, and selected release performance
summaries.

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
`openclaw/openclaw` full-validation run id and reads its attempt-qualified
`full-release-validation-<run-id>-<attempt>` manifest artifact. The ingest
rejects missing, duplicate, expired, malformed, or identity-mismatched
artifacts; child run ids and evidence-reuse provenance come only from the
validated manifest. Repository dispatches must provide the exact parent run
attempt; manual dispatches may omit it to resolve the current attempt. Schema
v2 records `runAttempt` on every persisted run while schema v1 remains readable.
Exact duplicate parent attempts are no-ops, and an older attempt cannot replace
a newer attempt for the same run id.

Both evidence workflows require an exact package spec and release ref. They
commit with the workflow's same-repository `github.token`, then verify that the
commit is reachable from `origin/main`, the remote evidence directory is
byte-identical, and its JSON still satisfies the release identity contract.

Manual ingest example:

```bash
gh workflow run openclaw-release-evidence-from-full-validation.yml \
  --repo openclaw/releases \
  --ref main \
  -f full_validation_run_id=24977011361 \
  -f full_validation_run_attempt=1 \
  -f release_id=2026.4.24 \
  -f release_ref=v2026.4.24 \
  -f package_spec=openclaw@2026.4.24
```

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

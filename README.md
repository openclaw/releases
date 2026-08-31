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

- `.github/workflows/ci.yml` checks the repository scripts, runs workflow
  regression tests, and verifies package-manager setup plus cache/artifact round
  trips on Linux and macOS for pull requests and pushes to `main`. It uses a
  read-only repository token and temporary fixtures; it does not publish releases
  or update the evidence ledger.
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

The scripts use only Node.js built-ins and require no dependency installation or
build step. Run local checks with Node.js 24 and Python 3:

```bash
node --check scripts/openclaw-release-evidence.mjs
node --check scripts/openclaw-release-evidence-from-full-validation.mjs
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

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

Evidence records include release ref provenance, npm package metadata, run URLs,
workflow names, refs, SHAs, pass/fail state, timing summaries, artifact names,
artifact sizes, and selected release performance summaries.

Evidence records do not store raw logs, provider payloads, live-channel
transcripts, signing material, credentials, environment dumps, or downloaded
release artifacts.

Both evidence workflows publish with checkout-managed ephemeral `GITHUB_TOKEN`
credentials and `contents:write`; they do not require a persistent push PAT.
Evidence commits do not trigger push-triggered Actions workflows. Auth repair
verification must use a new, clearly labeled verification record because
regenerating an existing release ID overwrites its stored evidence.

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

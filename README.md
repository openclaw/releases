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
- `.github/workflows/openclaw-npm-dist-tags.yml` promotes or syncs npm `latest`
  for OpenClaw and enforces the beta floor: after every successful `latest`
  mutation, on manual `sync_beta_to_stable` dispatch, and daily as a backstop,
  `beta` for `openclaw` and every published official plugin is advanced to at
  least its own `latest`; an equal or newer `beta` is preserved. The plugin
  inventory is read as data from `openclaw/openclaw` `main` manifests.
- `.github/workflows/openclaw-release-evidence.yml` records manually supplied
  release proof runs.
- `.github/workflows/openclaw-release-evidence-from-full-validation.yml` ingests
  child runs from the public `Full Release Validation` workflow.

The macOS publish workflow builds from public `openclaw/openclaw` tags and uses
the public repo's packaging scripts. Real publish runs promote previously
prepared artifacts rather than rebuilding during the final upload step. Stable
appcasts must match the packaged app's version and build, release ZIP URL and
byte length, and contain a Sparkle signature before retention and promotion.
An existing seed feed alone is not valid release output. The preflight uses
`pnpm release:check` to build and validate package contents once before metadata
validation; native app packaging retains its own matching runtime build.

### Prepare signed macOS artifacts before tagging

After freezing the final signed source commit on `release/YYYY.M.PATCH`, start
signing/notarization and Swift validation concurrently from this repository's
trusted `main`. Neither run creates a tag or publishes assets:

```bash
gh workflow run openclaw-macos-publish.yml --repo openclaw/releases --ref main \
  -f tag=vYYYY.M.PATCH -f pretag_source_sha=<exact-signed-final-source-sha> \
  -f preflight_only=true -f smoke_test_only=false \
  -f public_release_branch=release/YYYY.M.PATCH
gh workflow run openclaw-macos-validate.yml --repo openclaw/releases --ref main \
  -f tag=vYYYY.M.PATCH -f pretag_source_sha=<exact-signed-final-source-sha>
```

Pretag preparation supports stable versions. It requires the exact canonical
release branch head, valid GitHub commit signature verification, and matching
package identity before checking out or executing public source. It rejects
`source_ref`, smoke mode, notarization recovery, and publication. A tag created
while the run queues must point at the same commit. Normal tagged recovery and
promotion keep their existing provenance checks.

The app embeds its real source SHA in signed metadata. A later CHANGELOG-only
commit is therefore **not** equivalent for artifact promotion: finalize the
changelog before starting, or rerun the producer to rebuild, sign, and notarize
the new final source. Never relabel previously signed bytes. When the eventual
tag selects the unchanged pretag SHA, use the successful preflight and validation
run IDs in ordinary promotion after the public GitHub release exists.

### Resume a failed macOS notarization

Signed preflights retain a `macos-notarization-<tag>-<run-id>-<attempt>` Actions
artifact when the packaging script produces a valid recovery checkpoint. It
contains the signed app, symbols, available DMG, Apple submission records, and
the producer's Sparkle tools. Private signing keys are never included. Retention
is 30 days; keep these payloads in Actions rather than the evidence ledger.

Dispatch another signed preflight from `main`, using the checkpoint's exact
public source commit and failed run attempt:

```bash
gh workflow run openclaw-macos-publish.yml --repo openclaw/releases --ref main \
  -f tag=vYYYY.M.PATCH -f source_ref=<checkpoint-source-sha> \
  -f preflight_only=true -f smoke_test_only=false \
  -f resume_notarization_run_id=<failed-run-id> \
  -f resume_notarization_run_attempt=<failed-run-attempt> \
  -f public_release_branch=release/YYYY.M.PATCH
```

Recovery uses the same release authorization and `mac-release` environment. It verifies the producer,
release/source binding, checkpoint hashes and signing identity, then resumes
Apple submissions without rebuilding the app. An existing signed DMG is reused;
if the failure preceded DMG creation, packaging creates and signs it after the
app is notarized. The original Sparkle tools generate the final appcast.

Use the successful recovery run as `preflight_run_id` for ordinary promotion,
together with the successful validation run for the same source. Recovery does
not replace validation or allow direct promotion from a failed run. Older source
commits without the recovery interface, expired/missing checkpoints, and changed
source commits fail explicitly; recovery never falls back to rebuilding.

The scripts use only Node.js built-ins and require no dependency installation or
build step. Run local checks with Node.js 24 and Python 3:

```bash
node --check scripts/openclaw-release-evidence.mjs
node --check scripts/openclaw-release-evidence-from-full-validation.mjs
node --check scripts/release-npm-beta-floor.mjs
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
node --test 'tests/*.test.mjs'
```

## Release Approval

An explicit request to release OpenClaw authorizes the macOS release through
validation, signing, notarization, and promotion. Do not ask for a separate
macOS approval after the release has already been authorized.

- real macOS preflight and promotion jobs must use `mac-release`
- `mac-release` has no required reviewers or wait timer; the authorized
  operator dispatches the release workflows
- the environment permits deployments only from this repo's `main` branch
- successful validation and signed preflight artifacts for the exact tag and
  source remain required before promotion
- read-only maintainers can inspect runs; repository permissions control who
  can dispatch them

Keep signing and promotion secrets in `mac-release`, with its main-only branch
policy intact. Do not approve a job on someone else's behalf or use an alternate
signing path to bypass an enforced rule. Organization owners manage the
environment policy; changes to that policy require explicit owner direction.

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
Both writers run from `main`, share a per-release concurrency group, and verify
that the complete generated evidence directory is byte-identical on `origin/main`.
Unrelated concurrent commits can be rebased; changes within the same evidence
directory fail with a request to regenerate from current main. Even an unchanged
local record is checked against fresh remote state before reporting success.
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

## Nix Qualification

The CI workflow's `nix_source_phase` dispatch input is restricted to the reviewed
qualification branch and actor. `prefetch` records the exact source archive hash
and classifies the selected package's fixed-output dependency hash mismatch on
each native system. It is not package proof. After independent review, freeze
both systems' real hashes in `scripts/nix-source-qualification/hashes.json`;
`qualify` refuses missing or placeholder hashes.

Qualification builds the selected source through Home Manager's `gatewayPath`
and actual `home.packages`, then verifies one isolated generation, package
contents, Control UI assets, CLI exports, real packaged plugin CLI/RPC actions,
and supervisor cleanup. The ownership harness uses the selected patched source
and exact production dependencies from the installed package after pruning,
without a second dependency installation. It does not migrate an existing
installation or change pins, tags, releases, or deployment state. No local Nix
execution is supported.
The source dispatch skips normal CI's cache/artifact round-trip job; native jobs
upload neither caches nor artifacts. Raw output stays in disposable runner
scratch; only closed qualification receipts are printed.
Failures include bounded, scrubbed diagnostics. The macOS lane qualifies
macOS 26 on Apple Silicon, not every Darwin release.

Control UI proof checks the selected source's public-file inventory for installed
existence, then compares served identity bytes with installed postbuild files,
including root files and `asset-manifest.json`. The document is compared
structurally; source maps and directly unserved compression sidecars are excluded
from HTTP parity. This does not independently prove Vite's public-file transforms.

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

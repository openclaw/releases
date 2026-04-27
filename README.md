# releases-private

Private release automation for OpenClaw's real macOS signing, notarization,
Sparkle appcast generation, packaged release artifact generation, npm dist-tag
mutation, optional private runtime checks, and durable release evidence.

The source of truth stays in `openclaw/openclaw`:

- source code
- git tags
- GitHub releases
- npm publish workflow
- `appcast.xml` on `main`

This repo exists so release authority, private credentials, privileged
workflows, and durable release evidence do not live in `openclaw/openclaw`.
Public source, reusable test harnesses, and normal package publication stay in
the public repo.

## Workflow

- Separate private mac validation workflow:
  `.github/workflows/openclaw-macos-validate.yml`
- Real mac publish workflow:
  `.github/workflows/openclaw-macos-publish.yml`
- Optional private cross-OS release runtime workflow:
  `.github/workflows/openclaw-cross-os-release-checks.yml`
- Private npm dist-tag workflow:
  `.github/workflows/openclaw-npm-dist-tags.yml`
- Private release evidence workflow:
  `.github/workflows/openclaw-release-evidence.yml`
- The validation workflow is the required `swift test` lane for release
  readiness, and each successful run uploads a `macos-validate-<tag>` proof
  artifact. It does not build, sign, notarize, package, or upload release
  assets.
- The workflow checks out `openclaw/openclaw` at `refs/tags/<tag>` and uses the
  public repo's packaging scripts directly.
- Every successful run uploads the packaged macOS artifacts to this workflow as
  `macos-smoke-<tag>`, `macos-preflight-<tag>`, or `macos-release-<tag>`.
- Stable releases upload a `macos-appcast-<tag>` artifact here, but the workflow
  never pushes `appcast.xml` back to `main`.
- Real publish runs require:
  - `preflight_run_id=<successful private mac preflight run>`
  - `validate_run_id=<successful private mac validation run>`
- Real publish verifies both referenced runs came from this repo's `main`
  workflow definitions and that their saved release provenance matches the
  current public tag.
- Real publish promotes those already prepared artifacts instead of rebuilding
  and renotarizing again.
- Real publish now promotes and uploads those prepared artifacts from a cheap
  Ubuntu job; the mac runner is only used for private preflight and smoke-test
  runs.
- Real publish runs upload the `.zip`, `.dmg`, and `.dSYM.zip` files to the
  existing release in `openclaw/openclaw` automatically.
- All token-based npm dist-tag mutation now lives in the private workflow
  `.github/workflows/openclaw-npm-dist-tags.yml`, so the public repo can keep
  trusted publishing for `npm publish` without holding an npm write token.
- That private workflow handles three cases:
  - daily and manual `sync_beta_to_stable` reconciliation so `beta` can follow
    the current stable `latest`
  - manual `promote_beta_to_latest` for the beta-first stable release flow
  - manual `sync_stable_dist_tags` when operators want both `latest` and
    `beta` to point at the same already-published stable build immediately
- The scheduled reconciliation intentionally leaves `beta` alone when it already
  matches `latest` or when `beta` points at a newer future prerelease than the
  current stable release.
- No GitHub App secret is required. Public source checkout and appcast seeding
  happen without extra credentials, and the cross-repo release upload uses
  `OPENCLAW_PUBLIC_REPO_RELEASE_TOKEN`.
- `smoke_test_only=true` is available for branch-safe workflow smoke tests. It
  uses ad-hoc signing, skips notarization, skips shared appcast generation, and
  does not require the Apple signing/notary/Sparkle secrets.
- `preflight_only=true` remains the path that does the real build, signing,
  notarization, packaging, and stable appcast generation.
- Validation-only and preflight-only runs may still be dispatched from branches
  while iterating on workflow changes, but their run ids are not valid for real
  publish.
- The cross-OS release runtime workflow is manual and optional. It is for
  install, upgrade, gateway, and end-to-end validation on GitHub-hosted Linux,
  macOS, and Windows runners, and it is intentionally outside the critical
  release publish path.
- The cross-OS workflow builds and packs the candidate once, then reuses that
  same npm tarball across Linux, macOS, and Windows so every lane validates the
  exact same artifact.
- Do not start the real private mac publish until public npm preflight, public
  mac validation, private mac validation, and private mac preflight have all
  passed.
- `preflight_only=false` is now promotion-only and must reuse both:
  - a successful private preflight run via `preflight_run_id`
  - a successful private validation run via `validate_run_id`
- After a successful stable publish, an agent or maintainer must download that
  artifact and commit `appcast.xml` to `openclaw/openclaw` `main`.

## Release evidence ledger

The manual `OpenClaw Release Evidence` workflow is the durable release ledger.
It does not run tests and it does not publish anything. It takes the GitHub
Actions run ids that already proved a release candidate, fetches their run,
job, and artifact metadata, writes a human-readable summary plus machine-readable
JSON, and opens a pull request that records the result under
`evidence/<release-id>/`.

Use it when a release train needs a private, searchable, long-lived record of
what was validated. GitHub Actions summaries are the immediate operator UI and
Actions artifacts are the raw log store, but both are tied to individual run
pages. The evidence ledger is the canonical release-history index for:

- release validation runs from `openclaw/openclaw`
- package acceptance runs from `openclaw/openclaw`
- private mac validation or publish runs from this repo
- private cross-OS release checks from this repo
- npm dist-tag operations from this repo
- advisory runs that informed a release decision

Run the evidence workflow during or after a release train, usually once there is
enough signal to make a release decision. It is fine to rerun it for the same
`release_id`; the workflow overwrites that directory with the latest metadata
on a new evidence branch and opens a pull request for review and merge.

### Inputs

`release_id` names the evidence directory. Use the public package or tag identity
when possible:

```text
2026.4.27-beta.1
2026.4.27
2026.4.27-1
```

`release_ref` is optional and should be the public tag, release branch, or full
SHA that the evidence covers.

`package_spec` is optional and should be the npm package identity when the
evidence covers a published or candidate package, for example:

```text
openclaw@2026.4.27-beta.1
openclaw@beta
openclaw@2026.4.27
```

`notes` is optional release-manager context. Keep it short and free of secrets.

The workflow input `runs` is one run per line:

```text
<label> <owner/repo> <run-id> <blocking|advisory>
```

Example:

```text
full-release-validation openclaw/openclaw 24972498713 blocking
package-acceptance openclaw/openclaw 24972500000 blocking
private-cross-os openclaw/releases-private 24972511111 advisory
```

Recommended labels are lowercase, dash-separated, and stable across releases:

```text
full-release-validation
package-acceptance
npm-preflight
npm-publish
npm-dist-tags
macos-validate
macos-preflight
macos-publish
private-cross-os
qa-lab-all-lanes
```

Mark a run as `blocking` when a release should not proceed without it passing.
Mark a run as `advisory` when it informed the decision but should not fail the
release by itself, such as broad provider/media checks, experimental VM lanes,
or known-flaky third-party-service coverage.

### Outputs

Each evidence run writes:

- `evidence/<release-id>/release-evidence.md`
- `evidence/<release-id>/release-evidence.json`
- `evidence/<release-id>/index.json`
- `evidence/<release-id>/runs/<label>.json`

`release-evidence.md` is the operator-facing summary. It includes blocking and
advisory counts, run URLs, workflow names, refs, SHAs, artifact counts, and a
short failure section.

`release-evidence.json` is the machine-readable manifest for later tooling. It
contains the same release metadata plus normalized run, job, and artifact
metadata.

`index.json` is the small pointer file for listing evidence directories without
loading the full manifest.

`runs/<label>.json` stores the normalized metadata for each individual run so a
failed or interesting shard can be inspected directly.

### Storage policy

Store only summaries, run URLs, artifact metadata, timings, pass/fail state,
SHAs, package specs, and short release-manager notes here.

Do not commit:

- raw logs
- provider prompts or responses
- Matrix, Telegram, Discord, or other live-channel transcripts
- signing material, certificates, notarization credentials, or Sparkle keys
- token-bearing npm, GitHub, Apple, channel, or provider config
- downloaded release artifacts, `.zip`, `.dmg`, `.tgz`, or dSYM payloads
- secret-bearing environment dumps

Raw logs and bulky proof artifacts should stay in GitHub Actions artifacts. The
ledger links to those runs and artifacts instead of vendoring them into git.

## Required `mac-release` environment secrets

- `MACOS_DEVELOPER_ID_P12_BASE64`
- `MACOS_DEVELOPER_ID_P12_PASSWORD`
- `APP_STORE_CONNECT_API_KEY_P8`
- `APP_STORE_CONNECT_KEY_ID`
- `APP_STORE_CONNECT_ISSUER_ID`
- `SPARKLE_PRIVATE_KEY`
- `OPENCLAW_PUBLIC_REPO_RELEASE_TOKEN` (`contents:write` on `openclaw/openclaw`
  is sufficient)

## Required repo secrets for npm dist-tag operations

- `NPM_TOKEN` (used only for `npm dist-tag add`, not for trusted publishing)

## Required repo secrets for cross-OS runtime checks

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `MINIMAX_API_KEY`

The cross-OS workflow selects one provider lane per run. It requires the
matching provider key to exist as a repo secret, but it does not require Apple
signing or notarization secrets.

Optional repo variables for runner sizing:

- `OPENCLAW_RELEASE_CHECKS_UBUNTU_RUNNER`
- `OPENCLAW_RELEASE_CHECKS_WINDOWS_RUNNER`
- `OPENCLAW_RELEASE_CHECKS_MACOS_RUNNER`

Set those to the largest GitHub-hosted runner labels available to this repo if
you want to override the workflow defaults without editing the workflow file.

## Repo policy

- Workflow changes are code-owned by `@openclaw/openclaw-release-managers`.
- The `mac-release` environment exists and should hold the real mac publish
  secrets.
- `NPM_TOKEN` for `.github/workflows/openclaw-npm-dist-tags.yml` is a repo
  secret, not a `mac-release` environment secret.
- Real publish runs must be dispatched from this repo's `main` branch.

## Pending platform protections

Two GitHub settings could not be enabled through the API on this private repo
with the current org plan:

- branch protection on `main`
- required reviewers on the `mac-release` environment

When the billing plan supports them, enable:

- branch protection for `main`
- required reviewers on `mac-release`:
  `@openclaw/openclaw-release-managers`
- `prevent self-review` on `mac-release`
- keep `can admins bypass` disabled on `mac-release`

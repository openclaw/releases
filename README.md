# releases-private

Private release automation for OpenClaw's real macOS signing, notarization,
Sparkle appcast generation, and packaged release artifact generation.

The source of truth stays in `openclaw/openclaw`:

- source code
- git tags
- GitHub releases
- npm publish workflow
- `appcast.xml` on `main`

This repo exists so Apple signing, notarization, and Sparkle signing do not
live in `openclaw/openclaw`.

## Workflow

- Separate private mac validation workflow:
  `.github/workflows/openclaw-macos-validate.yml`
- Real mac publish workflow:
  `.github/workflows/openclaw-macos-publish.yml`
- Optional private cross-OS release runtime workflow:
  `.github/workflows/openclaw-cross-os-release-checks.yml`
- Private npm dist-tag sync workflow:
  `.github/workflows/openclaw-npm-dist-tags.yml`
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
- Stable npm dist-tag mutation now lives in the private workflow
  `.github/workflows/openclaw-npm-dist-tags.yml`, so the public repo can keep
  trusted publishing for `npm publish` without holding an npm write token.
- That private workflow is self-healing: it runs daily and can also be rerun
  manually without inputs.
- It only moves `npm beta` to the current stable `npm latest` after confirming
  the matching public release tag exists in `openclaw/openclaw`.
- It intentionally leaves `beta` alone when it already matches `latest` or when
  `beta` points at a newer future prerelease than the current stable release.
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

## Required `mac-release` environment secrets

- `MACOS_DEVELOPER_ID_P12_BASE64`
- `MACOS_DEVELOPER_ID_P12_PASSWORD`
- `APP_STORE_CONNECT_API_KEY_P8`
- `APP_STORE_CONNECT_KEY_ID`
- `APP_STORE_CONNECT_ISSUER_ID`
- `SPARKLE_PRIVATE_KEY`
- `OPENCLAW_PUBLIC_REPO_RELEASE_TOKEN` (`contents:write` on `openclaw/openclaw`
  is sufficient)
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
- The `mac-release` environment exists and should hold all real publish secrets.
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

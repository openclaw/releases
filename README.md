# releases-private

Private release automation for OpenClaw's real macOS signing, notarization,
Sparkle appcast generation, and GitHub release asset upload.

The source of truth stays in `openclaw/openclaw`:

- source code
- git tags
- GitHub releases
- npm publish workflow
- `appcast.xml` on `main`

This repo exists so Apple signing, notarization, Sparkle signing, and the
cross-repo upload token do not live in `openclaw/openclaw`.

## Workflow

- Real mac publish workflow:
  `.github/workflows/openclaw-macos-publish.yml`
- The workflow checks out `openclaw/openclaw` at `refs/tags/<tag>` and uses the
  public repo's packaging scripts directly.
- Stable releases upload a `macos-appcast-<tag>` artifact here, but the workflow
  never pushes `appcast.xml` back to `main`.
- After a successful stable publish, an agent or maintainer must download that
  artifact and commit `appcast.xml` to `openclaw/openclaw` `main`.

## Required `mac-release` environment secrets

- `OPENCLAW_PUBLIC_REPO_APP_ID`
- `OPENCLAW_PUBLIC_REPO_APP_PRIVATE_KEY`
- `MACOS_DEVELOPER_ID_P12_BASE64`
- `MACOS_DEVELOPER_ID_P12_PASSWORD`
- `APP_STORE_CONNECT_API_KEY_P8`
- `APP_STORE_CONNECT_KEY_ID`
- `APP_STORE_CONNECT_ISSUER_ID`
- `SPARKLE_PRIVATE_KEY`

## GitHub App contract

Install a GitHub App on `openclaw/openclaw` with the minimum permissions this
workflow needs:

- `contents: write`
- `metadata: read`

The workflow mints an installation token at runtime and uses that token for:

- checking out `openclaw/openclaw`
- reading `appcast.xml` from `main`
- checking that the GitHub release for the tag already exists
- uploading signed macOS assets to the existing GitHub release

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

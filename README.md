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

- Real mac publish workflow:
  `.github/workflows/openclaw-macos-publish.yml`
- The workflow checks out `openclaw/openclaw` at `refs/tags/<tag>` and uses the
  public repo's packaging scripts directly.
- Every successful run uploads the packaged macOS artifacts to this workflow as
  either `macos-preflight-<tag>` or `macos-release-<tag>`.
- Stable releases upload a `macos-appcast-<tag>` artifact here, but the workflow
  never pushes `appcast.xml` back to `main`.
- Real publish runs do not upload to the public GitHub release automatically.
  An agent or maintainer must download `macos-release-<tag>` and upload the
  `.zip`, `.dmg`, and `.dSYM.zip` files to the existing release in
  `openclaw/openclaw`.
- No GitHub App secret is required for the workflow anymore. Public source
  checkout and appcast seeding happen without extra credentials, and the public
  release upload happens outside Actions.
- After a successful stable publish, an agent or maintainer must download that
  artifact and commit `appcast.xml` to `openclaw/openclaw` `main`.

## Required `mac-release` environment secrets

- `MACOS_DEVELOPER_ID_P12_BASE64`
- `MACOS_DEVELOPER_ID_P12_PASSWORD`
- `APP_STORE_CONNECT_API_KEY_P8`
- `APP_STORE_CONNECT_KEY_ID`
- `APP_STORE_CONNECT_ISSUER_ID`
- `SPARKLE_PRIVATE_KEY`

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

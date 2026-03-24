2026-03-24

# Private macOS Release Security Status

This report describes the current security posture of `openclaw/releases-private` after the macOS release workflow migration from `openclaw/openclaw`.

It distinguishes between:

- verified controls that are live in GitHub today
- accepted operational decisions
- residual risk that remains by design

## Scope

This report covers:

- the private repo `openclaw/releases-private`
- the `mac-release` environment in that repo
- the private workflow `.github/workflows/openclaw-macos-publish.yml`
- the public repo `openclaw/openclaw` only where it affects the trust boundary for the private release flow

## Accepted operating model

The current operating model intentionally keeps collaboration broad:

- the `Maintainer` team retains `push` access to `openclaw/releases-private`
- retaining maintainer write was explicitly requested by Peter and Shadow
- release managers do not want that write access removed because it would slow down long-term collaboration
- a maintainer being able to start a premature private release run is accepted risk
- the non-negotiable boundary is secret exfiltration, not preventing every premature run
- the accepted worst case under this model is a premature release, not secret extraction

Additional accepted assumption:

- release-tag creation in `openclaw/openclaw` is restricted to `openclaw-release-managers`
- because the private workflow executes release code from the public tag, that tag remains part of the trust boundary

## Verified controls in `openclaw/releases-private`

### `main` ruleset

The repository ruleset `Protect main` is active on the default branch and currently enforces:

- pull request required
- 1 approving review required
- code owner review required
- only `squash` and `rebase` merges allowed
- force-push blocked via non-fast-forward restriction
- branch deletion blocked
- bypass actor: `@openclaw/openclaw-release-managers`

### Repo-wide CODEOWNERS

The repo-wide CODEOWNERS file on `main` is:

```text
* @openclaw/openclaw-release-managers
```

This means any change proposed to the private repo on `main`, including workflow changes, is owned by release managers.

### Environment protection

The `mac-release` environment currently has:

- `can_admins_bypass=false`
- deployment branch policy enabled
- custom branch policies turned on
- one allowed branch policy: `main`

This means only runs whose ref is `main` can deploy to `mac-release`.

### Team access

Current team permissions on `openclaw/releases-private`:

- `Maintainer`: `push`
- `openclaw-release-managers`: `maintain`
- `GitHub Moderators`: `pull`

Maintainers intentionally retain write access by operator decision.

## Verified controls in `openclaw/openclaw` that matter here

The private workflow checks out a public tag from `openclaw/openclaw` and executes release/build scripts from that tag.

Because of that, the public tag must be trusted.

The repository ruleset `release-tags` in `openclaw/openclaw` is active and currently:

- targets tags
- blocks tag creation, update, deletion, and non-fast-forward changes
- uses `@openclaw/openclaw-release-managers` as the bypass actor

Operationally, this means release tags are controlled by release managers, and that control is a central part of the current secret-protection model.

## What the current setup prevents

Under the current model, the following direct paths are blocked:

- maintainers cannot change the secrets-bearing workflow on `main` without a release-manager-reviewed PR
- maintainers cannot use a branch-modified workflow file to reach `mac-release`, because the environment allows only `main`
- maintainers cannot create arbitrary release tags in `openclaw/openclaw` if they are not release managers

## What the current setup still allows by design

The following is intentionally allowed:

- maintainers with repo write can manually dispatch the private workflow from `main`
- maintainers can observe workflow logs for runs they are allowed to access

This is accepted because the current risk decision is:

- premature release is acceptable
- direct secret exfiltration is not acceptable

## Secret-bearing materials used by the private workflow

The private workflow currently relies on secrets for:

- `MACOS_DEVELOPER_ID_P12_BASE64`
- `MACOS_DEVELOPER_ID_P12_PASSWORD`
- `APP_STORE_CONNECT_API_KEY_P8`
- `APP_STORE_CONNECT_KEY_ID`
- `APP_STORE_CONNECT_ISSUER_ID`
- `SPARKLE_PRIVATE_KEY`
- `OPENCLAW_PUBLIC_REPO_RELEASE_TOKEN`

Those secrets are used only in the private repo and only in jobs that target the `mac-release` environment.

## Residual risk and trust assumptions

The current model still has important residual risk and explicit trust assumptions:

- a maintainer with write access can start a run from `main`
- because environment required reviewers are not configured, there is no extra manual approval gate before a valid `main` run reaches `mac-release`
- the trust boundary includes the public tagged source from `openclaw/openclaw`, because the private workflow clones that tag and runs its release scripts

This means the current posture depends on these controls staying true:

- the private workflow definition on `main` remains release-manager-owned
- the `mac-release` environment remains limited to `main`
- public release tags remain release-manager-controlled
- release managers trust the tagged public source they choose to publish

## Current conclusion

The current configuration does not try to prevent every private workflow dispatch.

Instead, it enforces this narrower boundary:

- maintainers may retain repo write and may trigger runs
- only the trusted `main` workflow may access the `mac-release` environment
- workflow changes on `main` remain under release-manager review
- release-tag creation in the public source repo remains under release-manager control

Under the operator-approved risk model, the primary accepted residual risk is premature release execution.

The current design treats secret exfiltration as prevented by a combination of:

- release-manager ownership of the private repo contents on `main`
- `main`-only environment access
- release-manager control of public release tags

## Optional future hardening

These are not required by the current operating decision, but would reduce risk further if priorities change later:

- remove `Maintainer` write from `openclaw/releases-private`
- add an explicit actor allowlist before any secret-bearing job is allowed to run
- eliminate `OPENCLAW_PUBLIC_REPO_RELEASE_TOKEN` if the release upload flow is simplified again
- add environment required reviewers if GitHub plan/feature availability changes

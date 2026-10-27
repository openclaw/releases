# Approve a Windows Microsoft Store publication

`openclaw/releases` owns Microsoft Store submission for Gateway and Companion.
The Windows repositories build and qualify unsigned MSIX bundles. Their request
workflows and the core Gateway handoff can queue this central workflow; they
cannot approve it or use the central Store identity.

## Request and approve

Select an already successful canonical source run. Gateway uses a main-branch
`gateway-msix.yml` Store-only or official build. Companion uses a final stable
tag's `ci.yml` run or an approved `promote-alpha-release.yml` run. Alpha, PR,
failed, foreign, expired, and stale-attempt sources are rejected.

```powershell
gh workflow run windows-store-publish.yml --repo openclaw/releases --ref main `
  -f product=gateway -f run_id=SOURCE_RUN_ID
```

Use `product=companion` for the Companion Store product. A successful dispatch
means only that the request was accepted, not that Microsoft accepted a package.

The source job checks the actual environment protection, published source,
artifact identity, package identity/version, and bundle bytes without Store
credentials. Review its summary before approving: source and release-identity
tags/commits, source pipeline/run/attempt, package version, artifact ID, publisher
code commit, and bundle SHA-256. Gateway's payload and independently selected
release identity remain separate facts. Build qualification owns MSIX composition,
architecture, reserved-version allocation, inventory, and installed-upgrade proof;
the publisher does not rebuild or introduce another version-allocation policy.

Only `@openclaw/release-managers-openclaw` can approve the product's environment.
The approved job downloads the same artifact ID and rechecks current source,
attempt, release, hash, and protection settings before requesting an OIDC assertion.
It executes only reviewed central scripts, never scripts downloaded from a source
repository or artifact. The existing publisher preserves product metadata, owns
only its created draft, and never deletes an ambiguously accepted commit.

The preapproval source facts and Microsoft commit receipt are retained for 90 days.
`CommitStarted` is commit acceptance, not certification or public availability.
Follow that submission in Partner Center. On a failed or ambiguous upload/commit,
inspect the retained run and draft before another request; do not rebuild or
republish npm to recover Store delivery. Requests for the same product serialize
and do not cancel an active upload.

## Administrator cutover

These are required settings, not changes applied by merging the YAML. Until the
two environments have the exact required team/main/no-bypass protection, the
publisher fails before credential use. Repository and cloud administrators must
complete and read back the following cutover before enabling requests.

1. Merge the [evidence-writer PR compatibility change](https://github.com/openclaw/releases/pull/47) before enforcing PR-only
   `main`. Evidence updates must use ordinary checked PRs, not an automation bypass
   that could edit publisher code.
2. Correct the CODEOWNERS slug and verify team ID `16590423` has an explicit write
   grant on all three repositories. The native packaging grant needs independent
   verification; team members' individual access is not a substitute.
3. Review/import `config/windows-release-authority-ruleset.json` as an
   organization-owned ruleset and `config/windows-store-ci-ruleset.json` for this
   repository. Reconcile an existing matching rule instead of creating duplicates.
   The former requires PRs and release-manager review of authority paths, including
   CODEOWNERS and the policy templates themselves. Evidence-only PRs still require
   CI but do not require the release team. No bot or ordinary maintainer bypasses
   these rules. Retain existing required native checks, including Node's CI Gate.
4. Create/update both environments from `config/windows-store-environments.json`.
   For each, create the single deployment branch policy `{ "name": "main",
   "type": "branch" }` and remove other patterns. The templates allow an initiating
   release manager to approve, matching Node's existing stable-promotion policy;
   they still permit only the named team. Set prevent-self-review if a separate
   deployment initiator/approver is desired. App-dispatched jobs do not by themselves
   prove two distinct upstream humans.
5. Set `MSSTORE_TENANT_ID`, `MSSTORE_CLIENT_ID`, and `MSSTORE_APPLICATION_ID` as
   variables in each corresponding environment. Preserve the existing separate
   Gateway and Companion Entra applications and Partner Center product roles.
   Keep GitHub App `2729701` / `GH_APP_PRIVATE_KEY` available to these reviewed
   workflows, with the necessary installations. Reader tokens use only Actions
   read and Contents read on core and both Windows repositories. Requesters use
   only Actions write on `releases`; the evidence writer separately needs scoped
   Contents/Pull Requests write here. Verify grants rather than assuming them.
6. Reconcile/drain existing native Store runs and drafts. In the actual Store
   tenant, replace each native writer federation with its corresponding central
   environment federation. Audit other federated writers, passwords/certificates,
   and separate manual publishing access. Avoid a parallel unapproved writer
   window; removing a federation does not recall already-issued access tokens.
7. Read this repository's current OIDC subject configuration. With the currently
   configured prefix `repo:openclaw/releases`, use issuer
   `https://token.actions.githubusercontent.com`, audience
   `api://AzureADTokenExchange`, and subjects:
   - Gateway: `repo:openclaw/releases:environment:microsoft-store-gateway`
   - Companion: `repo:openclaw/releases:environment:microsoft-store-companion`
   Recompute if immutable/custom subjects are enabled. Remove native repository
   trusts; deleting their YAML or variables alone does not remove cloud authority.
8. Land the [Gateway request-only cutover](https://github.com/openclaw/openclaw-windows-packaging/pull/212),
   [Companion request-only cutover](https://github.com/openclaw/openclaw-windows-node/pull/1891),
   and [core handoff](https://github.com/openclaw/openclaw/pull/181446) together with
   the central owner. Preserve Node's separate stable-promotion gate. Gateway packaging's
   compatibility request is manual-only; core owns its normal automatic request,
   avoiding duplicate native/core dispatches. Companion's `MSSTORE_ENABLED` switch
   may queue requests after a successful eligible stable release; it never bypasses
   central approval. No new PAT or persistent Microsoft Store secret is required.

Use `gh api repos/openclaw/releases/environments/ENV` and its
`deployment-branch-policies` endpoint to verify the exact team and main-only/no-bypass
settings. Check effective active rulesets and
`gh api repos/openclaw/releases/codeowners/errors?ref=main`; an existing or named
ruleset is not proof that code review is enforced.

After setup, first prove an ordinary writer can queue but not approve a request,
and that old/native identities, wrong refs, revoked source authority, and substituted
bundles are rejected. A live Store submission requires explicit release authority;
local fixtures and a configured identity do not establish live acceptance.

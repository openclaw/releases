# Approve a Windows Microsoft Store publication

`openclaw/releases` owns Microsoft Store submission for Gateway and Companion.
The Windows repositories build and qualify unsigned MSIX bundles. Their request
workflows and the core Gateway handoff can queue this central workflow; they
cannot approve it or use the central Store identity.

## Request and approve

Select an already successful canonical source run. Gateway uses a main-branch
`gateway-msix.yml` Store-only or official build. Gateway production requires a
stable source; Development requires an official beta build with its packaging
GitHub prerelease already published. Companion uses a final stable
tag's `ci.yml` run or an approved `promote-alpha-release.yml` run. Alpha, PR,
failed, foreign, expired, and stale-attempt sources are rejected.

```powershell
gh workflow run windows-store-publish.yml --repo openclaw/releases --ref main `
  -f product=gateway -f run_id=SOURCE_RUN_ID -f channel=production
```

Use `product=companion` for the Companion Store product. A successful dispatch
means only that the request was accepted, not that Microsoft accepted a package.
Use `product=gateway -f channel=development` for a beta flight request. Both
Gateway destinations use the same protected `microsoft-store-gateway` environment
and require release-manager approval; selecting Development never bypasses it.

The source job checks the actual environment protection, published source,
artifact identity, package identity/version, and bundle bytes without Store
credentials. Review its summary before approving: source and release-identity
tags/commits, source pipeline/run/attempt, package version, artifact ID, publisher
code commit, and bundle SHA-256. Gateway's payload and independently selected
release identity remain separate facts. Approval also binds the Store destination
and configured flight GUID. Main-only source pipelines must belong to the actual
protected main branch history; an unqualified run branch name is not sufficient.
Build qualification owns MSIX composition,
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
and do not cancel an active upload, including concurrent production/flight requests.

## Gateway beta Development flight

Gateway betas are delivered through the existing **Development** package flight,
not the public production submission or a separate public `/beta` listing. Enroll
testers' Microsoft Store accounts in that flight's known-user group. Flight IDs
are product-specific; do not use the Companion flight or the numeric initial
submission ID. Verify the GUID with Microsoft's
[flight API](https://learn.microsoft.com/en-us/windows/uwp/monetize/get-a-flight).

Configure these **repository Actions variables in `openclaw/releases`**, not
environment overrides or caller inputs:

- `MSSTORE_GATEWAY_DEVELOPMENT_FLIGHT_ID`: the verified Gateway flight GUID. It
  is nonsecret so the credential-free source job can show it before approval.
- `MSSTORE_GATEWAY_DEVELOPMENT_ENABLED`: leave unset until qualification, then
  set to `true` to admit automated beta requests. Case variants of `true` work.

After setup, use an explicit manual request with `channel=development` and
`automatic=false` for qualification. It still validates the source and requires
release-manager approval. Finish or explicitly resolve the portal-created initial
draft; the publisher never adopts or deletes a foreign draft. Verify commit
acceptance, certification, and an enrolled tester's real Store install/upgrade
with retained data before activating automation. Neither an existing flight nor
passing fixtures establish this live delivery proof.

The coordinated core handoff sends `automatic=true`, builds the exact published
beta version/commit with packaging `release_channel=beta`, `signing_mode=official`,
and `publish_release=true`, then requests the central Development destination.
It retains signed GitHub assets and a separate unsigned Store bundle; sideload
packages are never uploaded to the Store. Use a protected release-tooling cut
containing that handoff; merging main does not update older frozen tooling refs.

Gateway source runs must retain `openclaw-gateway-msix-store-submission-<attempt>`,
`store-release-source-<attempt>`, and the immutable source-resolution artifact.
The witness binds run/attempt, pipeline commit, release channel/tag, bundle name,
and SHA-256. Missing historical witnesses are rejected, not reconstructed. Beta
also requires the published packaging prerelease to match that pipeline commit.
Production and Development cannot consume each other's release channel. Store
version allocation remains the builder's shared revision-zero stable/beta
sequence, with its existing installed-upgrade proof; the central publisher does
not allocate another version or rebuild the bundle.

The flight GUID, activation flag, source authority, and approved bytes are checked
again after approval. Pausing automation or changing the flight while a request
waits prevents that old approval from publishing. The publisher uses
[`flightPackages` and flight-scoped submissions](https://learn.microsoft.com/en-us/windows/uwp/monetize/manage-flight-submissions),
preserves flight settings and foreign production drafts, and retains channel,
flight GUID, and Microsoft commit acceptance in its receipt. No extra Store
identity, PAT, per-flight environment, or federation is required.

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
8. For Gateway, land [beta support #246](https://github.com/openclaw/openclaw-windows-packaging/pull/246)
   and [Store flight artifacts #247](https://github.com/openclaw/openclaw-windows-packaging/pull/247)
   before the [request-only cutover #212](https://github.com/openclaw/openclaw-windows-packaging/pull/212),
   [Companion request-only cutover](https://github.com/openclaw/openclaw-windows-node/pull/1891),
   and [core handoff](https://github.com/openclaw/openclaw/pull/181446) together with
   the central owner. Preserve Node's separate stable-promotion gate. Gateway packaging's
   compatibility request is manual-only; core owns its normal automatic request,
   avoiding duplicate native/core dispatches. Companion's `MSSTORE_ENABLED` switch
   may queue requests after a successful eligible stable release; it never bypasses
   central approval. No new PAT or persistent Microsoft Store secret is required.
   Copy the native Gateway flight GUID into the central repository variable above,
   and retire native `MSSTORE_ENABLED` / `MSSTORE_DEVELOPMENT_ENABLED` flags.
   Keep Development automation disabled until its qualified manual rehearsal.

Use `gh api repos/openclaw/releases/environments/ENV` and its
`deployment-branch-policies` endpoint to verify the exact team and main-only/no-bypass
settings. Check effective active rulesets and
`gh api repos/openclaw/releases/codeowners/errors?ref=main`; an existing or named
ruleset is not proof that code review is enforced.

After setup, first prove an ordinary writer can queue but not approve a request,
and that old/native identities, wrong refs, revoked source authority, and substituted
bundles are rejected. A live Store submission requires explicit release authority;
local fixtures and a configured identity do not establish live acceptance.

## Validate publisher changes locally

From the repository root in PowerShell 7:

```powershell
./tests/test-microsoft-store-authorization.ps1
./tests/test-microsoft-store-submission.ps1
./tests/test-microsoft-store-flight.ps1
./tests/test-microsoft-store-workflow.ps1
git diff --check
```

These use synthetic GitHub/Store responses and workflow handoff fixtures. They
cannot authenticate, submit a real bundle, prove environment enforcement, or
establish certification/tester delivery. Run the repository's Python and Node
workflow suites for CI/workflow changes as described in the README.

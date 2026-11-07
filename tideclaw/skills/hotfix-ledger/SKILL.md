---
name: hotfix-ledger
description: Operate the OpenClaw hotfix ledger through its authenticated HTTPS API, including CRUD, assessments, deletion, audit, bulk operations, and scoped recovery. Does not authorize shipping releases.
---

# Hotfix ledger

Base URL: `https://hotfix-ledger.openclaw.ai`. Use its HTTPS API for routine operations, not direct SQL.

## Authentication and contract discovery

Use the existing OpenClaw managed secret-egress path:

| Protected binding | Request header |
| --- | --- |
| `HOTFIX_LEDGER_CF_ACCESS_CLIENT_ID` | `CF-Access-Client-Id` |
| `HOTFIX_LEDGER_CF_ACCESS_CLIENT_SECRET` | `CF-Access-Client-Secret` |

Use Gateway-hosted execution with protected egress enabled and both bindings allowing `hotfix-ledger.openclaw.ai`. Pass injected opaque sentinels unchanged in the headers; native shell, sandbox, and remote-node commands do not inherit them. Without bindings, use hotfix ledger credentials from the local credential manager. If stored as `Header-Name: value`, strip the matching prefix and whitespace inside the loader; do not alter managed sentinels. Keep values out of chat, model context, logs, and artifacts. If credentials are unavailable, continue local release evidence and reconcile later.

Native API clients should send `Accept: application/json` and an identifying User-Agent, such as `OpenClaw-Hotfix-Ledger/1.0`. In verified production, the default Python client received Cloudflare edge error 1010 before the Worker; Node with an identifying User-Agent succeeded. Do not disable Access or weaken edge policy to diagnose a client failure.

Read these authenticated endpoints before work:

- `GET /v1/health`: expect 200, `{"ok":true}`, backend `d1-worker`.
- `GET /v1/capabilities`: deployed version/commit, schema version, supported permissions and limits.
- `GET /v1/openapi.json`: authoritative fields, enums, schemas and route methods; consult relevant operations rather than guessing request bodies.

All endpoints require authentication, including docs/admin. Actor and assessor come from the verified identity; do not submit either field. The existing service identity has business and administrative capabilities, but use them only within the human's task scope.

## Mutations, retries, and lists

Mutations require `Content-Type: application/json`, `Idempotency-Key`, and `X-Change-Reason`. Keys are 8–200 characters from letters, digits, `.`, `_`, `:`, `-`; reasons are nonempty, at most 2000 characters. Serialize JSON once and retain those exact bytes.

Replaying a completed operation requires the same authenticated actor, method, path, raw JSON bytes and key. It returns the original response with `Idempotency-Replayed: true`, even after deletion; replay never resurrects a row. Different content with the same key conflicts. Resolve uncertain writes with exact replay and authoritative GET, not a new creation key. Previews save no receipt; use a new key for execution.

PATCH and DELETE require the current `expectedRevision`. PATCH also needs at least one changed field. Assessment pair PUT uses revision 0 only for creation and the current revision for updates. Stale writes return 409. Optional omitted update fields persist. Business writes, audit and receipts commit atomically.

Lists return `{items, next}`. Follow `after=next` until null; `limit` is 1–100, default 50. Business lists order by ID; audit uses a numeric ID/cursor. Repository is `owner/name`, not a URL; URL-encode query values.

| Entity | Create | Individual read/update/delete | List |
| --- | --- | --- | --- |
| Hotfix | POST `/v1/hotfixes` | GET/PATCH/DELETE `/v1/hotfixes/{id}` | GET `/v1/hotfixes` |
| Release | POST `/v1/releases` | GET/PATCH/DELETE `/v1/releases/{id}` | GET `/v1/releases` |
| Assessment | PUT `/v1/releases/{releaseId}/hotfixes/{hotfixId}` | GET/PATCH/DELETE `/v1/assessments/{id}`; pair GET/PUT also supported | GET `/v1/assessments` |

Hotfix creation needs `repository`, `sourceUnitKey`, `summary`, `impact`, `severity`, `rationale`, `confidence`, `eligibility`. Release creation needs `repository`, `releaseKey`, `name`, `channel`, `gitRef`, `observedHeadSha`, `state`. Both allow explicit IDs; otherwise IDs are generated. Assessment PUT requires `expectedRevision`, `applicability`, `handling`, `assessedSha`; parents must share a repository. Use OpenAPI for optional fields and enum values. Repository and assessment relationships are immutable.

All business lists support `repository` and `q` (substring of summary/name/notes). Additional filters:

- Hotfix: `eligibility`, `severity`, `sourceUnitKey`.
- Release: `channel`, `state`, `releaseKey`.
- Assessment: `releaseId`, `hotfixId`, `applicability`, `handling`, `stale=0|1`.

Reference/dependency/evidence arrays contain strings, not objects. `stale` is numeric 0/1 comparing `assessedSha` with release `observedHeadSha`; GET/list also returns `currentHeadSha`. Reassess against the real head rather than merely relabeling old evidence. Archive/unarchive releases with revision-checked `state: archived|active`; archive remains listed and is not deletion. Hotfix eligibility is not archive.

## Permanent deletion

1. GET the intended ID/repository/revision.
2. DELETE with `{expectedRevision, dryRun:true}` and mutation headers; inspect `assessments`, `references`, and `blocked`.
3. Explicit `cascade:true` permits atomic deletion of linked assessments with their parent, never unrelated hotfixes/releases. Hotfix dependencies in other records still block cascade. Exact IDs and `hotfix:<id>` are machine references; free text is not. Repair those references explicitly with authorized revision-checked updates, then preview again.
4. Execute with a new key and current revision, omitting `dryRun`; include cascade only when intended.
5. Verify individual GET is 404 and the ID is absent from every relevant list page; check unrelated data remains intact.

Repeat deletion with a new key returns 404; exact successful-key replay returns its saved response. Deleted business rows disappear; immutable audit retains `beforeJson` and `afterJson:null`. Normal create/import cannot reuse historical IDs. Named backup restore is the explicit recovery path.

## Audit, diagnosis, and recovery

- `GET /v1/audit-events`: filters `entityType=hotfix|release|release_hotfix`, `entityId`, pagination. Before/after JSON are decoded objects/null. Audit cannot be modified.
- `GET /v1/admin/diagnostics?repository=owner%2Frepo`: counts, stale assessments, dangling `hotfix:` references; foreign-key check is database-wide. Diagnostics do not rewrite records. Reconcile with explicit revision-checked updates.
- `GET /v1/admin/migrations`: applied/expected migrations and operator procedure. Future migrations require independent provider backup, disposable rehearsal, reviewed migration/deployment and verification. No arbitrary SQL or shell API.

Errors include `requestId`/`X-Request-Id`. Preserve status/code/ID, not credentials. Correct 400/413/414/415 input issues; investigate 401/403 authentication/identity; 404 is absent target/route. Reconcile 409 revision/key/dependency/preview conflicts before retrying. Unexpected 500 requires operator diagnosis. A Cloudflare edge response without backend/request-ID headers is not proof of a Worker failure.

### Export/import

GET `/v1/admin/export?repository=owner%2Frepo` returns `{format:"hotfix-ledger/v1",repository,hotfixes:[],releases:[],assessments:[]}`. Retain complete exported records. Audit, receipts, backups and derived freshness fields are excluded. Snapshot limit is 1,500,000 bytes; recovery also allows at most 150 total business records.

POST `/v1/admin/import` with `{repository,snapshot}` for validated create-only preview. Existing/historical IDs conflict, all rows must match scope, and assessment parents must be included. Execute with the same scope/snapshot, `execute:true`, returned `previewHash`, and a new key. Import is atomic. Changed scope state invalidates the preview; authoritative revisions/actor are newly recorded, not imported as history.

### Backup/restore

POST `/v1/admin/backups` with `{repository}` creates an immutable logical snapshot, returning 201, ID/hash and `status:complete`. GET `/v1/admin/backups/{id}` for metadata/status; list with repository and pagination.

POST `/v1/admin/restore` with `{repository,backupId}` for preview. Inspect every change and `preservedExtraRecords`; execute with `execute:true`, current `previewHash`, and a new key. Restore atomically merges backup records, can recreate deleted IDs with increasing revisions, preserves extra current rows, and preserves old audit/receipts. It is not reset-all or an exact rewind.

Logical backups share D1 with business data and are not independent disaster recovery. Full database recovery uses operator-owned D1 SQL export/Time Travel. Rehearse import/restore on disposable environments, not by overwriting production for an acceptance test.

### Bulk

POST `/v1/admin/bulk` with `{repository,items:[{method,path,body}]}`. Paths are business `/v1` routes; all targets/creates must match scope. POST creates require explicit IDs. Maximum 20 items.

Default preview validates current state, not hypothetical earlier items. Execute with `execute:true` and a new key. Execution is sequential and not atomic as a whole; inspect every per-item status even when the envelope is HTTP 200. Each successful item is atomic and has a stable child receipt for interrupted-retry safety. Reconcile before submitting a revised batch with a new key.

## Acceptance and delivery

Use unique synthetic IDs/source keys and record preexisting state. Prove CRUD, empty/populated and filtered/paginated lists, stale-revision rejection, exact replay, assessment freshness, dependency conflicts and explicit cascade. Delete only owned synthetic entities and verify absence plus unchanged unrelated records; audit remains intentionally. Report exact leftover IDs if cleanup fails.

This file is a replacement skill artifact. Delivery does not mean it is installed in Roboclaw's Team skill store. Its installation owner should publish/refresh through the existing skill workflow; do not restart or alter a live Gateway solely to install it. The authenticated OpenAPI contract is already available independently of skill rollout.

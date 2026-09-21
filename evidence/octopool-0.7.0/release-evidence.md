# OpenClaw Release Evidence: octopool-0.7.0

Generated: 2026-09-21T16:08:25.656Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.7.0` |
| Release ref input | not recorded |
| Release ref status | not-recorded |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 6 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `source-ci` | CI | `main` | `641ce3c3e734` | 6m 7s | 9m 47s | 9s | [35581140905](https://github.com/openclaw/octopool/actions/runs/35581140905) | 0 |
| pass | blocking | `source-codeql` | Push on main | `main` | `641ce3c3e734` | 1m 58s | 4m 0s | 10s | [35581140115](https://github.com/openclaw/octopool/actions/runs/35581140115) | 0 |
| pass | blocking | `release-commit-ci` | CI | `main` | `59aaed9fef09` | 5m 54s | 9m 0s | 3s | [35618333962](https://github.com/openclaw/octopool/actions/runs/35618333962) | 0 |
| pass | blocking | `release-commit-codeql` | Push on main | `main` | `59aaed9fef09` | 1m 52s | 3m 55s | 4s | [35618333351](https://github.com/openclaw/octopool/actions/runs/35618333351) | 0 |
| pass | blocking | `release-artifacts` | release | `main` | `59aaed9fef09` | 1m 32s | 1m 27s | 4s | [35620950142](https://github.com/openclaw/octopool/actions/runs/35620950142) | 0 |
| pass | blocking | `homebrew-promotion` | Update octopool for v0.7.0 (request-id=octopool-0.7.0-311cee92f06c; source-tag-object=4eb59d9d2ad6e84658c368114f8861908a2e2dc5; source-tag-commit=59aaed9fef09930ff2d475aca91c08efd62ee603) | `main` | `b46c3bef9d54` | 1m 48s | 1m 35s | 12s | [35622721906](https://github.com/openclaw/homebrew-tap/actions/runs/35622721906) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 59s | `source-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35581140905/job/106274053174) |
| 5m 50s | `release-commit-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35618333962/job/106394748246) |
| 3m 48s | `source-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35581140905/job/106274052788) |
| 3m 10s | `release-commit-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35618333962/job/106394747916) |
| 1m 48s | `source-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35581140115/job/106274055335) |
| 1m 47s | `release-commit-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35618333351/job/106394754714) |
| 1m 35s | `homebrew-promotion` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35622721906/job/106409492994) |
| 1m 27s | `release-artifacts` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35620950142/job/106403562869) |
| 1m 26s | `release-commit-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35618333351/job/106394754910) |
| 1m 25s | `source-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35581140115/job/106274054974) |
| 47s | `source-codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35581140115/job/106274055238) |
| 42s | `release-commit-codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35618333351/job/106394754398) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 12s | 1m 35s | `homebrew-promotion` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35622721906/job/106409492994) |
| 10s | 1m 25s | `source-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35581140115/job/106274054974) |
| 10s | 47s | `source-codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35581140115/job/106274055238) |
| 9s | 3m 48s | `source-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35581140905/job/106274052788) |
| 9s | 1m 48s | `source-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35581140115/job/106274055335) |
| 7s | 5m 59s | `source-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35581140905/job/106274053174) |
| 4s | 42s | `release-commit-codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35618333351/job/106394754398) |
| 4s | 1m 47s | `release-commit-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35618333351/job/106394754714) |
| 4s | 1m 26s | `release-commit-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35618333351/job/106394754910) |
| 4s | 1m 27s | `release-artifacts` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35620950142/job/106403562869) |
| 3s | 3m 10s | `release-commit-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35618333962/job/106394747916) |
| 3s | 5m 50s | `release-commit-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35618333962/job/106394748246) |

## Notes

Octopool 0.7.0 is published at https://github.com/openclaw/octopool/releases/tag/v0.7.0.

Source commit: `59aaed9fef09930ff2d475aca91c08efd62ee603`. Signed annotated tag object: `4eb59d9d2ad6e84658c368114f8861908a2e2dc5`.

Both Darwin binaries are signed with Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), notarized (Accepted), and pass strict signature, hardened runtime and Gatekeeper checks after public redownload. All six public archives match final checksums. Linux and Windows bytes were unchanged during signing. Native version: `octopool 0.7.0 (59aaed9, 2026-09-21T15:44:21Z)`.

Final checksums.txt SHA-256: `d2cd1a5a25e416ab34cec27b8fe3974a40c1380b051534041a36e8d8afb9b797`. Homebrew promotion `59ef602082761436a59930e87cecc079c4324f53` matches the reviewed four-platform formula and final hashes.

| Asset | SHA-256 |
|---|---|
| octopool_0.7.0_darwin_amd64.tar.gz | `c9e119206187d445691b52db0eb7500cb76629e66fe9a438ff2c0525473cb2d6` |
| octopool_0.7.0_darwin_arm64.tar.gz | `5bf911aebdb057c1389a096564deb3becdec9220a95585ab55d8ed99e68c215d` |
| octopool_0.7.0_linux_amd64.tar.gz | `efedbea89c91276112a090107c637157fc5ed0e1287369fbbf24adff22faf180` |
| octopool_0.7.0_linux_arm64.tar.gz | `de241e89e3a1cdfa7cd9429dcc6fb298369e7c3fb9f08117aadaab65f322e372` |
| octopool_0.7.0_windows_amd64.zip | `5a0cf91e6f7d18c063f6d2f27d08c04672eee8d9dd69754f677d327852eada9b` |
| octopool_0.7.0_windows_arm64.zip | `c6abaf365a3231b8af15432f879c7f4d5459adf1842d005e466616524f9553cc` |

Both Workers serve the release commit at 100%. Health is 3/3. The published CLI passed fresh production relay-only PR v2, issue list, tagged release metadata and latest release metadata reads. A Homebrew canary passed exact binary hash/version, signature/Gatekeeper, both shell relay paths and preservation of enrollment, native tools and prior service instances. No fleet-wide performance or GitHub quota-saving claim is inferred.

The initial tag-triggered Actions run failed at startup with zero jobs. One documented workflow_dispatch recovery succeeded; no artifact job was retried after publication.

The published release body matches this finalized changelog:

## 0.7.0 - 2026-09-21

### Features

- Serve PR merge commit, draft, author, and head-owner projections from the public PR page with `pr-summary-v2`, hydrating login-only identities and retrying incomplete projections through exact relay reads while preserving freshness.
- Read public release tags, URLs, publication times, and draft/prerelease flags from GitHub pages for metadata-only release views, retaining exact API responses for names, raw Markdown, creation times, and release lists.

### Fixes

- Parse manually triggered Actions run timestamps with exact graph evidence, cap list-page hydration at eight cards with its own shared 2500 ms deadline after the normally timed list fetch, and abort failed enrichment without publishing partial lists.
- Report schema and field requirements for invalid guarded REST payloads while preserving rewrite-policy confidentiality and blocked-error compatibility.
- Accept all GitHub REST merge methods and omitted merge defaults under string rewrite protection, resolving and pinning the current PR head when `sha` is omitted.
- Keep supported issue views and complete issue lists readable from public HTML when API quota is exhausted, without requiring unused assignee pagination data; requested labels still require completeness, and assignee/milestone selections retain exact API handling.
- Fall back to guarded local gh sooner on pool cooldowns with one default retry after one second, and cap shim relay read attempts at 20 seconds with configurable timeouts that never retry, preserving no-fallback and watch ownership rules.
- Reuse the shared one-hour workflow catalogue for PR status-check rollups while keeping checks and runs live; retry missing workflow names once live for rollups and ordinary checks, preserving fresh watch confirmation and `OCTOPOOL_FRESH=1`.
- Try available no-quota pages before anonymous API revalidation, skip unusable zero-age body-cache reads while retaining validators and fill ownership, and avoid retrying depleted anonymous quota for Actions completion proof; clarify that GitHub REST 304 validations consume quota.
- Restore token-free page reuse for human Actions run views/lists and watch reads against current GitHub markup, preserve capped list counts as lower bounds, paginate complete job groups, and render skipped jobs without inventing timestamps.
- Read exact Actions events from the run-owned workflow graph and reject ambiguous trigger prose, falling back to REST for the whole list when any hydrated event remains unproven.

### Upgrade notes

- Deploy both Workers and upgrade the CLI for the new PR/release HTML projections, Actions page repairs, and faster guarded fallback. Older CLIs keep working on `pr-summary-v1`. No database migration, re-login, or cache purge is required.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


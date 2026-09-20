# OpenClaw Release Evidence: octopool-0.6.8

Generated: 2026-09-20T08:19:14.191Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.8` |
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
| Blocking | 4 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `ci` | CI | `main` | `ac914d7e3b78` | 5m 34s | 9m 4s | 3s | [35496323908](https://github.com/openclaw/octopool/actions/runs/35496323908) | 0 |
| pass | blocking | `codeql` | Push on main | `main` | `ac914d7e3b78` | 1m 35s | 3m 34s | 4s | [35496323610](https://github.com/openclaw/octopool/actions/runs/35496323610) | 0 |
| pass | blocking | `release` | release | `v0.6.8` | `ac914d7e3b78` | 1m 32s | 1m 28s | 3s | [35496610962](https://github.com/openclaw/octopool/actions/runs/35496610962) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.6.8 (request-id=octopool-0.6.8-20260920-b4e0f4b41912; source-tag-object=1ff3ada2de300d2e83ce3b6f4aa7efba545fa59f; source-tag-commit=ac914d7e3b78ada9201f58436c01f7708a586c79) | `main` | `2595e8277386` | 1m 40s | 1m 32s | 7s | [35498232500](https://github.com/openclaw/homebrew-tap/actions/runs/35498232500) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 31s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35496323908/job/106039836350) |
| 3m 33s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35496323908/job/106039836233) |
| 1m 32s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35496323610/job/106039837121) |
| 1m 32s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35498232500/job/106045141669) |
| 1m 28s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35496610962/job/106040627159) |
| 1m 23s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35496323610/job/106039837181) |
| 39s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35496323610/job/106039837103) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 7s | 1m 32s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35498232500/job/106045141669) |
| 4s | 1m 23s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35496323610/job/106039837181) |
| 3s | 5m 31s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35496323908/job/106039836350) |
| 3s | 39s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35496323610/job/106039837103) |
| 3s | 1m 32s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35496323610/job/106039837121) |
| 3s | 1m 28s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35496610962/job/106040627159) |
| 2s | 3m 33s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35496323908/job/106039836233) |

## Notes

Octopool 0.6.8 is published at https://github.com/openclaw/octopool/releases/tag/v0.6.8 .

Source commit: ac914d7e3b78ada9201f58436c01f7708a586c79. Signed annotated tag object: 1ff3ada2de300d2e83ce3b6f4aa7efba545fa59f, with GitHub signature verification valid. The published release body matches the finalized dated changelog below.

Both Darwin executables were signed with Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), notarized with Apple Accepted status, and verified with strict signature, hardened-runtime and Gatekeeper checks. Fresh public downloads of all six archives and their extracted binaries match the final inventory. Linux and Windows retain their CI-produced bytes.

Version output: octopool 0.6.8 (ac914d7, 2026-09-20T07:20:47Z).

Final archive SHA-256 values:

- octopool_0.6.8_darwin_amd64.tar.gz: 6fa79530d292f993a7b67e4651a1a9dca5fdcaa593b915ce06127ec69c1fbd84
- octopool_0.6.8_darwin_arm64.tar.gz: 13eb05f6936c660c2063c040941a686de2d23445bac17acb35c6d683997281e0
- octopool_0.6.8_linux_amd64.tar.gz: 2f41c3483c130f5cffcda393a8e18bb7a85abb83cd622a02435e42979b5b9e54
- octopool_0.6.8_linux_arm64.tar.gz: d7a3b35f18fdf3ad7632f2651a57be1576a780a71b81d89de79b67579d7c11a1
- octopool_0.6.8_windows_amd64.zip: 2c1db18b90a44456ffb4e776f5cc29d8341362fd8c1989ac6e8f2ea6693b6416
- octopool_0.6.8_windows_arm64.zip: fde23d3fea37f656cf4ab4aa21a2af32c83ca33ab62f60070fb1065845d5ab16

Final executable SHA-256 values:

- octopool_0.6.8_darwin_amd64.tar.gz: 181571274d004c73dd66c141acb740d3fa2da83161e551913ecbf0c8feb70dde
- octopool_0.6.8_darwin_arm64.tar.gz: 095976cf4dd9c19401139de720cb2fba69c9bb613bf6b30e12b0f8f52c9a516d
- octopool_0.6.8_linux_amd64.tar.gz: 490736f8c1b2b4f481802090c54e10ef42abe7e1af9ef00f00bec89787745389
- octopool_0.6.8_linux_arm64.tar.gz: 5511aff1c6c35a8aeb668b8c18462b87f58078cd740335b366f61dd9b26d3e70
- octopool_0.6.8_windows_amd64.zip: 0697134faaf4736715faaec41332e30277480f529aeadb11931cefc2c489d82f
- octopool_0.6.8_windows_arm64.zip: b6330c267f1cd41bda4733fc848c1c20f0e0e1d4fa2ad5e657dedb9be0611880

Apple notarization submissions:

- darwin_amd64: ba06a70b-7235-4cb9-925f-d3e142e044b3 (Accepted)
- darwin_arm64: 311b30f0-5855-46af-b2a0-0192f0a30bcb (Accepted)

Homebrew promotion: https://github.com/openclaw/homebrew-tap/commit/87798e699eb0f90fc877da95dbcef340686664e6 . Formula SHA-256: 8fee466252d3095768e8d7aec7e284e53288b6d9e49347516842b6079b8ca2b4. Published formula bytes exactly match the independently reviewed candidate and all four final platform hashes.

Both Cloudflare Workers deployed from the release commit at 100% traffic: authoritative 0fee106c-0c02-4aa2-bba4-b7c8f8dfb22f; public proxy 8a1e0bcc-68a4-4c9b-b529-79d411f2d1a2. Public smoke checks on both hosts, authenticated pool health (2/2), and a no-fallback relay read passed. A nine-run production cache read retained identical results and reused cache; this is an outcome observation, not a quota measurement. No migration, re-login, or cache purge was performed.

Runtime source passed full CI and the compiled CLI to isolated Workerd/D1/Durable Object to public GitHub release gate. Scoped live proofs for the included fixes cover exact cache reuse, freshness, HTTP faults and output failures; deliberately injected faults are not claims of natural production incidents. The release commit only finalizes notes, with runtime code unchanged from the reviewed main cut.

Finalized changelog:

## 0.6.8 - 2026-09-20

### Fixes

- Fail JSON output on short writes or a failed final newline instead of reporting success, and emit quota notices only after complete output.
- Reuse complete short or empty shaped Actions run-list pages for smaller requests, avoiding redundant GitHub fetches while retaining count, pagination, freshness, and filtered-fallback checks.
- Honor `OCTOPOOL_FRESH=1` on direct request GET reads while preserving explicit cache-control headers, string protection, and raw response behavior.
- Keep fresh anonymous run-completion proof usable during pooled identity lookup failures, avoiding extra metadata requests and preserving the existing one-hour completed-attempt jobs cache.
- Reuse eligible bounded-stale responses during transient GitHub server, network, and timeout failures while preserving explicit freshness, cache expiry, quota feedback, and cold-request errors.
- Route machine-readable run lists filtered by commit or event through the shared REST cache, preserving native filter values, protected dispatch, and freshness controls.
- Reuse fresh larger shaped Actions run-list pages for small human-readable requests, preserving the first 25 runs, filtered totals, exact fallback, source expiry, and identity checks without another GitHub fetch.
- Honor explicit cache-age limits for completed Actions logs, checking upstream existence before forced-fresh reads while reusing unchanged log bytes.
- Stop run and PR-check watches immediately on oversized relay responses, avoiding repeated downloads and backoff delays.
- Stop first-page validators from refreshing complete Actions job aggregates without checking later pages, including entries cached by older Workers; single-page validation and existing cache lifetimes remain unchanged.
- Release discarded API and Actions-log redirect bodies before follow-up downloads, existence-probe completion, or redirect rejection, without changing redirect policy, credential handling, or log bytes.

### Upgrade notes

- Upgrade the CLI and deploy the Workers to receive all fixes. No database migration, re-login, or cache purge is required.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


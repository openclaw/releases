# OpenClaw Release Evidence: octopool-0.6.10

Generated: 2026-09-21T03:33:28.148Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.10` |
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
| Blocking | 8 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `pr-ci` | CI | `codex/scripts-pr-cache-coverage` | `c7059169c11c` | 5m 51s | 9m 2s | 3s | [35554375475](https://github.com/openclaw/octopool/actions/runs/35554375475) | 0 |
| pass | blocking | `pr-codeql` | PR #168 | `refs/pull/168/head` | `c7059169c11c` | 1m 17s | 2m 44s | 4s | [35554372096](https://github.com/openclaw/octopool/actions/runs/35554372096) | 0 |
| pass | blocking | `merged-main-ci` | CI | `main` | `1678170c6ffb` | 5m 44s | 9m 26s | 10s | [35555019160](https://github.com/openclaw/octopool/actions/runs/35555019160) | 0 |
| pass | blocking | `merged-main-codeql` | Push on main | `main` | `1678170c6ffb` | 1m 52s | 3m 48s | 13s | [35555018473](https://github.com/openclaw/octopool/actions/runs/35555018473) | 0 |
| pass | blocking | `release-commit-ci` | CI | `main` | `00c442d8084a` | 5m 1s | 8m 33s | 3s | [35555354524](https://github.com/openclaw/octopool/actions/runs/35555354524) | 0 |
| pass | blocking | `release-commit-codeql` | Push on main | `main` | `00c442d8084a` | 1m 47s | 4m 0s | 4s | [35555354059](https://github.com/openclaw/octopool/actions/runs/35555354059) | 0 |
| pass | blocking | `release-artifacts` | release | `v0.6.10` | `00c442d8084a` | 1m 28s | 1m 25s | 2s | [35555420897](https://github.com/openclaw/octopool/actions/runs/35555420897) | 0 |
| pass | blocking | `homebrew-promotion` | Update octopool for v0.6.10 (request-id=octopool-0.6.10-ce707f444a53; source-tag-object=13c38f749efe2b39d79db52496e1eb06f098d5fd; source-tag-commit=00c442d8084ad26eb5a5003f7372170e75a20c8a) | `main` | `d8da8276eab0` | 1m 22s | 1m 12s | 9s | [35556898483](https://github.com/openclaw/homebrew-tap/actions/runs/35556898483) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 47s | `pr-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35554375475/job/106195031363) |
| 5m 38s | `merged-main-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35555019160/job/106196889075) |
| 4m 58s | `release-commit-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35555354524/job/106197837434) |
| 3m 48s | `merged-main-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35555019160/job/106196889208) |
| 3m 35s | `release-commit-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35555354524/job/106197837357) |
| 3m 15s | `pr-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35554375475/job/106195031250) |
| 1m 42s | `release-commit-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555354059/job/106197838753) |
| 1m 41s | `merged-main-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555018473/job/106196889231) |
| 1m 28s | `release-commit-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555354059/job/106197838793) |
| 1m 25s | `release-artifacts` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35555420897/job/106198027507) |
| 1m 22s | `merged-main-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555018473/job/106196889255) |
| 1m 13s | `pr-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35554372096/job/106195025132) |
| 1m 12s | `homebrew-promotion` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35556898483/job/106202153307) |
| 50s | `release-commit-codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555354059/job/106197838690) |
| 49s | `pr-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35554372096/job/106195025156) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 13s | 1m 22s | `merged-main-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555018473/job/106196889255) |
| 10s | 3m 48s | `merged-main-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35555019160/job/106196889208) |
| 10s | 1m 41s | `merged-main-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555018473/job/106196889231) |
| 9s | 45s | `merged-main-codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555018473/job/106196889137) |
| 9s | 1m 12s | `homebrew-promotion` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35556898483/job/106202153307) |
| 5s | 5m 38s | `merged-main-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35555019160/job/106196889075) |
| 4s | 42s | `pr-codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35554372096/job/106195025031) |
| 4s | 1m 13s | `pr-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35554372096/job/106195025132) |
| 4s | 49s | `pr-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35554372096/job/106195025156) |
| 4s | 50s | `release-commit-codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555354059/job/106197838690) |
| 4s | 1m 42s | `release-commit-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555354059/job/106197838753) |
| 4s | 1m 28s | `release-commit-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35555354059/job/106197838793) |
| 3s | 3m 15s | `pr-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35554375475/job/106195031250) |
| 3s | 5m 47s | `pr-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35554375475/job/106195031363) |
| 3s | 3m 35s | `release-commit-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35555354524/job/106197837357) |

## Notes

Octopool 0.6.10 is published at https://github.com/openclaw/octopool/releases/tag/v0.6.10.

Source commit: `00c442d8084ad26eb5a5003f7372170e75a20c8a`. Signed annotated tag object: `13c38f749efe2b39d79db52496e1eb06f098d5fd`; GitHub reports the signature verified.

Both Darwin binaries are signed with Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), notarized (Accepted), and pass strict signature, hardened runtime, and Gatekeeper Notarized Developer ID checks after public re-download. All six public archives match the final checksums; Linux and Windows bytes were unchanged during signing. Each binary build record identifies the exact clean release commit and expected OS/architecture. Native version: `octopool 0.6.10 (00c442d, 2026-09-21T02:49:17Z)`.

Final checksums.txt SHA-256: `795fc3a598985a802c7f1d77635ff0d3d460560789aaace2e0d51105c09f57db`.

| Asset | SHA-256 |
|---|---|
| octopool_0.6.10_darwin_amd64.tar.gz | `d56b710d9fd78a022334a681213ff5240db28fcd5b86fb0ef56bd4aac48dd72e` |
| octopool_0.6.10_darwin_arm64.tar.gz | `b19838c5dc35b1df4e5b6de74daf22ad77dbbb715d62afe1184f7d28acdb53e8` |
| octopool_0.6.10_linux_amd64.tar.gz | `c108d30fb5e013e0a3296d2bd6112115e07c13c74a61e69a0cf5899b9a5489fa` |
| octopool_0.6.10_linux_arm64.tar.gz | `4b4f00ce08b5fd7fdf438d35b08104e02addca48d0ecac14c2857606ba08e6f2` |
| octopool_0.6.10_windows_amd64.zip | `99b0567cc1d2aa5d8b0f761104766f5650b28f91b420584cd14941d66cec27eb` |
| octopool_0.6.10_windows_arm64.zip | `adeebaadd9a4756419c0a3be6797db080c194867a78616a1aef2143a246751ce` |

Both Workers serve this release commit at 100%; public health, two healthy pooled identities, and a forced-fresh relay-only public repository read passed. PR #168 was independently reviewed, with final matching/older Worker proof against real public GitHub, explicit cache reuse and preserved freshness. Isolated cache-hit timings do not establish fleet-wide gains or GitHub quota savings.

After installation, the published CLI also passed nine production GraphQL reads against public PR166 with native fallback disabled. Each of the three query shapes reported a shared-cache hit on its opted-in repeat; default-fresh reads completed successfully and all three observations per shape returned identical JSON.

The published release body matches the finalized changelog exactly:

## 0.6.10 - 2026-09-20

### Features

- Relay machine-readable run lists filtered by `--created` through the shared cache, preserving GitHub date/range syntax, explicit freshness, and guarded native fallback.

### Fixes

- Keep explicit GitHub.com API reads on the relay and pool the landing tools' exact public PR CI and merge-snapshot GraphQL queries, preserving live reads by default, opt-in bounded reuse, local protection rules, and upstream failures; viewer-dependent previews retain local credentials.
- Reuse complete raw Actions jobs pages across smaller page sizes without changing REST bodies, source expiry, identity eligibility, or explicit freshness.
- Avoid repeating an anonymous API request after rate-limited cache revalidation, retaining public HTML fallback, live visibility and identity checks, and normal anonymous attempts on later requests.
- Acquire PR check-runs and statuses concurrently to reduce checks, rollup, and watch latency while preserving per-request policy checks, bounded pagination, output order, and terminal errors before native fallback.
- Acquire PR-check Actions runs and workflow catalogues concurrently after validating check identities, reducing metadata latency while preserving complete pagination, workflow associations, lazy skipping, and terminal-error handling.

### Upgrade notes

- Upgrade the CLI and deploy both Workers for pooled landing reads, broader cache reuse, and faster PR-check metadata. Newly routed explicit-host REST and landing GraphQL reads stay fresh by default; advisory reads can opt into bounded reuse. No database migration, re-login, or cache purge is required.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


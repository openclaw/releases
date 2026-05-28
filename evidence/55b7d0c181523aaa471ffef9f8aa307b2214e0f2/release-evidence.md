# OpenClaw Release Evidence: 55b7d0c181523aaa471ffef9f8aa307b2214e0f2

Generated: 2026-05-13T07:04:30.570Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `55b7d0c181523aaa471ffef9f8aa307b2214e0f2` |
| Release ref input | `55b7d0c181523aaa471ffef9f8aa307b2214e0f2` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `55b7d0c181523aaa471ffef9f8aa307b2214e0f2` |
| Release ref SHA | `55b7d0c181523aaa471ffef9f8aa307b2214e0f2` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/55b7d0c18152-1778654417215` | `55b7d0c18152` | 23m 44s | 57m 28s | 23m 11s | [25782903029](https://github.com/openclaw/openclaw/actions/runs/25782903029) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/55b7d0c18152-1778654417215` | `55b7d0c18152` | 3m 14s | 1h 0m 8s | 3m 11s | [25782922657](https://github.com/openclaw/openclaw/actions/runs/25782922657) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/55b7d0c18152-1778654417215` | `55b7d0c18152` | 21m 58s | 5h 27m 49s | 21m 55s | [25782921450](https://github.com/openclaw/openclaw/actions/runs/25782921450) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/55b7d0c18152-1778654417215` | `55b7d0c18152` | 3m 49s | 3m 33s | 15s | [25783062793](https://github.com/openclaw/openclaw/actions/runs/25783062793) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 22m 50s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25782903029/job/75729414763) |
| 22m 21s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782903029/job/75729414811) |
| 16m 6s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730106278) |
| 13m 36s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730015749) |
| 9m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75729781727) |
| 7m 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730551882) |
| 7m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730551856) |
| 7m 12s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730015823) |
| 6m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75729781673) |
| 6m 54s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75729781726) |
| 6m 31s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730442051) |
| 6m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75729781721) |
| 4m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782903029/job/75729875460) |
| 3m 47s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782903029/job/75729414769) |
| 3m 33s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25783062793/job/75729902498) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 23m 11s | 32s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25782903029/job/75732355953) |
| 21m 55s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75732248169) |
| 17m 0s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75731581555) |
| 9m 8s | 4m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730551867) |
| 9m 8s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730551877) |
| 9m 8s | 7m 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730551882) |
| 9m 8s | 3m 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730551897) |
| 9m 7s | 4m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730551833) |
| 9m 7s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730551837) |
| 9m 7s | 4m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730551853) |
| 9m 7s | 7m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75730551856) |
| 4m 2s | 4m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782903029/job/75729875460) |
| 3m 11s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782922657/job/75729832167) |
| 3m 10s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25782922657/job/75729842875) |
| 3m 6s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782922657/job/75729832176) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25782903029
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25782903029/job/75729414763
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25782903029/job/75732355953
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25782922657
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25782922657/job/75729832173
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25782922657/job/75729842875
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25782921450
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: failure - https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75729781703
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25782921450/job/75732248169

## Notes

Automatically requested by Full Release Validation 25782903029 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


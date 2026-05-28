# OpenClaw Release Evidence: 021373a4541e53cc5a29e7cd672e578a96fe3276

Generated: 2026-05-04T21:24:45.299Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `021373a4541e53cc5a29e7cd672e578a96fe3276` |
| Release ref input | `021373a4541e53cc5a29e7cd672e578a96fe3276` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `021373a4541e53cc5a29e7cd672e578a96fe3276` |
| Release ref SHA | `021373a4541e53cc5a29e7cd672e578a96fe3276` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/021373a4541e-1777926880078` | `021373a4541e` | 49m 35s | 1h 17m 54s | 49m 8s | [25342091128](https://github.com/openclaw/openclaw/actions/runs/25342091128) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/021373a4541e-1777926880078` | `021373a4541e` | 6m 27s | 1h 20m 22s | 6m 24s | [25342112377](https://github.com/openclaw/openclaw/actions/runs/25342112377) | 4 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/021373a4541e-1777926880078` | `021373a4541e` | 47m 59s | 13h 40m 21s | 47m 56s | [25342113747](https://github.com/openclaw/openclaw/actions/runs/25342113747) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/021373a4541e-1777926880078` | `021373a4541e` | 3m 48s | 2m 13s | 1m 34s | [25342221983](https://github.com/openclaw/openclaw/actions/runs/25342221983) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 48m 37s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342091128/job/74301739949) |
| 42m 25s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74302505495) |
| 22m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74302188899) |
| 22m 21s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74302189012) |
| 21m 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74303189733) |
| 21m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74302188830) |
| 20m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74302188898) |
| 20m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74302188890) |
| 20m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74302189043) |
| 19m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74302188850) |
| 19m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74302188871) |
| 15m 19s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342091128/job/74301739951) |
| 6m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342091128/job/74301739979) |
| 4m 22s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342091128/job/74302137119) |
| 4m 5s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342112377/job/74301808344) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 49m 8s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25342091128/job/74309356155) |
| 47m 56s | 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74309263131) |
| 33m 8s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74306697321) |
| 14m 26s | 1m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74303189754) |
| 14m 25s | 1m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74303189722) |
| 14m 25s | 1m 37s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74303189726) |
| 8m 58s | 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74303189720) |
| 8m 58s | 21m 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74303189733) |
| 8m 57s | 2m 4s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74303144743) |
| 8m 57s | 1m 18s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74303144750) |
| 8m 57s | 7m 20s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342113747/job/74303144756) |
| 6m 24s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342112377/job/74302795027) |
| 5m 40s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342112377/job/74302677675) |
| 5m 39s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342112377/job/74302677682) |
| 5m 34s | 3s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25342112377/job/74302677670) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25342091128
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25342091128/job/74309356155

## Notes

Automatically requested by Full Release Validation 25342091128 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


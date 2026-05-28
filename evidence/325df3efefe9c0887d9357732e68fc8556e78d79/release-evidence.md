# OpenClaw Release Evidence: 325df3efefe9c0887d9357732e68fc8556e78d79

Generated: 2026-05-05T09:42:29.396Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `325df3efefe9c0887d9357732e68fc8556e78d79` |
| Release ref input | `325df3efefe9c0887d9357732e68fc8556e78d79` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `325df3efefe9c0887d9357732e68fc8556e78d79` |
| Release ref SHA | `325df3efefe9c0887d9357732e68fc8556e78d79` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/325df3efefe9-1777970215501` | `325df3efefe9` | 1h 5m 5s | 1h 25m 35s | 1h 4m 30s | [25366254491](https://github.com/openclaw/openclaw/actions/runs/25366254491) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/325df3efefe9-1777970215501` | `325df3efefe9` | 4m 47s | 1h 20m 6s | 4m 42s | [25366274619](https://github.com/openclaw/openclaw/actions/runs/25366274619) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/325df3efefe9-1777970215501` | `325df3efefe9` | 1h 3m 33s | 13h 30m 23s | 1h 3m 30s | [25366271072](https://github.com/openclaw/openclaw/actions/runs/25366271072) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/325df3efefe9-1777970215501` | `325df3efefe9` | 2m 23s | 1m 47s | 36s | [25366373111](https://github.com/openclaw/openclaw/actions/runs/25366373111) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 4m 10s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366254491/job/74377778187) |
| 1h 0m 20s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378128610) |
| 32m 36s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378385706) |
| 28m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74379344905) |
| 24m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378129121) |
| 24m 2s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378129291) |
| 23m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378129129) |
| 23m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378129231) |
| 22m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378129165) |
| 22m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378129158) |
| 22m 11s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378129214) |
| 10m 18s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366254491/job/74377778206) |
| 5m 13s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366254491/job/74377778278) |
| 3m 47s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366274619/job/74377860672) |
| 2m 52s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366254491/job/74378126174) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 4m 30s | 35s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25366254491/job/74387456480) |
| 1h 3m 30s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74387348322) |
| 47m 45s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74384330383) |
| 15m 33s | 2m 0s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74379590678) |
| 15m 33s | 1m 29s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74379590717) |
| 15m 33s | 1m 6s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74379590721) |
| 15m 32s | 1m 58s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74379590673) |
| 15m 32s | 3m 6s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74379590682) |
| 15m 31s | 1m 59s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74379590651) |
| 15m 31s | 1m 37s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74379590654) |
| 15m 31s | 1m 28s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74379590662) |
| 4m 42s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366274619/job/74378465014) |
| 4m 42s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366274619/job/74378465025) |
| 4m 42s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366274619/job/74378480777) |
| 4m 36s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25366274619/job/74378464993) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25366254491
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25366254491/job/74387456480
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25366271072
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378128610
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74378535446
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25366271072/job/74387348322

## Notes

Automatically requested by Full Release Validation 25366254491 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 2026.5.10-beta.4

Generated: 2026-05-11T17:10:18.371Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.10-beta.4` |
| Release ref input | `v2026.5.10-beta.4` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.10-beta.4` |
| Release ref SHA | `28076586edee28aff2786615a7dcadc38c94c73e` |
| Runs at release SHA | none |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `788ef05384da` | 2h 5m 28s | 2h 23m 23s | 2h 4m 47s | [25678407279](https://github.com/openclaw/openclaw/actions/runs/25678407279) | 1 |
| fail | blocking | `normal-ci` | CI | `main` | `788ef05384da` | 51m 4s | 3h 51m 57s | 51m 1s | [25678438838](https://github.com/openclaw/openclaw/actions/runs/25678438838) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `fb4d18bcbab5` | 48m 48s | 6h 19m 33s | 51m 31s | [25678445075](https://github.com/openclaw/openclaw/actions/runs/25678445075) | 18 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `main` | `4bb7acd88b42` | 2h 0m 37s | 2h 0m 29s | 7s | [25678630188](https://github.com/openclaw/openclaw/actions/runs/25678630188) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 2h 0m 51s | `full-release-validation` | Run package Telegram E2E | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25678407279/job/75383600492) |
| 2h 0m 29s | `postpublish-telegram` | Run package Telegram E2E | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25678630188/job/75383655428) |
| 14m 42s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75384181313) |
| 13m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75383553898) |
| 12m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75383553899) |
| 12m 43s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75383553868) |
| 10m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75383553863) |
| 9m 43s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75383554066) |
| 9m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75383553867) |
| 9m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75383553931) |
| 9m 27s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75383553988) |
| 9m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75383553895) |
| 7m 18s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75383025133) |
| 7m 4s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75383025014) |
| 6m 52s | `normal-ci` | check-additional-extension-package-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75383025126) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2h 4m 47s | 40s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25678407279/job/75407015690) |
| 51m 31s | 1m 41s | `release-checks` | Run QA Lab parity report | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75393290223) |
| 51m 4s | 59s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75393246517) |
| 51m 1s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75393205539) |
| 51m 1s | 2s | `normal-ci` | check-additional | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75393226433) |
| 51m 0s | 59s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75393245679) |
| 51m 0s | 3m 11s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75393245869) |
| 50m 48s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75393180288) |
| 50m 48s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75393180297) |
| 50m 48s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75393180343) |
| 50m 7s |  | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75393081466) |
| 50m 7s |  | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75393081474) |
| 50m 7s |  | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75393081478) |
| 50m 7s |  | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75393081484) |
| 50m 7s |  | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25678445075/job/75393081491) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25678407279
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25678407279/job/75382894418
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25678407279/job/75382894438
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25678407279/job/75382894524
  - Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25678407279/job/75383600492
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25678407279/job/75407015690
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25678438838
  - checks-fast-protocol: failure - https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75383024799
  - check-test-types: failure - https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75383025003
  - check-lint: failure - https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75383025092
  - check-additional-boundaries-d: failure - https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75383025494
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75393038161
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25678438838/job/75393226433
- `postpublish-telegram`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25678630188
  - Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25678630188/job/75383655428

## Notes

Automatically requested by Full Release Validation 25678407279 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 766d02ff3b8901868168ce7dddec4d177b789c39

Generated: 2026-05-05T04:58:57.470Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `766d02ff3b8901868168ce7dddec4d177b789c39` |
| Release ref input | `766d02ff3b8901868168ce7dddec4d177b789c39` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `766d02ff3b8901868168ce7dddec4d177b789c39` |
| Release ref SHA | `766d02ff3b8901868168ce7dddec4d177b789c39` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/766d02ff3b89-1777951455806` | `766d02ff3b89` | 1h 34m 19s | 1h 44m 21s | 1h 33m 48s | [25356136430](https://github.com/openclaw/openclaw/actions/runs/25356136430) | 0 |
| pass | blocking | `normal-ci` | CI | `release-ci/766d02ff3b89-1777951455806` | `766d02ff3b89` | 3m 42s | 1h 16m 31s | 3m 39s | [25356147467](https://github.com/openclaw/openclaw/actions/runs/25356147467) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/766d02ff3b89-1777951455806` | `766d02ff3b89` | 1h 33m 9s | 12h 3m 7s | 1h 33m 6s | [25356150730](https://github.com/openclaw/openclaw/actions/runs/25356150730) | 5 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 33m 20s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356136430/job/74345723940) |
| 1h 30m 19s | `release-checks` | Run repo/live E2E validation / validate_repo_e2e | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345955017) |
| 1h 0m 17s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345955010) |
| 25m 20s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149166) |
| 24m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345955208) |
| 24m 17s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149187) |
| 21m 21s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345955214) |
| 20m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345955231) |
| 20m 4s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345955215) |
| 19m 56s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149175) |
| 19m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345955218) |
| 4m 10s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356136430/job/74345723942) |
| 3m 42s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356136430/job/74345723939) |
| 3m 22s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356147467/job/74345752374) |
| 2m 33s | `normal-ci` | checks-node-core-runtime-infra-state | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356147467/job/74345752537) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 33m 48s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25356136430/job/74353143495) |
| 1h 33m 6s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74353117919) |
| 5m 20s | 3m 22s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149252) |
| 5m 18s | 17m 3s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149170) |
| 5m 18s | 14m 21s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149186) |
| 5m 18s | 13m 28s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149206) |
| 5m 17s | 13m 16s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149150) |
| 5m 17s | 14m 25s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149151) |
| 5m 17s | 13m 21s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149152) |
| 5m 17s | 14m 23s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149154) |
| 5m 17s | 14m 4s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74346149155) |
| 3m 39s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356147467/job/74346044633) |
| 2m 56s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356147467/job/74345977635) |
| 2m 46s | 6s | `full-release-validation` | Run package Telegram E2E | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25356136430/job/74345937825) |
| 2m 9s | 2s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356147467/job/74345910828) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25356136430
  - Prepare release package artifact: failure - https://github.com/openclaw/openclaw/actions/runs/25356136430/job/74345723944
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25356136430/job/74345937825
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25356136430/job/74353143495
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25356150730
  - Prepare release package artifact: failure - https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345851031
  - install_smoke_release_checks / root_dockerfile_image: failure - https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345867709
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345955010
  - Run repo/live E2E validation / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74345955017
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25356150730/job/74353117919

## Notes

Automatically requested by Full Release Validation 25356136430 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


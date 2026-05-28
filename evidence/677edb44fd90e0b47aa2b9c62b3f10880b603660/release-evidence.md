# OpenClaw Release Evidence: 677edb44fd90e0b47aa2b9c62b3f10880b603660

Generated: 2026-05-05T10:37:21.012Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `677edb44fd90e0b47aa2b9c62b3f10880b603660` |
| Release ref input | `677edb44fd90e0b47aa2b9c62b3f10880b603660` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `677edb44fd90e0b47aa2b9c62b3f10880b603660` |
| Release ref SHA | `677edb44fd90e0b47aa2b9c62b3f10880b603660` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/677edb44fd90-1777973532762` | `677edb44fd90` | 1h 4m 37s | 1h 33m 37s | 1h 4m 4s | [25368652485](https://github.com/openclaw/openclaw/actions/runs/25368652485) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/677edb44fd90-1777973532762` | `677edb44fd90` | 4m 16s | 1h 17m 9s | 4m 11s | [25368671040](https://github.com/openclaw/openclaw/actions/runs/25368671040) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/677edb44fd90-1777973532762` | `677edb44fd90` | 1h 3m 5s | 13h 47m 19s | 1h 3m 2s | [25368671354](https://github.com/openclaw/openclaw/actions/runs/25368671354) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/677edb44fd90-1777973532762` | `677edb44fd90` | 6m 10s | 1m 38s | 4m 31s | [25368785624](https://github.com/openclaw/openclaw/actions/runs/25368785624) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 3m 36s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368652485/job/74386096490) |
| 1h 0m 35s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74386477568) |
| 48m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388208666) |
| 37m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74386478384) |
| 37m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74386478281) |
| 26m 11s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388320513) |
| 24m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74386478362) |
| 22m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74386478344) |
| 20m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74386478354) |
| 20m 3s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74386478312) |
| 19m 36s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388320458) |
| 15m 52s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368652485/job/74386096528) |
| 6m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368652485/job/74386491678) |
| 4m 41s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368652485/job/74386096558) |
| 3m 30s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671040/job/74386159101) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 4m 4s | 33s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25368652485/job/74395589950) |
| 1h 3m 2s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74395519997) |
| 1h 2m 11s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74395398520) |
| 18m 1s | 16m 11s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388320426) |
| 18m 1s | 17m 23s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388320452) |
| 18m 1s | 19m 36s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388320458) |
| 18m 1s | 14m 27s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388320459) |
| 18m 1s | 15m 46s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388320507) |
| 18m 1s | 26m 11s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388320513) |
| 18m 1s | 16m 16s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388320516) |
| 18m 1s | 3m 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388320544) |
| 4m 31s | 1m 38s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368785624/job/74386515352) |
| 4m 11s | 5s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671040/job/74386733742) |
| 2m 57s | 6m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368652485/job/74386491678) |
| 2m 52s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25368671040/job/74386547989) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25368652485
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25368652485/job/74395589950
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25368671354
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74386477568
  - Run repo/live E2E validation / Live media suites (Native live media video plugins C): failure - https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74386477704
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74386815147
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74388208666
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74395398520
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25368671354/job/74395519997

## Notes

Automatically requested by Full Release Validation 25368652485 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


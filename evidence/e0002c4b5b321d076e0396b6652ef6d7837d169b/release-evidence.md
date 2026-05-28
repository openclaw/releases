# OpenClaw Release Evidence: e0002c4b5b321d076e0396b6652ef6d7837d169b

Generated: 2026-05-05T02:48:38.790Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `e0002c4b5b321d076e0396b6652ef6d7837d169b` |
| Release ref input | `e0002c4b5b321d076e0396b6652ef6d7837d169b` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `e0002c4b5b321d076e0396b6652ef6d7837d169b` |
| Release ref SHA | `e0002c4b5b321d076e0396b6652ef6d7837d169b` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/e0002c4b5b32-1777945448787` | `e0002c4b5b32` | 1h 4m 8s | 1h 21m 52s | 1h 3m 35s | [25353409278](https://github.com/openclaw/openclaw/actions/runs/25353409278) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/e0002c4b5b32-1777945448787` | `e0002c4b5b32` | 4m 1s | 1h 15m 11s | 3m 58s | [25353419128](https://github.com/openclaw/openclaw/actions/runs/25353419128) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/e0002c4b5b32-1777945448787` | `e0002c4b5b32` | 1h 2m 48s | 13h 2m 7s | 1h 2m 45s | [25353419398](https://github.com/openclaw/openclaw/actions/runs/25353419398) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/e0002c4b5b32-1777945448787` | `e0002c4b5b32` | 2m 5s | 1m 50s | 15s | [25353492204](https://github.com/openclaw/openclaw/actions/runs/25353492204) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 3m 16s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353409278/job/74337663327) |
| 1h 0m 18s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74337862862) |
| 32m 31s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338018329) |
| 32m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338299547) |
| 21m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74337862927) |
| 21m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74337862937) |
| 21m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74337862954) |
| 20m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74337862936) |
| 20m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74337862935) |
| 20m 11s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338045534) |
| 19m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74337862958) |
| 8m 46s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353409278/job/74337663337) |
| 4m 13s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353409278/job/74337663339) |
| 3m 40s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419128/job/74337690835) |
| 2m 35s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353409278/job/74337663341) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 3m 35s | 32s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25353409278/job/74342711093) |
| 1h 2m 45s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74342666674) |
| 39m 51s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74340896759) |
| 7m 49s | 2m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338299544) |
| 7m 49s | 32m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338299547) |
| 7m 49s | 1m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338299554) |
| 7m 48s | 2m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338299543) |
| 7m 47s | 58s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338299551) |
| 7m 47s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338299552) |
| 7m 35s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338299849) |
| 7m 34s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338299716) |
| 3m 58s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419128/job/74337997235) |
| 2m 53s | 2m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353409278/job/74337881364) |
| 2m 48s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419128/job/74337894628) |
| 2m 12s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25353419128/job/74337844436) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25353409278
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25353409278/job/74342711093
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25353419398
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74337862862
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74337862870
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338045549
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338045552
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): failure - https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338045556
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338045557
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338045562
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338045564
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74338045574
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25353419398/job/74342666674

## Notes

Automatically requested by Full Release Validation 25353409278 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


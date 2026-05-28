# OpenClaw Release Evidence: 1bfc66da33e5b2483c07726c2108bb89f9830c2f

Generated: 2026-05-03T16:07:15.483Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `1bfc66da33e5b2483c07726c2108bb89f9830c2f` |
| Release ref input | `1bfc66da33e5b2483c07726c2108bb89f9830c2f` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `1bfc66da33e5b2483c07726c2108bb89f9830c2f` |
| Release ref SHA | `1bfc66da33e5b2483c07726c2108bb89f9830c2f` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/1bfc66da33e5-1777822510326` | `1bfc66da33e5` | 31m 44s | 47m 33s | 31m 15s | [25283323153](https://github.com/openclaw/openclaw/actions/runs/25283323153) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/1bfc66da33e5-1777822510326` | `1bfc66da33e5` | 3m 47s | 1h 9m 10s | 3m 44s | [25283330380](https://github.com/openclaw/openclaw/actions/runs/25283330380) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/1bfc66da33e5-1777822510326` | `1bfc66da33e5` | 30m 28s | 13h 17m 51s | 30m 25s | [25283329203](https://github.com/openclaw/openclaw/actions/runs/25283329203) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/1bfc66da33e5-1777822510326` | `1bfc66da33e5` | 1m 57s | 1m 44s | 12s | [25283379566](https://github.com/openclaw/openclaw/actions/runs/25283379566) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 31m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283323153/job/74123865179) |
| 26m 13s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124091354) |
| 25m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74123991199) |
| 23m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74123991188) |
| 23m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74123991183) |
| 22m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74123991196) |
| 21m 19s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124091374) |
| 20m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74123991229) |
| 19m 38s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124091359) |
| 19m 22s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74123991206) |
| 19m 20s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124091350) |
| 7m 12s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283323153/job/74123865167) |
| 4m 11s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283323153/job/74123865168) |
| 3m 28s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283330380/job/74123887481) |
| 2m 18s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283323153/job/74123865173) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 31m 15s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25283323153/job/74125602898) |
| 30m 25s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74125572033) |
| 30m 3s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74125552712) |
| 12m 34s | 1m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124556140) |
| 12m 34s | 17m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124556146) |
| 12m 34s | 1m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124556147) |
| 12m 34s | 2m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124556154) |
| 12m 33s | 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124556144) |
| 12m 32s | 7m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124556151) |
| 12m 23s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124556256) |
| 12m 23s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124556359) |
| 3m 44s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283330380/job/74124079123) |
| 2m 37s | 2m 15s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283323153/job/74123999260) |
| 2m 25s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283330380/job/74124007613) |
| 1m 59s | 2s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283330380/job/74123979050) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25283323153
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25283323153/job/74125602898
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25283330380
  - check-test-types: failure - https://github.com/openclaw/openclaw/actions/runs/25283330380/job/74123887459
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25283330380/job/74123967106
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25283329203
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74124091374
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25283329203/job/74125572033

## Notes

Automatically requested by Full Release Validation 25283323153 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


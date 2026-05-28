# OpenClaw Release Evidence: f368201790d2ee07da0c99021eb74a6ba7f9874b

Generated: 2026-05-04T20:30:29.757Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `f368201790d2ee07da0c99021eb74a6ba7f9874b` |
| Release ref input | `f368201790d2ee07da0c99021eb74a6ba7f9874b` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `f368201790d2ee07da0c99021eb74a6ba7f9874b` |
| Release ref SHA | `f368201790d2ee07da0c99021eb74a6ba7f9874b` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/f368201790d2-1777924186543` | `f368201790d2` | 40m 9s | 1h 3m 3s | 39m 37s | [25339951566](https://github.com/openclaw/openclaw/actions/runs/25339951566) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/f368201790d2-1777924186543` | `f368201790d2` | 4m 20s | 1h 18m 54s | 4m 16s | [25339978363](https://github.com/openclaw/openclaw/actions/runs/25339978363) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/f368201790d2-1777924186543` | `f368201790d2` | 38m 31s | 13h 28m 17s | 38m 28s | [25339979125](https://github.com/openclaw/openclaw/actions/runs/25339979125) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/f368201790d2-1777924186543` | `f368201790d2` | 2m 40s | 2m 35s | 5s | [25340130384](https://github.com/openclaw/openclaw/actions/runs/25340130384) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 39m 11s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339951566/job/74294585524) |
| 31m 27s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295248852) |
| 23m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295918897) |
| 22m 6s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74294976758) |
| 21m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74294976755) |
| 20m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74294976760) |
| 20m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74294976842) |
| 20m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74294976753) |
| 20m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74294976813) |
| 19m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74294976799) |
| 19m 11s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295233130) |
| 12m 54s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339951566/job/74294585502) |
| 4m 41s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339951566/job/74294585488) |
| 3m 39s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339978363/job/74294664522) |
| 2m 47s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339951566/job/74294585483) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 39m 37s | 32s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25339951566/job/74300824250) |
| 38m 28s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74300718462) |
| 31m 54s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74299683792) |
| 8m 28s | 2m 41s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295926341) |
| 8m 28s | 2m 59s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295926346) |
| 8m 28s | 2m 14s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295926370) |
| 8m 28s | 1m 58s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295926462) |
| 8m 27s | 3m 48s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295926319) |
| 8m 27s | 2m 29s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295926320) |
| 8m 27s | 1m 51s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295926321) |
| 8m 27s | 2m 38s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295926335) |
| 4m 16s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339978363/job/74295268330) |
| 3m 21s | 2m 47s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339951566/job/74295046457) |
| 2m 47s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339978363/job/74295049180) |
| 2m 19s | 3s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339978363/job/74294975901) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25339951566
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25339951566/job/74300824250
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25339979125
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74295248852
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25339979125/job/74300718462

## Notes

Automatically requested by Full Release Validation 25339951566 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


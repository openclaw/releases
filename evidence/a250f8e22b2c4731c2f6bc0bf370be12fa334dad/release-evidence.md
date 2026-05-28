# OpenClaw Release Evidence: a250f8e22b2c4731c2f6bc0bf370be12fa334dad

Generated: 2026-05-03T17:25:47.607Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `a250f8e22b2c4731c2f6bc0bf370be12fa334dad` |
| Release ref input | `a250f8e22b2c4731c2f6bc0bf370be12fa334dad` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `a250f8e22b2c4731c2f6bc0bf370be12fa334dad` |
| Release ref SHA | `a250f8e22b2c4731c2f6bc0bf370be12fa334dad` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/a250f8e22b2c-1777827460656` | `a250f8e22b2c` | 27m 44s | 53m 31s | 27m 19s | [25285172912](https://github.com/openclaw/openclaw/actions/runs/25285172912) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/a250f8e22b2c-1777827460656` | `a250f8e22b2c` | 3m 52s | 1h 12m 35s | 3m 48s | [25285182446](https://github.com/openclaw/openclaw/actions/runs/25285182446) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/a250f8e22b2c-1777827460656` | `a250f8e22b2c` | 26m 25s | 12h 56m 48s | 26m 22s | [25285182605](https://github.com/openclaw/openclaw/actions/runs/25285182605) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/a250f8e22b2c-1777827460656` | `a250f8e22b2c` | 1m 50s | 1m 34s | 15s | [25285236976](https://github.com/openclaw/openclaw/actions/runs/25285236976) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 26m 54s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285172912/job/74128449860) |
| 22m 30s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128669889) |
| 22m 26s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128575804) |
| 22m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128575797) |
| 22m 4s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128575812) |
| 21m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128575821) |
| 20m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128575813) |
| 19m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128575794) |
| 19m 13s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128575815) |
| 19m 3s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128575563) |
| 19m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128575805) |
| 17m 20s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285172912/job/74128449862) |
| 4m 8s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285172912/job/74128449851) |
| 3m 26s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182446/job/74128471433) |
| 3m 26s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182446/job/74128471453) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 19s | 24s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285172912/job/74129955082) |
| 26m 22s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74129928170) |
| 23m 11s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74129752818) |
| 6m 28s | 16m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128820735) |
| 6m 28s | 1m 34s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128820736) |
| 6m 28s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128820737) |
| 6m 27s | 2m 8s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128820727) |
| 6m 27s | 1m 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128820729) |
| 6m 27s | 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128820733) |
| 6m 25s | 1m 56s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128816214) |
| 6m 25s | 1m 42s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128816251) |
| 3m 48s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182446/job/74128677615) |
| 2m 41s | 2m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285172912/job/74128585606) |
| 2m 30s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182446/job/74128599837) |
| 2m 12s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285182446/job/74128581555) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25285172912
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25285172912/job/74129955082
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25285182605
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74128820735
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74129752818
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25285182605/job/74129928170

## Notes

Automatically requested by Full Release Validation 25285172912 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


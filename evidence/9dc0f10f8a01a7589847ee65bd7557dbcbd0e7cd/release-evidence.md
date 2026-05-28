# OpenClaw Release Evidence: 9dc0f10f8a01a7589847ee65bd7557dbcbd0e7cd

Generated: 2026-05-03T16:11:37.094Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `9dc0f10f8a01a7589847ee65bd7557dbcbd0e7cd` |
| Release ref input | `9dc0f10f8a01a7589847ee65bd7557dbcbd0e7cd` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `9dc0f10f8a01a7589847ee65bd7557dbcbd0e7cd` |
| Release ref SHA | `9dc0f10f8a01a7589847ee65bd7557dbcbd0e7cd` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/9dc0f10f8a01-1777822880020` | `9dc0f10f8a01` | 29m 44s | 45m 12s | 29m 18s | [25283458378](https://github.com/openclaw/openclaw/actions/runs/25283458378) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/9dc0f10f8a01-1777822880020` | `9dc0f10f8a01` | 3m 57s | 1h 9m 6s | 3m 53s | [25283464987](https://github.com/openclaw/openclaw/actions/runs/25283464987) | 4 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/9dc0f10f8a01-1777822880020` | `9dc0f10f8a01` | 28m 41s | 13h 11m 16s | 28m 36s | [25283465542](https://github.com/openclaw/openclaw/actions/runs/25283465542) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/9dc0f10f8a01-1777822880020` | `9dc0f10f8a01` | 1m 46s | 1m 32s | 13s | [25283520063](https://github.com/openclaw/openclaw/actions/runs/25283520063) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 29m 4s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283458378/job/74124204548) |
| 21m 59s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124430814) |
| 21m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124562751) |
| 21m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124326138) |
| 21m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124326118) |
| 21m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124326156) |
| 21m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124326151) |
| 20m 27s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124326137) |
| 19m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124326142) |
| 19m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124326155) |
| 19m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124326152) |
| 6m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283458378/job/74124204527) |
| 4m 15s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283458378/job/74124204544) |
| 3m 35s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283464987/job/74124218539) |
| 2m 21s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283458378/job/74124204532) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 29m 18s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25283458378/job/74125842947) |
| 28m 36s | 4s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74125818838) |
| 28m 29s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74125811683) |
| 6m 33s | 1m 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124562766) |
| 6m 32s | 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124562752) |
| 6m 32s | 2m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124562756) |
| 6m 32s | 1m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124562759) |
| 6m 32s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124562761) |
| 6m 31s | 21m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124562751) |
| 6m 26s | 2m 19s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124555476) |
| 6m 26s | 1m 46s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283465542/job/74124555479) |
| 3m 53s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283464987/job/74124416958) |
| 2m 33s | 2m 19s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283458378/job/74124333613) |
| 2m 33s | 4s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25283464987/job/74124348133) |
| 2m 4s | 2s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283464987/job/74124316011) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25283458378
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25283458378/job/74125842947
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25283464987
  - checks-node-agentic-control-plane-runtime: failure - https://github.com/openclaw/openclaw/actions/runs/25283464987/job/74124218658
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25283464987/job/74124348133

## Notes

Automatically requested by Full Release Validation 25283458378 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


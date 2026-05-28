# OpenClaw Release Evidence: 2026.5.4-beta.1

Generated: 2026-05-04T11:38:42.733Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.4-beta.1` |
| Release ref input | `release/2026.5.4` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.5.4` |
| Release ref SHA | `dc97d0dd0686573bead8a10255deda3289601c95` |
| Runs at release SHA | none |
| Package spec | `openclaw@2026.5.4-beta.1` |
| npm status | error |
| npm error | npm registry /openclaw/2026.5.4-beta.1 failed: 404 Not Found "version not found: 2026.5.4-beta.1" |
| npm expected version match | no |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `89a15fddaf84` | 57m 30s (+3m 20s) | 50m 23s (-2m 48s) | 57m 1s | [25314477023](https://github.com/openclaw/openclaw/actions/runs/25314477023) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `5efbb3078a15` | 4m 19s (+11s) | 1h 20m 31s (-17s) | 4m 16s | [25315303690](https://github.com/openclaw/openclaw/actions/runs/25315303690) | 1 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `5efbb3078a15` | 36m 13s (+6m 19s) | 7h 49m 18s (+18m 59s) | 36m 9s | [25315301852](https://github.com/openclaw/openclaw/actions/runs/25315301852) | 40 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 36m 51s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74211330312) |
| 31m 16s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211917136) |
| 25m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74212367544) |
| 21m 2s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211648752) |
| 18m 56s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-smoke, Native live ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211648970) |
| 18m 9s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211867453) |
| 17m 36s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-smoke, native-live-src-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211648755) |
| 16m 4s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211867462) |
| 15m 58s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211867450) |
| 15m 42s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211648941) |
| 14m 48s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211648643) |
| 8m 13s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74211330319) |
| 4m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74211330303) |
| 3m 45s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315303690/job/74211408561) |
| 2m 29s | `normal-ci` | checks-node-core-fast | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315303690/job/74211408874) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 57m 1s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74216047714) |
| 36m 9s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74215962698) |
| 34m 47s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74215620411) |
| 20m 12s | 4m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74211330303) |
| 20m 12s | 8m 13s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74211330319) |
| 20m 7s | 36m 51s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74211330312) |
| 20m 4s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74211330835) |
| 20m 4s | 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74211331269) |
| 19m 54s | 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74211304058) |
| 8m 16s | 1m 40s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74212384125) |
| 8m 16s | 1m 22s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74212384221) |
| 8m 15s | 59s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74212384135) |
| 8m 15s | 7m 45s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74212384218) |
| 8m 15s | 2m 3s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74212384219) |
| 8m 15s | 1m 57s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74212384224) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 29m 54s | 36m 13s | +6m 19s | +18m 59s |
| `full-release-validation` | 54m 10s | 57m 30s | +3m 20s | -2m 48s |
| `normal-ci` | 4m 8s | 4m 19s | +11s | -17s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25314477023
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25314477023/job/74216047714
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25315303690
  - build-artifacts: failure - https://github.com/openclaw/openclaw/actions/runs/25315303690/job/74211408413
  - build-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25315303690/job/74211536256
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25315303690/job/74211738248
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25315303690/job/74211917485
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25315301852
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211505066
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74211917136
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25315301852/job/74215962698

## Notes

Automatically requested by Full Release Validation 25314477023 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


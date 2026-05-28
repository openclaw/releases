# OpenClaw Release Evidence: d522a18971495ad85583d6d5866b9949278ffb3a

Generated: 2026-05-05T00:24:47.279Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `d522a18971495ad85583d6d5866b9949278ffb3a` |
| Release ref input | `d522a18971495ad85583d6d5866b9949278ffb3a` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `d522a18971495ad85583d6d5866b9949278ffb3a` |
| Release ref SHA | `d522a18971495ad85583d6d5866b9949278ffb3a` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/d522a1897149-1777938335433` | `d522a1897149` | 38m 39s | 59m 40s | 38m 13s | [25349761232](https://github.com/openclaw/openclaw/actions/runs/25349761232) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/d522a1897149-1777938335433` | `d522a1897149` | 4m 20s | 1h 14m 11s | 4m 17s | [25349778457](https://github.com/openclaw/openclaw/actions/runs/25349778457) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/d522a1897149-1777938335433` | `d522a1897149` | 37m 26s | 11h 43m 26s | 37m 22s | [25349775318](https://github.com/openclaw/openclaw/actions/runs/25349775318) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/d522a1897149-1777938335433` | `d522a1897149` | 1m 56s | 1m 37s | 18s | [25349865604](https://github.com/openclaw/openclaw/actions/runs/25349865604) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 37m 48s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349761232/job/74326668035) |
| 32m 19s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327090474) |
| 28m 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327337768) |
| 21m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74326931045) |
| 21m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74326931036) |
| 20m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74326931050) |
| 20m 57s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74326931046) |
| 20m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74326931018) |
| 20m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327138106) |
| 20m 33s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327138102) |
| 19m 13s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327138093) |
| 11m 56s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349761232/job/74326668036) |
| 4m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349761232/job/74326668051) |
| 3m 56s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349778457/job/74326711988) |
| 3m 43s | `normal-ci` | checks-node-core-runtime-infra-state | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25349778457/job/74326712178) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 38m 13s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25349761232/job/74330385481) |
| 37m 22s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74330351592) |
| 35m 31s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74330164472) |
| 6m 32s | 28m 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327337768) |
| 6m 32s | 2m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327337773) |
| 6m 31s | 1m 45s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327337752) |
| 6m 31s | 1m 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327337758) |
| 6m 30s | 1m 28s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327319830) |
| 6m 30s | 1m 56s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327319864) |
| 6m 30s | 1m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327337735) |
| 6m 30s | 1m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327337764) |
| 4m 17s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349778457/job/74327126047) |
| 3m 59s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25349778457/job/74327102998) |
| 2m 52s | 2m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349761232/job/74326932244) |
| 2m 5s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25349778457/job/74326909332) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25349761232
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25349761232/job/74330385481
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25349778457
  - checks-node-core-runtime-infra-state: failure - https://github.com/openclaw/openclaw/actions/runs/25349778457/job/74326712178
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25349778457/job/74327102998
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25349775318
  - Run repo/live E2E validation / validate_release_live_cache: failure - https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74326930855
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): failure - https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74327138086
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25349775318/job/74330351592

## Notes

Automatically requested by Full Release Validation 25349761232 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


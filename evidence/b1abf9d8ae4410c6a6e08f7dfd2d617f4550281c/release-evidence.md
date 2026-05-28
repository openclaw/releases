# OpenClaw Release Evidence: b1abf9d8ae4410c6a6e08f7dfd2d617f4550281c

Generated: 2026-05-06T09:19:51.437Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `b1abf9d8ae4410c6a6e08f7dfd2d617f4550281c` |
| Release ref input | `b1abf9d8ae4410c6a6e08f7dfd2d617f4550281c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `b1abf9d8ae4410c6a6e08f7dfd2d617f4550281c` |
| Release ref SHA | `b1abf9d8ae4410c6a6e08f7dfd2d617f4550281c` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/b1abf9d8ae44-1778055216241` | `b1abf9d8ae44` | 1h 5m 45s | 1h 31m 25s | 1h 5m 7s | [25423996696](https://github.com/openclaw/openclaw/actions/runs/25423996696) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/b1abf9d8ae44-1778055216241` | `b1abf9d8ae44` | 5m 59s | 1h 28m 13s | 5m 57s | [25424015911](https://github.com/openclaw/openclaw/actions/runs/25424015911) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/b1abf9d8ae44-1778055216241` | `b1abf9d8ae44` | 1h 4m 2s | 13h 31m 1s | 1h 3m 59s | [25424020027](https://github.com/openclaw/openclaw/actions/runs/25424020027) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/b1abf9d8ae44-1778055216241` | `b1abf9d8ae44` | 2m 16s | 1m 35s | 40s | [25424128700](https://github.com/openclaw/openclaw/actions/runs/25424128700) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 4m 36s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423996696/job/74572769557) |
| 1h 0m 37s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573146393) |
| 32m 0s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573444595) |
| 29m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573923821) |
| 27m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573146972) |
| 23m 51s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573545964) |
| 23m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573146970) |
| 23m 9s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573545906) |
| 22m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573146954) |
| 21m 26s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573545975) |
| 21m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573146936) |
| 14m 27s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423996696/job/74572769573) |
| 6m 18s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423996696/job/74572769559) |
| 3m 51s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424015911/job/74572832366) |
| 2m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423996696/job/74573140952) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 5m 7s | 37s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423996696/job/74582383683) |
| 1h 3m 59s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74582275910) |
| 42m 29s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74578877605) |
| 13m 16s | 1m 51s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74574370210) |
| 13m 16s | 1m 56s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74574370246) |
| 13m 15s | 1m 16s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74574370151) |
| 13m 15s | 2m 31s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74574370164) |
| 13m 15s | 1m 21s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74574370189) |
| 13m 15s | 1m 26s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74574370198) |
| 13m 15s | 1m 26s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74574370216) |
| 13m 15s | 1m 29s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74574370240) |
| 5m 57s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424015911/job/74573615243) |
| 5m 0s | 3s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424015911/job/74573464761) |
| 4m 58s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424015911/job/74573452916) |
| 4m 54s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25424015911/job/74573452933) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25423996696
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25423996696/job/74582383683
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25424020027
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573146393
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573545921
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin): failure - https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74573923798
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74578877605
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25424020027/job/74582275910

## Notes

Automatically requested by Full Release Validation 25423996696 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


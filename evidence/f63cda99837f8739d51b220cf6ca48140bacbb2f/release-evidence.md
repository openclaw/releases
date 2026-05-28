# OpenClaw Release Evidence: f63cda99837f8739d51b220cf6ca48140bacbb2f

Generated: 2026-05-09T23:22:10.794Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `f63cda99837f8739d51b220cf6ca48140bacbb2f` |
| Release ref input | `f63cda99837f8739d51b220cf6ca48140bacbb2f` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `f63cda99837f8739d51b220cf6ca48140bacbb2f` |
| Release ref SHA | `f63cda99837f8739d51b220cf6ca48140bacbb2f` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/f63cda99837f-1778368325431` | `f63cda99837f` | 9m 41s | 30m 25s | 9m 15s | [25614206182](https://github.com/openclaw/openclaw/actions/runs/25614206182) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/f63cda99837f-1778368325431` | `f63cda99837f` | 4m 54s | 1h 15m 59s | 2m 44s | [25614213024](https://github.com/openclaw/openclaw/actions/runs/25614213024) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/f63cda99837f-1778368325431` | `f63cda99837f` | 9m 20s | 4h 10m 13s | 9m 16s | [25614211420](https://github.com/openclaw/openclaw/actions/runs/25614211420) | 44 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/f63cda99837f-1778368325431` | `f63cda99837f` | 3m 29s | 3m 16s | 13s | [25614261895](https://github.com/openclaw/openclaw/actions/runs/25614261895) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 8m 58s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614206182/job/75189335682) |
| 8m 58s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614206182/job/75189335684) |
| 6m 29s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442888) |
| 6m 21s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442937) |
| 6m 20s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442945) |
| 5m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442957) |
| 5m 15s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614206182/job/75189335697) |
| 4m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442955) |
| 4m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442952) |
| 4m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442951) |
| 4m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442959) |
| 4m 33s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533903) |
| 4m 32s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533909) |
| 4m 22s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614213024/job/75189354991) |
| 3m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614206182/job/75189458437) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 9m 16s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189756864) |
| 9m 15s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614206182/job/75189741769) |
| 9m 9s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189751890) |
| 7m 28s | 1m 28s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663283) |
| 7m 28s | 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663286) |
| 7m 28s | 1m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663288) |
| 7m 27s | 1m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663273) |
| 7m 27s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663274) |
| 7m 27s | 1m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663278) |
| 7m 27s | 1m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663282) |
| 7m 26s | 1m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663272) |
| 3m 6s | 3m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614206182/job/75189458437) |
| 2m 44s | 2s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614213024/job/75189456785) |
| 2m 28s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614213024/job/75189444113) |
| 2m 10s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614213024/job/75189435544) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614206182
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614206182/job/75189335682
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614206182/job/75189335684
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25614206182/job/75189741769
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25614213024
  - checks-node-agentic-commands-onboard-config: failure - https://github.com/openclaw/openclaw/actions/runs/25614213024/job/75189355153
  - checks-node-agentic-commands-doctor-shared: failure - https://github.com/openclaw/openclaw/actions/runs/25614213024/job/75189355166
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25614213024/job/75189456785
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442888
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442937
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189442945
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533899
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533901
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533903
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533904
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533907
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533908
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533909
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533910
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189533914
  - Run repo/live E2E validation / Docker live models (Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189553180
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189553206
  - Run Docker release-path validation / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644603
  - Run Docker release-path validation / Docker E2E (package/update Anthropic install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644604
  - Run Docker release-path validation / Docker E2E (core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644605
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644607
  - Run Docker release-path validation / Docker E2E (plugins/runtime install B): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644618
  - Run Docker release-path validation / Docker E2E (plugins/runtime install H): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644621
  - Run Docker release-path validation / Docker E2E (plugins/runtime install G): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644623
  - Run Docker release-path validation / Docker E2E (plugins/runtime install C): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644624
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644627
  - Run Docker release-path validation / Docker E2E (plugins/runtime install D): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644628
  - Run Docker release-path validation / Docker E2E (plugins/runtime install A): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189644629
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663272
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663273
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663274
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663276
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663277
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663278
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663279
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663280
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663281
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663282
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663283
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663285
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189663288
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189751890
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25614211420/job/75189756864

## Notes

Automatically requested by Full Release Validation 25614206182 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


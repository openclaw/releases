# OpenClaw Release Evidence: 7c56c48eff3ccf513a57b0ffe445762b4287178e

Generated: 2026-05-03T19:35:45.467Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `7c56c48eff3ccf513a57b0ffe445762b4287178e` |
| Release ref input | `7c56c48eff3ccf513a57b0ffe445762b4287178e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `7c56c48eff3ccf513a57b0ffe445762b4287178e` |
| Release ref SHA | `7c56c48eff3ccf513a57b0ffe445762b4287178e` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/7c56c48eff3c-1777835188895` | `7c56c48eff3c` | 28m 52s | 44m 8s | 28m 26s | [25288051490](https://github.com/openclaw/openclaw/actions/runs/25288051490) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/7c56c48eff3c-1777835188895` | `7c56c48eff3c` | 4m 11s | 1h 13m 2s | 4m 8s | [25288058606](https://github.com/openclaw/openclaw/actions/runs/25288058606) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/7c56c48eff3c-1777835188895` | `7c56c48eff3c` | 27m 33s | 13h 9m 47s | 27m 29s | [25288058701](https://github.com/openclaw/openclaw/actions/runs/25288058701) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/7c56c48eff3c-1777835188895` | `7c56c48eff3c` | 1m 38s | 1m 35s | 3s | [25288104100](https://github.com/openclaw/openclaw/actions/runs/25288104100) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 28m 10s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288051490/job/74135532670) |
| 25m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135643991) |
| 23m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135644009) |
| 23m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135643984) |
| 22m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135643983) |
| 21m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135643985) |
| 21m 3s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135644000) |
| 20m 12s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135712497) |
| 19m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135712492) |
| 18m 59s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135712508) |
| 18m 59s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135712512) |
| 6m 42s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288051490/job/74135532669) |
| 4m 44s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288051490/job/74135532661) |
| 3m 43s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058606/job/74135552572) |
| 2m 42s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058606/job/74135552596) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 28m 26s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25288051490/job/74137134111) |
| 27m 29s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74137095576) |
| 24m 32s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74136927521) |
| 6m 19s | 1m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135877256) |
| 6m 19s | 18m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135877260) |
| 6m 19s | 2m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135877262) |
| 6m 18s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135877255) |
| 6m 18s | 1m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135877257) |
| 6m 9s | 2m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135877261) |
| 6m 8s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135877422) |
| 6m 7s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135877329) |
| 4m 8s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058606/job/74135759763) |
| 2m 35s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058606/job/74135668804) |
| 2m 27s | 1m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288051490/job/74135650374) |
| 2m 18s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25288058606/job/74135653305) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25288051490
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25288051490/job/74137134111
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25288058701
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74135877260
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74136927521
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25288058701/job/74137095576

## Notes

Automatically requested by Full Release Validation 25288051490 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 1f7418536456416f87cd5d82caaf5b3e86aa8357

Generated: 2026-05-10T06:24:28.147Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `1f7418536456416f87cd5d82caaf5b3e86aa8357` |
| Release ref input | `1f7418536456416f87cd5d82caaf5b3e86aa8357` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `1f7418536456416f87cd5d82caaf5b3e86aa8357` |
| Release ref SHA | `1f7418536456416f87cd5d82caaf5b3e86aa8357` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/1f7418536456-1778391230` | `1f7418536456` | 50m 14s | 1h 14m 14s | 49m 46s | [25620882255](https://github.com/openclaw/openclaw/actions/runs/25620882255) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/1f7418536456-1778391230` | `1f7418536456` | 2m 58s | 1h 7m 30s | 2m 40s | [25620886867](https://github.com/openclaw/openclaw/actions/runs/25620886867) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/1f7418536456-1778391230` | `1f7418536456` | 49m 17s | 7h 57m 21s | 49m 13s | [25620886873](https://github.com/openclaw/openclaw/actions/runs/25620886873) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/1f7418536456-1778391230` | `1f7418536456` | 3m 3s | 3m 0s | 3s | [25620944190](https://github.com/openclaw/openclaw/actions/runs/25620944190) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 49m 33s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620882255/job/75207137186) |
| 42m 26s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207401895) |
| 42m 1s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207503975) |
| 25m 22s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274661) |
| 23m 5s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207503983) |
| 14m 17s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620882255/job/75207137184) |
| 14m 0s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207401897) |
| 13m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274731) |
| 11m 55s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207401891) |
| 11m 42s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207401901) |
| 11m 41s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207401896) |
| 11m 26s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207401900) |
| 3m 22s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620882255/job/75207137183) |
| 3m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620882255/job/75207317972) |
| 3m 12s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620882255/job/75207137182) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 49m 46s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620882255/job/75209602192) |
| 49m 13s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75209588128) |
| 15m 1s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207927477) |
| 7m 56s | 4m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207543783) |
| 7m 54s | 1m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207543819) |
| 7m 53s | 4m 44s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207543811) |
| 7m 53s | 4m 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207543813) |
| 7m 53s | 4m 28s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207543817) |
| 7m 52s | 4m 22s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207543798) |
| 7m 52s | 2m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207543803) |
| 7m 52s | 1m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207543804) |
| 3m 35s | 3m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620882255/job/75207317972) |
| 2m 40s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886867/job/75207283764) |
| 2m 4s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886867/job/75207251961) |
| 2m 4s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620886867/job/75207251964) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25620882255
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25620882255/job/75209602192
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274708
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274719
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274720
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274721
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274723
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274731
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274741
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274742
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274744
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274746
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274749
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274757
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274762
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274766
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274769
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207274780
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207364301
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207364303
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207364304
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207364306
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207364307
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207364309
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207364314
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207503975
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75207503983
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25620886873/job/75209588128

## Notes

Automatically requested by Full Release Validation 25620882255 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


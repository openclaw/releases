# OpenClaw Release Evidence: b25dc1704fa9ccae753154bc26a11b2378d9327c

Generated: 2026-05-06T10:47:04.014Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `b25dc1704fa9ccae753154bc26a11b2378d9327c` |
| Release ref input | `b25dc1704fa9ccae753154bc26a11b2378d9327c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `b25dc1704fa9ccae753154bc26a11b2378d9327c` |
| Release ref SHA | `b25dc1704fa9ccae753154bc26a11b2378d9327c` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 0 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/b25dc1704fa9-1778062409684` | `b25dc1704fa9` | 33m 6s | 1h 0m 39s | 32m 30s | [25429284831](https://github.com/openclaw/openclaw/actions/runs/25429284831) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/b25dc1704fa9-1778062409684` | `b25dc1704fa9` | 5m 19s | 1h 25m 53s | 4m 24s | [25429307835](https://github.com/openclaw/openclaw/actions/runs/25429307835) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/b25dc1704fa9-1778062409684` | `b25dc1704fa9` | 8m 35s | 11h 4m 38s | 8m 35s | [25429309018](https://github.com/openclaw/openclaw/actions/runs/25429309018) | 38 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/b25dc1704fa9-1778062409684` | `b25dc1704fa9` | 2m 13s | 1m 44s | 28s | [25429430307](https://github.com/openclaw/openclaw/actions/runs/25429430307) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 31m 54s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25429284831/job/74591001220) |
| 23m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74591437908) |
| 23m 3s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74591437820) |
| 22m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74591437778) |
| 21m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74591437893) |
| 21m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74591437788) |
| 20m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74591437754) |
| 20m 2s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74591437930) |
| 19m 54s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74591818680) |
| 18m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74591437875) |
| 18m 17s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74591818669) |
| 16m 56s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429284831/job/74591001238) |
| 5m 45s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429284831/job/74591001208) |
| 3m 51s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429307835/job/74591076415) |
| 2m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429284831/job/74591420632) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 32m 30s | 35s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25429284831/job/74595801325) |
| 8m 35s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74592310313) |
| 8m 33s | 2m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74592310336) |
| 8m 33s | 6m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74592310382) |
| 8m 32s | 6m 46s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74592310333) |
| 8m 31s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74592310327) |
| 8m 30s | 1m 24s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74592310370) |
| 8m 21s | 1m 13s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74592275635) |
| 8m 21s | 1m 27s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74592275646) |
| 8m 21s | 1m 43s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74592275649) |
| 8m 21s | 1m 41s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429309018/job/74592275670) |
| 4m 24s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429307835/job/74591694584) |
| 3m 31s | 1m 47s | `normal-ci` | checks-windows-node-test | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429307835/job/74591076394) |
| 3m 9s | 2m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429284831/job/74591420632) |
| 2m 53s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25429307835/job/74591463821) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25429284831
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25429284831/job/74591001220
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25429284831/job/74595801325

## Notes

Automatically requested by Full Release Validation 25429284831 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


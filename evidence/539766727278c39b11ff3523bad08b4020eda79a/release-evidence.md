# OpenClaw Release Evidence: 539766727278c39b11ff3523bad08b4020eda79a

Generated: 2026-05-04T09:48:49.052Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `539766727278c39b11ff3523bad08b4020eda79a` |
| Release ref input | `539766727278c39b11ff3523bad08b4020eda79a` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `539766727278c39b11ff3523bad08b4020eda79a` |
| Release ref SHA | `539766727278c39b11ff3523bad08b4020eda79a` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/539766727278-1777885852502` | `539766727278` | 37m 32s | 59m 23s | 37m 1s | [25310757811](https://github.com/openclaw/openclaw/actions/runs/25310757811) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/539766727278-1777885852502` | `539766727278` | 4m 18s | 1h 24m 55s | 4m 14s | [25310778910](https://github.com/openclaw/openclaw/actions/runs/25310778910) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/539766727278-1777885852502` | `539766727278` | 36m 4s | 13h 53m 48s | 36m 1s | [25310779825](https://github.com/openclaw/openclaw/actions/runs/25310779825) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/539766727278-1777885852502` | `539766727278` | 1m 50s | 1m 40s | 9s | [25310882683](https://github.com/openclaw/openclaw/actions/runs/25310882683) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 36m 34s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310757811/job/74196854109) |
| 31m 1s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197431311) |
| 23m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197204385) |
| 22m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197204372) |
| 20m 38s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197204370) |
| 20m 34s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197204371) |
| 20m 12s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197567081) |
| 20m 11s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197567079) |
| 19m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197204360) |
| 19m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197799426) |
| 19m 19s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197567050) |
| 12m 45s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310757811/job/74196854096) |
| 4m 46s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310757811/job/74196854106) |
| 3m 43s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310778910/job/74196929871) |
| 2m 54s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310778910/job/74196929799) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 37m 1s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25310757811/job/74201779049) |
| 36m 1s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74201699311) |
| 26m 44s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74200465096) |
| 7m 2s | 4m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197799409) |
| 7m 2s | 1m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197799411) |
| 7m 2s | 2m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197799443) |
| 7m 2s | 1m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197799489) |
| 7m 1s | 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197799407) |
| 7m 1s | 19m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197799426) |
| 6m 50s | 4m 28s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197737106) |
| 6m 44s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197799696) |
| 4m 14s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310778910/job/74197438508) |
| 3m 9s | 2s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25310778910/job/74197305386) |
| 2m 54s | 2m 15s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310757811/job/74197190545) |
| 2m 25s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25310778910/job/74197193119) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25310757811
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25310757811/job/74201779049
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25310778910
  - checks-node-core-runtime-infra-process: failure - https://github.com/openclaw/openclaw/actions/runs/25310778910/job/74196930214
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25310778910/job/74197305386
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25310779825
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197061574
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74197431311
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25310779825/job/74201699311

## Notes

Automatically requested by Full Release Validation 25310757811 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


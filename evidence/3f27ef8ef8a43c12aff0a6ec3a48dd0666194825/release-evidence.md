# OpenClaw Release Evidence: 3f27ef8ef8a43c12aff0a6ec3a48dd0666194825

Generated: 2026-05-03T22:38:55.268Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `3f27ef8ef8a43c12aff0a6ec3a48dd0666194825` |
| Release ref input | `3f27ef8ef8a43c12aff0a6ec3a48dd0666194825` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `3f27ef8ef8a43c12aff0a6ec3a48dd0666194825` |
| Release ref SHA | `3f27ef8ef8a43c12aff0a6ec3a48dd0666194825` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/3f27ef8ef8a4-1777847227130` | `3f27ef8ef8a4` | 11m 22s | 29m 45s | 10m 59s | [25292611910](https://github.com/openclaw/openclaw/actions/runs/25292611910) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/3f27ef8ef8a4-1777847227130` | `3f27ef8ef8a4` | 6m 10s | 1h 19m 22s | 6m 7s | [25292619127](https://github.com/openclaw/openclaw/actions/runs/25292619127) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/3f27ef8ef8a4-1777847227130` | `3f27ef8ef8a4` | 11m 4s | 6h 21m 54s | 11m 1s | [25292617622](https://github.com/openclaw/openclaw/actions/runs/25292617622) | 38 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/3f27ef8ef8a4-1777847227130` | `3f27ef8ef8a4` | 1m 47s | 1m 43s | 3s | [25292669106](https://github.com/openclaw/openclaw/actions/runs/25292669106) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 10m 44s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292611910/job/74146567765) |
| 8m 27s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678903) |
| 8m 27s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678941) |
| 8m 26s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678942) |
| 8m 26s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678945) |
| 8m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678937) |
| 8m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678947) |
| 8m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678952) |
| 8m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678961) |
| 8m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678963) |
| 8m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678968) |
| 7m 10s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292611910/job/74146567769) |
| 6m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292611910/job/74146567763) |
| 5m 45s | `normal-ci` | checks-node-agentic-control-plane-runtime | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292619127/job/74146586341) |
| 3m 37s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292619127/job/74146586204) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 11m 1s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74147132986) |
| 10m 59s | 22s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292611910/job/74147120236) |
| 10m 49s | 4s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74147127392) |
| 10m 22s | 8s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778325) |
| 9m 54s | 50s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778327) |
| 6m 32s | 1m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146898463) |
| 6m 32s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146898476) |
| 6m 30s | 1m 34s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146898462) |
| 6m 30s | 4m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146898468) |
| 6m 30s | 1m 37s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146898472) |
| 6m 25s | 2m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146898461) |
| 6m 7s | 2s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292619127/job/74146884634) |
| 3m 54s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292619127/job/74146775189) |
| 2m 44s | 2m 15s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292611910/job/74146687229) |
| 2m 40s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292619127/job/74146708929) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292611910
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292611910/job/74146567765
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25292611910/job/74147120236
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25292619127
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25292619127/job/74146708932
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25292619127/job/74146884634
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146633939
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678903
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678937
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678941
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678942
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678944
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678945
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678946
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678947
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678951
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678952
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678956
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678960
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678961
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678963
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146678968
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778316
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778319
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778320
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778321
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778325
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778327
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778328
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778329
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146778336
  - Run repo/live E2E validation / Docker live models (MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810485
  - Run repo/live E2E validation / Docker live models (OpenCode): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810486
  - Run repo/live E2E validation / Docker live models (OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810487
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810488
  - Run repo/live E2E validation / Docker live models (Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810489
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810490
  - Run repo/live E2E validation / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810491
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810492
  - Run repo/live E2E validation / Docker live models (Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810496
  - Run repo/live E2E validation / Docker live models (xAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810498
  - Run repo/live E2E validation / Docker live models (Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810501
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810503
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810506
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810513
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810515
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810516
  - Run repo/live E2E validation / Docker live models (Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146810517
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74146898468
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74147127392
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25292617622/job/74147132986

## Notes

Automatically requested by Full Release Validation 25292611910 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


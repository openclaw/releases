# OpenClaw Release Evidence: de4903ec7a830b34ef2f5c10cf6f29bdb7005598

Generated: 2026-05-04T19:12:52.982Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `de4903ec7a830b34ef2f5c10cf6f29bdb7005598` |
| Release ref input | `de4903ec7a830b34ef2f5c10cf6f29bdb7005598` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `de4903ec7a830b34ef2f5c10cf6f29bdb7005598` |
| Release ref SHA | `de4903ec7a830b34ef2f5c10cf6f29bdb7005598` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/de4903ec7a83-1777920923821` | `de4903ec7a83` | 16m 55s | 49m 19s | 16m 24s | [25337355559](https://github.com/openclaw/openclaw/actions/runs/25337355559) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/de4903ec7a83-1777920923821` | `de4903ec7a83` | 8m 31s | 1h 20m 34s | 8m 28s | [25337381566](https://github.com/openclaw/openclaw/actions/runs/25337381566) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/de4903ec7a83-1777920923821` | `de4903ec7a83` | 16m 34s | 6h 25m 18s | 16m 30s | [25337381932](https://github.com/openclaw/openclaw/actions/runs/25337381932) | 34 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/de4903ec7a83-1777920923821` | `de4903ec7a83` | 5m 24s | 1m 48s | 3m 35s | [25337504371](https://github.com/openclaw/openclaw/actions/runs/25337504371) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 15m 54s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337355559/job/74285880278) |
| 15m 48s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337355559/job/74285880272) |
| 11m 13s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586420) |
| 11m 0s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586440) |
| 10m 57s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586432) |
| 9m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293645) |
| 9m 34s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293621) |
| 9m 34s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293640) |
| 9m 34s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586417) |
| 9m 34s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586419) |
| 9m 33s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293198) |
| 9m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293550) |
| 8m 44s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25337355559/job/74285880339) |
| 5m 49s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25337355559/job/74286294760) |
| 3m 44s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25337381566/job/74285966306) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 16m 30s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288612358) |
| 16m 24s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25337355559/job/74288496912) |
| 15m 25s | 7s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288444232) |
| 14m 5s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234303) |
| 14m 5s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234318) |
| 14m 5s | 1m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234327) |
| 14m 5s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234347) |
| 14m 5s | 1m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234354) |
| 14m 5s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234415) |
| 14m 5s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234994) |
| 14m 5s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288235070) |
| 8m 28s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25337381566/job/74287299892) |
| 8m 25s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25337381566/job/74287285880) |
| 8m 23s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25337381566/job/74287285888) |
| 8m 19s | 4s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25337381566/job/74287285914) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337355559
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337355559/job/74285880272
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337355559/job/74285880278
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25337355559/job/74288496912
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286119490
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293198
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293550
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293585
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293590
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293592
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293594
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293621
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293633
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293640
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293645
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293649
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293686
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293690
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293707
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286293750
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586411
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586417
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586418
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586419
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586420
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586425
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586431
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586432
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74286586440
  - Run Docker release-path validation / Docker E2E (plugins/runtime install C): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287223891
  - Run Docker release-path validation / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287223898
  - Run Docker release-path validation / Docker E2E (plugins/runtime install E): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287223915
  - Run Docker release-path validation / Docker E2E (plugins/runtime plugins): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287223940
  - Run Docker release-path validation / Docker E2E (package/update Anthropic install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287223947
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287223971
  - Run repo/live E2E validation / Docker live models (Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287255998
  - Run repo/live E2E validation / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256006
  - Run repo/live E2E validation / Docker live models (Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256013
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256014
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256027
  - Run repo/live E2E validation / Docker live models (OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256031
  - Run repo/live E2E validation / Docker live models (Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256033
  - Run repo/live E2E validation / Docker live models (MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256035
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256041
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256042
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256065
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256067
  - Run repo/live E2E validation / Docker live models (OpenCode): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256110
  - Run repo/live E2E validation / Docker live models (Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256125
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256126
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256128
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256137
  - Run repo/live E2E validation / Docker live models (xAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287256161
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74287297403
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234303
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234318
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234327
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234347
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234354
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288234415
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288444232
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25337381932/job/74288612358

## Notes

Automatically requested by Full Release Validation 25337355559 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


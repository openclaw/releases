# OpenClaw Release Evidence: d33273204018bf120d67318a304992872764b4cf

Generated: 2026-05-09T16:15:13.013Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `d33273204018bf120d67318a304992872764b4cf` |
| Release ref input | `d33273204018bf120d67318a304992872764b4cf` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `d33273204018bf120d67318a304992872764b4cf` |
| Release ref SHA | `d33273204018bf120d67318a304992872764b4cf` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 3 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/d33273204018-1778342764428` | `d33273204018` | 8m 48s | 27m 22s | 8m 16s | [25605520138](https://github.com/openclaw/openclaw/actions/runs/25605520138) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/d33273204018-1778342764428` | `d33273204018` | 4m 7s | 1h 14m 45s | 2m 45s | [25605527721](https://github.com/openclaw/openclaw/actions/runs/25605527721) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/d33273204018-1778342764428` | `d33273204018` | 8m 32s | 3h 48m 51s | 8m 27s | [25605528137](https://github.com/openclaw/openclaw/actions/runs/25605528137) | 44 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/d33273204018-1778342764428` | `d33273204018` | 3m 11s | 2m 56s | 14s | [25605580825](https://github.com/openclaw/openclaw/actions/runs/25605580825) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 7m 58s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605520138/job/75166625179) |
| 7m 58s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605520138/job/75166625203) |
| 5m 32s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754765) |
| 5m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754910) |
| 5m 20s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754901) |
| 5m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754922) |
| 5m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754898) |
| 4m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754912) |
| 4m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754895) |
| 4m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754919) |
| 4m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605520138/job/75166625180) |
| 4m 34s | `release-checks` | install_smoke_release_checks / installer_smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166807721) |
| 4m 26s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754908) |
| 3m 22s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605520138/job/75166763250) |
| 3m 18s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605527721/job/75166642406) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 8m 27s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75167083100) |
| 8m 16s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25605520138/job/75167052396) |
| 8m 15s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75167072194) |
| 7m 2s | 1m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979188) |
| 7m 2s | 1m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979209) |
| 7m 1s | 1m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979182) |
| 7m 1s | 1m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979183) |
| 7m 1s | 1m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979184) |
| 7m 1s | 1m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979185) |
| 7m 1s | 1m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979186) |
| 7m 1s | 46s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979187) |
| 3m 2s | 3m 22s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605520138/job/75166763250) |
| 2m 45s | 4s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25605527721/job/75166767196) |
| 2m 2s | 3s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605527721/job/75166728150) |
| 2m 1s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605527721/job/75166731230) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605520138
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605520138/job/75166625179
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605520138/job/75166625203
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25605520138/job/75167052396
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25605527721
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25605527721/job/75166715708
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25605527721/job/75166767196
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137
  - Run QA Lab live Telegram lane: failure - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166697337
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754765
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754898
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754901
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754910
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166754922
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166807721
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166837431
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166837462
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166837468
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166847692
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166847693
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166847696
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166847697
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166847698
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166847700
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166847702
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166847708
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166847714
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166887074
  - Run Docker release-path validation / Docker E2E (core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971347
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971349
  - Run Docker release-path validation / Docker E2E (plugins/runtime install B): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971351
  - Run Docker release-path validation / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971352
  - Run Docker release-path validation / Docker E2E (plugins/runtime install A): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971355
  - Run Docker release-path validation / Docker E2E (plugins/runtime install D): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971357
  - Run Docker release-path validation / Docker E2E (plugins/runtime install F): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971359
  - Run Docker release-path validation / Docker E2E (plugins/runtime install G): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971363
  - Run Docker release-path validation / Docker E2E (plugins/runtime install C): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971365
  - Run Docker release-path validation / Docker E2E (package/update Anthropic install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971367
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971368
  - Run Docker release-path validation / Docker E2E (plugins/runtime install E): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971377
  - Run Docker release-path validation / Docker E2E (plugins/runtime plugins): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971378
  - Run Docker release-path validation / Docker E2E (plugins/runtime install H): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166971398
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979182
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979183
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979184
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979185
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979186
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979187
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979188
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979189
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979190
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979191
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979195
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979196
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979203
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75166979209
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75167072194
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25605528137/job/75167083100
- `postpublish-telegram`: failure - https://github.com/openclaw/openclaw/actions/runs/25605580825
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25605580825/job/75166772145

## Notes

Automatically requested by Full Release Validation 25605520138 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


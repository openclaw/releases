# OpenClaw Release Evidence: 453daa0ddfb1963a8ff926f03ceaeae0a946e8e6

Generated: 2026-05-10T00:01:46.031Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `453daa0ddfb1963a8ff926f03ceaeae0a946e8e6` |
| Release ref input | `453daa0ddfb1963a8ff926f03ceaeae0a946e8e6` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `453daa0ddfb1963a8ff926f03ceaeae0a946e8e6` |
| Release ref SHA | `453daa0ddfb1963a8ff926f03ceaeae0a946e8e6` |
| Runs at release SHA | `full-release-validation` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.9` | `453daa0ddfb1` | 10m 5s | 30m 45s | 9m 32s | [25614886495](https://github.com/openclaw/openclaw/actions/runs/25614886495) | 1 |
| pass | blocking | `normal-ci` | CI | `main` | `4c72240a56b8` | 4m 18s | 1h 16m 4s | 4m 1s | [25614892673](https://github.com/openclaw/openclaw/actions/runs/25614892673) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `4c72240a56b8` | 9m 44s | 4h 10m 51s | 9m 40s | [25614892455](https://github.com/openclaw/openclaw/actions/runs/25614892455) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `main` | `0311fe9d8a85` | 3m 15s | 3m 1s | 14s | [25614947122](https://github.com/openclaw/openclaw/actions/runs/25614947122) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 9m 16s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614886495/job/75191049504) |
| 9m 14s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614886495/job/75191049505) |
| 6m 50s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191154910) |
| 6m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191155024) |
| 6m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191155053) |
| 5m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191155046) |
| 5m 28s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191155039) |
| 5m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191155057) |
| 5m 14s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191214565) |
| 4m 57s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234174) |
| 4m 56s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234187) |
| 4m 55s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234167) |
| 4m 41s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614886495/job/75191049507) |
| 4m 2s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614892673/job/75191064456) |
| 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614886495/job/75191181553) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 9m 40s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191478364) |
| 9m 32s | 32s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614886495/job/75191454607) |
| 9m 30s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191470345) |
| 7m 45s | 1m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369654) |
| 7m 44s | 1m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369652) |
| 7m 43s | 1m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369644) |
| 7m 43s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369647) |
| 7m 43s | 1m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369648) |
| 7m 43s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369656) |
| 7m 42s | 1m 46s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369642) |
| 7m 42s | 1m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369643) |
| 4m 1s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614892673/job/75191222456) |
| 3m 21s | 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614886495/job/75191181553) |
| 2m 12s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614892673/job/75191147031) |
| 1m 56s | 3s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614892673/job/75191134910) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614886495
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614886495/job/75191049504
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614886495/job/75191049505
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25614886495/job/75191454607
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191154910
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191155024
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191155053
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191214565
  - Run repo/live E2E validation / Docker live models (Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191214570
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191214580
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234166
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234167
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234171
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234172
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234174
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234176
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234177
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234180
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191234187
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367372
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367373
  - Run Docker release-path validation / Docker E2E (plugins/runtime install A): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367377
  - Run Docker release-path validation / Docker E2E (package/update Anthropic install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367387
  - Run Docker release-path validation / Docker E2E (plugins/runtime install E): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367390
  - Run Docker release-path validation / Docker E2E (plugins/runtime install C): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367391
  - Run Docker release-path validation / Docker E2E (plugins/runtime install F): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367393
  - Run Docker release-path validation / Docker E2E (plugins/runtime install G): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367394
  - Run Docker release-path validation / Docker E2E (plugins/runtime install H): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367396
  - Run Docker release-path validation / Docker E2E (plugins/runtime plugins): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367397
  - Run Docker release-path validation / Docker E2E (plugins/runtime install D): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367398
  - Run Docker release-path validation / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367399
  - Run Docker release-path validation / Docker E2E (plugins/runtime install B): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191367403
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369642
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369644
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369645
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369646
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369647
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369648
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369651
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369652
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369653
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369654
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369656
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191369660
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191470345
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25614892455/job/75191478364

## Notes

Automatically requested by Full Release Validation 25614886495 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


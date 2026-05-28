# OpenClaw Release Evidence: 8b33c00eda43b5a8574aacb3ee9fb010bccd6d4b

Generated: 2026-05-09T16:25:54.605Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `8b33c00eda43b5a8574aacb3ee9fb010bccd6d4b` |
| Release ref input | `8b33c00eda43b5a8574aacb3ee9fb010bccd6d4b` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `8b33c00eda43b5a8574aacb3ee9fb010bccd6d4b` |
| Release ref SHA | `8b33c00eda43b5a8574aacb3ee9fb010bccd6d4b` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/8b33c00eda43-1778343310736` | `8b33c00eda43` | 10m 13s | 27m 48s | 9m 47s | [25605709599](https://github.com/openclaw/openclaw/actions/runs/25605709599) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/8b33c00eda43-1778343310736` | `8b33c00eda43` | 3m 37s | 1h 19m 14s | 2m 49s | [25605719132](https://github.com/openclaw/openclaw/actions/runs/25605719132) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/8b33c00eda43-1778343310736` | `8b33c00eda43` | 10m 3s | 3h 51m 39s | 9m 58s | [25605718417](https://github.com/openclaw/openclaw/actions/runs/25605718417) | 46 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/8b33c00eda43-1778343310736` | `8b33c00eda43` | 3m 4s | 2m 52s | 11s | [25605774569](https://github.com/openclaw/openclaw/actions/runs/25605774569) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 9m 22s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605709599/job/75167120298) |
| 7m 42s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605709599/job/75167120295) |
| 7m 9s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167260976) |
| 7m 8s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167261069) |
| 7m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167261066) |
| 6m 43s | `release-checks` | Run repo/live E2E validation / prepare_live_test_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167260983) |
| 5m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167261088) |
| 5m 20s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167261087) |
| 5m 10s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379924) |
| 5m 9s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379921) |
| 5m 9s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379922) |
| 4m 54s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379927) |
| 4m 15s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605709599/job/75167120304) |
| 3m 21s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605709599/job/75167268087) |
| 3m 15s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605719132/job/75167148242) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 9m 58s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167724353) |
| 9m 50s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167716968) |
| 9m 47s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25605709599/job/75167683668) |
| 9m 16s |  | `release-checks` | Run repo/live E2E validation / Docker live models (selected providers) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167681966) |
| 9m 16s |  | `release-checks` | Run repo/live E2E validation / Docker live models (${{ matrix.provider_label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167682005) |
| 9m 16s |  | `release-checks` | Run repo/live E2E validation / Docker live suites (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167682120) |
| 7m 45s | 1m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577109) |
| 7m 45s | 1m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577118) |
| 7m 45s | 2m 4s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577127) |
| 7m 45s | 1m 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577129) |
| 7m 44s | 1m 28s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577111) |
| 2m 49s | 3m 21s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605709599/job/75167268087) |
| 2m 49s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605719132/job/75167287074) |
| 2m 22s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605719132/job/75167264226) |
| 2m 9s | 3s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605719132/job/75167252585) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605709599
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605709599/job/75167120298
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25605709599/job/75167683668
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417
  - Run QA Lab live Telegram lane: failure - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167195853
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167260976
  - Run repo/live E2E validation / prepare_live_test_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167260983
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167261066
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167261069
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: failure - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167261096
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379921
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379922
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379924
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379925
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379926
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379927
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379929
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379930
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167379934
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167441770
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167517627
  - Run Docker release-path validation / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167517631
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167517652
  - Run Docker release-path validation / Docker E2E (plugins/runtime install D): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167517656
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577103
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577105
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577108
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577109
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577110
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577111
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577113
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577115
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577118
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577123
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577127
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167577129
  - Run repo/live E2E validation / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167681966
  - Run repo/live E2E validation / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167682005
  - Run repo/live E2E validation / Docker live suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167682120
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167716968
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25605718417/job/75167724353
- `postpublish-telegram`: failure - https://github.com/openclaw/openclaw/actions/runs/25605774569
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25605774569/job/75167276993

## Notes

Automatically requested by Full Release Validation 25605709599 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


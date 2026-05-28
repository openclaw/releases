# OpenClaw Release Evidence: 3f2123456b1795386fdc796cdcd4bd2fe2827aea

Generated: 2026-05-09T15:37:03.850Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `3f2123456b1795386fdc796cdcd4bd2fe2827aea` |
| Release ref input | `3f2123456b1795386fdc796cdcd4bd2fe2827aea` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `3f2123456b1795386fdc796cdcd4bd2fe2827aea` |
| Release ref SHA | `3f2123456b1795386fdc796cdcd4bd2fe2827aea` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/3f2123456b17-1778339903152` | `3f2123456b17` | 18m 16s | 45m 50s | 17m 49s | [25604528997](https://github.com/openclaw/openclaw/actions/runs/25604528997) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/3f2123456b17-1778339903152` | `3f2123456b17` | 10m 32s | 1h 25m 54s | 2m 47s | [25604536152](https://github.com/openclaw/openclaw/actions/runs/25604536152) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/3f2123456b17-1778339903152` | `3f2123456b17` | 17m 27s | 5h 0m 6s | 17m 23s | [25604536422](https://github.com/openclaw/openclaw/actions/runs/25604536422) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/3f2123456b17-1778339903152` | `3f2123456b17` | 3m 1s | 2m 48s | 12s | [25604596346](https://github.com/openclaw/openclaw/actions/runs/25604596346) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 17m 23s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25604528997/job/75164050124) |
| 14m 49s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164202956) |
| 11m 50s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164299448) |
| 10m 57s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604528997/job/75164050118) |
| 10m 53s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604528997/job/75164050129) |
| 10m 0s | `normal-ci` | macos-node | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536152/job/75164069590) |
| 7m 36s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164203062) |
| 7m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482250) |
| 7m 21s | `release-checks` | Run QA Lab parity lane (candidate) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164130488) |
| 7m 14s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164288131) |
| 7m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482238) |
| 6m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164203099) |
| 6m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482247) |
| 6m 32s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164288128) |
| 3m 52s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604536152/job/75164069605) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 17m 49s | 26s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604528997/job/75165012734) |
| 17m 23s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75165014683) |
| 15m 9s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164897078) |
| 8m 42s | 54s | `release-checks` | Run QA Lab parity report | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164551916) |
| 7m 39s | 7m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482238) |
| 7m 38s | 5m 46s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482249) |
| 7m 38s | 7m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482250) |
| 7m 38s | 6m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482252) |
| 7m 37s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482237) |
| 7m 37s | 1m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482242) |
| 7m 37s | 2m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482243) |
| 3m 1s | 3m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604528997/job/75164209989) |
| 2m 47s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536152/job/75164217567) |
| 2m 13s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604536152/job/75164184884) |
| 2m 9s | 2s | `normal-ci` | check | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604536152/job/75164179489) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25604528997
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25604528997/job/75164050124
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25604528997/job/75165012734
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25604536152
  - macos-node: failure - https://github.com/openclaw/openclaw/actions/runs/25604536152/job/75164069590
  - check-test-types: failure - https://github.com/openclaw/openclaw/actions/runs/25604536152/job/75164069603
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25604536152/job/75164168838
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25604536152/job/75164179489
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25604536152/job/75164217567
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25604536422
  - Run QA Lab parity lane (baseline): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164130492
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164202956
  - install_smoke_release_checks / installer_smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164286679
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164288141
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164299440
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164299448
  - cross_os_release_checks / Windows / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164299449
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164343317
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164462805
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164462806
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482238
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482245
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482247
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482249
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482250
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482252
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164482260
  - Run QA Lab parity report: failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164551916
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75164897078
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25604536422/job/75165014683

## Notes

Automatically requested by Full Release Validation 25604528997 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: e2cddbc66760f1cc6b9bd03b08a33fd813a63c64

Generated: 2026-05-10T01:15:31.128Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `e2cddbc66760f1cc6b9bd03b08a33fd813a63c64` |
| Release ref input | `e2cddbc66760f1cc6b9bd03b08a33fd813a63c64` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `e2cddbc66760f1cc6b9bd03b08a33fd813a63c64` |
| Release ref SHA | `e2cddbc66760f1cc6b9bd03b08a33fd813a63c64` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/e2cddbc66760-1778374995727` | `e2cddbc66760` | 11m 51s | 28m 52s | 11m 24s | [25616147785](https://github.com/openclaw/openclaw/actions/runs/25616147785) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/e2cddbc66760-1778374995727` | `e2cddbc66760` | 2m 39s | 1h 2m 35s | 2m 36s | [25616155710](https://github.com/openclaw/openclaw/actions/runs/25616155710) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/e2cddbc66760-1778374995727` | `e2cddbc66760` | 11m 27s | 4h 58m 21s | 11m 23s | [25616154145](https://github.com/openclaw/openclaw/actions/runs/25616154145) | 45 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/e2cddbc66760-1778374995727` | `e2cddbc66760` | 3m 11s | 3m 2s | 8s | [25616197559](https://github.com/openclaw/openclaw/actions/runs/25616197559) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 11m 0s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616147785/job/75194481109) |
| 8m 28s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194609646) |
| 7m 48s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616147785/job/75194481111) |
| 7m 18s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194609777) |
| 6m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194609782) |
| 6m 10s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714944) |
| 6m 9s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194709559) |
| 6m 9s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714928) |
| 6m 9s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714933) |
| 6m 8s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194709557) |
| 5m 56s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714926) |
| 5m 55s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714927) |
| 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616147785/job/75194606465) |
| 3m 9s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616147785/job/75194481107) |
| 3m 2s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616197559/job/75194613542) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 11m 24s | 26s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25616147785/job/75195006107) |
| 11m 23s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75195028479) |
| 11m 15s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75195022194) |
| 7m 33s | 2m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833707) |
| 7m 33s | 3m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833709) |
| 7m 33s | 3m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833716) |
| 7m 32s | 1m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833692) |
| 7m 32s | 3m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833694) |
| 7m 32s | 1m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833695) |
| 7m 32s | 3m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833696) |
| 7m 32s | 3m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833701) |
| 2m 48s | 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616147785/job/75194606465) |
| 2m 36s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616155710/job/75194620146) |
| 2m 5s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616155710/job/75194594570) |
| 2m 3s | 4s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616155710/job/75194592881) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616147785
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616147785/job/75194481109
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25616147785/job/75195006107
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194609646
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194709533
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194709557
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194709559
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194709564
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714922
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714925
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714926
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714927
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714928
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714933
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714934
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714937
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194714944
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194757709
  - Run Docker release-path validation / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194825375
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194825383
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194825386
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833694
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833696
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833701
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833704
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833706
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833709
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833712
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): cancelled - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75194833716
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75195022194
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25616154145/job/75195028479

## Notes

Automatically requested by Full Release Validation 25616147785 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


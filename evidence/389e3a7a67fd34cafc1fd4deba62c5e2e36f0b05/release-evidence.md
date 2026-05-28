# OpenClaw Release Evidence: 389e3a7a67fd34cafc1fd4deba62c5e2e36f0b05

Generated: 2026-05-10T02:10:01.875Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `389e3a7a67fd34cafc1fd4deba62c5e2e36f0b05` |
| Release ref input | `389e3a7a67fd34cafc1fd4deba62c5e2e36f0b05` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `389e3a7a67fd34cafc1fd4deba62c5e2e36f0b05` |
| Release ref SHA | `389e3a7a67fd34cafc1fd4deba62c5e2e36f0b05` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/389e3a7a67fd-1778375672075` | `389e3a7a67fd` | 54m 59s | 1h 15m 49s | 54m 32s | [25616340383](https://github.com/openclaw/openclaw/actions/runs/25616340383) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/389e3a7a67fd-1778375672075` | `389e3a7a67fd` | 3m 8s | 1h 4m 55s | 3m 5s | [25616346524](https://github.com/openclaw/openclaw/actions/runs/25616346524) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/389e3a7a67fd-1778375672075` | `389e3a7a67fd` | 53m 41s | 8h 10m 16s | 53m 36s | [25616346695](https://github.com/openclaw/openclaw/actions/runs/25616346695) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/389e3a7a67fd-1778375672075` | `389e3a7a67fd` | 2m 57s | 2m 53s | 3s | [25616395568](https://github.com/openclaw/openclaw/actions/runs/25616395568) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 54m 14s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616340383/job/75195018450) |
| 48m 20s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195235181) |
| 28m 18s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195346045) |
| 26m 37s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195346033) |
| 24m 32s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195143631) |
| 13m 56s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195235182) |
| 11m 59s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195235176) |
| 11m 39s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195235173) |
| 11m 29s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195235167) |
| 11m 28s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195235191) |
| 11m 15s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616340383/job/75195018453) |
| 11m 8s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195235164) |
| 3m 39s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616340383/job/75195018456) |
| 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616340383/job/75195152105) |
| 2m 53s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616395568/job/75195158693) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 54m 32s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25616340383/job/75197560167) |
| 53m 36s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75197533295) |
| 14m 35s | 7s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195688086) |
| 7m 11s | 2m 10s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195357819) |
| 7m 10s | 4m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195357810) |
| 7m 10s | 1m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195357817) |
| 7m 9s | 1m 44s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195357798) |
| 7m 9s | 4m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195357812) |
| 7m 9s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195357814) |
| 7m 8s | 1m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195357801) |
| 7m 7s | 2m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195357800) |
| 3m 5s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346524/job/75195169580) |
| 3m 4s | 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616340383/job/75195152105) |
| 2m 2s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346524/job/75195121958) |
| 2m 2s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616346524/job/75195122510) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25616340383
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25616340383/job/75197560167
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25616346695
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195346033
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195346035
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75195346045
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25616346695/job/75197533295

## Notes

Automatically requested by Full Release Validation 25616340383 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


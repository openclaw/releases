# OpenClaw Release Evidence: 463e8ae0a7a6cadc597f6427dba0d7eaace6e036

Generated: 2026-05-10T05:48:13.364Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `463e8ae0a7a6cadc597f6427dba0d7eaace6e036` |
| Release ref input | `463e8ae0a7a6cadc597f6427dba0d7eaace6e036` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `463e8ae0a7a6cadc597f6427dba0d7eaace6e036` |
| Release ref SHA | `463e8ae0a7a6cadc597f6427dba0d7eaace6e036` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/463e8ae0a7a6-1778388400000` | `463e8ae0a7a6` | 1h 1m 46s | 1h 19m 42s | 1h 1m 14s | [25620083126](https://github.com/openclaw/openclaw/actions/runs/25620083126) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/463e8ae0a7a6-1778388400000` | `463e8ae0a7a6` | 3m 23s | 1h 10m 28s | 2m 50s | [25620088856](https://github.com/openclaw/openclaw/actions/runs/25620088856) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/463e8ae0a7a6-1778388400000` | `463e8ae0a7a6` | 1h 0m 17s | 7h 47m 22s | 1h 0m 13s | [25620089642](https://github.com/openclaw/openclaw/actions/runs/25620089642) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/463e8ae0a7a6-1778388400000` | `463e8ae0a7a6` | 2m 46s | 2m 42s | 3s | [25620144476](https://github.com/openclaw/openclaw/actions/runs/25620144476) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 0m 54s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620083126/job/75204987697) |
| 52m 31s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205301128) |
| 43m 4s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205209196) |
| 28m 20s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205101034) |
| 13m 31s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205209189) |
| 11m 56s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205209186) |
| 11m 30s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205209191) |
| 11m 28s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205209195) |
| 11m 14s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205209197) |
| 11m 6s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205209190) |
| 11m 3s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205209192) |
| 7m 44s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620083126/job/75204987698) |
| 3m 38s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620083126/job/75204987699) |
| 3m 27s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620083126/job/75204987702) |
| 3m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620083126/job/75205133855) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 1m 14s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620083126/job/75207850807) |
| 1h 0m 13s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75207821367) |
| 16m 8s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205666308) |
| 7m 56s | 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205311499) |
| 7m 55s | 8m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205311469) |
| 7m 55s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205311474) |
| 7m 54s | 4m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205311468) |
| 7m 53s | 4m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205311471) |
| 7m 52s | 1m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205311451) |
| 7m 52s | 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205311452) |
| 7m 52s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205311473) |
| 3m 45s | 3m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620083126/job/75205133855) |
| 2m 50s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620088856/job/75205110465) |
| 2m 35s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620088856/job/75205100245) |
| 2m 35s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620088856/job/75205100249) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25620083126
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25620083126/job/75207850807
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25620089642
  - cross_os_release_checks / Linux / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205209194
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75205301128
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25620089642/job/75207821367

## Notes

Automatically requested by Full Release Validation 25620083126 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


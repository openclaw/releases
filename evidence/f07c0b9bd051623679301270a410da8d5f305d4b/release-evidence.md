# OpenClaw Release Evidence: f07c0b9bd051623679301270a410da8d5f305d4b

Generated: 2026-05-10T00:31:40.030Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `f07c0b9bd051623679301270a410da8d5f305d4b` |
| Release ref input | `f07c0b9bd051623679301270a410da8d5f305d4b` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `f07c0b9bd051623679301270a410da8d5f305d4b` |
| Release ref SHA | `f07c0b9bd051623679301270a410da8d5f305d4b` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/f07c0b9bd051-1778371590877` | `f07c0b9bd051` | 24m 36s | 45m 29s | 24m 10s | [25615161167](https://github.com/openclaw/openclaw/actions/runs/25615161167) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/f07c0b9bd051-1778371590877` | `f07c0b9bd051` | 3m 0s | 1h 5m 26s | 2m 56s | [25615166620](https://github.com/openclaw/openclaw/actions/runs/25615166620) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/f07c0b9bd051-1778371590877` | `f07c0b9bd051` | 23m 56s | 6h 54m 1s | 23m 53s | [25615167267](https://github.com/openclaw/openclaw/actions/runs/25615167267) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/f07c0b9bd051-1778371590877` | `f07c0b9bd051` | 2m 59s | 2m 56s | 3s | [25615213638](https://github.com/openclaw/openclaw/actions/runs/25615213638) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 23m 53s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615161167/job/75191739847) |
| 21m 14s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75191859511) |
| 19m 3s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75191938364) |
| 17m 5s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192039737) |
| 14m 37s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192039757) |
| 13m 24s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75191938381) |
| 12m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192047815) |
| 11m 48s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615161167/job/75191739852) |
| 11m 46s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75191938376) |
| 11m 43s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75191938383) |
| 11m 34s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75191938401) |
| 11m 33s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75191938368) |
| 3m 21s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615161167/job/75191862628) |
| 3m 9s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615161167/job/75191739851) |
| 2m 56s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615213638/job/75191868929) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 24m 10s | 26s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615161167/job/75192877207) |
| 23m 53s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192880265) |
| 19m 44s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192673658) |
| 6m 55s | 12m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192047815) |
| 6m 55s | 1m 44s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192047816) |
| 6m 55s | 2m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192047826) |
| 6m 55s | 4m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192047828) |
| 6m 55s | 1m 34s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192047831) |
| 6m 55s | 1m 28s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192047832) |
| 6m 54s | 4m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192047818) |
| 6m 54s | 10m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192047819) |
| 3m 0s | 3m 21s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615161167/job/75191862628) |
| 2m 56s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615166620/job/75191872803) |
| 2m 31s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615166620/job/75191855053) |
| 1m 59s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615166620/job/75191829918) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615161167
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615161167/job/75191739847
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25615161167/job/75192877207
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615167267
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75191859511
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75191938364
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192039737
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192039757
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25615167267/job/75192880265

## Notes

Automatically requested by Full Release Validation 25615161167 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: release-2026.5.4

Generated: 2026-05-04T13:00:49.156Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `release-2026.5.4` |
| Release ref input | `release/2026.5.4` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.5.4` |
| Release ref SHA | `b4d5ebdcf1612511f3c90b03ac0dee176b4cbf8e` |
| Runs at release SHA | none |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `8469a51326d7` | 1h 1m 24s (+24m 8s) | 37m 18s (+16s) | 1h 1m 15s | [25317697670](https://github.com/openclaw/openclaw/actions/runs/25317697670) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `a90be474f441` | 36m 27s (-8s) | 1h 58m 23s (-7m 52s) | 36m 23s | [25318763088](https://github.com/openclaw/openclaw/actions/runs/25318763088) | 12 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 37m 1s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74222238984) |
| 31m 19s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864358) |
| 14m 30s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864350) |
| 12m 1s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864354) |
| 11m 23s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864422) |
| 11m 13s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864322) |
| 11m 5s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864318) |
| 11m 2s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864951) |
| 10m 49s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864341) |
| 2m 32s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222439259) |
| 1m 3s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222282484) |
| 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74222211366) |
| 8s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74227841223) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74222239236) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74222239470) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 1m 15s | 8s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74227841223) |
| 36m 23s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74227730321) |
| 24m 6s | 37m 1s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74222238984) |
| 23m 58s |  | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74222239712) |
| 23m 58s |  | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74222239935) |
| 23m 57s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74222239236) |
| 23m 57s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74222239470) |
| 23m 48s | 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74222211366) |
| 4m 56s | 31m 19s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864358) |
| 4m 54s | 12m 1s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864354) |
| 4m 50s | 1m 2s | `release-checks` | cross_os_release_checks / Windows / installer fresh | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864334) |
| 4m 25s | 11m 23s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864422) |
| 4m 25s | 11m 2s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864951) |
| 4m 22s | 10m 49s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864341) |
| 4m 17s | 11m 13s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864322) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 37m 16s | 1h 1m 24s | +24m 8s | +16s |
| `release-checks` | 36m 35s | 36m 27s | -8s | -7m 52s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25317697670
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25317697670/job/74227841223
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25318763088
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864334
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74222864358
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25318763088/job/74227730321

## Notes

Automatically requested by Full Release Validation 25317697670 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


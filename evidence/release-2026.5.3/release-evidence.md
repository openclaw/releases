# OpenClaw Release Evidence: release-2026.5.3

Generated: 2026-05-03T17:23:29.435Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `release-2026.5.3` |
| Release ref input | `release/2026.5.3` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.5.3` |
| Release ref SHA | `ad863498fad68185e6d8f106fa36445989825a71` |
| Runs at release SHA | none |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `3617778aaf8a` | 45m 14s (+18m 18s) | 1h 9m 1s (+21m 40s) | 44m 52s | [25284741367](https://github.com/openclaw/openclaw/actions/runs/25284741367) | 1 |
| pass | blocking | `normal-ci` | CI | `main` | `4e82cacc84dc` | 4m 8s (-3m 45s) | 1h 9m 24s (-12m 23s) | 4m 5s | [25284975286](https://github.com/openclaw/openclaw/actions/runs/25284975286) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `4e82cacc84dc` | 33m 4s (+7m 34s) | 22m 43s (-13h 12m 56s) | 33m 0s | [25284975523](https://github.com/openclaw/openclaw/actions/runs/25284975523) | 5 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `main` | `c5b559d4ee32` | 1m 52s (+1s) | 1m 41s (+4s) | 10s | [25285030859](https://github.com/openclaw/openclaw/actions/runs/25285030859) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 33m 40s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74127959100) |
| 25m 22s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74127959093) |
| 7m 29s | `release-checks` | Run QA Lab parity lane (baseline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129309604) |
| 4m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74127959115) |
| 3m 50s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975286/job/74127975849) |
| 2m 53s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129368385) |
| 2m 42s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975286/job/74127975807) |
| 2m 28s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74127959116) |
| 2m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74128096422) |
| 2m 13s | `normal-ci` | checks-node-core-fast | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975286/job/74127975991) |
| 2m 1s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975286/job/74127975797) |
| 1m 59s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129309603) |
| 1m 51s | `normal-ci` | checks-node-core-runtime-infra-process | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975286/job/74127975975) |
| 1m 46s | `release-checks` | Run QA Lab parity lane (candidate) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129309608) |
| 1m 43s | `normal-ci` | check-additional-extension-package-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975286/job/74127975855) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 44m 52s | 22s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74129826154) |
| 33m 0s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129791645) |
| 32m 3s | 55s | `release-checks` | Run QA Lab parity report | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129738010) |
| 26m 7s |  | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129402906) |
| 26m 7s |  | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129402968) |
| 26m 7s |  | `release-checks` | cross_os_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129403062) |
| 25m 33s | 2m 53s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129368385) |
| 25m 33s | 37s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129368392) |
| 25m 33s | 46s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129368396) |
| 25m 32s | 0s | `release-checks` | Run repo/live E2E validation / plan_docker_lane_groups | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129369088) |
| 25m 32s | 0s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129369118) |
| 13m 39s | 2m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74128096422) |
| 11m 10s | 25m 22s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74127959093) |
| 11m 10s | 33m 40s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74127959100) |
| 11m 10s | 4m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74127959115) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 26m 56s | 45m 14s | +18m 18s | +21m 40s |
| `release-checks` | 25m 30s | 33m 4s | +7m 34s | -13h 12m 56s |
| `normal-ci` | 7m 53s | 4m 8s | -3m 45s | -12m 23s |
| `postpublish-telegram` | 1m 51s | 1m 52s | +1s | +4s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25284741367
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25284741367/job/74129826154
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25284975523
  - Prepare release package artifact: failure - https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129309605
  - Run repo/live E2E validation / validate_selected_ref: failure - https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129309661
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25284975523/job/74129791645

## Notes

Automatically requested by Full Release Validation 25284741367 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


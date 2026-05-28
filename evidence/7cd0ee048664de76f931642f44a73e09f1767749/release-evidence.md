# OpenClaw Release Evidence: 7cd0ee048664de76f931642f44a73e09f1767749

Generated: 2026-05-09T22:23:22.067Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `7cd0ee048664de76f931642f44a73e09f1767749` |
| Release ref input | `7cd0ee048664de76f931642f44a73e09f1767749` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `7cd0ee048664de76f931642f44a73e09f1767749` |
| Release ref SHA | `7cd0ee048664de76f931642f44a73e09f1767749` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/7cd0ee048664-1778363343212` | `7cd0ee048664` | 34m 1s | 1h 25m 22s | 33m 29s | [25612656456](https://github.com/openclaw/openclaw/actions/runs/25612656456) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/7cd0ee048664-1778363343212` | `7cd0ee048664` | 11m 37s | 1h 26m 55s | 2m 44s | [25612663230](https://github.com/openclaw/openclaw/actions/runs/25612663230) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/7cd0ee048664-1778363343212` | `7cd0ee048664` | 33m 18s | 7h 28m 9s | 33m 15s | [25612663489](https://github.com/openclaw/openclaw/actions/runs/25612663489) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/7cd0ee048664-1778363343212` | `7cd0ee048664` | 3m 20s | 3m 5s | 14s | [25612717907](https://github.com/openclaw/openclaw/actions/runs/25612717907) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 33m 10s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612656456/job/75185367629) |
| 33m 10s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612656456/job/75185367633) |
| 28m 13s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185495739) |
| 27m 28s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185600007) |
| 25m 54s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185717691) |
| 23m 41s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185717669) |
| 13m 26s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185600005) |
| 11m 55s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185600017) |
| 11m 54s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185600013) |
| 11m 52s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612656456/job/75185367630) |
| 11m 43s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185600008) |
| 11m 41s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185600016) |
| 11m 16s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185600011) |
| 11m 1s | `normal-ci` | macos-node | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25612663230/job/75185383654) |
| 3m 49s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612656456/job/75185501542) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 33m 29s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25612656456/job/75187018852) |
| 33m 15s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75187025930) |
| 15m 11s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75186113327) |
| 7m 34s | 2m 22s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185729624) |
| 7m 34s | 1m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185729648) |
| 7m 33s | 4m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185729628) |
| 7m 33s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185729649) |
| 7m 32s | 1m 13s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185729630) |
| 7m 32s | 4m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185729635) |
| 7m 32s | 4m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185729636) |
| 7m 32s | 3m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185729650) |
| 2m 57s | 3m 49s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612656456/job/75185501542) |
| 2m 44s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663230/job/75185508977) |
| 2m 9s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663230/job/75185474797) |
| 2m 4s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612663230/job/75185470383) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612656456
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612656456/job/75185367629
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612656456/job/75185367633
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25612656456/job/75187018852
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25612663230
  - macos-node: failure - https://github.com/openclaw/openclaw/actions/runs/25612663230/job/75185383654
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612663489
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185600007
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185717669
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75185717691
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25612663489/job/75187025930

## Notes

Automatically requested by Full Release Validation 25612656456 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


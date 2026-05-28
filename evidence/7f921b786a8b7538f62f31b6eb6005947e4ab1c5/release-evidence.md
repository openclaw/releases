# OpenClaw Release Evidence: 7f921b786a8b7538f62f31b6eb6005947e4ab1c5

Generated: 2026-05-10T03:12:26.426Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `7f921b786a8b7538f62f31b6eb6005947e4ab1c5` |
| Release ref input | `7f921b786a8b7538f62f31b6eb6005947e4ab1c5` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `7f921b786a8b7538f62f31b6eb6005947e4ab1c5` |
| Release ref SHA | `7f921b786a8b7538f62f31b6eb6005947e4ab1c5` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/7f921b786a8b-1778381753506` | `7f921b786a8b` | 16m 4s | 34m 26s | 15m 38s | [25618147505](https://github.com/openclaw/openclaw/actions/runs/25618147505) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/7f921b786a8b-1778381753506` | `7f921b786a8b` | 2m 39s | 1h 8m 46s | 2m 36s | [25618152321](https://github.com/openclaw/openclaw/actions/runs/25618152321) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/7f921b786a8b-1778381753506` | `7f921b786a8b` | 15m 29s | 6h 17m 1s | 15m 24s | [25618152505](https://github.com/openclaw/openclaw/actions/runs/25618152505) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/7f921b786a8b-1778381753506` | `7f921b786a8b` | 3m 0s | 2m 48s | 11s | [25618206417](https://github.com/openclaw/openclaw/actions/runs/25618206417) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 15m 16s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25618147505/job/75199721501) |
| 12m 49s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199830501) |
| 10m 7s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975930) |
| 10m 5s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975904) |
| 10m 5s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975919) |
| 9m 52s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975923) |
| 9m 51s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199964715) |
| 9m 50s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975913) |
| 9m 29s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975905) |
| 9m 11s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199964726) |
| 9m 9s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975912) |
| 8m 49s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618147505/job/75199721497) |
| 3m 21s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618147505/job/75199869867) |
| 3m 15s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618147505/job/75199721498) |
| 3m 11s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618147505/job/75199721494) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 15m 38s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25618147505/job/75200524310) |
| 15m 24s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200533412) |
| 15m 16s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200527255) |
| 8m 2s | 4m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200119314) |
| 8m 1s | 5m 43s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200119308) |
| 8m 1s | 1m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200119361) |
| 8m 0s | 1m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200119279) |
| 8m 0s | 4m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200119284) |
| 8m 0s | 7m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200119289) |
| 8m 0s | 4m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200119302) |
| 8m 0s | 4m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200119312) |
| 3m 32s | 3m 21s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618147505/job/75199869867) |
| 2m 36s | 2s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25618152321/job/75199838985) |
| 2m 31s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152321/job/75199830186) |
| 2m 25s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618152321/job/75199830184) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618147505
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618147505/job/75199721501
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25618147505/job/75200524310
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25618152321
  - checks-node-core-fast: failure - https://github.com/openclaw/openclaw/actions/runs/25618152321/job/75199736758
  - checks-node-agentic-cli: failure - https://github.com/openclaw/openclaw/actions/runs/25618152321/job/75199736763
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25618152321/job/75199838985
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199830501
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975904
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975905
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975906
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975912
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975913
  - cross_os_release_checks / Linux / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975915
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975919
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975923
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75199975930
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200096743
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200119289
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): cancelled - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200119303
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200527255
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25618152505/job/75200533412

## Notes

Automatically requested by Full Release Validation 25618147505 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


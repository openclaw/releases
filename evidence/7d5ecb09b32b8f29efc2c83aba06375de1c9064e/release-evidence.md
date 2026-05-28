# OpenClaw Release Evidence: 7d5ecb09b32b8f29efc2c83aba06375de1c9064e

Generated: 2026-05-10T00:54:29.522Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `7d5ecb09b32b8f29efc2c83aba06375de1c9064e` |
| Release ref input | `7d5ecb09b32b8f29efc2c83aba06375de1c9064e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `7d5ecb09b32b8f29efc2c83aba06375de1c9064e` |
| Release ref SHA | `7d5ecb09b32b8f29efc2c83aba06375de1c9064e` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/7d5ecb09b32b-1778373425055` | `7d5ecb09b32b` | 17m 1s | 37m 56s | 16m 34s | [25615689321](https://github.com/openclaw/openclaw/actions/runs/25615689321) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/7d5ecb09b32b-1778373425055` | `7d5ecb09b32b` | 2m 49s | 1h 6m 33s | 2m 47s | [25615695328](https://github.com/openclaw/openclaw/actions/runs/25615695328) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/7d5ecb09b32b-1778373425055` | `7d5ecb09b32b` | 16m 22s | 6h 6m 50s | 16m 19s | [25615694947](https://github.com/openclaw/openclaw/actions/runs/25615694947) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/7d5ecb09b32b-1778373425055` | `7d5ecb09b32b` | 3m 10s | 3m 6s | 3s | [25615744700](https://github.com/openclaw/openclaw/actions/runs/25615744700) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 16m 18s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615689321/job/75193198790) |
| 13m 50s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193322610) |
| 11m 55s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421719) |
| 11m 37s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421728) |
| 11m 30s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421720) |
| 11m 22s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615689321/job/75193198789) |
| 11m 14s | `release-checks` | cross_os_release_checks / Windows / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421722) |
| 11m 8s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421717) |
| 11m 7s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421715) |
| 11m 4s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421716) |
| 11m 4s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421721) |
| 11m 4s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421724) |
| 3m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615689321/job/75193334762) |
| 3m 12s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615689321/job/75193198798) |
| 3m 6s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615744700/job/75193342572) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 16m 34s | 26s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615689321/job/75193994439) |
| 16m 19s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193996914) |
| 14m 35s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193914363) |
| 7m 10s | 1m 17s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193544116) |
| 7m 10s | 1m 19s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193544152) |
| 7m 9s | 1m 43s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193544102) |
| 7m 9s | 9m 8s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193544104) |
| 7m 9s | 1m 39s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193544107) |
| 7m 9s | 2m 5s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193544113) |
| 7m 9s | 1m 24s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193544115) |
| 7m 8s | 2m 43s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193543061) |
| 2m 59s | 3m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615689321/job/75193334762) |
| 2m 47s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615695328/job/75193343760) |
| 2m 13s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615695328/job/75193308110) |
| 2m 7s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615695328/job/75193308115) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615689321
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615689321/job/75193198790
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25615689321/job/75193994439
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615694947
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193322610
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193390322
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421717
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421719
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421722
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421724
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193421728
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193544095
  - Run Docker release-path validation / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193544104
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193544106
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25615694947/job/75193996914

## Notes

Automatically requested by Full Release Validation 25615689321 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


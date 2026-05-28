# OpenClaw Release Evidence: 3ded12d2c82927b0856532af1bdba5c304310c56

Generated: 2026-05-09T21:00:59.474Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `3ded12d2c82927b0856532af1bdba5c304310c56` |
| Release ref input | `3ded12d2c82927b0856532af1bdba5c304310c56` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `3ded12d2c82927b0856532af1bdba5c304310c56` |
| Release ref SHA | `3ded12d2c82927b0856532af1bdba5c304310c56` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/3ded12d2c829-1778357173485` | `3ded12d2c829` | 54m 30s | 2h 6m 0s | 53m 56s | [25610596909](https://github.com/openclaw/openclaw/actions/runs/25610596909) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/3ded12d2c829-1778357173485` | `3ded12d2c829` | 53m 11s | 2h 12m 2s | 2m 58s | [25610603977](https://github.com/openclaw/openclaw/actions/runs/25610603977) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/3ded12d2c829-1778357173485` | `3ded12d2c829` | 53m 17s | 8h 29m 19s | 53m 13s | [25610604031](https://github.com/openclaw/openclaw/actions/runs/25610604031) | 45 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/3ded12d2c829-1778357173485` | `3ded12d2c829` | 3m 20s | 3m 7s | 12s | [25610657016](https://github.com/openclaw/openclaw/actions/runs/25610657016) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 53m 31s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610596909/job/75180002346) |
| 53m 23s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610596909/job/75180002342) |
| 52m 58s | `normal-ci` | macos-swift | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610603977/job/75180018765) |
| 48m 35s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180246110) |
| 42m 28s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180246104) |
| 33m 31s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180367589) |
| 26m 25s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180367545) |
| 23m 44s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180134290) |
| 21m 1s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180246109) |
| 14m 3s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180246115) |
| 13m 29s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180246096) |
| 11m 56s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610596909/job/75180002352) |
| 11m 42s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180246095) |
| 11m 31s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180246106) |
| 4m 14s | `normal-ci` | android-test-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610603977/job/75180018795) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 53m 56s | 33s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25610596909/job/75182863253) |
| 53m 13s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75182849845) |
| 17m 15s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180956827) |
| 9m 53s | 1m 29s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180524951) |
| 9m 53s | 1m 29s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180524955) |
| 9m 53s | 1m 32s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180524964) |
| 9m 53s | 1m 28s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180524979) |
| 9m 53s | 1m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180524981) |
| 9m 53s | 1m 17s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180524982) |
| 9m 53s | 2m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180524990) |
| 9m 53s | 2m 7s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180525001) |
| 2m 58s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610603977/job/75180152061) |
| 2m 57s | 3m 47s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610596909/job/75180139786) |
| 2m 8s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610603977/job/75180116101) |
| 2m 4s | 3m 43s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610603977/job/75180018799) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610596909
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610596909/job/75180002342
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610596909/job/75180002346
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25610596909/job/75182863253
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610603977
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610603977/job/75180018765
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610604031
  - cross_os_release_checks / macOS / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180246109
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180246110
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180367545
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75180367589
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25610604031/job/75182849845

## Notes

Automatically requested by Full Release Validation 25610596909 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


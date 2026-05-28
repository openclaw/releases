# OpenClaw Release Evidence: 9a42779911fed7ffbbb7cef26ce6a94f5f7b90e5

Generated: 2026-05-09T19:14:56.669Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `9a42779911fed7ffbbb7cef26ce6a94f5f7b90e5` |
| Release ref input | `9a42779911fed7ffbbb7cef26ce6a94f5f7b90e5` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `9a42779911fed7ffbbb7cef26ce6a94f5f7b90e5` |
| Release ref SHA | `9a42779911fed7ffbbb7cef26ce6a94f5f7b90e5` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/9a42779911fe-1778352719727` | `9a42779911fe` | 22m 38s | 1h 2m 37s | 22m 5s | [25609100782](https://github.com/openclaw/openclaw/actions/runs/25609100782) | 1 |
| running | blocking | `normal-ci` | CI | `release-ci/9a42779911fe-1778352719727` | `9a42779911fe` | 21m 21s | 1h 18m 45s | 16m 9s | [25609109089](https://github.com/openclaw/openclaw/actions/runs/25609109089) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/9a42779911fe-1778352719727` | `9a42779911fe` | 21m 46s | 6h 36m 37s | 21m 43s | [25609109436](https://github.com/openclaw/openclaw/actions/runs/25609109436) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/9a42779911fe-1778352719727` | `9a42779911fe` | 3m 21s | 3m 7s | 13s | [25609165205](https://github.com/openclaw/openclaw/actions/runs/25609165205) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 21m 41s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609100782/job/75176069241) |
| 21m 37s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609100782/job/75176069244) |
| 19m 7s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176207253) |
| 16m 19s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176321309) |
| 15m 11s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176321305) |
| 14m 31s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176436901) |
| 13m 49s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176321323) |
| 12m 16s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609100782/job/75176069238) |
| 12m 6s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176321304) |
| 11m 57s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176436885) |
| 11m 44s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176321299) |
| 11m 33s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176321306) |
| 11m 11s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176321302) |
| 10m 1s | `normal-ci` | macos-node | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609109089/job/75176087327) |
| 3m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609100782/job/75176209219) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 22m 5s | 32s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609100782/job/75177238516) |
| 21m 43s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75177242431) |
| 16m 9s |  | `normal-ci` | macos-swift |  | [job](https://github.com/openclaw/openclaw/actions/runs/25609109089/job/75176087345) |
| 14m 7s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176846357) |
| 7m 11s | 1m 8s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176441856) |
| 7m 11s | 1m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176441857) |
| 7m 11s | 3m 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176441858) |
| 7m 11s | 6m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176441866) |
| 7m 11s | 4m 45s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176441876) |
| 7m 11s | 4m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176441880) |
| 7m 10s | 11m 57s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176436885) |
| 7m 10s | 1m 54s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176436889) |
| 3m 4s | 3m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609100782/job/75176209219) |
| 2m 40s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109089/job/75176215457) |
| 2m 37s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609109089/job/75176206695) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609100782
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609100782/job/75176069241
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609100782/job/75176069244
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25609100782/job/75177238516
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609109436
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176207253
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176321309
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176436885
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75176436901
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25609109436/job/75177242431

## Notes

Automatically requested by Full Release Validation 25609100782 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


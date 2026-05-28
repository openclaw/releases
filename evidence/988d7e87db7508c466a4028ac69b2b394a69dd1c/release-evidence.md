# OpenClaw Release Evidence: 988d7e87db7508c466a4028ac69b2b394a69dd1c

Generated: 2026-05-09T18:53:10.599Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `988d7e87db7508c466a4028ac69b2b394a69dd1c` |
| Release ref input | `988d7e87db7508c466a4028ac69b2b394a69dd1c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `988d7e87db7508c466a4028ac69b2b394a69dd1c` |
| Release ref SHA | `988d7e87db7508c466a4028ac69b2b394a69dd1c` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/988d7e87db75-1778351334602` | `988d7e87db75` | 23m 46s | 1h 6m 17s | 23m 16s | [25608611922](https://github.com/openclaw/openclaw/actions/runs/25608611922) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/988d7e87db75-1778351334602` | `988d7e87db75` | 22m 41s | 1h 23m 47s | 20m 23s | [25608620504](https://github.com/openclaw/openclaw/actions/runs/25608620504) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/988d7e87db75-1778351334602` | `988d7e87db75` | 22m 36s | 6h 51m 59s | 15m 39s | [25608620512](https://github.com/openclaw/openclaw/actions/runs/25608620512) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/988d7e87db75-1778351334602` | `988d7e87db75` | 3m 10s | 2m 49s | 20s | [25608676323](https://github.com/openclaw/openclaw/actions/runs/25608676323) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 22m 57s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608611922/job/75174767447) |
| 22m 57s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608611922/job/75174767449) |
| 20m 31s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75174918154) |
| 17m 47s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175038868) |
| 16m 19s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175159429) |
| 16m 11s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175159431) |
| 14m 5s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175038881) |
| 13m 56s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175038869) |
| 13m 55s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608611922/job/75174767452) |
| 12m 30s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175014186) |
| 12m 28s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175159430) |
| 11m 44s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175038867) |
| 11m 28s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175038878) |
| 10m 0s | `normal-ci` | macos-node | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25608620504/job/75174788382) |
| 3m 20s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620504/job/75174788386) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 23m 16s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25608611922/job/75176061731) |
| 20m 23s | 2m 17s | `normal-ci` | macos-swift | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608620504/job/75174788365) |
| 15m 39s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175655175) |
| 8m 28s | 11m 15s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175038873) |
| 7m 12s | 8m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175181368) |
| 7m 12s | 4m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175181370) |
| 7m 12s | 5m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175181371) |
| 7m 12s | 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175181377) |
| 7m 11s | 1m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175181355) |
| 7m 11s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175181358) |
| 7m 11s | 1m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175181359) |
| 7m 11s | 2m 8s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620512/job/75175181364) |
| 2m 48s | 3m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608611922/job/75174920781) |
| 2m 45s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620504/job/75174940043) |
| 2m 27s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608620504/job/75174915659) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608611922
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608611922/job/75174767447
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608611922/job/75174767449
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25608611922/job/75176061731
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608620504
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608620504/job/75174788365
  - macos-node: failure - https://github.com/openclaw/openclaw/actions/runs/25608620504/job/75174788382

## Notes

Automatically requested by Full Release Validation 25608611922 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


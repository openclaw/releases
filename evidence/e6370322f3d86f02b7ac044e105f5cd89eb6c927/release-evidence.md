# OpenClaw Release Evidence: e6370322f3d86f02b7ac044e105f5cd89eb6c927

Generated: 2026-05-09T21:01:03.139Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `e6370322f3d86f02b7ac044e105f5cd89eb6c927` |
| Release ref input | `e6370322f3d86f02b7ac044e105f5cd89eb6c927` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `e6370322f3d86f02b7ac044e105f5cd89eb6c927` |
| Release ref SHA | `e6370322f3d86f02b7ac044e105f5cd89eb6c927` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/e6370322f3d8-1778359525182` | `e6370322f3d8` | 15m 13s | 47m 43s | 14m 40s | [25611396859](https://github.com/openclaw/openclaw/actions/runs/25611396859) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/e6370322f3d8-1778359525182` | `e6370322f3d8` | 14m 1s | 1h 44m 31s | 2m 56s | [25611403128](https://github.com/openclaw/openclaw/actions/runs/25611403128) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/e6370322f3d8-1778359525182` | `e6370322f3d8` | 14m 37s | 5h 51m 46s | 14m 34s | [25611403305](https://github.com/openclaw/openclaw/actions/runs/25611403305) | 44 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/e6370322f3d8-1778359525182` | `e6370322f3d8` | 3m 7s | 2m 55s | 11s | [25611458192](https://github.com/openclaw/openclaw/actions/runs/25611458192) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 14m 20s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611396859/job/75182132157) |
| 14m 20s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611396859/job/75182132160) |
| 13m 44s | `normal-ci` | macos-node | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403128/job/75182151929) |
| 13m 44s | `normal-ci` | macos-swift | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403128/job/75182151963) |
| 12m 16s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611396859/job/75182132163) |
| 11m 50s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182272126) |
| 9m 57s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368529) |
| 9m 57s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368545) |
| 9m 56s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368555) |
| 9m 39s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368541) |
| 9m 39s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368554) |
| 9m 39s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368556) |
| 9m 17s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368531) |
| 9m 17s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368533) |
| 9m 13s | `release-checks` | cross_os_release_checks / Windows / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368562) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 14m 40s | 32s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25611396859/job/75182864548) |
| 14m 34s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182885081) |
| 14m 22s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182870537) |
| 7m 9s | 1m 33s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500837) |
| 7m 8s | 7m 13s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500811) |
| 7m 8s | 4m 19s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500813) |
| 7m 8s | 7m 24s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500814) |
| 7m 8s | 1m 50s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500815) |
| 7m 8s | 1m 16s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500825) |
| 7m 8s | 1m 47s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500826) |
| 7m 8s | 1m 26s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500829) |
| 3m 3s | 3m 19s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611396859/job/75182283178) |
| 2m 56s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611403128/job/75182295130) |
| 2m 8s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611403128/job/75182248099) |
| 2m 3s | 4s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611403128/job/75182249582) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611396859
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611396859/job/75182132157
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611396859/job/75182132160
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25611396859/job/75182864548
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403128
  - macos-node: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403128/job/75182151929
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403128/job/75182151963
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182272126
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182342331
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368529
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368531
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368533
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368541
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368545
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368554
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368555
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368556
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182368562
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182499737
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500811
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500814
  - Run Docker release-path validation / Docker E2E (plugins/runtime install H): cancelled - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182500824
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182870537
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25611403305/job/75182885081

## Notes

Automatically requested by Full Release Validation 25611396859 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


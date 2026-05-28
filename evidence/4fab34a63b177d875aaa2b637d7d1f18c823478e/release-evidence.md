# OpenClaw Release Evidence: 4fab34a63b177d875aaa2b637d7d1f18c823478e

Generated: 2026-05-04T21:02:10.799Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `4fab34a63b177d875aaa2b637d7d1f18c823478e` |
| Release ref input | `4fab34a63b177d875aaa2b637d7d1f18c823478e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `4fab34a63b177d875aaa2b637d7d1f18c823478e` |
| Release ref SHA | `4fab34a63b177d875aaa2b637d7d1f18c823478e` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/4fab34a63b17-1777926239509` | `4fab34a63b17` | 37m 51s | 37m 34s | 37m 43s | [25341602438](https://github.com/openclaw/openclaw/actions/runs/25341602438) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/4fab34a63b17-1777926239509` | `4fab34a63b17` | 37m 3s | 57m 40s | 37m 0s | [25341619503](https://github.com/openclaw/openclaw/actions/runs/25341619503) | 6 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 37m 19s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341602438/job/74300007384) |
| 31m 14s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300651026) |
| 11m 26s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300651059) |
| 11m 14s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300650994) |
| 2m 19s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300204469) |
| 1m 0s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300039950) |
| 25s | `release-checks` | cross_os_release_checks / prepare | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300576086) |
| 8s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341602438/job/74299978801) |
| 7s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25341602438/job/74305996331) |
| 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74305940397) |
| 0s | `release-checks` | Run repo/live E2E validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300204690) |
| 0s | `release-checks` | Run QA Lab live Slack lane | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300204788) |
| 0s | `release-checks` | Run QA Lab parity lane (${{ matrix.lane }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300204800) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 37m 43s | 7s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25341602438/job/74305996331) |
| 37m 0s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74305940397) |
| 5m 37s | 31m 14s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300651026) |
| 4m 10s | 11m 14s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300650994) |
| 3m 56s | 11m 26s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300651059) |
| 3m 29s | 25s | `release-checks` | cross_os_release_checks / prepare | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300576086) |
| 3m 27s | 0s | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300576127) |
| 3m 27s | 0s | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300576449) |
| 1m 8s | 2m 19s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300204469) |
| 1m 7s |  | `release-checks` | Run QA Lab live Matrix lane | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300205326) |
| 1m 6s | 0s | `release-checks` | Run repo/live E2E validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300204690) |
| 15s | 37m 19s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25341602438/job/74300007384) |
| 13s |  | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25341602438/job/74300007851) |
| 13s |  | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25341602438/job/74300007874) |
| 13s |  | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25341602438/job/74300007937) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25341602438
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25341602438/job/74305996331
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25341619503
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74300651026
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25341619503/job/74305940397

## Notes

Automatically requested by Full Release Validation 25341602438 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: ecab09870a3b31ecb528718bb5d20562fa94d0c5

Generated: 2026-05-04T01:15:54.207Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `ecab09870a3b31ecb528718bb5d20562fa94d0c5` |
| Release ref input | `ecab09870a3b31ecb528718bb5d20562fa94d0c5` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `ecab09870a3b31ecb528718bb5d20562fa94d0c5` |
| Release ref SHA | `ecab09870a3b31ecb528718bb5d20562fa94d0c5` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/ecab09870a3b-1777856189854` | `ecab09870a3b` | 19m 10s | 19m 2s | 19m 2s | [25295902805](https://github.com/openclaw/openclaw/actions/runs/25295902805) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/ecab09870a3b-1777856189854` | `ecab09870a3b` | 18m 14s | 1h 37m 20s | 18m 11s | [25295909708](https://github.com/openclaw/openclaw/actions/runs/25295909708) | 11 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 18m 47s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74154582533) |
| 13m 12s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856370) |
| 12m 0s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856377) |
| 11m 29s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856376) |
| 11m 19s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856372) |
| 11m 14s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856380) |
| 11m 5s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856374) |
| 10m 59s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856383) |
| 10m 51s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856378) |
| 2m 31s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154661136) |
| 1m 7s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856412) |
| 8s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74154571367) |
| 7s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74155760105) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74154582776) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74154582778) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 19m 2s | 7s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74155760105) |
| 18m 11s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74155713716) |
| 5m 11s | 1m 7s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856412) |
| 4m 56s | 12m 0s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856377) |
| 4m 51s | 13m 12s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856370) |
| 4m 28s | 10m 51s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856378) |
| 4m 28s | 11m 14s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856380) |
| 4m 27s | 10m 59s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856383) |
| 4m 14s | 11m 19s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856372) |
| 4m 14s | 11m 5s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856374) |
| 4m 14s | 11m 29s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856376) |
| 13s | 18m 47s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74154582533) |
| 12s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74154582776) |
| 12s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74154582778) |
| 12s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74154582808) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25295902805
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25295902805/job/74155760105
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25295909708
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74154856412
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25295909708/job/74155713716

## Notes

Automatically requested by Full Release Validation 25295902805 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: ac00d7882a2c6d986fadd72ee1c50940c2b4dc76

Generated: 2026-05-04T03:01:16.969Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `ac00d7882a2c6d986fadd72ee1c50940c2b4dc76` |
| Release ref input | `ac00d7882a2c6d986fadd72ee1c50940c2b4dc76` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `ac00d7882a2c6d986fadd72ee1c50940c2b4dc76` |
| Release ref SHA | `ac00d7882a2c6d986fadd72ee1c50940c2b4dc76` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/ac00d7882a2c-1777863295010` | `ac00d7882a2c` | 6m 6s | 5m 56s | 6m 1s | [25298725875](https://github.com/openclaw/openclaw/actions/runs/25298725875) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/ac00d7882a2c-1777863295010` | `ac00d7882a2c` | 5m 16s | 8m 5s | 5m 12s | [25298733934](https://github.com/openclaw/openclaw/actions/runs/25298733934) | 3 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 45s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74161759046) |
| 4m 1s | `release-checks` | Run QA Lab live Slack lane | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834428) |
| 1m 54s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834423) |
| 1m 4s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834427) |
| 1m 3s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161769792) |
| 7s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74161748253) |
| 4s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74162133772) |
| 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74162095643) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74161759211) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74161759247) |
| 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74161759303) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74161759304) |
| 0s | `release-checks` | Run QA Lab parity lane (${{ matrix.lane }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834515) |
| 0s | `release-checks` | Run repo/live E2E validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834554) |
| 0s | `release-checks` | Run QA Lab parity report | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834572) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6m 1s | 4s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74162133772) |
| 5m 12s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74162095643) |
| 1m 9s | 1m 54s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834423) |
| 1m 9s | 1m 4s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834427) |
| 1m 9s | 4m 1s | `release-checks` | Run QA Lab live Slack lane | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834428) |
| 1m 8s | 0s | `release-checks` | Run QA Lab parity lane (${{ matrix.lane }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834515) |
| 1m 8s | 0s | `release-checks` | Run repo/live E2E validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834554) |
| 1m 8s | 0s | `release-checks` | Run QA Lab parity report | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834572) |
| 1m 8s | 0s | `release-checks` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834578) |
| 1m 8s | 0s | `release-checks` | cross_os_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834616) |
| 1m 8s | 0s | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834638) |
| 13s | 5m 45s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74161759046) |
| 11s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74161759211) |
| 11s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74161759247) |
| 11s | 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74161759303) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25298725875
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25298725875/job/74162133772
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25298733934
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74161834428
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25298733934/job/74162095643

## Notes

Automatically requested by Full Release Validation 25298725875 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


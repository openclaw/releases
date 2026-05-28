# OpenClaw Release Evidence: 1ab00c44699dbe2527c3b200d0f3d9791200d2df

Generated: 2026-05-07T00:43:54.829Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `1ab00c44699dbe2527c3b200d0f3d9791200d2df` |
| Release ref input | `1ab00c44699dbe2527c3b200d0f3d9791200d2df` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `1ab00c44699dbe2527c3b200d0f3d9791200d2df` |
| Release ref SHA | `1ab00c44699dbe2527c3b200d0f3d9791200d2df` |
| Runs at release SHA | `full-release-validation` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `release-ci/1ab00c44699d-1778092677570` | `1ab00c44699d` | 6h 5m 37s | 6h 5m 13s | 6h 5m 33s | [25454042037](https://github.com/openclaw/openclaw/actions/runs/25454042037) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 6h 5m 1s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678645354) |
| 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678591880) |
| 3s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74729711598) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678645949) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678646121) |
| 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678646170) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678646195) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6h 5m 33s | 3s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74729711598) |
| 30s | 6h 5m 1s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678645354) |
| 21s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678645949) |
| 21s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678646121) |
| 21s | 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678646170) |
| 21s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678646195) |
| 12s | 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678591880) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25454042037
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74678645354
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25454042037/job/74729711598

## Notes

Automatically requested by Full Release Validation 25454042037 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


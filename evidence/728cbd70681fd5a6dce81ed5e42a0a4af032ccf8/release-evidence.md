# OpenClaw Release Evidence: 728cbd70681fd5a6dce81ed5e42a0a4af032ccf8

Generated: 2026-04-29T17:55:09.266Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `728cbd70681fd5a6dce81ed5e42a0a4af032ccf8` |
| Release ref input | `728cbd70681fd5a6dce81ed5e42a0a4af032ccf8` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `728cbd70681fd5a6dce81ed5e42a0a4af032ccf8` |
| Release ref SHA | `728cbd70681fd5a6dce81ed5e42a0a4af032ccf8` |
| Runs at release SHA | none |
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
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `53e0874864cb` | 2h 12m 45s | 59m 25s | 2h 12m 39s | [25118708250](https://github.com/openclaw/openclaw/actions/runs/25118708250) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 19m 42s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921478) |
| 19m 42s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921481) |
| 19m 42s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921580) |
| 14s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73613038382) |
| 5s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73619448211) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921898) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2h 12m 39s | 5s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73619448211) |
| 15m 5s | 19m 42s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921478) |
| 15m 5s | 19m 42s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921481) |
| 15m 5s | 19m 42s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921580) |
| 15m 5s | 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921898) |
| 14m 51s | 14s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73613038382) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25118708250
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921478
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921481
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73615921580
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25118708250/job/73619448211

## Notes

Automatically requested by Full Release Validation 25118708250 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


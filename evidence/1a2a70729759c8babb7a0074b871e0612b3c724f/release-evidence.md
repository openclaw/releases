# OpenClaw Release Evidence: 1a2a70729759c8babb7a0074b871e0612b3c724f

Generated: 2026-04-29T15:56:58.397Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `1a2a70729759c8babb7a0074b871e0612b3c724f` |
| Release ref input | `1a2a70729759c8babb7a0074b871e0612b3c724f` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `1a2a70729759c8babb7a0074b871e0612b3c724f` |
| Release ref SHA | `1a2a70729759c8babb7a0074b871e0612b3c724f` |
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

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `240362bf6d0e` | 19m 31s | 4m 59s | [25118448812](https://github.com/openclaw/openclaw/actions/runs/25118448812) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 4m 52s | `full-release-validation` | Resolve target ref | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25118448812/job/73612101936) |
| 7s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25118448812/job/73613021531) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25118448812
  - Resolve target ref: cancelled - https://github.com/openclaw/openclaw/actions/runs/25118448812/job/73612101936
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25118448812/job/73613021418
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25118448812/job/73613021524
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25118448812/job/73613021531
  - Run post-publish Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25118448812/job/73613021669
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25118448812/job/73613021754

## Notes

Automatically requested by Full Release Validation 25118448812 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


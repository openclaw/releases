# OpenClaw Release Evidence: 5370add03b9dae95efb44b2199879ee73ec85966

Generated: 2026-04-29T15:56:29.152Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `5370add03b9dae95efb44b2199879ee73ec85966` |
| Release ref input | `5370add03b9dae95efb44b2199879ee73ec85966` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `5370add03b9dae95efb44b2199879ee73ec85966` |
| Release ref SHA | `5370add03b9dae95efb44b2199879ee73ec85966` |
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
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `1390eadd9289` | 29m 1s | 12m 9s | [25117937001](https://github.com/openclaw/openclaw/actions/runs/25117937001) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 12m 3s | `full-release-validation` | Resolve target ref | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25117937001/job/73610229231) |
| 6s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25117937001/job/73612510331) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25117937001
  - Resolve target ref: cancelled - https://github.com/openclaw/openclaw/actions/runs/25117937001/job/73610229231
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25117937001/job/73612510135
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25117937001/job/73612510331
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25117937001/job/73612510359
  - Run post-publish Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25117937001/job/73612510469
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25117937001/job/73612510477

## Notes

Automatically requested by Full Release Validation 25117937001 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


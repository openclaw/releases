# OpenClaw Release Evidence: 09d044e0f4

Generated: 2026-04-28T00:00:42.291Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `09d044e0f4` |
| Release ref input | `09d044e0f4` |
| Release ref status | not-found |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
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
| fail | blocking | `full-release-validation` | Full Release Validation | `release/2026.4.26` | `09d044e0f494` | 53s | 45s | [25026100167](https://github.com/openclaw/openclaw/actions/runs/25026100167) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 43s | `full-release-validation` | Resolve target ref | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25026100167/job/73297425803) |
| 2s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25026100167/job/73297512055) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25026100167
  - Resolve target ref: failure - https://github.com/openclaw/openclaw/actions/runs/25026100167/job/73297425803
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25026100167/job/73297512055

## Notes

Automatically requested by Full Release Validation 25026100167 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


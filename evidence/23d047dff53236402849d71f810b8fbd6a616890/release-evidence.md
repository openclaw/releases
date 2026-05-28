# OpenClaw Release Evidence: 23d047dff53236402849d71f810b8fbd6a616890

Generated: 2026-04-27T13:35:02.742Z
Release ref: `23d047dff53236402849d71f810b8fbd6a616890`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 0 | 0 | 2 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `c00ef238bea9` | [24998076529](https://github.com/openclaw/openclaw/actions/runs/24998076529) | 0 |
| running | blocking | `normal-ci` | CI | `main` | `ad0f600450ef` | [24998122446](https://github.com/openclaw/openclaw/actions/runs/24998122446) | 0 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `ad0f600450ef` | [24998125172](https://github.com/openclaw/openclaw/actions/runs/24998125172) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998076529
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998076529/job/73200441653
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998076529/job/73200441655
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24998076529/job/73200651586

## Notes

Automatically requested by Full Release Validation 24998076529 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


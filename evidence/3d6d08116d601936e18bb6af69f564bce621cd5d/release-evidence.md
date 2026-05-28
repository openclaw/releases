# OpenClaw Release Evidence: 3d6d08116d601936e18bb6af69f564bce621cd5d

Generated: 2026-04-27T07:20:37.744Z
Release ref: `3d6d08116d601936e18bb6af69f564bce621cd5d`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `3d6d08116d60` | [24981178181](https://github.com/openclaw/openclaw/actions/runs/24981178181) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `baace37fefe2` | [24981209072](https://github.com/openclaw/openclaw/actions/runs/24981209072) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `baace37fefe2` | [24981209211](https://github.com/openclaw/openclaw/actions/runs/24981209211) | 19 |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/24981178181
  - Run normal full CI: failure - https://github.com/openclaw/openclaw/actions/runs/24981178181/job/73143595325
  - Run release/live/Docker/QA validation: failure - https://github.com/openclaw/openclaw/actions/runs/24981178181/job/73143595351
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24981178181/job/73145610978
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/24981209072
  - check-docs: failure - https://github.com/openclaw/openclaw/actions/runs/24981209072/job/73143631836
  - checks-node-agentic-plugin-sdk: failure - https://github.com/openclaw/openclaw/actions/runs/24981209072/job/73143632024
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/24981209072/job/73144039121

## Notes

Automatically requested by Full Release Validation 24981178181 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


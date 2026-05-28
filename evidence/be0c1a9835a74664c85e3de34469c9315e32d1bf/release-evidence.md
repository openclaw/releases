# OpenClaw Release Evidence: be0c1a9835a74664c85e3de34469c9315e32d1bf

Generated: 2026-04-27T16:35:08.900Z
Release ref: `be0c1a9835a74664c85e3de34469c9315e32d1bf`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 0 | 0 | 2 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `be0c1a9835a7` | [25006780615](https://github.com/openclaw/openclaw/actions/runs/25006780615) | 0 |
| running | blocking | `normal-ci` | CI | `main` | `be0c1a9835a7` | [25006824613](https://github.com/openclaw/openclaw/actions/runs/25006824613) | 0 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `be0c1a9835a7` | [25006825536](https://github.com/openclaw/openclaw/actions/runs/25006825536) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25006780615
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25006780615/job/73231747243
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25006780615/job/73231747247
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25006780615/job/73233626072

## Notes

Automatically requested by Full Release Validation 25006780615 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


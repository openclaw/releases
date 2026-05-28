# OpenClaw Release Evidence: 56ca4e2269dfd7bc8bdb17a297f438f44f2c1f34

Generated: 2026-04-27T08:40:59.598Z
Release ref: `56ca4e2269dfd7bc8bdb17a297f438f44f2c1f34`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `56ca4e2269df` | [24984903871](https://github.com/openclaw/openclaw/actions/runs/24984903871) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `e21c909bd020` | [24984939140](https://github.com/openclaw/openclaw/actions/runs/24984939140) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `e21c909bd020` | [24984939809](https://github.com/openclaw/openclaw/actions/runs/24984939809) | 6 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24984903871
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24984903871/job/73155755316
  - Run normal full CI: failure - https://github.com/openclaw/openclaw/actions/runs/24984903871/job/73155755449
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24984903871/job/73156330632
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/24984939140
  - check-lint: failure - https://github.com/openclaw/openclaw/actions/runs/24984939140/job/73155804323
  - check-test-types: failure - https://github.com/openclaw/openclaw/actions/runs/24984939140/job/73155804324
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/24984939140/job/73155919110

## Notes

Automatically requested by Full Release Validation 24984903871 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 1b581b4c71215d7f9d5a894bc460faadf21cfc06

Generated: 2026-04-27T11:49:01.117Z
Release ref: `1b581b4c71215d7f9d5a894bc460faadf21cfc06`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 0 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `1b581b4c7121` | [24988474853](https://github.com/openclaw/openclaw/actions/runs/24988474853) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `fee16865b229` | [24988511161](https://github.com/openclaw/openclaw/actions/runs/24988511161) | 3 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `main` | `fee16865b229` | [24988512874](https://github.com/openclaw/openclaw/actions/runs/24988512874) | 21 |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/24988474853
  - Run release/live/Docker/QA validation: failure - https://github.com/openclaw/openclaw/actions/runs/24988474853/job/73167811066
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24988474853/job/73179073496

## Notes

Manual refresh after rerunning failed Windows installer fresh child job; OpenClaw Release Checks attempt 2 passed. Full Release Validation wrapper remains advisory because it cannot update after child rerun.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


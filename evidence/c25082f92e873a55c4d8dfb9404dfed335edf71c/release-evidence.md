# OpenClaw Release Evidence: c25082f92e873a55c4d8dfb9404dfed335edf71c

Generated: 2026-04-27T08:36:12.863Z
Release ref: `c25082f92e873a55c4d8dfb9404dfed335edf71c`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `c25082f92e87` | [24984839690](https://github.com/openclaw/openclaw/actions/runs/24984839690) | 0 |
| running | blocking | `normal-ci` | CI | `main` | `56ca4e2269df` | [24984875812](https://github.com/openclaw/openclaw/actions/runs/24984875812) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `56ca4e2269df` | [24984876341](https://github.com/openclaw/openclaw/actions/runs/24984876341) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24984839690
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/24984839690/job/73155543348
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24984839690/job/73155543386
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24984839690/job/73155670198
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24984876341
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/24984876341/job/73155564275
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/24984876341/job/73155648392
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/24984876341/job/73155648445
  - Run QA Lab parity gate: cancelled - https://github.com/openclaw/openclaw/actions/runs/24984876341/job/73155648621
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/24984876341/job/73155648877

## Notes

Automatically requested by Full Release Validation 24984839690 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


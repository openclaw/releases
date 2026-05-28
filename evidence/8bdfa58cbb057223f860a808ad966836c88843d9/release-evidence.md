# OpenClaw Release Evidence: 8bdfa58cbb057223f860a808ad966836c88843d9

Generated: 2026-04-27T08:10:57.940Z
Release ref: `8bdfa58cbb057223f860a808ad966836c88843d9`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `8bdfa58cbb05` | [24983762289](https://github.com/openclaw/openclaw/actions/runs/24983762289) | 0 |
| running | blocking | `normal-ci` | CI | `main` | `563718c2e4c4` | [24983799517](https://github.com/openclaw/openclaw/actions/runs/24983799517) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `563718c2e4c4` | [24983799848](https://github.com/openclaw/openclaw/actions/runs/24983799848) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983762289
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983762289/job/73151980949
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983762289/job/73151980969
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24983762289/job/73152196780
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983799848
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983799848/job/73152001222
  - Run QA Lab parity gate: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983799848/job/73152173032
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/24983799848/job/73152173093
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983799848/job/73152173095
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983799848/job/73152173544

## Notes

Automatically requested by Full Release Validation 24983762289 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


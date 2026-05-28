# OpenClaw Release Evidence: c41126dbbb9b8b865ce10764bd6417a6e3320720

Generated: 2026-04-27T15:24:54.909Z
Release ref: `c41126dbbb9b8b865ce10764bd6417a6e3320720`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `c41126dbbb9b` | [25002155064](https://github.com/openclaw/openclaw/actions/runs/25002155064) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `c41126dbbb9b` | [25002218643](https://github.com/openclaw/openclaw/actions/runs/25002218643) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `c41126dbbb9b` | [25002216540](https://github.com/openclaw/openclaw/actions/runs/25002216540) | 22 |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25002155064
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25002155064/job/73221179231
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25002216540
  - Run QA Lab parity gate: failure - https://github.com/openclaw/openclaw/actions/runs/25002216540/job/73216452467
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-l-z, Native live plugins L-Z, node scripts/...: failure - https://github.com/openclaw/openclaw/actions/runs/25002216540/job/73216625518
  - cross_os_release_checks / macOS / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25002216540/job/73216954932
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25002216540/job/73221067718

## Notes

Automatically requested by Full Release Validation 25002155064 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


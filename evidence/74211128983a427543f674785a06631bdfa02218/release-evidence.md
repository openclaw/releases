# OpenClaw Release Evidence: 74211128983a427543f674785a06631bdfa02218

Generated: 2026-04-27T08:58:56.262Z
Release ref: `74211128983a427543f674785a06631bdfa02218`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `74211128983a` | [24985828822](https://github.com/openclaw/openclaw/actions/runs/24985828822) | 0 |
| running | blocking | `normal-ci` | CI | `main` | `caba05b94a26` | [24985866027](https://github.com/openclaw/openclaw/actions/runs/24985866027) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `caba05b94a26` | [24985867328](https://github.com/openclaw/openclaw/actions/runs/24985867328) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985828822
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985828822/job/73158854264
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985828822/job/73158854270
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24985828822/job/73158993763
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985867328
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985867328/job/73158875893
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985867328/job/73158964415
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/24985867328/job/73158964547
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985867328/job/73158964553
  - Run QA Lab parity gate: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985867328/job/73158964565

## Notes

Automatically requested by Full Release Validation 24985828822 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


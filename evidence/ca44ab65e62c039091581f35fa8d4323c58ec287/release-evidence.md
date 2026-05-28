# OpenClaw Release Evidence: ca44ab65e62c039091581f35fa8d4323c58ec287

Generated: 2026-04-27T06:47:50.650Z
Release ref: `ca44ab65e62c039091581f35fa8d4323c58ec287`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `ca44ab65e62c` | [24979917565](https://github.com/openclaw/openclaw/actions/runs/24979917565) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `ca44ab65e62c` | [24979947793](https://github.com/openclaw/openclaw/actions/runs/24979947793) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `ca44ab65e62c` | [24979947785](https://github.com/openclaw/openclaw/actions/runs/24979947785) | 19 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24979917565
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24979917565/job/73139699575
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24979917565/job/73141775848

## Notes

Automatically requested by Full Release Validation 24979917565 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


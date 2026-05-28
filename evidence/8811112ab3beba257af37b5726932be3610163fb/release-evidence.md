# OpenClaw Release Evidence: 8811112ab3beba257af37b5726932be3610163fb

Generated: 2026-04-27T07:00:06.459Z
Release ref: `8811112ab3beba257af37b5726932be3610163fb`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `8811112ab3be` | [24980624017](https://github.com/openclaw/openclaw/actions/runs/24980624017) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `8811112ab3be` | [24980654029](https://github.com/openclaw/openclaw/actions/runs/24980654029) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `8811112ab3be` | [24980653833](https://github.com/openclaw/openclaw/actions/runs/24980653833) | 19 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24980624017
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24980624017/job/73141841829
  - Run normal full CI: failure - https://github.com/openclaw/openclaw/actions/runs/24980624017/job/73141841830
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24980624017/job/73143163293
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/24980654029
  - checks-node-core-runtime-shared: failure - https://github.com/openclaw/openclaw/actions/runs/24980654029/job/73141875262
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/24980654029/job/73142272077

## Notes

Automatically requested by Full Release Validation 24980624017 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


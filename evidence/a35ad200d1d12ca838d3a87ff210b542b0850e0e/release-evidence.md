# OpenClaw Release Evidence: a35ad200d1d12ca838d3a87ff210b542b0850e0e

Generated: 2026-04-27T08:54:20.250Z
Release ref: `a35ad200d1d12ca838d3a87ff210b542b0850e0e`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `a35ad200d1d1` | [24985105270](https://github.com/openclaw/openclaw/actions/runs/24985105270) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `a35ad200d1d1` | [24985141544](https://github.com/openclaw/openclaw/actions/runs/24985141544) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `a35ad200d1d1` | [24985141920](https://github.com/openclaw/openclaw/actions/runs/24985141920) | 20 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985105270
  - Run normal full CI: failure - https://github.com/openclaw/openclaw/actions/runs/24985105270/job/73156421305
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985105270/job/73156421329
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24985105270/job/73158289152
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/24985141544
  - check-lint: failure - https://github.com/openclaw/openclaw/actions/runs/24985141544/job/73156468463
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/24985141544/job/73156584524

## Notes

Automatically requested by Full Release Validation 24985105270 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


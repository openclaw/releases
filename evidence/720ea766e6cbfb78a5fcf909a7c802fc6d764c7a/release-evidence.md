# OpenClaw Release Evidence: 720ea766e6cbfb78a5fcf909a7c802fc6d764c7a

Generated: 2026-04-27T07:43:03.195Z
Release ref: `720ea766e6cbfb78a5fcf909a7c802fc6d764c7a`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `720ea766e6cb` | [24982131697](https://github.com/openclaw/openclaw/actions/runs/24982131697) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `720ea766e6cb` | [24982165171](https://github.com/openclaw/openclaw/actions/runs/24982165171) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `720ea766e6cb` | [24982164832](https://github.com/openclaw/openclaw/actions/runs/24982164832) | 21 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24982131697
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24982131697/job/73146687436
  - Run normal full CI: failure - https://github.com/openclaw/openclaw/actions/runs/24982131697/job/73146687450
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24982131697/job/73148435868
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/24982165171
  - checks-node-core-fast-support: failure - https://github.com/openclaw/openclaw/actions/runs/24982165171/job/73146726996
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/24982165171/job/73146966493
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/24982165171/job/73147191177

## Notes

Automatically requested by Full Release Validation 24982131697 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


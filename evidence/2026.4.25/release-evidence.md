# OpenClaw Release Evidence: 2026.4.25

Generated: 2026-04-27T12:37:03.890Z
Release ref: `v2026.4.25`
Package spec: `openclaw@2026.4.25`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 0 | 0 | 3 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `252c63429ecf` | [24995015431](https://github.com/openclaw/openclaw/actions/runs/24995015431) | 0 |
| running | blocking | `normal-ci` | CI | `main` | `252c63429ecf` | [24995069603](https://github.com/openclaw/openclaw/actions/runs/24995069603) | 2 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `252c63429ecf` | [24995070521](https://github.com/openclaw/openclaw/actions/runs/24995070521) | 0 |
| running | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `main` | `252c63429ecf` | [24995069268](https://github.com/openclaw/openclaw/actions/runs/24995069268) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24995015431
  - Run post-publish Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/24995015431/job/73189786747
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24995015431/job/73189786761
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/24995015431/job/73189786783
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24995015431/job/73190867991

## Notes

Automatically requested by Full Release Validation 24995015431 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


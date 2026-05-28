# OpenClaw Release Evidence: 090063bd43ed8420d8c5384292eee6b427e3d8d6

Generated: 2026-04-27T07:02:59.566Z
Release ref: `090063bd43ed8420d8c5384292eee6b427e3d8d6`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `090063bd43ed` | [24981065682](https://github.com/openclaw/openclaw/actions/runs/24981065682) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `89230f248017` | [24981099154](https://github.com/openclaw/openclaw/actions/runs/24981099154) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `89230f248017` | [24981099489](https://github.com/openclaw/openclaw/actions/runs/24981099489) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981065682
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981065682/job/73143239617
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981065682/job/73143239627
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24981065682/job/73143516193
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981099154
  - check-docs: failure - https://github.com/openclaw/openclaw/actions/runs/24981099154/job/73143278183
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981099154/job/73143278208
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981099154/job/73143278209
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981099154/job/73143278210
  - checks-node-agentic-agents: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981099154/job/73143278390
  - checks-node-agentic-control-plane: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981099154/job/73143278393
  - checks-node-agentic-plugin-sdk: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981099154/job/73143278400
  - checks-node-auto-reply-reply-commands-state-routing: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981099154/job/73143278452
  - checks-node-auto-reply-reply-dispatch: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981099154/job/73143278466
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/24981099154/job/73143527699

## Notes

Automatically requested by Full Release Validation 24981065682 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


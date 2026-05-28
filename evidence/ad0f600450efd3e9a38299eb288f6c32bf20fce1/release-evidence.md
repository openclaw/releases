# OpenClaw Release Evidence: ad0f600450efd3e9a38299eb288f6c32bf20fce1

Generated: 2026-04-27T13:38:43.058Z
Release ref: `ad0f600450efd3e9a38299eb288f6c32bf20fce1`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `eb1a2010606b` | [24998172983](https://github.com/openclaw/openclaw/actions/runs/24998172983) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `eb1a2010606b` | [24998225031](https://github.com/openclaw/openclaw/actions/runs/24998225031) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `eb1a2010606b` | [24998226102](https://github.com/openclaw/openclaw/actions/runs/24998226102) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998172983
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998172983/job/73200796501
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998172983/job/73200796510
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24998172983/job/73201302974
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73200860277
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73200860310
  - checks-node-extensions-shard-5: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73200860545
  - checks-node-core-runtime-infra: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73200860637
  - checks-node-core-fast-support: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73200860642
  - checks-node-agentic-plugin-sdk: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73200860666
  - checks-node-extensions-shard-4: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73200860749
  - checks-node-auto-reply-reply-commands-state-routing: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73200860805
  - checks-node-agentic-agents: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73200860936
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73201192836
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73201193231
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73201193253
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73201193266
  - checks-node-extensions: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73201194546
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998225031/job/73201219164

## Notes

Automatically requested by Full Release Validation 24998172983 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


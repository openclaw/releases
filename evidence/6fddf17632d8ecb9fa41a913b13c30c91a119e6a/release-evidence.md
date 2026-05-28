# OpenClaw Release Evidence: 6fddf17632d8ecb9fa41a913b13c30c91a119e6a

Generated: 2026-04-27T08:57:29.264Z
Release ref: `6fddf17632d8ecb9fa41a913b13c30c91a119e6a`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `6fddf17632d8` | [24985687964](https://github.com/openclaw/openclaw/actions/runs/24985687964) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `b81eaf8a4e89` | [24985725944](https://github.com/openclaw/openclaw/actions/runs/24985725944) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `b81eaf8a4e89` | [24985727368](https://github.com/openclaw/openclaw/actions/runs/24985727368) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985687964
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985687964/job/73158386781
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985687964/job/73158386788
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24985687964/job/73158772259
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158422338
  - checks-node-extensions-shard-4: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158422376
  - checks-node-extensions-shard-3: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158422418
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158422476
  - checks-node-extensions-shard-5: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158422481
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158422528
  - checks-node-agentic-agents: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158422644
  - checks-node-agentic-plugin-sdk: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158422674
  - checks-node-auto-reply-reply-dispatch: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158422725
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158735955
  - checks-node-extensions: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158783279
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158798892
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158798984
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158798993
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158799423
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/24985725944/job/73158799453

## Notes

Automatically requested by Full Release Validation 24985687964 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


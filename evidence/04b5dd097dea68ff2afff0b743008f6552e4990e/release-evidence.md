# OpenClaw Release Evidence: 04b5dd097dea68ff2afff0b743008f6552e4990e

Generated: 2026-04-27T16:23:38.059Z
Release ref: `04b5dd097dea68ff2afff0b743008f6552e4990e`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `04b5dd097dea` | [25005799806](https://github.com/openclaw/openclaw/actions/runs/25005799806) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `b72414c94e0a` | [25005843281](https://github.com/openclaw/openclaw/actions/runs/25005843281) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `b72414c94e0a` | [25005844548](https://github.com/openclaw/openclaw/actions/runs/25005844548) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005799806
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005799806/job/73228218836
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005799806/job/73228218886
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25005799806/job/73231669990
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228308846
  - checks-node-compat-node22: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228308848
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228308893
  - check-test-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228308905
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228308939
  - check-prod-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309009
  - checks-fast-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309013
  - checks-fast-contracts-plugins: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309044
  - android-test-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309161
  - checks-node-extensions-shard-3: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309176
  - checks-node-extensions-shard-1: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309192
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309200
  - checks-node-extensions-shard-4: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309221
  - checks-node-extensions-shard-6: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309229
  - checks-node-extensions-shard-2: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309235
  - android-test-third-party: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309271
  - checks-node-extensions-shard-5: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309292
  - checks-node-core-runtime-infra: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309397
  - checks-node-agentic-control-plane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73228309465
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73231607063
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73231607070
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73231607178
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73231607328
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73231607418
  - checks-node-extensions: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73231607716
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005843281/job/73231607935
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005844548
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005844548/job/73228253432
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005844548/job/73231608052
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25005844548/job/73231608089
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005844548/job/73231608426
  - Run QA Lab parity gate: cancelled - https://github.com/openclaw/openclaw/actions/runs/25005844548/job/73231608557

## Notes

Automatically requested by Full Release Validation 25005799806 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: a2af8054e1a480a4171c944cb41847e3285927e4

Generated: 2026-04-27T14:19:54.588Z
Release ref: `a2af8054e1a480a4171c944cb41847e3285927e4`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `a2af8054e1a4` | [25000113033](https://github.com/openclaw/openclaw/actions/runs/25000113033) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `a2af8054e1a4` | [25000160296](https://github.com/openclaw/openclaw/actions/runs/25000160296) | 0 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `a2af8054e1a4` | [25000162299](https://github.com/openclaw/openclaw/actions/runs/25000162299) | 11 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000113033
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000113033/job/73207744766
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000113033/job/73207744815
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25000113033/job/73208883617
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296
  - checks-fast-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811012
  - checks-node-compat-node22: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811026
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811027
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811069
  - checks-node-extensions-shard-1: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811086
  - checks-node-extensions-shard-6: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811097
  - checks-fast-contracts-plugins: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811107
  - checks-node-extensions-shard-3: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811119
  - checks-node-extensions-shard-5: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811126
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811159
  - checks-node-extensions-shard-4: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811160
  - check-test-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811196
  - checks-node-extensions-shard-2: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811224
  - check-prod-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811225
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811238
  - android-test-third-party: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811279
  - checks-node-core-runtime-infra: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811546
  - checks-node-agentic-plugins: failure - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811567
  - checks-node-agentic-control-plane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811588
  - checks-node-agentic-agents: failure - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73207811596
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73208894394
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73208900674
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73208900934
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73208900936
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73208900974
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73208934833
  - checks-node-extensions: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000160296/job/73208939075

## Notes

Automatically requested by Full Release Validation 25000113033 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


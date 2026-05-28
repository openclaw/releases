# OpenClaw Release Evidence: 42fc17609387ce01f347872469652f720fb6d4be

Generated: 2026-04-27T14:41:30.317Z
Release ref: `42fc17609387ce01f347872469652f720fb6d4be`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `42fc17609387` | [25001066242](https://github.com/openclaw/openclaw/actions/runs/25001066242) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `42fc17609387` | [25001118463](https://github.com/openclaw/openclaw/actions/runs/25001118463) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `42fc17609387` | [25001120337](https://github.com/openclaw/openclaw/actions/runs/25001120337) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001066242
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001066242/job/73211182438
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001066242/job/73211182453
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25001066242/job/73212991187
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245447
  - checks-fast-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245454
  - checks-node-compat-node22: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245456
  - check-prod-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245483
  - checks-fast-contracts-plugins: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245492
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245513
  - checks-node-extensions-shard-3: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245523
  - checks-node-extensions-shard-6: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245531
  - android-test-third-party: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245538
  - checks-node-extensions-shard-1: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245544
  - checks-node-extensions-shard-5: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245560
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245576
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245590
  - check-test-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245591
  - android-test-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245594
  - checks-node-extensions-shard-2: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245604
  - checks-node-extensions-shard-4: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245637
  - checks-node-agentic-control-plane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245673
  - checks-node-core-runtime-infra: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73211245767
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73212881747
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73212882025
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73212882051
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73212882278
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73212882286
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73212882475
  - checks-node-extensions: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001118463/job/73212882641
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001120337
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001120337/job/73211223087
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001120337/job/73212885726
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25001120337/job/73212885759
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001120337/job/73212886100
  - Run QA Lab parity gate: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001120337/job/73212886353

## Notes

Automatically requested by Full Release Validation 25001066242 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


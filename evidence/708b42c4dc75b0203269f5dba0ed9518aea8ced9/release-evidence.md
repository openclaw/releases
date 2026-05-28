# OpenClaw Release Evidence: 708b42c4dc75b0203269f5dba0ed9518aea8ced9

Generated: 2026-04-27T14:49:40.925Z
Release ref: `708b42c4dc75b0203269f5dba0ed9518aea8ced9`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `708b42c4dc75` | [25001971102](https://github.com/openclaw/openclaw/actions/runs/25001971102) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `fd6c9fc7f5f6` | [25001636309](https://github.com/openclaw/openclaw/actions/runs/25001636309) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `fd6c9fc7f5f6` | [25001636847](https://github.com/openclaw/openclaw/actions/runs/25001636847) | 0 |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25001971102
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25001971102/job/73214543233
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309
  - checks-node-compat-node22: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213129806
  - checks-fast-contracts-plugins: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213129823
  - checks-fast-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213129838
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213129941
  - checks-node-extensions-shard-1: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213129982
  - checks-node-extensions-shard-2: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213129987
  - checks-node-extensions-shard-5: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213129990
  - checks-node-extensions-shard-6: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130091
  - check-prod-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130145
  - android-test-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130172
  - checks-node-extensions-shard-3: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130208
  - check-test-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130220
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130233
  - checks-node-extensions-shard-4: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130236
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130268
  - android-test-third-party: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130307
  - checks-node-core-runtime-infra: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130340
  - checks-node-agentic-control-plane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130389
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73213130538
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73214261950
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73214262039
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73214262242
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73214262456
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73214262640
  - checks-node-extensions: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73214263253
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636309/job/73214263858
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636847
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636847/job/73213118964
  - Run QA Lab parity gate: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636847/job/73214263091
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636847/job/73214263254
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25001636847/job/73214263271
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25001636847/job/73214263930

## Notes

Automatically requested by Full Release Validation 25001971102 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


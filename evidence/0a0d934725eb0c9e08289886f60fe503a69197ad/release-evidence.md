# OpenClaw Release Evidence: 0a0d934725eb0c9e08289886f60fe503a69197ad

Generated: 2026-04-27T23:30:04.295Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `0a0d934725eb0c9e08289886f60fe503a69197ad` |
| Release ref input | `0a0d934725eb0c9e08289886f60fe503a69197ad` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `0a0d934725eb0c9e08289886f60fe503a69197ad` |
| Release ref SHA | `0a0d934725eb0c9e08289886f60fe503a69197ad` |
| Runs at release SHA | `full-release-validation` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `0a0d934725eb` | 2m 3s | 2m 50s | [25025037863](https://github.com/openclaw/openclaw/actions/runs/25025037863) | 0 |
| running | blocking | `normal-ci` | CI | `main` | `fc055e2393cd` | 41s | 22m 34s | [25025068544](https://github.com/openclaw/openclaw/actions/runs/25025068544) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `fc055e2393cd` | 51s | 43s | [25025068858](https://github.com/openclaw/openclaw/actions/runs/25025068858) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 57s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025037863/job/73294244534) |
| 57s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025037863/job/73294244565) |
| 47s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025037863/job/73294158379) |
| 42s | `normal-ci` | build-artifacts | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068544/job/73294282421) |
| 42s | `normal-ci` | checks-node-extensions-shard-4 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068544/job/73294282449) |
| 42s | `normal-ci` | android-test-third-party | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068544/job/73294282509) |
| 41s | `normal-ci` | checks-fast-bundled | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068544/job/73294282404) |
| 41s | `normal-ci` | checks-node-extensions-shard-6 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068544/job/73294282451) |
| 41s | `normal-ci` | checks-node-extensions-shard-5 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068544/job/73294282452) |
| 41s | `normal-ci` | checks-node-extensions-shard-3 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068544/job/73294282456) |
| 40s | `normal-ci` | checks-fast-contracts-plugins | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068544/job/73294282399) |
| 40s | `normal-ci` | checks-node-compat-node22 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068544/job/73294282417) |
| 40s | `normal-ci` | checks-node-extensions-shard-2 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068544/job/73294282464) |
| 40s | `release-checks` | resolve_target | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025068858/job/73294258865) |
| 9s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025037863/job/73294349658) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025037863
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025037863/job/73294244534
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025037863/job/73294244565
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25025037863/job/73294349658
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025068858
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025068858/job/73294258865
  - Run QA Lab parity lane (${{ matrix.lane }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025068858/job/73294334759
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025068858/job/73294334845
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25025068858/job/73294335030
  - Run QA Lab parity report: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025068858/job/73294335039
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025068858/job/73294335055

## Notes

Automatically requested by Full Release Validation 25025037863 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


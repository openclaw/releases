# OpenClaw Release Evidence: fb4d9fc4fb5e6901603b17bc7967ee488eca565c

Generated: 2026-04-27T21:19:13.494Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `fb4d9fc4fb5e6901603b17bc7967ee488eca565c` |
| Release ref input | `fb4d9fc4fb5e6901603b17bc7967ee488eca565c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `fb4d9fc4fb5e6901603b17bc7967ee488eca565c` |
| Release ref SHA | `fb4d9fc4fb5e6901603b17bc7967ee488eca565c` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `fb4d9fc4fb5e` | 4m 55s | 8m 37s | [25019895993](https://github.com/openclaw/openclaw/actions/runs/25019895993) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `fb4d9fc4fb5e` | 3m 54s | 56m 10s | [25019933876](https://github.com/openclaw/openclaw/actions/runs/25019933876) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `fb4d9fc4fb5e` | 3m 36s | 26m 52s | [25019933459](https://github.com/openclaw/openclaw/actions/runs/25019933459) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 3m 54s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25019895993/job/73277578215) |
| 3m 53s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25019895993/job/73277578216) |
| 2m 11s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627921) |
| 2m 9s | `normal-ci` | checks-node-extensions-shard-2 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627692) |
| 2m 1s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627730) |
| 1m 59s | `normal-ci` | build-artifacts | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627588) |
| 1m 57s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627924) |
| 1m 56s | `normal-ci` | checks-node-extensions-shard-6 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627701) |
| 1m 53s | `normal-ci` | checks-node-core-runtime-infra | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627932) |
| 1m 50s | `normal-ci` | checks-node-extensions-shard-5 | success | [job](https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627749) |
| 1m 38s | `normal-ci` | checks-node-auto-reply-reply-dispatch | success | [job](https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627908) |
| 1m 38s | `normal-ci` | checks-node-auto-reply-reply-commands-state-routing | success | [job](https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627927) |
| 1m 31s | `release-checks` | Run QA Lab parity gate | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25019933459/job/73277934995) |
| 1m 31s | `release-checks` | Run QA Lab live Matrix lane | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25019933459/job/73277935078) |
| 1m 29s | `release-checks` | Run QA Lab live Telegram lane | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25019933459/job/73277935034) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019895993
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019895993/job/73277578215
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019895993/job/73277578216
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25019895993/job/73278142361
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627588
  - checks-fast-contracts-plugins: failure - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627640
  - checks-node-extensions-shard-2: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627692
  - checks-node-extensions-shard-6: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627701
  - check-additional-runtime-topology-architecture: failure - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627728
  - check-additional-boundaries: failure - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627761
  - checks-node-core-runtime-infra: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73277627932
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73278127323
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73278127376
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73278127386
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73278127490
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73278127500
  - checks-node-extensions: cancelled - https://github.com/openclaw/openclaw/actions/runs/25019933876/job/73278154256

## Notes

Automatically requested by Full Release Validation 25019895993 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


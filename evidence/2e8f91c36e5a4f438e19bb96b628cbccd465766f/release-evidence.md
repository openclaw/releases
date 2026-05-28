# OpenClaw Release Evidence: 2e8f91c36e5a4f438e19bb96b628cbccd465766f

Generated: 2026-04-28T13:30:37.874Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2e8f91c36e5a4f438e19bb96b628cbccd465766f` |
| Release ref input | `2e8f91c36e5a4f438e19bb96b628cbccd465766f` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `2e8f91c36e5a4f438e19bb96b628cbccd465766f` |
| Release ref SHA | `2e8f91c36e5a4f438e19bb96b628cbccd465766f` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.4.27` | `2e8f91c36e5a` | 23m 26s | 46m 1s | [25054609840](https://github.com/openclaw/openclaw/actions/runs/25054609840) | 0 |
| fail | blocking | `normal-ci` | CI | `release/2026.4.27` | `2e8f91c36e5a` | 22m 54s | 1h 5m 33s | [25054629760](https://github.com/openclaw/openclaw/actions/runs/25054629760) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.4.27` | `2e8f91c36e5a` | 20m 59s | 4m 32s | [25054631607](https://github.com/openclaw/openclaw/actions/runs/25054631607) | 2 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 22m 51s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25054609840/job/73391352485) |
| 22m 49s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25054609840/job/73391352569) |
| 2m 54s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422383) |
| 2m 29s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422183) |
| 2m 24s | `normal-ci` | checks-node-auto-reply-reply-commands-state-routing | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422608) |
| 2m 11s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422168) |
| 2m 7s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422140) |
| 2m 4s | `normal-ci` | checks-node-core-runtime-infra | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422506) |
| 1m 57s | `release-checks` | Run QA Lab parity lane (candidate) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054631607/job/73395179530) |
| 1m 56s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422121) |
| 1m 53s | `normal-ci` | checks-node-extensions-shard-2 | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422271) |
| 1m 47s | `normal-ci` | checks-node-extensions-shard-5 | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422253) |
| 1m 46s | `normal-ci` | checks-node-extensions-shard-1 | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422515) |
| 1m 40s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054631607/job/73395179551) |
| 49s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25054631607/job/73391394536) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25054609840
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25054609840/job/73391352485
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25054609840/job/73391352569
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25054609840/job/73395507499
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25054629760
  - checks-node-extensions-shard-5: failure - https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73391422253
  - checks-node-extensions: failure - https://github.com/openclaw/openclaw/actions/runs/25054629760/job/73395378280

## Notes

Automatically requested by Full Release Validation 25054609840 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


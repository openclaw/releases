# OpenClaw Release Evidence: f71f5bc5866f40306c6fb6fb05b67ddced5d2b26

Generated: 2026-04-27T23:28:18.797Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `f71f5bc5866f40306c6fb6fb05b67ddced5d2b26` |
| Release ref input | `f71f5bc5866f40306c6fb6fb05b67ddced5d2b26` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `f71f5bc5866f40306c6fb6fb05b67ddced5d2b26` |
| Release ref SHA | `f71f5bc5866f40306c6fb6fb05b67ddced5d2b26` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `f71f5bc5866f` | 3m 44s | 6m 14s | [25024926855](https://github.com/openclaw/openclaw/actions/runs/25024926855) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `90b6665deddd` | 2m 32s | 55m 8s | [25024957707](https://github.com/openclaw/openclaw/actions/runs/25024957707) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `90b6665deddd` | 1m 59s | 10m 57s | [25024957933](https://github.com/openclaw/openclaw/actions/runs/25024957933) | 4 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 2m 40s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024926855/job/73293890076) |
| 2m 39s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024926855/job/73293890081) |
| 2m 12s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957933/job/73293975974) |
| 2m 5s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293924841) |
| 2m 2s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293925139) |
| 1m 58s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293924888) |
| 1m 58s | `normal-ci` | checks-node-extensions-shard-1 | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293924956) |
| 1m 56s | `release-checks` | Run QA Lab parity lane (baseline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957933/job/73293975999) |
| 1m 55s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293925115) |
| 1m 48s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293925029) |
| 1m 45s | `normal-ci` | checks-node-auto-reply-reply-commands-state-routing | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293925166) |
| 1m 43s | `normal-ci` | checks-node-core-runtime-infra | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293925105) |
| 1m 39s | `normal-ci` | checks-node-extensions-shard-5 | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293924944) |
| 1m 38s | `normal-ci` | checks-node-core-runtime-media-ui | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293925114) |
| 1m 28s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024957933/job/73293975984) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25024926855
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25024926855/job/73293890076
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25024926855/job/73293890081
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25024926855/job/73294168455
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25024957707
  - checks-fast-contracts-plugins: failure - https://github.com/openclaw/openclaw/actions/runs/25024957707/job/73293924915

## Notes

Automatically requested by Full Release Validation 25024926855 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 3fc8277eb2fec7ab0bccb136927e4d1da89243bb

Generated: 2026-04-28T15:02:13.378Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `3fc8277eb2fec7ab0bccb136927e4d1da89243bb` |
| Release ref input | `3fc8277eb2fec7ab0bccb136927e4d1da89243bb` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `3fc8277eb2fec7ab0bccb136927e4d1da89243bb` |
| Release ref SHA | `3fc8277eb2fec7ab0bccb136927e4d1da89243bb` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 0 | 0 | 2 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.4.27` | `3fc8277eb2fe` | 23m 29s | 46m 6s | [25059393466](https://github.com/openclaw/openclaw/actions/runs/25059393466) | 0 |
| running | blocking | `normal-ci` | CI | `release/2026.4.27` | `3fc8277eb2fe` | 23m 12s | 1h 4m 31s | [25059417698](https://github.com/openclaw/openclaw/actions/runs/25059417698) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.4.27` | `3fc8277eb2fe` | 21m 29s | 53s | [25059416693](https://github.com/openclaw/openclaw/actions/runs/25059416693) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 22m 54s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25059393466/job/73408894803) |
| 22m 53s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25059393466/job/73408894689) |
| 2m 40s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059417698/job/73408989471) |
| 2m 31s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059417698/job/73408989137) |
| 2m 23s | `normal-ci` | checks-node-extensions-shard-2 | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059417698/job/73408989198) |
| 2m 18s | `normal-ci` | checks-node-auto-reply-reply-commands-state-routing | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059417698/job/73408989444) |
| 2m 6s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059417698/job/73408989342) |
| 2m 0s | `normal-ci` | checks-node-core-runtime-infra | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059417698/job/73408989387) |
| 1m 58s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059417698/job/73408989239) |
| 1m 55s | `normal-ci` | checks-node-extensions-shard-4 | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059417698/job/73408989361) |
| 1m 48s | `normal-ci` | checks-node-core-runtime-media-ui | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059417698/job/73408989372) |
| 1m 47s | `normal-ci` | checks-node-extensions-shard-6 | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059417698/job/73408989294) |
| 45s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059416693/job/73408939489) |
| 10s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25059393466/job/73413335540) |
| 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25059393466/job/73408853069) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25059393466
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25059393466/job/73408894689
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25059393466/job/73408894803
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25059393466/job/73413335540

## Notes

Automatically requested by Full Release Validation 25059393466 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


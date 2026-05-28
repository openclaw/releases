# OpenClaw Release Evidence: release-2026.4.29

Generated: 2026-04-30T17:49:29.926Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `release-2026.4.29` |
| Release ref input | `release/2026.4.29` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.4.29` |
| Release ref SHA | `9204476b19f49d7cfd452ba014a22d5314cf410d` |
| Runs at release SHA | none |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `7969f1f07ccc` | 12m 51s | 12m 35s | 12m 46s | [25180074194](https://github.com/openclaw/openclaw/actions/runs/25180074194) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `7969f1f07ccc` | 12m 5s | 24m 56s | 12m 1s | [25180092654](https://github.com/openclaw/openclaw/actions/runs/25180092654) | 4 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 12m 22s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73822696327) |
| 7m 55s | `release-checks` | Run QA Lab parity lane (baseline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822874635) |
| 7m 12s | `release-checks` | Run QA Lab live Matrix lane | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822874621) |
| 7m 10s | `release-checks` | Run QA Lab parity lane (candidate) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822874620) |
| 1m 40s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822874629) |
| 56s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822722443) |
| 8s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73822653379) |
| 5s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73824646310) |
| 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73824602693) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73822696739) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73822696876) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73822697023) |
| 0s | `release-checks` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822875141) |
| 0s | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822875274) |
| 0s | `release-checks` | Run repo/live E2E validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822875342) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 12m 46s | 5s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73824646310) |
| 12m 1s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73824602693) |
| 11m 59s | 0s | `release-checks` | Run QA Lab parity report | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73824603016) |
| 4m 3s | 7m 10s | `release-checks` | Run QA Lab parity lane (candidate) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822874620) |
| 4m 3s | 7m 12s | `release-checks` | Run QA Lab live Matrix lane | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822874621) |
| 4m 3s | 1m 40s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822874629) |
| 4m 3s | 7m 55s | `release-checks` | Run QA Lab parity lane (baseline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822874635) |
| 1m 1s | 0s | `release-checks` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822875141) |
| 1m 1s | 0s | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822875274) |
| 1m 1s | 0s | `release-checks` | Run repo/live E2E validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822875342) |
| 1m 1s | 0s | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822875346) |
| 22s | 12m 22s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73822696327) |
| 19s | 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73822696739) |
| 19s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73822696876) |
| 19s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73822697023) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25180074194
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25180074194/job/73824646310
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25180092654
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822874620
  - Run QA Lab live Matrix lane: failure - https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73822874621
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25180092654/job/73824602693

## Notes

Automatically requested by Full Release Validation 25180074194 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


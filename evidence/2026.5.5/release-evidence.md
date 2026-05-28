# OpenClaw Release Evidence: 2026.5.5

Generated: 2026-05-06T10:08:54.097Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.5` |
| Release ref input | `v2026.5.5` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.5` |
| Release ref SHA | `b1abf9d8ae4410c6a6e08f7dfd2d617f4550281c` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.5` | `7615b425c530` | 42m 28s (+19m 18s) | 30m 7s (+7m 19s) | 42m 19s | [25427163061](https://github.com/openclaw/openclaw/actions/runs/25427163061) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.5` | `7615b425c530` | 29m 35s (+7m 36s) | 2h 21m 6s (+2h 1m 35s) | 29m 30s | [25427720390](https://github.com/openclaw/openclaw/actions/runs/25427720390) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 29m 50s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74585463056) |
| 20m 21s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548240) |
| 16m 30s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548203) |
| 15m 34s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548192) |
| 15m 20s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548207) |
| 14m 37s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548204) |
| 14m 32s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548217) |
| 14m 23s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548239) |
| 14m 5s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548194) |
| 13m 22s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548221) |
| 1m 3s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74585512185) |
| 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74585418902) |
| 8s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74590136130) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74585463540) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 42m 19s | 8s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74590136130) |
| 29m 30s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74590080735) |
| 12m 20s | 29m 50s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74585463056) |
| 12m 11s |  | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74585463660) |
| 12m 11s |  | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74585463718) |
| 12m 11s |  | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74585463722) |
| 12m 10s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74585463540) |
| 12m 1s | 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74585418902) |
| 9m 2s | 14m 5s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548194) |
| 9m 2s | 15m 20s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548207) |
| 9m 1s | 16m 30s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548203) |
| 9m 1s | 14m 37s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548204) |
| 9m 1s | 14m 32s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548217) |
| 9m 1s | 13m 22s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548221) |
| 9m 1s | 14m 23s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548239) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 23m 10s | 42m 28s | +19m 18s | +7m 19s |
| `release-checks` | 21m 59s | 29m 35s | +7m 36s | +2h 1m 35s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25427163061
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25427163061/job/74590136130
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25427720390
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74586548207
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25427720390/job/74590080735

## Notes

Automatically requested by Full Release Validation 25427163061 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


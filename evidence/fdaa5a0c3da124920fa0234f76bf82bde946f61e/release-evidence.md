# OpenClaw Release Evidence: fdaa5a0c3da124920fa0234f76bf82bde946f61e

Generated: 2026-05-04T21:57:14.445Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `fdaa5a0c3da124920fa0234f76bf82bde946f61e` |
| Release ref input | `fdaa5a0c3da124920fa0234f76bf82bde946f61e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `fdaa5a0c3da124920fa0234f76bf82bde946f61e` |
| Release ref SHA | `fdaa5a0c3da124920fa0234f76bf82bde946f61e` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release-ci/fdaa5a0c3da1-1777928789783` | `fdaa5a0c3da1` | 50m 25s | 50m 14s | 50m 18s | [25343558579](https://github.com/openclaw/openclaw/actions/runs/25343558579) | 0 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/fdaa5a0c3da1-1777928789783` | `fdaa5a0c3da1` | 49m 25s | 1h 9m 8s | 49m 21s | [25343576603](https://github.com/openclaw/openclaw/actions/runs/25343576603) | 6 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 49m 56s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74306804592) |
| 42m 17s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307496254) |
| 11m 29s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307496274) |
| 11m 21s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307496269) |
| 2m 20s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307011400) |
| 1m 7s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74306832388) |
| 31s | `release-checks` | cross_os_release_checks / prepare | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307389565) |
| 12s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74306765405) |
| 6s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74314011742) |
| 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74313927719) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74306804891) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74306804898) |
| 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74306805062) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74306805151) |
| 0s | `release-checks` | Run QA Lab live Matrix lane | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307011680) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 50m 18s | 6s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74314011742) |
| 49m 21s | 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74313927719) |
| 6m 56s | 42m 17s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307496254) |
| 6m 22s | 11m 21s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307496269) |
| 4m 39s | 11m 29s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307496274) |
| 3m 49s | 31s | `release-checks` | cross_os_release_checks / prepare | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307389565) |
| 3m 41s |  | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307389514) |
| 3m 41s |  | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307389587) |
| 1m 20s | 2m 20s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307011400) |
| 1m 12s | 0s | `release-checks` | Run QA Lab live Matrix lane | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307011680) |
| 1m 12s | 0s | `release-checks` | install_smoke_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343576603/job/74307011692) |
| 20s | 49m 56s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74306804592) |
| 17s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74306804891) |
| 17s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74306804898) |
| 17s | 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25343558579/job/74306805062) |

## Notes

Automatically requested by Full Release Validation 25343558579 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


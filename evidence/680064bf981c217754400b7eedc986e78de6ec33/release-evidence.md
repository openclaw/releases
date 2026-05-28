# OpenClaw Release Evidence: 680064bf981c217754400b7eedc986e78de6ec33

Generated: 2026-05-06T12:10:03.576Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `680064bf981c217754400b7eedc986e78de6ec33` |
| Release ref input | `680064bf981c217754400b7eedc986e78de6ec33` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `680064bf981c217754400b7eedc986e78de6ec33` |
| Release ref SHA | `680064bf981c217754400b7eedc986e78de6ec33` |
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
| pass | advisory | `full-release-validation` | Full Release Validation | `release-ci/680064bf981c-1778067135699` | `680064bf981c` | 37m 35s (+30m 34s) | 37m 25s (+30m 52s) | 37m 28s | [25432697266](https://github.com/openclaw/openclaw/actions/runs/25432697266) | 0 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/680064bf981c-1778067135699` | `680064bf981c` | 36m 53s (+31m 14s) | 40m 58s (+34m 43s) | 36m 50s | [25432714412](https://github.com/openclaw/openclaw/actions/runs/25432714412) | 6 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 37m 8s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74602723356) |
| 32m 13s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74603397942) |
| 3m 8s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74603398054) |
| 2m 21s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74602948067) |
| 1m 40s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74603397962) |
| 1m 11s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74602750864) |
| 23s | `release-checks` | cross_os_release_checks / prepare | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74603319194) |
| 11s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74602688527) |
| 6s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74608346920) |
| 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74608290652) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74602723818) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74602723893) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74602723958) |
| 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74602723995) |
| 0s | `release-checks` | Run QA Lab parity report | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74602948894) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 37m 28s | 6s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74608346920) |
| 36m 50s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74608290652) |
| 4m 27s | 32m 13s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74603397942) |
| 4m 27s | 1m 40s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74603397962) |
| 4m 27s | 3m 8s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74603398054) |
| 4m 1s | 23s | `release-checks` | cross_os_release_checks / prepare | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74603319194) |
| 3m 52s | 0s | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74603319411) |
| 3m 52s | 0s | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74603319541) |
| 1m 31s | 2m 21s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74602948067) |
| 1m 23s |  | `release-checks` | Run QA Lab live Telegram lane | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74602948329) |
| 1m 23s |  | `release-checks` | install_smoke_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432714412/job/74602948587) |
| 17s | 37m 8s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74602723356) |
| 16s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74602723818) |
| 16s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74602723893) |
| 16s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25432697266/job/74602723958) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 5m 39s | 36m 53s | +31m 14s | +34m 43s |
| `full-release-validation` | 7m 1s | 37m 35s | +30m 34s | +30m 52s |

## Notes

Automatically requested by Full Release Validation 25432697266 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


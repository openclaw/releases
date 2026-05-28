# OpenClaw Release Evidence: 15901513a3e29e54bd0be58158db2af4051646ca

Generated: 2026-04-29T21:15:51.834Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `15901513a3e29e54bd0be58158db2af4051646ca` |
| Release ref input | `15901513a3e29e54bd0be58158db2af4051646ca` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `15901513a3e29e54bd0be58158db2af4051646ca` |
| Release ref SHA | `15901513a3e29e54bd0be58158db2af4051646ca` |
| Runs at release SHA | none |
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
| pass | advisory | `full-release-validation` | Full Release Validation | `main` | `9ccd0158984f` | 18m 36s (+7m 48s) | 17m 17s (+6m 46s) | 18m 27s | [25133464604](https://github.com/openclaw/openclaw/actions/runs/25133464604) | 0 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `main` | `585c2bdba389` | 16m 40s (+7m 1s) | 20m 1s (+14m 40s) | 16m 37s | [25133531609](https://github.com/openclaw/openclaw/actions/runs/25133531609) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 16m 57s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73665763492) |
| 14m 25s | `release-checks` | install_smoke_release_checks / install-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666124845) |
| 4m 31s | `release-checks` | install_smoke_release_checks / docker-e2e-fast | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666124893) |
| 53s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73665939963) |
| 12s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73665709162) |
| 9s | `release-checks` | install_smoke_release_checks / preflight | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666091859) |
| 8s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73668438371) |
| 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73668396146) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73665763970) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73665763979) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73665764047) |
| 0s | `release-checks` | Run repo/live E2E validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666091973) |
| 0s | `release-checks` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666091985) |
| 0s | `release-checks` | Run QA Lab live Telegram lane | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666092077) |
| 0s | `release-checks` | Run QA Lab parity report | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666092202) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 18m 27s | 8s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73668438371) |
| 16m 37s | 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73668396146) |
| 2m 10s | 14m 25s | `release-checks` | install_smoke_release_checks / install-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666124845) |
| 2m 10s | 4m 31s | `release-checks` | install_smoke_release_checks / docker-e2e-fast | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666124893) |
| 2m 9s |  | `release-checks` | install_smoke_release_checks / install-smoke-fast | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666125099) |
| 1m 59s | 9s | `release-checks` | install_smoke_release_checks / preflight | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666091859) |
| 1m 57s |  | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666092267) |
| 1m 57s |  | `release-checks` | Run QA Lab live Matrix lane | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666092342) |
| 1m 57s |  | `release-checks` | Run QA Lab parity lane (${{ matrix.lane }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666092433) |
| 1m 57s |  | `release-checks` | cross_os_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666092705) |
| 1m 56s | 0s | `release-checks` | Run repo/live E2E validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133531609/job/73666091973) |
| 1m 21s | 16m 57s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73665763492) |
| 1m 19s | 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73665763970) |
| 1m 19s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73665763979) |
| 1m 19s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25133464604/job/73665764047) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 10m 48s | 18m 36s | +7m 48s | +6m 46s |
| `release-checks` | 9m 39s | 16m 40s | +7m 1s | +14m 40s |

## Notes

Automatically requested by Full Release Validation 25133464604 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


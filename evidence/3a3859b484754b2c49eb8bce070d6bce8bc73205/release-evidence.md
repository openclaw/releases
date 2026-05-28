# OpenClaw Release Evidence: 3a3859b484754b2c49eb8bce070d6bce8bc73205

Generated: 2026-04-28T18:21:35.574Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `3a3859b484754b2c49eb8bce070d6bce8bc73205` |
| Release ref input | `3a3859b484754b2c49eb8bce070d6bce8bc73205` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `3a3859b484754b2c49eb8bce070d6bce8bc73205` |
| Release ref SHA | `3a3859b484754b2c49eb8bce070d6bce8bc73205` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.4.27` | `3a3859b48475` | 9m 50s | 9m 39s | [25069851059](https://github.com/openclaw/openclaw/actions/runs/25069851059) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.4.27` | `3a3859b48475` | 8m 41s | 8m 33s | [25069869120](https://github.com/openclaw/openclaw/actions/runs/25069869120) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 9m 22s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25069851059/job/73446907654) |
| 8m 31s | `release-checks` | resolve_target | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73446942853) |
| 10s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25069851059/job/73446874944) |
| 7s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25069851059/job/73448384717) |
| 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448280191) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25069851059/job/73446907893) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25069851059/job/73446908230) |
| 0s | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448280133) |
| 0s | `release-checks` | cross_os_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448280167) |
| 0s | `release-checks` | Run QA Lab parity report | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448280384) |
| 0s | `release-checks` | live_and_e2e_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448280488) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25069851059
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25069851059/job/73446907654
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25069851059/job/73448384717
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25069869120
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73446942853
  - Run QA Lab parity lane (${{ matrix.lane }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448279925
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448279927
  - Prepare release package artifact: cancelled - https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448280113
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448280191
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448280216
  - Run QA Lab parity report: cancelled - https://github.com/openclaw/openclaw/actions/runs/25069869120/job/73448280384

## Notes

Automatically requested by Full Release Validation 25069851059 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


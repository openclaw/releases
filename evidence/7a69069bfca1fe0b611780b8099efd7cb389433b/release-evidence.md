# OpenClaw Release Evidence: 7a69069bfca1fe0b611780b8099efd7cb389433b

Generated: 2026-04-29T12:39:49.166Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `7a69069bfca1fe0b611780b8099efd7cb389433b` |
| Release ref input | `7a69069bfca1fe0b611780b8099efd7cb389433b` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `7a69069bfca1fe0b611780b8099efd7cb389433b` |
| Release ref SHA | `7a69069bfca1fe0b611780b8099efd7cb389433b` |
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

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `8f2dd02d2df6` | 1m 4s (-1m 18s) | 55s (-1m 8s) | [25109275508](https://github.com/openclaw/openclaw/actions/runs/25109275508) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `8f2dd02d2df6` | 55s (-39s) | 41s (-4m 23s) | [25109292636](https://github.com/openclaw/openclaw/actions/runs/25109292636) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 41s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25109275508/job/73578631096) |
| 38s | `release-checks` | resolve_target | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578664765) |
| 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25109275508/job/73578600900) |
| 5s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25109275508/job/73578749206) |
| 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776395) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25109275508/job/73578631514) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25109275508/job/73578631559) |
| 0s | `release-checks` | install_smoke_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776054) |
| 0s | `release-checks` | Run QA Lab parity lane (${{ matrix.lane }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776087) |
| 0s | `release-checks` | Run QA Lab live Telegram lane | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776144) |
| 0s | `release-checks` | Run repo/live E2E validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776345) |
| 0s | `release-checks` | Run QA Lab parity report | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776492) |
| 0s | `release-checks` | Prepare release package artifact | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776540) |
| 0s | `release-checks` | Run QA Lab live Matrix lane | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776563) |
| 0s | `release-checks` | cross_os_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776706) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 2m 22s | 1m 4s | -1m 18s | -1m 8s |
| `release-checks` | 1m 34s | 55s | -39s | -4m 23s |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25109275508
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25109275508/job/73578631096
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25109275508/job/73578749206
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25109292636
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578664765
  - Run QA Lab parity lane (${{ matrix.lane }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776087
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776144
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776395
  - Run QA Lab parity report: cancelled - https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776492
  - Prepare release package artifact: cancelled - https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776540
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25109292636/job/73578776563

## Notes

Automatically requested by Full Release Validation 25109275508 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: e0d48a89133a6ac8516ca4a249c0a45207e75f80

Generated: 2026-05-10T08:52:38.621Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `e0d48a89133a6ac8516ca4a249c0a45207e75f80` |
| Release ref input | `e0d48a89133a6ac8516ca4a249c0a45207e75f80` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `e0d48a89133a6ac8516ca4a249c0a45207e75f80` |
| Release ref SHA | `e0d48a89133a6ac8516ca4a249c0a45207e75f80` |
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

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/e0d48a89133a-1778400110` | `e0d48a89133a` | 50m 9s | 50m 0s | 49m 55s | [25623545377](https://github.com/openclaw/openclaw/actions/runs/25623545377) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/e0d48a89133a-1778400110` | `e0d48a89133a` | 49m 1s | 7h 56m 46s | 48m 57s | [25623552268](https://github.com/openclaw/openclaw/actions/runs/25623552268) | 48 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 49m 38s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75214432867) |
| 42m 58s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214709980) |
| 30m 22s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214839033) |
| 24m 13s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214569407) |
| 13m 34s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214709981) |
| 12m 7s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214709987) |
| 11m 49s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214709978) |
| 11m 35s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214709977) |
| 11m 33s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214709976) |
| 11m 19s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214709982) |
| 11m 3s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214709967) |
| 13s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75217035423) |
| 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75214423265) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75214432963) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75214433019) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 49m 55s | 13s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75217035423) |
| 48m 57s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75216999603) |
| 18m 13s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75215383821) |
| 8m 4s | 2m 4s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214839020) |
| 8m 4s | 1m 17s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214839021) |
| 8m 4s | 1m 56s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214839034) |
| 8m 4s | 2m 3s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214839047) |
| 8m 3s | 8m 22s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214837908) |
| 8m 3s | 1m 47s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214839012) |
| 8m 3s | 1m 7s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214839015) |
| 8m 3s | 1m 32s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214839018) |
| 15s | 49m 38s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75214432867) |
| 13s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75214432963) |
| 13s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75214433019) |
| 13s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75214433147) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25623545377
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25623545377/job/75217035423
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25623552268
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75214839033
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25623552268/job/75216999603

## Notes

Automatically requested by Full Release Validation 25623545377 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


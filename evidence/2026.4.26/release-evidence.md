# OpenClaw Release Evidence: 2026.4.26

Generated: 2026-04-28T06:41:13.847Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.4.26` |
| Release ref input | `be8c24633aaa7ef0425ae1178f096ee8dd6226c0` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `be8c24633aaa7ef0425ae1178f096ee8dd6226c0` |
| Release ref SHA | `be8c24633aaa7ef0425ae1178f096ee8dd6226c0` |
| Runs at release SHA | none |
| Package spec | `openclaw@2026.4.26` |
| npm status | published |
| npm resolved version | `2026.4.26` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta`, `latest` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-04-28T01:32:04.075Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.4.26.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `main` | `577a540880a7` | 14m 29s | 14m 18s | [25037501099](https://github.com/openclaw/openclaw/actions/runs/25037501099) | 0 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `main` | `cb8b3274884e` | 13m 12s | 53m 56s | [25037535150](https://github.com/openclaw/openclaw/actions/runs/25037535150) | 11 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 13m 25s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037501099/job/73332581728) |
| 8m 38s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037535150/job/73333046910) |
| 7m 1s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037535150/job/73333046898) |
| 5m 37s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037535150/job/73333046892) |
| 5m 37s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037535150/job/73333046932) |
| 5m 34s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037535150/job/73333046906) |
| 4m 49s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037535150/job/73333046915) |
| 4m 44s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037535150/job/73333046889) |
| 4m 31s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037535150/job/73333046917) |
| 4m 15s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037535150/job/73333046926) |
| 2m 31s | `release-checks` | cross_os_release_checks / prepare | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037535150/job/73332763265) |
| 47s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037501099/job/73332491612) |
| 6s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25037501099/job/73334050142) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25037501099/job/73332582071) |

## Notes

Automatically requested by Full Release Validation 25037501099 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


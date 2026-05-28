# OpenClaw Release Evidence: f5e875f4f3d454f927ebc8796edeb815107f02aa

Generated: 2026-05-03T23:41:10.345Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `f5e875f4f3d454f927ebc8796edeb815107f02aa` |
| Release ref input | `f5e875f4f3d454f927ebc8796edeb815107f02aa` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `f5e875f4f3d454f927ebc8796edeb815107f02aa` |
| Release ref SHA | `f5e875f4f3d454f927ebc8796edeb815107f02aa` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 0 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/f5e875f4f3d4-1777850957732` | `f5e875f4f3d4` | 11m 25s | 33m 6s | 10m 55s | [25293941212](https://github.com/openclaw/openclaw/actions/runs/25293941212) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/f5e875f4f3d4-1777850957732` | `f5e875f4f3d4` | 10m 46s | 1h 10m 46s | 8m 44s | [25293948310](https://github.com/openclaw/openclaw/actions/runs/25293948310) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/f5e875f4f3d4-1777850957732` | `f5e875f4f3d4` | 6m 21s | 1h 40m 34s | 6m 21s | [25293946917](https://github.com/openclaw/openclaw/actions/runs/25293946917) | 27 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/f5e875f4f3d4-1777850957732` | `f5e875f4f3d4` | 1m 34s | 1m 31s | 3s | [25293998811](https://github.com/openclaw/openclaw/actions/runs/25293998811) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 10m 40s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25293941212/job/74149736616) |
| 10m 33s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25293941212/job/74149736595) |
| 7m 18s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293941212/job/74149736598) |
| 4m 30s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74149924946) |
| 4m 15s | `release-checks` | Run repo/live E2E validation / Live media suites (Native live media video plugins C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74149852794) |
| 4m 2s | `release-checks` | Run QA Lab live Slack lane | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74149800769) |
| 3m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74149852920) |
| 3m 38s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293948310/job/74149754895) |
| 3m 6s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74149962088) |
| 2m 49s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293948310/job/74149754880) |
| 2m 46s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74149962097) |
| 2m 34s | `release-checks` | Run repo/live E2E validation / Live media suites (Native live media video plugins B) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74149852789) |
| 2m 33s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150049331) |
| 2m 28s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74149800770) |
| 2m 18s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74149852932) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 10m 55s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293941212/job/74150260713) |
| 8m 44s | 2m 1s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293948310/job/74149754859) |
| 6m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150063450) |
| 6m 21s | 1m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150063454) |
| 6m 21s | 1m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150063455) |
| 6m 21s | 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150063457) |
| 6m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150063458) |
| 6m 21s | 1m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150063460) |
| 6m 19s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150063507) |
| 6m 19s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150063590) |
| 6m 3s | 1m 39s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150049319) |
| 6m 3s | 1m 39s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293946917/job/74150049321) |
| 3m 54s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293948310/job/74149949408) |
| 2m 34s | 1m 45s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293941212/job/74149858993) |
| 2m 30s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293948310/job/74149875998) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25293941212
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25293941212/job/74149736595
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25293941212/job/74149736616
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25293941212/job/74150260713

## Notes

Automatically requested by Full Release Validation 25293941212 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


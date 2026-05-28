# OpenClaw Release Evidence: 430654bc94176e709c8cca14625e483eefef4edf

Generated: 2026-05-09T23:52:50.564Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `430654bc94176e709c8cca14625e483eefef4edf` |
| Release ref input | `430654bc94176e709c8cca14625e483eefef4edf` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `430654bc94176e709c8cca14625e483eefef4edf` |
| Release ref SHA | `430654bc94176e709c8cca14625e483eefef4edf` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/430654bc9417-1778369042604` | `430654bc9417` | 28m 1s | 54m 26s | 27m 18s | [25614417427](https://github.com/openclaw/openclaw/actions/runs/25614417427) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/430654bc9417-1778369042604` | `430654bc9417` | 1m 8s | 1h 20m 7s | 11m 28s | [25614422142](https://github.com/openclaw/openclaw/actions/runs/25614422142) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/430654bc9417-1778369042604` | `430654bc9417` | 27m 13s | 7h 11m 57s | 27m 10s | [25614422195](https://github.com/openclaw/openclaw/actions/runs/25614422195) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/430654bc9417-1778369042604` | `430654bc9417` | 3m 4s | 2m 48s | 15s | [25614467669](https://github.com/openclaw/openclaw/actions/runs/25614467669) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 27m 2s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614417427/job/75189874288) |
| 24m 28s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75189985461) |
| 21m 51s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190075192) |
| 20m 4s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190178218) |
| 20m 4s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190178238) |
| 14m 35s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190075207) |
| 12m 44s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190075182) |
| 12m 15s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614417427/job/75189874308) |
| 11m 47s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190075178) |
| 11m 42s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190075173) |
| 11m 32s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190075180) |
| 11m 27s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190075190) |
| 8m 22s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614417427/job/75189874282) |
| 7m 53s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422142/job/75190378596) |
| 4m 15s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422142/job/75190378576) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 18s | 41s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614417427/job/75191041375) |
| 27m 10s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75191045583) |
| 15m 3s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190522501) |
| 11m 28s | 1m 4s | `normal-ci` | checks-windows-node-test | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422142/job/75190378432) |
| 7m 58s | 4m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190218362) |
| 7m 54s | 4m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190218328) |
| 7m 54s | 4m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190218330) |
| 7m 54s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190218341) |
| 7m 54s | 4m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190218343) |
| 7m 54s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190218344) |
| 7m 54s | 7m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190218360) |
| 7m 53s | 1m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190218318) |
| 2m 54s | 3m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614417427/job/75189988236) |
| 2m 47s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422142/job/75190379308) |
| 2m 30s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614422142/job/75190378965) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614417427
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614417427/job/75189874288
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25614417427/job/75191041375
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614422195
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75189985461
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: failure - https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75189985554
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75189985593
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190056845
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190075192
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190178201
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190178218
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75190178238
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25614422195/job/75191045583

## Notes

Automatically requested by Full Release Validation 25614417427 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


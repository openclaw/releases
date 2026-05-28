# OpenClaw Release Evidence: b8c6b2f7edeadd9f1b4ac258235a0244ba127fac

Generated: 2026-05-10T02:54:38.284Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `b8c6b2f7edeadd9f1b4ac258235a0244ba127fac` |
| Release ref input | `b8c6b2f7edeadd9f1b4ac258235a0244ba127fac` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `b8c6b2f7edeadd9f1b4ac258235a0244ba127fac` |
| Release ref SHA | `b8c6b2f7edeadd9f1b4ac258235a0244ba127fac` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/b8c6b2f7edea-1778378659999` | `b8c6b2f7edea` | 49m 50s | 1h 8m 20s | 49m 20s | [25617206837](https://github.com/openclaw/openclaw/actions/runs/25617206837) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/b8c6b2f7edea-1778378659999` | `b8c6b2f7edea` | 2m 44s | 1h 14m 3s | 2m 35s | [25617212702](https://github.com/openclaw/openclaw/actions/runs/25617212702) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/b8c6b2f7edea-1778378659999` | `b8c6b2f7edea` | 48m 35s | 7h 39m 45s | 48m 31s | [25617213255](https://github.com/openclaw/openclaw/actions/runs/25617213255) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/b8c6b2f7edea-1778378659999` | `b8c6b2f7edea` | 2m 48s | 2m 45s | 3s | [25617284827](https://github.com/openclaw/openclaw/actions/runs/25617284827) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 49m 1s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617206837/job/75197337009) |
| 42m 57s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197591750) |
| 26m 44s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197705669) |
| 26m 10s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197465804) |
| 13m 43s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197591746) |
| 13m 35s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197591762) |
| 12m 11s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197591749) |
| 11m 43s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197591765) |
| 11m 41s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197591754) |
| 11m 23s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197591753) |
| 11m 7s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197591766) |
| 8m 49s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617206837/job/75197337008) |
| 3m 25s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617206837/job/75197337019) |
| 3m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617206837/job/75197514567) |
| 3m 8s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617206837/job/75197337011) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 49m 20s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25617206837/job/75199617690) |
| 48m 31s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75199598126) |
| 16m 0s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75198115099) |
| 7m 43s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197714799) |
| 7m 43s | 8m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197714849) |
| 7m 43s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197714862) |
| 7m 42s | 1m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197714802) |
| 7m 42s | 4m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197714809) |
| 7m 42s | 4m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197714814) |
| 7m 42s | 1m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197714819) |
| 7m 42s | 4m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197714824) |
| 3m 48s | 3m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617206837/job/75197514567) |
| 2m 35s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617212702/job/75197468959) |
| 2m 24s | 3s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617212702/job/75197460327) |
| 2m 13s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25617212702/job/75197451609) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25617206837
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25617206837/job/75199617690
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25617213255
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75197705669
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25617213255/job/75199598126

## Notes

Automatically requested by Full Release Validation 25617206837 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


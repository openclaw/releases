# OpenClaw Release Evidence: d608af95e99d1173d3e73d5d3ae4239932419f8b

Generated: 2026-05-09T20:01:10.996Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `d608af95e99d1173d3e73d5d3ae4239932419f8b` |
| Release ref input | `d608af95e99d1173d3e73d5d3ae4239932419f8b` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `d608af95e99d1173d3e73d5d3ae4239932419f8b` |
| Release ref SHA | `d608af95e99d1173d3e73d5d3ae4239932419f8b` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/d608af95e99d-1778354835279` | `d608af95e99d` | 33m 26s | 1h 30m 13s | 32m 57s | [25609801951](https://github.com/openclaw/openclaw/actions/runs/25609801951) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/d608af95e99d-1778354835279` | `d608af95e99d` | 32m 18s | 1h 45m 17s | 2m 46s | [25609808577](https://github.com/openclaw/openclaw/actions/runs/25609808577) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/d608af95e99d-1778354835279` | `d608af95e99d` | 32m 38s | 8h 27m 44s | 32m 33s | [25609811106](https://github.com/openclaw/openclaw/actions/runs/25609811106) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/d608af95e99d-1778354835279` | `d608af95e99d` | 3m 22s | 3m 5s | 17s | [25609859325](https://github.com/openclaw/openclaw/actions/runs/25609859325) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 32m 39s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609801951/job/75177945297) |
| 32m 33s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609801951/job/75177945295) |
| 32m 2s | `normal-ci` | macos-swift | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609808577/job/75177964620) |
| 28m 3s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178200402) |
| 25m 25s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178327465) |
| 24m 31s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178081882) |
| 18m 1s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609801951/job/75177945294) |
| 16m 28s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178327458) |
| 15m 35s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178200393) |
| 13m 54s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178200400) |
| 11m 43s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178200405) |
| 11m 42s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178200395) |
| 11m 34s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178164774) |
| 11m 33s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178200416) |
| 3m 51s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609801951/job/75178082087) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 32m 57s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609801951/job/75179662263) |
| 32m 33s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75179666444) |
| 14m 23s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178714128) |
| 14m 13s | 11m 17s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178200408) |
| 13m 18s | 11m 43s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178200405) |
| 7m 6s | 1m 19s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178327541) |
| 7m 5s | 1m 4s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178326720) |
| 7m 5s | 1m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178326721) |
| 7m 5s | 2m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178326726) |
| 7m 5s | 4m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178326729) |
| 7m 5s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178326732) |
| 2m 48s | 3m 51s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609801951/job/75178082087) |
| 2m 46s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609808577/job/75178104200) |
| 2m 36s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609808577/job/75178090889) |
| 2m 14s | 2m 14s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609808577/job/75177964637) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609801951
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609801951/job/75177945295
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609801951/job/75177945297
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25609801951/job/75179662263
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609808577
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609808577/job/75177964620
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609811106
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178200402
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178327458
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75178327465
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25609811106/job/75179666444

## Notes

Automatically requested by Full Release Validation 25609801951 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


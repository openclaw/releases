# OpenClaw Release Evidence: 6ed94b914204c006eae2932a48b07b45d87e6ba9

Generated: 2026-05-09T17:35:40.020Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `6ed94b914204c006eae2932a48b07b45d87e6ba9` |
| Release ref input | `6ed94b914204c006eae2932a48b07b45d87e6ba9` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `6ed94b914204c006eae2932a48b07b45d87e6ba9` |
| Release ref SHA | `6ed94b914204c006eae2932a48b07b45d87e6ba9` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/6ed94b914204-1778347045059` | `6ed94b914204` | 17m 47s | 45m 3s | 17m 17s | [25607026690](https://github.com/openclaw/openclaw/actions/runs/25607026690) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/6ed94b914204-1778347045059` | `6ed94b914204` | 11m 24s | 1h 25m 13s | 2m 43s | [25607034298](https://github.com/openclaw/openclaw/actions/runs/25607034298) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/6ed94b914204-1778347045059` | `6ed94b914204` | 16m 33s | 5h 52m 4s | 16m 29s | [25607034817](https://github.com/openclaw/openclaw/actions/runs/25607034817) | 46 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/6ed94b914204-1778347045059` | `6ed94b914204` | 3m 15s | 3m 1s | 13s | [25607100101](https://github.com/openclaw/openclaw/actions/runs/25607100101) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 16m 59s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607026690/job/75170603806) |
| 13m 50s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170759222) |
| 11m 59s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607026690/job/75170603811) |
| 11m 42s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892093) |
| 11m 34s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892104) |
| 11m 34s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892116) |
| 11m 8s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892096) |
| 11m 6s | `release-checks` | cross_os_release_checks / Windows / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892123) |
| 11m 0s | `normal-ci` | macos-node | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607034298/job/75170626057) |
| 10m 54s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892094) |
| 10m 26s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892092) |
| 9m 4s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040975) |
| 9m 1s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171041034) |
| 8m 46s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607026690/job/75170603833) |
| 3m 55s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607034298/job/75170625977) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 17m 17s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607026690/job/75171592620) |
| 16m 29s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171561460) |
| 15m 19s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171502545) |
| 15m 13s | 1m 1s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892108) |
| 15m 12s | 1m 6s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892117) |
| 7m 17s | 4m 15s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040986) |
| 7m 17s | 1m 44s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040991) |
| 7m 17s | 1m 38s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171041000) |
| 7m 17s | 9m 1s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171041034) |
| 7m 16s | 1m 47s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040977) |
| 7m 16s | 1m 20s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040995) |
| 3m 7s | 3m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607026690/job/75170776372) |
| 2m 43s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607034298/job/75170771939) |
| 2m 19s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607034298/job/75170746385) |
| 2m 19s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607034298/job/75170746386) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607026690
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607026690/job/75170603806
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25607026690/job/75171592620
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25607034298
  - macos-node: failure - https://github.com/openclaw/openclaw/actions/runs/25607034298/job/75170626057
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170759222
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892092
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892093
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892094
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892104
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892108
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892116
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892117
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75170892123
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): failure - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040359
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): failure - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040360
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): failure - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040375
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): failure - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040379
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): failure - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040391
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): failure - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040392
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): failure - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040407
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171040975
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171041034
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171502545
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25607034817/job/75171561460

## Notes

Automatically requested by Full Release Validation 25607026690 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


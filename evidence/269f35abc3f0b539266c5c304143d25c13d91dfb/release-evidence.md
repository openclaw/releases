# OpenClaw Release Evidence: 269f35abc3f0b539266c5c304143d25c13d91dfb

Generated: 2026-05-09T17:05:01.705Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `269f35abc3f0b539266c5c304143d25c13d91dfb` |
| Release ref input | `269f35abc3f0b539266c5c304143d25c13d91dfb` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `269f35abc3f0b539266c5c304143d25c13d91dfb` |
| Release ref SHA | `269f35abc3f0b539266c5c304143d25c13d91dfb` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/269f35abc3f0-1778345167137` | `269f35abc3f0` | 18m 31s | 43m 58s | 17m 49s | [25606371422](https://github.com/openclaw/openclaw/actions/runs/25606371422) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/269f35abc3f0-1778345167137` | `269f35abc3f0` | 3m 40s | 1h 18m 40s | 12m 11s | [25606380140](https://github.com/openclaw/openclaw/actions/runs/25606380140) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/269f35abc3f0-1778345167137` | `269f35abc3f0` | 17m 36s | 6h 8m 47s | 17m 33s | [25606380008](https://github.com/openclaw/openclaw/actions/runs/25606380008) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/269f35abc3f0-1778345167137` | `269f35abc3f0` | 3m 15s | 2m 58s | 17s | [25606435869](https://github.com/openclaw/openclaw/actions/runs/25606435869) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 17m 26s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606371422/job/75168888938) |
| 14m 58s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169031856) |
| 13m 12s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134049) |
| 12m 50s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134054) |
| 12m 37s | `release-checks` | cross_os_release_checks / Windows / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134057) |
| 11m 49s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134066) |
| 11m 42s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134060) |
| 11m 27s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134062) |
| 11m 14s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134075) |
| 11m 6s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134052) |
| 11m 4s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134073) |
| 10m 49s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606371422/job/75168888933) |
| 8m 17s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606371422/job/75168888931) |
| 3m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606371422/job/75169041030) |
| 3m 23s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380140/job/75169550884) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 17m 49s | 41s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606371422/job/75169856976) |
| 17m 33s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169860550) |
| 14m 39s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169704564) |
| 12m 11s | 3m 23s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380140/job/75169550884) |
| 7m 22s | 1m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284965) |
| 7m 20s | 4m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284913) |
| 7m 20s | 4m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284921) |
| 7m 20s | 3m 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284926) |
| 7m 20s | 4m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284929) |
| 7m 20s | 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284930) |
| 7m 20s | 7m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284934) |
| 7m 19s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284901) |
| 3m 3s | 3m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606371422/job/75169041030) |
| 2m 48s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380140/job/75169552201) |
| 2m 39s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606380140/job/75169551575) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606371422
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606371422/job/75168888938
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25606371422/job/75169856976
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606380008
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169031856
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134049
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134054
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169134057
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169265620
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169265621
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284911
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284913
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284919
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284921
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284926
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284929
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169284934
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169704564
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25606380008/job/75169860550

## Notes

Automatically requested by Full Release Validation 25606371422 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


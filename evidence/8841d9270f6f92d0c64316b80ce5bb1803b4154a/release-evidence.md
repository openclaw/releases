# OpenClaw Release Evidence: 8841d9270f6f92d0c64316b80ce5bb1803b4154a

Generated: 2026-05-10T07:36:37.826Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `8841d9270f6f92d0c64316b80ce5bb1803b4154a` |
| Release ref input | `8841d9270f6f92d0c64316b80ce5bb1803b4154a` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `8841d9270f6f92d0c64316b80ce5bb1803b4154a` |
| Release ref SHA | `8841d9270f6f92d0c64316b80ce5bb1803b4154a` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/8841d9270f6f-1778395577` | `8841d9270f6f` | 50m 1s | 1h 9m 21s | 49m 30s | [25622149366](https://github.com/openclaw/openclaw/actions/runs/25622149366) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/8841d9270f6f-1778395577` | `8841d9270f6f` | 3m 32s | 1h 13m 18s | 2m 41s | [25622155543](https://github.com/openclaw/openclaw/actions/runs/25622155543) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/8841d9270f6f-1778395577` | `8841d9270f6f` | 48m 46s | 8h 6m 21s | 48m 43s | [25622155880](https://github.com/openclaw/openclaw/actions/runs/25622155880) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/8841d9270f6f-1778395577` | `8841d9270f6f` | 3m 20s | 3m 8s | 11s | [25622213202](https://github.com/openclaw/openclaw/actions/runs/25622213202) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 49m 11s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622149366/job/75210655631) |
| 42m 43s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75210910654) |
| 26m 37s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75210765096) |
| 22m 4s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211024608) |
| 17m 18s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211024606) |
| 13m 46s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75210910648) |
| 11m 56s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75210910649) |
| 11m 41s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75210910660) |
| 11m 40s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75210910653) |
| 11m 28s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75210910659) |
| 11m 18s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75210910642) |
| 8m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622149366/job/75210655627) |
| 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622149366/job/75210805362) |
| 3m 41s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622149366/job/75210655630) |
| 3m 19s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155543/job/75210668354) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 49m 30s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25622149366/job/75213100507) |
| 48m 43s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75213081336) |
| 17m 47s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211564538) |
| 8m 1s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211035931) |
| 8m 1s | 6m 45s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211035932) |
| 8m 1s | 5m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211035935) |
| 8m 1s | 9m 45s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211035939) |
| 8m 1s | 2m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211035940) |
| 8m 1s | 5m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211035943) |
| 8m 1s | 1m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211035947) |
| 8m 1s | 6m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211035950) |
| 3m 35s | 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622149366/job/75210805362) |
| 2m 41s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155543/job/75210781393) |
| 2m 37s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155543/job/75210774190) |
| 2m 31s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622155543/job/75210774195) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25622149366
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25622149366/job/75213100507
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25622155880
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211024606
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75211024608
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25622155880/job/75213081336

## Notes

Automatically requested by Full Release Validation 25622149366 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


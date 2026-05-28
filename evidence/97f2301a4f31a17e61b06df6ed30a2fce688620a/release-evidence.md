# OpenClaw Release Evidence: 97f2301a4f31a17e61b06df6ed30a2fce688620a

Generated: 2026-05-09T18:29:56.412Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `97f2301a4f31a17e61b06df6ed30a2fce688620a` |
| Release ref input | `97f2301a4f31a17e61b06df6ed30a2fce688620a` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `97f2301a4f31a17e61b06df6ed30a2fce688620a` |
| Release ref SHA | `97f2301a4f31a17e61b06df6ed30a2fce688620a` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/97f2301a4f31-1778350008799` | `97f2301a4f31` | 22m 40s | 51m 20s | 22m 9s | [25608146839](https://github.com/openclaw/openclaw/actions/runs/25608146839) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/97f2301a4f31-1778350008799` | `97f2301a4f31` | 12m 27s | 1h 22m 37s | 2m 49s | [25608156481](https://github.com/openclaw/openclaw/actions/runs/25608156481) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/97f2301a4f31-1778350008799` | `97f2301a4f31` | 22m 8s | 6h 44m 25s | 22m 5s | [25608154349](https://github.com/openclaw/openclaw/actions/runs/25608154349) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/97f2301a4f31-1778350008799` | `97f2301a4f31` | 3m 44s | 3m 27s | 16s | [25608216099](https://github.com/openclaw/openclaw/actions/runs/25608216099) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 21m 49s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608146839/job/75173490012) |
| 19m 21s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173624167) |
| 16m 30s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173750529) |
| 15m 7s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173885119) |
| 13m 47s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173750520) |
| 12m 51s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608146839/job/75173490017) |
| 12m 9s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173750523) |
| 12m 2s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173750525) |
| 12m 0s | `normal-ci` | macos-swift | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25608156481/job/75173514618) |
| 11m 45s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173750556) |
| 11m 33s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173750536) |
| 11m 27s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173750521) |
| 11m 22s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173885108) |
| 8m 51s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608146839/job/75173490014) |
| 4m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608146839/job/75173646346) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 22m 9s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25608146839/job/75174752105) |
| 22m 5s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75174764993) |
| 17m 45s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75174524740) |
| 13m 37s | 8m 9s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173750546) |
| 7m 20s | 1m 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173911011) |
| 7m 19s | 1m 39s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173910996) |
| 7m 19s | 7m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173911000) |
| 7m 19s | 3m 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173911010) |
| 7m 18s | 1m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173910998) |
| 7m 18s | 2m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173911006) |
| 7m 14s | 4m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173910988) |
| 3m 10s | 4m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608146839/job/75173646346) |
| 2m 49s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608156481/job/75173652875) |
| 2m 18s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608156481/job/75173621759) |
| 2m 4s | 4s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25608156481/job/75173608783) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608146839
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608146839/job/75173490012
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25608146839/job/75174752105
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25608156481
  - macos-swift: failure - https://github.com/openclaw/openclaw/actions/runs/25608156481/job/75173514618
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608154349
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173624167
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173750529
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173750546
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173885108
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75173885119
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25608154349/job/75174764993

## Notes

Automatically requested by Full Release Validation 25608146839 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


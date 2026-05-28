# OpenClaw Release Evidence: bce62ce0706a7d298263ed8a9234bd5808e03b5e

Generated: 2026-05-09T16:46:12.684Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `bce62ce0706a7d298263ed8a9234bd5808e03b5e` |
| Release ref input | `bce62ce0706a7d298263ed8a9234bd5808e03b5e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `bce62ce0706a7d298263ed8a9234bd5808e03b5e` |
| Release ref SHA | `bce62ce0706a7d298263ed8a9234bd5808e03b5e` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/bce62ce0706a-1778344405029` | `bce62ce0706a` | 12m 20s | 31m 16s | 11m 54s | [25606110984](https://github.com/openclaw/openclaw/actions/runs/25606110984) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/bce62ce0706a-1778344405029` | `bce62ce0706a` | 3m 59s | 1h 13m 40s | 2m 56s | [25606119225](https://github.com/openclaw/openclaw/actions/runs/25606119225) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/bce62ce0706a-1778344405029` | `bce62ce0706a` | 12m 18s | 5h 16m 3s | 12m 16s | [25606119163](https://github.com/openclaw/openclaw/actions/runs/25606119163) | 45 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/bce62ce0706a-1778344405029` | `bce62ce0706a` | 2m 58s | 2m 43s | 15s | [25606176541](https://github.com/openclaw/openclaw/actions/runs/25606176541) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 11m 35s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606110984/job/75168193501) |
| 9m 24s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168317939) |
| 8m 49s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606110984/job/75168193496) |
| 7m 52s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437585) |
| 7m 28s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168408030) |
| 7m 11s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168318055) |
| 7m 10s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437570) |
| 7m 10s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437574) |
| 6m 59s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437563) |
| 6m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168318068) |
| 6m 54s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437572) |
| 6m 48s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437593) |
| 4m 13s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606110984/job/75168193502) |
| 3m 22s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119225/job/75168220233) |
| 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606110984/job/75168346052) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 12m 16s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168870511) |
| 11m 54s | 26s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606110984/job/75168828344) |
| 11m 44s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168840610) |
| 7m 8s | 1m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575941) |
| 7m 7s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575918) |
| 7m 7s | 4m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575927) |
| 7m 7s | 4m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575932) |
| 7m 7s | 4m 28s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575939) |
| 7m 6s | 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575933) |
| 7m 6s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575934) |
| 7m 6s | 1m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575935) |
| 3m 1s | 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606110984/job/75168346052) |
| 2m 56s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119225/job/75168357228) |
| 2m 8s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119225/job/75168317381) |
| 2m 4s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606119225/job/75168313873) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606110984
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606110984/job/75168193501
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25606110984/job/75168828344
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168317939
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168408030
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437562
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437563
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437566
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437570
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437572
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437573
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437574
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437585
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168437593
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168475918
  - Run Docker release-path validation / Docker E2E (plugins/runtime install E): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168562249
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168562256
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168562261
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575916
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575923
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575924
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575927
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575930
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575932
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): failure - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575938
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168575939
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168840610
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25606119163/job/75168870511

## Notes

Automatically requested by Full Release Validation 25606110984 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


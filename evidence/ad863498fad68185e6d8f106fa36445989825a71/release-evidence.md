# OpenClaw Release Evidence: ad863498fad68185e6d8f106fa36445989825a71

Generated: 2026-05-03T17:49:28.042Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `ad863498fad68185e6d8f106fa36445989825a71` |
| Release ref input | `ad863498fad68185e6d8f106fa36445989825a71` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `ad863498fad68185e6d8f106fa36445989825a71` |
| Release ref SHA | `ad863498fad68185e6d8f106fa36445989825a71` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/ad863498fad6-1777828469395` | `ad863498fad6` | 34m 33s | 52m 34s | 34m 4s | [25285564275](https://github.com/openclaw/openclaw/actions/runs/25285564275) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/ad863498fad6-1777828469395` | `ad863498fad6` | 3m 53s | 1h 12m 14s | 3m 48s | [25285572555](https://github.com/openclaw/openclaw/actions/runs/25285572555) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/ad863498fad6-1777828469395` | `ad863498fad6` | 33m 22s | 13h 27m 22s | 33m 19s | [25285573220](https://github.com/openclaw/openclaw/actions/runs/25285573220) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/ad863498fad6-1777828469395` | `ad863498fad6` | 1m 50s | 1m 35s | 15s | [25285633618](https://github.com/openclaw/openclaw/actions/runs/25285633618) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 33m 44s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285564275/job/74129381692) |
| 26m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129756908) |
| 23m 36s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129511478) |
| 23m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129511485) |
| 23m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129511498) |
| 22m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129511497) |
| 22m 34s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129511496) |
| 22m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129511504) |
| 21m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129511492) |
| 21m 21s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129511505) |
| 20m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129511483) |
| 9m 11s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285564275/job/74129381691) |
| 4m 16s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285564275/job/74129381696) |
| 3m 31s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285572555/job/74129400136) |
| 2m 54s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285572555/job/74129400117) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 34m 4s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285564275/job/74131212958) |
| 33m 19s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74131194080) |
| 33m 12s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74131188173) |
| 6m 44s | 1m 13s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129756893) |
| 6m 44s | 1m 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129756903) |
| 6m 43s | 1m 24s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129756886) |
| 6m 43s | 7m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129756889) |
| 6m 43s | 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129756899) |
| 6m 43s | 26m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129756908) |
| 6m 29s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129756972) |
| 6m 29s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129756994) |
| 3m 48s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285572555/job/74129603055) |
| 2m 45s | 2m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285564275/job/74129526224) |
| 2m 31s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285572555/job/74129532340) |
| 2m 13s | 2s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285572555/job/74129508520) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25285564275
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25285564275/job/74131212958
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25285572555
  - check-dependencies: failure - https://github.com/openclaw/openclaw/actions/runs/25285572555/job/74129400099
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25285572555/job/74129464031
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25285573220
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129620408
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74129756908
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74131188173
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25285573220/job/74131194080

## Notes

Automatically requested by Full Release Validation 25285564275 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


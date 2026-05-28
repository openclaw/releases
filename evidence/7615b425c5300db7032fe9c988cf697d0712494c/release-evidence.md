# OpenClaw Release Evidence: 7615b425c5300db7032fe9c988cf697d0712494c

Generated: 2026-05-06T10:41:33.320Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `7615b425c5300db7032fe9c988cf697d0712494c` |
| Release ref input | `7615b425c5300db7032fe9c988cf697d0712494c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `7615b425c5300db7032fe9c988cf697d0712494c` |
| Release ref SHA | `7615b425c5300db7032fe9c988cf697d0712494c` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.5` | `7615b425c530` | 1h 4m 42s | 1h 36m 3s | 1h 4m 5s | [25427630916](https://github.com/openclaw/openclaw/actions/runs/25427630916) | 1 |
| pass | blocking | `normal-ci` | CI | `release/2026.5.5` | `7615b425c530` | 4m 29s | 1h 25m 2s | 4m 25s | [25427647235](https://github.com/openclaw/openclaw/actions/runs/25427647235) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.5` | `7615b425c530` | 1h 2m 58s | 13h 50m 37s | 1h 2m 55s | [25427652790](https://github.com/openclaw/openclaw/actions/runs/25427652790) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release/2026.5.5` | `7615b425c530` | 7m 9s | 1m 45s | 5m 23s | [25427765577](https://github.com/openclaw/openclaw/actions/runs/25427765577) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 3m 40s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427630916/job/74585231222) |
| 1h 0m 18s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585663751) |
| 32m 38s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585961282) |
| 28m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74587023821) |
| 25m 48s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585966588) |
| 24m 34s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585664162) |
| 24m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585664132) |
| 23m 3s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585664098) |
| 22m 43s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585664209) |
| 22m 16s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585664165) |
| 21m 55s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585966636) |
| 16m 58s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427630916/job/74585231169) |
| 7m 22s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427630916/job/74585630245) |
| 4m 44s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427630916/job/74585231224) |
| 3m 55s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427647235/job/74585287300) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 4m 5s | 36s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25427630916/job/74594992710) |
| 1h 2m 55s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74594893232) |
| 42m 41s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74591881200) |
| 14m 2s | 2m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74587023830) |
| 14m 1s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74587023807) |
| 14m 1s | 1m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74587023809) |
| 14m 1s | 7m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74587023818) |
| 14m 1s | 28m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74587023821) |
| 14m 1s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74587023848) |
| 11m 16s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74587023826) |
| 11m 15s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74587024287) |
| 5m 23s | 1m 45s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427765577/job/74585672971) |
| 4m 25s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427647235/job/74585918433) |
| 2m 59s | 7m 22s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427630916/job/74585630245) |
| 2m 51s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25427647235/job/74585685917) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25427630916
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25427630916/job/74594992710
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25427652790
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585663751
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74585966632
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25427652790/job/74594893232

## Notes

Automatically requested by Full Release Validation 25427630916 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


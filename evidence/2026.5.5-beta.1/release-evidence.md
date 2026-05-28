# OpenClaw Release Evidence: 2026.5.5-beta.1

Generated: 2026-05-06T03:46:14.337Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.5-beta.1` |
| Release ref input | `013a2c50f62fad3941bfa51b8ac9a548e603b842` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `013a2c50f62fad3941bfa51b8ac9a548e603b842` |
| Release ref SHA | `013a2c50f62fad3941bfa51b8ac9a548e603b842` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | `openclaw@2026.5.5-beta.1` |
| npm status | published |
| npm resolved version | `2026.5.5-beta.1` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-06T02:33:08.137Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.5-beta.1.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/013a2c50f62f-1778035183068` | `013a2c50f62f` | 1h 6m 10s (+26m 32s) | 1h 20m 57s (+29m 28s) | 1h 5m 39s | [25413532465](https://github.com/openclaw/openclaw/actions/runs/25413532465) | 0 |
| fail | blocking | `normal-ci` | CI | `release-ci/013a2c50f62f-1778035183068` | `013a2c50f62f` | 4m 13s (-3s) | 1h 21m 30s (+8m 48s) | 4m 9s | [25413545621](https://github.com/openclaw/openclaw/actions/runs/25413545621) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/013a2c50f62f-1778035183068` | `013a2c50f62f` | 1h 4m 45s (+26m 47s) | 12h 56m 54s (+11h 31m 57s) | 1h 4m 42s | [25413548935](https://github.com/openclaw/openclaw/actions/runs/25413548935) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/013a2c50f62f-1778035183068` | `013a2c50f62f` | 1m 55s | 1m 42s | 12s | [25413546004](https://github.com/openclaw/openclaw/actions/runs/25413546004) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 5m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413532465/job/74540170595) |
| 1h 0m 18s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540530003) |
| 32m 17s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540687304) |
| 28m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540875947) |
| 24m 15s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540716174) |
| 23m 45s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540716181) |
| 21m 43s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540530109) |
| 21m 35s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540716171) |
| 21m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540530142) |
| 20m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540530114) |
| 20m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540530126) |
| 8m 14s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413532465/job/74540170609) |
| 4m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413532465/job/74540170594) |
| 3m 45s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413545621/job/74540198126) |
| 3m 8s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413545621/job/74540198103) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 5m 39s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25413532465/job/74545471375) |
| 1h 4m 42s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74545449708) |
| 37m 16s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74543245033) |
| 9m 0s | 28m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540875947) |
| 9m 0s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540875953) |
| 9m 0s | 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540875969) |
| 9m 0s | 1m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540875973) |
| 8m 59s | 1m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540875938) |
| 8m 59s | 1m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540875949) |
| 8m 58s | 1m 39s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540875939) |
| 8m 55s | 1m 56s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540869848) |
| 4m 9s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413545621/job/74540496472) |
| 3m 2s | 2s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25413545621/job/74540417751) |
| 2m 15s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413545621/job/74540347928) |
| 2m 14s | 4s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25413545621/job/74540347919) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 37m 58s | 1h 4m 45s | +26m 47s | +11h 31m 57s |
| `full-release-validation` | 39m 38s | 1h 6m 10s | +26m 32s | +29m 28s |
| `normal-ci` | 4m 16s | 4m 13s | -3s | +8m 48s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25413532465
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25413532465/job/74545471375
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25413545621
  - checks-node-agentic-commands-onboard-config: failure - https://github.com/openclaw/openclaw/actions/runs/25413545621/job/74540198300
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25413545621/job/74540417751
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25413548935
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540530003
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540716140
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin): failure - https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540875938
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74540875947
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74543245033
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25413548935/job/74545449708

## Notes

Automatically requested by Full Release Validation 25413532465 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


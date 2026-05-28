# OpenClaw Release Evidence: a1d44ea1222a7bfd1be0aea97696a905007f9dea

Generated: 2026-05-03T18:09:53.138Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `a1d44ea1222a7bfd1be0aea97696a905007f9dea` |
| Release ref input | `a1d44ea1222a7bfd1be0aea97696a905007f9dea` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `a1d44ea1222a7bfd1be0aea97696a905007f9dea` |
| Release ref SHA | `a1d44ea1222a7bfd1be0aea97696a905007f9dea` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/a1d44ea1222a-1777829996054` | `a1d44ea1222a` | 29m 25s | 50m 8s | 29m 1s | [25286132520](https://github.com/openclaw/openclaw/actions/runs/25286132520) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/a1d44ea1222a-1777829996054` | `a1d44ea1222a` | 3m 59s | 1h 9m 19s | 3m 55s | [25286142409](https://github.com/openclaw/openclaw/actions/runs/25286142409) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/a1d44ea1222a-1777829996054` | `a1d44ea1222a` | 28m 9s | 13h 2m 16s | 28m 7s | [25286143042](https://github.com/openclaw/openclaw/actions/runs/25286143042) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/a1d44ea1222a-1777829996054` | `a1d44ea1222a` | 1m 47s | 1m 31s | 15s | [25286192446](https://github.com/openclaw/openclaw/actions/runs/25286192446) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 28m 39s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286132520/job/74130767309) |
| 23m 3s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74130886864) |
| 22m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74130886908) |
| 21m 0s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74130886890) |
| 20m 38s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74130886865) |
| 20m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74131165225) |
| 20m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74130886878) |
| 19m 42s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74130886705) |
| 19m 23s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74130971495) |
| 19m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74130886881) |
| 19m 5s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74130971551) |
| 12m 17s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286132520/job/74130767305) |
| 4m 10s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286132520/job/74130767312) |
| 3m 27s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286142409/job/74130787839) |
| 2m 16s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286132520/job/74130767300) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 29m 1s | 24s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25286132520/job/74132317260) |
| 28m 7s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74132284282) |
| 27m 53s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74132275654) |
| 7m 28s | 20m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74131165225) |
| 7m 28s | 1m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74131165226) |
| 7m 28s | 1m 28s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74131165228) |
| 7m 28s | 2m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74131165242) |
| 7m 27s | 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74131165217) |
| 7m 27s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74131165221) |
| 7m 18s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74131165344) |
| 7m 18s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74131165509) |
| 3m 55s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286142409/job/74130975694) |
| 2m 43s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286142409/job/74130909466) |
| 2m 37s | 2m 14s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286132520/job/74130888104) |
| 2m 2s | 4s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286142409/job/74130877454) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25286132520
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25286132520/job/74132317260
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25286143042
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74131165225
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74132275654
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25286143042/job/74132284282

## Notes

Automatically requested by Full Release Validation 25286132520 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


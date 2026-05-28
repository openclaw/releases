# OpenClaw Release Evidence: fc7e2a10c8fcadf8f38d3645cb05848accfa4b5d

Generated: 2026-05-04T18:58:48.964Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `fc7e2a10c8fcadf8f38d3645cb05848accfa4b5d` |
| Release ref input | `fc7e2a10c8fcadf8f38d3645cb05848accfa4b5d` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `fc7e2a10c8fcadf8f38d3645cb05848accfa4b5d` |
| Release ref SHA | `fc7e2a10c8fcadf8f38d3645cb05848accfa4b5d` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 0 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/fc7e2a10c8fc-1777918968735` | `fc7e2a10c8fc` | 35m 25s | 1h 22m 20s | 34m 55s | [25335809272](https://github.com/openclaw/openclaw/actions/runs/25335809272) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/fc7e2a10c8fc-1777918968735` | `fc7e2a10c8fc` | 4m 13s | 1h 18m 40s | 4m 10s | [25335834948](https://github.com/openclaw/openclaw/actions/runs/25335834948) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/fc7e2a10c8fc-1777918968735` | `fc7e2a10c8fc` | 34m 4s | 13h 58m 11s | 34m 4s | [25335829371](https://github.com/openclaw/openclaw/actions/runs/25335829371) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/fc7e2a10c8fc-1777918968735` | `fc7e2a10c8fc` | 5m 35s | 2m 54s | 2m 40s | [25335949040](https://github.com/openclaw/openclaw/actions/runs/25335949040) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 34m 34s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25335809272/job/74280683894) |
| 34m 6s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25335809272/job/74280683840) |
| 26m 33s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74281364279) |
| 24m 3s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74281364275) |
| 23m 13s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74281118192) |
| 20m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74281117905) |
| 20m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74281117968) |
| 19m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74281117980) |
| 19m 33s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282193591) |
| 19m 22s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74281117900) |
| 19m 13s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74281117904) |
| 19m 6s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282193631) |
| 5m 56s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335809272/job/74281083351) |
| 4m 47s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335809272/job/74280683836) |
| 3m 44s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335834948/job/74280766732) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 34m 55s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25335809272/job/74286192556) |
| 34m 4s |  | `release-checks` | Run package acceptance / Verify package acceptance |  | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74286131480) |
| 15m 31s | 2m 22s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282983589) |
| 15m 31s | 1m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282983591) |
| 15m 31s | 7m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282983600) |
| 15m 31s | 1m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282983604) |
| 15m 31s | 18m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282983606) |
| 15m 29s | 6m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282983663) |
| 14m 13s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282983897) |
| 14m 12s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282983770) |
| 13m 39s | 14m 16s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335829371/job/74282193479) |
| 4m 10s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335834948/job/74281385241) |
| 3m 24s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335834948/job/74281246595) |
| 3m 19s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335834948/job/74281232165) |
| 3m 14s | 4s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25335834948/job/74281232181) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25335809272
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25335809272/job/74280683840
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25335809272/job/74280683894
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25335809272/job/74286192556

## Notes

Automatically requested by Full Release Validation 25335809272 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


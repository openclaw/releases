# OpenClaw Release Evidence: 30e259b9c565bfb57ed51ced07fb4e19cd312b3d

Generated: 2026-05-04T18:59:34.294Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `30e259b9c565bfb57ed51ced07fb4e19cd312b3d` |
| Release ref input | `30e259b9c565bfb57ed51ced07fb4e19cd312b3d` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `30e259b9c565bfb57ed51ced07fb4e19cd312b3d` |
| Release ref SHA | `30e259b9c565bfb57ed51ced07fb4e19cd312b3d` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/30e259b9c565-1777912193256` | `30e259b9c565` | 2h 29m 23s | 3h 17m 38s | 2h 28m 43s | [25330485566](https://github.com/openclaw/openclaw/actions/runs/25330485566) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/30e259b9c565-1777912193256` | `30e259b9c565` | 9m 20s | 1h 18m 5s | 9m 17s | [25330508320](https://github.com/openclaw/openclaw/actions/runs/25330508320) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/30e259b9c565-1777912193256` | `30e259b9c565` | 2h 27m 44s | 16h 2m 15s | 2h 27m 40s | [25330513857](https://github.com/openclaw/openclaw/actions/runs/25330513857) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/30e259b9c565-1777912193256` | `30e259b9c565` | 6m 14s | 1m 43s | 4m 30s | [25330620892](https://github.com/openclaw/openclaw/actions/runs/25330620892) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 2h 28m 12s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330485566/job/74262668830) |
| 2h 5m 0s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74264049332) |
| 31m 42s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74263426937) |
| 30m 12s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330485566/job/74262668769) |
| 25m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74266381132) |
| 23m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74263059509) |
| 22m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74263059632) |
| 21m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74263059434) |
| 21m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74263059480) |
| 21m 27s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74264135628) |
| 21m 22s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74263059431) |
| 20m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74263059533) |
| 9m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330485566/job/74262668795) |
| 6m 22s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330485566/job/74263058735) |
| 3m 43s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330508320/job/74262739555) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2h 28m 43s | 39s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25330485566/job/74286332219) |
| 2h 27m 40s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74286239194) |
| 48m 41s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74270440993) |
| 23m 18s | 1m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74266381100) |
| 23m 18s | 1m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74266381187) |
| 23m 17s | 2m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74266381119) |
| 23m 17s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74266381125) |
| 23m 17s | 25m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74266381132) |
| 23m 5s | 7m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74266381109) |
| 23m 3s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74266381575) |
| 23m 3s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74266381844) |
| 9m 17s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330508320/job/74264178226) |
| 8m 42s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330508320/job/74264075412) |
| 8m 37s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330508320/job/74264075395) |
| 8m 36s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25330508320/job/74264075392) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25330485566
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25330485566/job/74286332219
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25330513857
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74262907170
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74263426937
  - Run Docker release-path validation / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74264049332
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25330513857/job/74286239194

## Notes

Automatically requested by Full Release Validation 25330485566 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


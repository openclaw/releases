# OpenClaw Release Evidence: 096c4c22b54a83941d29476275f8be6650f16e02

Generated: 2026-05-03T23:02:01.693Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `096c4c22b54a83941d29476275f8be6650f16e02` |
| Release ref input | `096c4c22b54a83941d29476275f8be6650f16e02` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `096c4c22b54a83941d29476275f8be6650f16e02` |
| Release ref SHA | `096c4c22b54a83941d29476275f8be6650f16e02` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/096c4c22b54a-1777847455886` | `096c4c22b54a` | 30m 47s | 51m 43s | 30m 17s | [25292690122](https://github.com/openclaw/openclaw/actions/runs/25292690122) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/096c4c22b54a-1777847455886` | `096c4c22b54a` | 9m 30s | 1h 25m 41s | 7m 29s | [25292695946](https://github.com/openclaw/openclaw/actions/runs/25292695946) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/096c4c22b54a-1777847455886` | `096c4c22b54a` | 29m 49s | 13h 16m 26s | 29m 46s | [25292696486](https://github.com/openclaw/openclaw/actions/runs/25292696486) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/096c4c22b54a-1777847455886` | `096c4c22b54a` | 1m 44s | 1m 38s | 5s | [25292748301](https://github.com/openclaw/openclaw/actions/runs/25292748301) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 30m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292690122/job/74146760413) |
| 25m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146878754) |
| 22m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74147132411) |
| 21m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146878743) |
| 21m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146878765) |
| 21m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146878742) |
| 20m 33s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146944707) |
| 20m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146878744) |
| 19m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146878745) |
| 19m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146878764) |
| 19m 38s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146944712) |
| 9m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292690122/job/74146760415) |
| 6m 41s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292690122/job/74146760426) |
| 5m 56s | `normal-ci` | checks-node-agentic-control-plane-runtime | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292695946/job/74146777656) |
| 3m 33s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292695946/job/74146777491) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 30m 17s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292690122/job/74148272186) |
| 29m 46s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74148260755) |
| 29m 39s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74148254496) |
| 7m 53s | 10m 51s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146976186) |
| 7m 53s | 10m 54s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146976197) |
| 7m 45s | 11m 15s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146976185) |
| 7m 29s | 2m 0s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292695946/job/74146777464) |
| 7m 15s | 22m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74147132411) |
| 7m 15s | 1m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74147132413) |
| 7m 15s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74147132414) |
| 7m 15s | 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74147132417) |
| 7m 14s | 2m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74147132410) |
| 6m 14s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292695946/job/74147086785) |
| 6m 7s | 39s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292695946/job/74146777457) |
| 3m 58s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292695946/job/74146966165) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25292690122
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25292690122/job/74148272186
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25292695946
  - checks-fast-contracts-plugins-c: failure - https://github.com/openclaw/openclaw/actions/runs/25292695946/job/74146777471
  - check-dependencies: failure - https://github.com/openclaw/openclaw/actions/runs/25292695946/job/74146777490
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25292695946/job/74146833754
  - checks-fast-contracts-plugins: failure - https://github.com/openclaw/openclaw/actions/runs/25292695946/job/74146857909
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25292696486
  - Run repo/live E2E validation / Live media suites (Native live plugins A-K): failure - https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74146878655
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74147132411
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74148254496
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25292696486/job/74148260755

## Notes

Automatically requested by Full Release Validation 25292690122 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


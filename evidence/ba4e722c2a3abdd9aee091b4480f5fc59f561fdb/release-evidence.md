# OpenClaw Release Evidence: ba4e722c2a3abdd9aee091b4480f5fc59f561fdb

Generated: 2026-05-03T22:55:17.451Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `ba4e722c2a3abdd9aee091b4480f5fc59f561fdb` |
| Release ref input | `ba4e722c2a3abdd9aee091b4480f5fc59f561fdb` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `ba4e722c2a3abdd9aee091b4480f5fc59f561fdb` |
| Release ref SHA | `ba4e722c2a3abdd9aee091b4480f5fc59f561fdb` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/ba4e722c2a3a-1777847063339` | `ba4e722c2a3a` | 30m 21s | 48m 39s | 29m 58s | [25292554504](https://github.com/openclaw/openclaw/actions/runs/25292554504) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/ba4e722c2a3a-1777847063339` | `ba4e722c2a3a` | 6m 18s | 1h 26m 3s | 6m 13s | [25292559631](https://github.com/openclaw/openclaw/actions/runs/25292559631) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/ba4e722c2a3a-1777847063339` | `ba4e722c2a3a` | 29m 11s | 13h 13m 35s | 29m 6s | [25292560247](https://github.com/openclaw/openclaw/actions/runs/25292560247) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/ba4e722c2a3a-1777847063339` | `ba4e722c2a3a` | 1m 44s | 1m 40s | 3s | [25292609577](https://github.com/openclaw/openclaw/actions/runs/25292609577) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 29m 41s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292554504/job/74146429267) |
| 24m 45s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146641574) |
| 22m 24s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146542280) |
| 21m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146542271) |
| 21m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146542272) |
| 21m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146542291) |
| 20m 47s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146542298) |
| 20m 11s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146641548) |
| 19m 53s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146641613) |
| 19m 30s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146542292) |
| 19m 13s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146641616) |
| 7m 11s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292554504/job/74146429269) |
| 6m 47s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292554504/job/74146429265) |
| 5m 55s | `normal-ci` | checks-node-agentic-control-plane-runtime | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146444139) |
| 3m 47s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146444012) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 29m 58s | 23s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292554504/job/74147945753) |
| 29m 6s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74147922064) |
| 23m 17s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74147632336) |
| 6m 22s | 2m 13s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146745176) |
| 6m 22s | 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146745183) |
| 6m 21s | 16m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146745172) |
| 6m 21s | 1m 22s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146745177) |
| 6m 20s | 1m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146745174) |
| 6m 20s | 1m 19s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146745179) |
| 6m 15s | 1m 35s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146739382) |
| 6m 14s | 2m 7s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146739376) |
| 6m 13s | 4s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146745321) |
| 4m 5s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146636323) |
| 2m 34s | 2m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292554504/job/74146542427) |
| 2m 14s | 3s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146545116) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25292554504
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25292554504/job/74147945753
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25292559631
  - checks-fast-contracts-plugins-c: failure - https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146443847
  - check-dependencies: failure - https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146443895
  - checks-node-core-runtime-infra-process: failure - https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146444116
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146518340
  - checks-fast-contracts-plugins: failure - https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146526629
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25292559631/job/74146745321
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25292560247
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74146745172
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74147632336
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25292560247/job/74147922064

## Notes

Automatically requested by Full Release Validation 25292554504 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


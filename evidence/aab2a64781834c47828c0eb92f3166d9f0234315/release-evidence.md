# OpenClaw Release Evidence: aab2a64781834c47828c0eb92f3166d9f0234315

Generated: 2026-05-04T02:01:35.648Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `aab2a64781834c47828c0eb92f3166d9f0234315` |
| Release ref input | `aab2a64781834c47828c0eb92f3166d9f0234315` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `aab2a64781834c47828c0eb92f3166d9f0234315` |
| Release ref SHA | `aab2a64781834c47828c0eb92f3166d9f0234315` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/aab2a6478183-1777858191264` | `aab2a6478183` | 31m 12s | 49m 17s | 30m 47s | [25296701063](https://github.com/openclaw/openclaw/actions/runs/25296701063) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/aab2a6478183-1777858191264` | `aab2a6478183` | 6m 14s | 1h 27m 45s | 6m 11s | [25296710416](https://github.com/openclaw/openclaw/actions/runs/25296710416) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/aab2a6478183-1777858191264` | `aab2a6478183` | 29m 53s | 14h 10m 45s | 29m 49s | [25296712153](https://github.com/openclaw/openclaw/actions/runs/25296712153) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/aab2a6478183-1777858191264` | `aab2a6478183` | 1m 45s | 1m 41s | 3s | [25296771490](https://github.com/openclaw/openclaw/actions/runs/25296771490) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 30m 26s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296701063/job/74156629661) |
| 27m 26s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156775698) |
| 27m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156775737) |
| 27m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156775692) |
| 26m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156775713) |
| 25m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156775730) |
| 22m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156775716) |
| 21m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156775690) |
| 21m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156775708) |
| 21m 3s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156775681) |
| 21m 1s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156849545) |
| 6m 47s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296701063/job/74156629658) |
| 6m 47s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296701063/job/74156629660) |
| 5m 54s | `normal-ci` | checks-node-agentic-control-plane-runtime | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296710416/job/74156654766) |
| 4m 4s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296710416/job/74156654597) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 30m 47s | 24s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25296701063/job/74158484606) |
| 29m 49s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74158442869) |
| 25m 41s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74158200643) |
| 11m 10s | 1m 50s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74157327562) |
| 11m 9s | 1m 42s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74157327567) |
| 11m 8s | 1m 47s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74157327563) |
| 11m 8s | 1m 33s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74157327575) |
| 11m 8s | 1m 27s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74157327582) |
| 11m 7s | 3m 38s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74157327555) |
| 11m 7s | 1m 30s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74157327566) |
| 11m 7s | 1m 41s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74157327580) |
| 6m 11s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296710416/job/74157028042) |
| 4m 21s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296710416/job/74156908852) |
| 2m 44s | 2m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296701063/job/74156786920) |
| 2m 9s | 2s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25296710416/job/74156765474) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25296701063
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25296701063/job/74158484606
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25296712153
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74156714459
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25296712153/job/74158442869

## Notes

Automatically requested by Full Release Validation 25296701063 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


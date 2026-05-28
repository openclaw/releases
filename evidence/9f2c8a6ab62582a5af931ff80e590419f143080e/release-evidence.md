# OpenClaw Release Evidence: 9f2c8a6ab62582a5af931ff80e590419f143080e

Generated: 2026-05-04T23:17:47.096Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `9f2c8a6ab62582a5af931ff80e590419f143080e` |
| Release ref input | `9f2c8a6ab62582a5af931ff80e590419f143080e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `9f2c8a6ab62582a5af931ff80e590419f143080e` |
| Release ref SHA | `9f2c8a6ab62582a5af931ff80e590419f143080e` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/9f2c8a6ab625-1777933735309` | `9f2c8a6ab625` | 48m 20s | 1h 16m 7s | 47m 48s | [25347022290](https://github.com/openclaw/openclaw/actions/runs/25347022290) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/9f2c8a6ab625-1777933735309` | `9f2c8a6ab625` | 3m 56s | 1h 12m 15s | 3m 52s | [25347034954](https://github.com/openclaw/openclaw/actions/runs/25347034954) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/9f2c8a6ab625-1777933735309` | `9f2c8a6ab625` | 47m 6s | 11h 35m 33s | 47m 1s | [25347035707](https://github.com/openclaw/openclaw/actions/runs/25347035707) | 31 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/9f2c8a6ab625-1777933735309` | `9f2c8a6ab625` | 7m 16s | 1m 41s | 5m 34s | [25347148794](https://github.com/openclaw/openclaw/actions/runs/25347148794) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 47m 26s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347022290/job/74318170453) |
| 37m 54s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74318694736) |
| 22m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74318481845) |
| 21m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74318481870) |
| 21m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74318481837) |
| 21m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74318481849) |
| 20m 16s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74318481889) |
| 19m 33s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74319456574) |
| 18m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74318481888) |
| 18m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74318481786) |
| 18m 35s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74319456568) |
| 13m 26s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347022290/job/74318170454) |
| 7m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347022290/job/74318528783) |
| 4m 12s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347022290/job/74318170448) |
| 3m 36s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347034954/job/74318209363) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 47m 48s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25347022290/job/74323588361) |
| 47m 1s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74323540095) |
| 16m 22s | 1m 25s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74320070253) |
| 16m 22s | 1m 52s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74320070264) |
| 16m 22s | 2m 5s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74320070286) |
| 15m 43s | 1m 11s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74320070243) |
| 15m 43s | 2m 40s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74320070245) |
| 15m 43s | 2m 4s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74320070250) |
| 15m 43s | 1m 50s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74320070252) |
| 15m 43s | 7m 39s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74320070254) |
| 15m 43s | 1m 39s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74320070258) |
| 5m 34s | 1m 41s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347148794/job/74318546339) |
| 3m 52s | 4s | `normal-ci` | check-additional | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25347034954/job/74318674500) |
| 2m 57s | 7m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25347022290/job/74318528783) |
| 2m 47s | 4s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25347034954/job/74318532532) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25347022290
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25347022290/job/74323588361
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25347034954
  - check-lint: failure - https://github.com/openclaw/openclaw/actions/runs/25347034954/job/74318209301
  - check-additional-extension-bundled: failure - https://github.com/openclaw/openclaw/actions/runs/25347034954/job/74318209333
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25347034954/job/74318409124
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25347034954/job/74318418576
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25347034954/job/74318532532
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25347034954/job/74318674500
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25347035707
  - Run repo/live E2E validation / validate_release_live_cache: failure - https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74318481324
  - Run package acceptance / Resolve package candidate: failure - https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74318636044
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74319293854
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): failure - https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74319456596
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74319456670
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25347035707/job/74323540095

## Notes

Automatically requested by Full Release Validation 25347022290 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


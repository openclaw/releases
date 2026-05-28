# OpenClaw Release Evidence: a3f6f24b79a5c35bb2267c8936e733c55be67c5f

Generated: 2026-05-04T19:55:12.740Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `a3f6f24b79a5c35bb2267c8936e733c55be67c5f` |
| Release ref input | `a3f6f24b79a5c35bb2267c8936e733c55be67c5f` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `a3f6f24b79a5c35bb2267c8936e733c55be67c5f` |
| Release ref SHA | `a3f6f24b79a5c35bb2267c8936e733c55be67c5f` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/a3f6f24b79a5-1777922056350` | `a3f6f24b79a5` | 40m 24s | 58m 48s | 39m 53s | [25338244513](https://github.com/openclaw/openclaw/actions/runs/25338244513) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/a3f6f24b79a5-1777922056350` | `a3f6f24b79a5` | 4m 14s | 1h 18m 4s | 4m 11s | [25338266091](https://github.com/openclaw/openclaw/actions/runs/25338266091) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/a3f6f24b79a5-1777922056350` | `a3f6f24b79a5` | 38m 44s | 13h 49m 59s | 38m 40s | [25338267149](https://github.com/openclaw/openclaw/actions/runs/25338267149) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/a3f6f24b79a5-1777922056350` | `a3f6f24b79a5` | 2m 21s | 2m 15s | 5s | [25338386206](https://github.com/openclaw/openclaw/actions/runs/25338386206) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 39m 21s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338244513/job/74288961554) |
| 31m 33s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74289656111) |
| 22m 24s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74289642510) |
| 22m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74290189190) |
| 22m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74289331881) |
| 21m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74289331836) |
| 20m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74289331843) |
| 20m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74289331854) |
| 19m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74289331827) |
| 19m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74289331832) |
| 19m 2s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74289331452) |
| 8m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338244513/job/74288961578) |
| 4m 41s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338244513/job/74288961553) |
| 3m 42s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338266091/job/74289032476) |
| 2m 47s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338244513/job/74289386886) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 39m 53s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25338244513/job/74295212524) |
| 38m 40s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74295095194) |
| 38m 25s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74295072857) |
| 16m 2s | 1m 13s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74290155677) |
| 16m 2s | 3m 16s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74290155683) |
| 16m 2s | 2m 15s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74290155690) |
| 16m 2s | 7m 31s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74290155726) |
| 16m 2s | 1m 38s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74290155729) |
| 16m 2s | 1m 42s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74290155739) |
| 16m 2s | 1m 48s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74290155747) |
| 16m 2s | 6m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74290189158) |
| 4m 11s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338266091/job/74289620783) |
| 3m 35s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338266091/job/74289525635) |
| 3m 35s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338266091/job/74289543374) |
| 3m 34s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25338266091/job/74289525628) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25338244513
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25338244513/job/74295212524
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25338267149
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74289656111
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25338267149/job/74295095194

## Notes

Automatically requested by Full Release Validation 25338244513 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 864b1be1b3205141f0e0e8ddf83f38aff334dc23

Generated: 2026-05-04T23:39:17.925Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `864b1be1b3205141f0e0e8ddf83f38aff334dc23` |
| Release ref input | `864b1be1b3205141f0e0e8ddf83f38aff334dc23` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `864b1be1b3205141f0e0e8ddf83f38aff334dc23` |
| Release ref SHA | `864b1be1b3205141f0e0e8ddf83f38aff334dc23` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/864b1be1b320-1777935598454` | `864b1be1b320` | 38m 52s | 55m 45s | 38m 25s | [25348178218](https://github.com/openclaw/openclaw/actions/runs/25348178218) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/864b1be1b320-1777935598454` | `864b1be1b320` | 3m 54s | 1h 17m 11s | 3m 51s | [25348196146](https://github.com/openclaw/openclaw/actions/runs/25348196146) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/864b1be1b320-1777935598454` | `864b1be1b320` | 37m 37s | 11h 54m 6s | 37m 34s | [25348194700](https://github.com/openclaw/openclaw/actions/runs/25348194700) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/864b1be1b320-1777935598454` | `864b1be1b320` | 1m 40s | 1m 35s | 4s | [25348278075](https://github.com/openclaw/openclaw/actions/runs/25348278075) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 38m 6s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348178218/job/74321808180) |
| 32m 9s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74322289705) |
| 24m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74322654519) |
| 23m 18s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74322107446) |
| 22m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74322107462) |
| 22m 20s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74322107410) |
| 21m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74322107404) |
| 20m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74322107430) |
| 20m 47s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74322107456) |
| 20m 30s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74323009417) |
| 19m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74322107441) |
| 8m 15s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348178218/job/74321808136) |
| 4m 11s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348178218/job/74321808211) |
| 3m 29s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348196146/job/74321862023) |
| 2m 36s | `normal-ci` | checks-node-core-runtime-infra-state | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348196146/job/74321862129) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 38m 25s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25348178218/job/74325921478) |
| 37m 34s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74325878831) |
| 33m 45s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74325481297) |
| 11m 21s | 15m 18s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74323009349) |
| 11m 21s | 13m 6s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74323009353) |
| 11m 21s | 13m 19s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74323009354) |
| 11m 21s | 13m 35s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74323009355) |
| 11m 21s | 12m 49s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74323009381) |
| 11m 21s | 14m 38s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74323009388) |
| 11m 21s | 1m 10s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74323009409) |
| 11m 21s | 17m 50s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74323009412) |
| 3m 51s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348196146/job/74322267467) |
| 2m 53s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25348196146/job/74322155769) |
| 2m 38s | 2m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348178218/job/74322081406) |
| 2m 16s | 2s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25348196146/job/74322077553) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25348178218
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25348178218/job/74325921478
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25348196146
  - checks-node-agentic-commands-doctor: failure - https://github.com/openclaw/openclaw/actions/runs/25348196146/job/74321862158
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25348196146/job/74322155769
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25348194700
  - Run repo/live E2E validation / validate_release_live_cache: failure - https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74322107029
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): failure - https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74323009409
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25348194700/job/74325878831

## Notes

Automatically requested by Full Release Validation 25348178218 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


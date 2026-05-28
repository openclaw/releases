# OpenClaw Release Evidence: 2026.5.3-beta.4

Generated: 2026-05-04T04:14:34.349Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.3-beta.4` |
| Release ref input | `v2026.5.3-beta.4` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.3-beta.4` |
| Release ref SHA | `c6c64e2acfd8407744b08428a1b627f8a14484ed` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.3` | `c6c64e2acfd8` | 33m 32s (+27m 55s) | 53m 16s (+34m 49s) | 33m 5s | [25299855527](https://github.com/openclaw/openclaw/actions/runs/25299855527) | 1 |
| pass | blocking | `normal-ci` | CI | `release/2026.5.3` | `c6c64e2acfd8` | 3m 54s (-8s) | 1h 12m 13s (-11m 1s) | 3m 49s | [25299870289](https://github.com/openclaw/openclaw/actions/runs/25299870289) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.3` | `c6c64e2acfd8` | 32m 5s (+26m 58s) | 13h 13m 12s (+11h 29m 33s) | 32m 2s | [25299870554](https://github.com/openclaw/openclaw/actions/runs/25299870554) | 37 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release/2026.5.3` | `c6c64e2acfd8` | 1m 41s (+6s) | 1m 38s (+7s) | 3s | [25299936448](https://github.com/openclaw/openclaw/actions/runs/25299936448) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 32m 32s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299855527/job/74164848271) |
| 28m 10s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165074747) |
| 22m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74164996807) |
| 21m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74164996782) |
| 21m 20s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74164996776) |
| 20m 47s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74164996808) |
| 20m 4s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165074743) |
| 19m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74164996823) |
| 19m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74164996798) |
| 19m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74164996812) |
| 18m 58s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165074754) |
| 11m 15s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299855527/job/74164848257) |
| 4m 9s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299855527/job/74164848261) |
| 3m 29s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870289/job/74164871255) |
| 2m 25s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299855527/job/74164848258) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 33m 5s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25299855527/job/74166902700) |
| 32m 2s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74166865966) |
| 23m 44s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74166333148) |
| 14m 8s | 0s | `release-checks` | Run QA Lab parity report | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165731337) |
| 6m 11s | 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165235912) |
| 6m 11s | 1m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165235919) |
| 6m 10s | 1m 28s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165235883) |
| 6m 10s | 17m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165235894) |
| 6m 10s | 1m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165235902) |
| 6m 0s | 2m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165235881) |
| 5m 59s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165236105) |
| 3m 49s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870289/job/74165091739) |
| 3m 6s | 2m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299855527/job/74165012046) |
| 2m 43s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870289/job/74165024670) |
| 2m 32s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25299870289/job/74165006416) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 5m 37s | 33m 32s | +27m 55s | +34m 49s |
| `release-checks` | 5m 7s | 32m 5s | +26m 58s | +11h 29m 33s |
| `normal-ci` | 4m 2s | 3m 54s | -8s | -11m 1s |
| `postpublish-telegram` | 1m 35s | 1m 41s | +6s | +7s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25299855527
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25299855527/job/74166902700
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25299870554
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74164927940
  - Run QA Lab parity lane (baseline): failure - https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74164927943
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74164927955
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165074747
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): failure - https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165074748
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165074755
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74165091588
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25299870554/job/74166865966

## Notes

Automatically requested by Full Release Validation 25299855527 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


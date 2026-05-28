# OpenClaw Release Evidence: e65017b0f98f3f2dc3f53d4fbfa4b3a6b5bbdcb0

Generated: 2026-05-10T06:24:17.632Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `e65017b0f98f3f2dc3f53d4fbfa4b3a6b5bbdcb0` |
| Release ref input | `e65017b0f98f3f2dc3f53d4fbfa4b3a6b5bbdcb0` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `e65017b0f98f3f2dc3f53d4fbfa4b3a6b5bbdcb0` |
| Release ref SHA | `e65017b0f98f3f2dc3f53d4fbfa4b3a6b5bbdcb0` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/e65017b0f98f-1778390222` | `e65017b0f98f` | 1h 6m 48s | 1h 29m 27s | 1h 6m 14s | [25620598794](https://github.com/openclaw/openclaw/actions/runs/25620598794) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/e65017b0f98f-1778390222` | `e65017b0f98f` | 3m 12s | 1h 8m 5s | 2m 38s | [25620603418](https://github.com/openclaw/openclaw/actions/runs/25620603418) | 1 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/e65017b0f98f-1778390222` | `e65017b0f98f` | 1h 5m 21s | 10h 25m 11s | 1h 5m 18s | [25620603693](https://github.com/openclaw/openclaw/actions/runs/25620603693) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/e65017b0f98f-1778390222` | `e65017b0f98f` | 2m 49s | 2m 46s | 3s | [25620661454](https://github.com/openclaw/openclaw/actions/runs/25620661454) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 6m 0s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620598794/job/75206321933) |
| 57m 41s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206667313) |
| 42m 42s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206568723) |
| 26m 51s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431853) |
| 14m 24s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206565855) |
| 13m 33s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206568711) |
| 13m 21s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206432014) |
| 12m 24s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620598794/job/75206321932) |
| 11m 51s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206568720) |
| 11m 50s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206568715) |
| 11m 30s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206568717) |
| 11m 26s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206568714) |
| 3m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620598794/job/75206321927) |
| 3m 21s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620598794/job/75206321926) |
| 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620598794/job/75206483348) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 6m 14s | 33s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620598794/job/75209586872) |
| 1h 5m 18s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75209555852) |
| 15m 37s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75207084427) |
| 7m 55s | 4m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206683957) |
| 7m 55s | 1m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206683964) |
| 7m 55s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206683978) |
| 7m 55s | 2m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206683987) |
| 7m 55s | 5m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206683988) |
| 7m 55s | 5m 4s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206683997) |
| 7m 55s | 5m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206683999) |
| 7m 55s | 1m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206684009) |
| 3m 36s | 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620598794/job/75206483348) |
| 2m 38s | 4s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620603418/job/75206443772) |
| 1m 57s | 3s | `normal-ci` | check | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620603418/job/75206415104) |
| 1m 54s | 2s | `normal-ci` | check-additional | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620603418/job/75206412374) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25620598794
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25620598794/job/75209586872
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25620603418
  - build-artifacts: failure - https://github.com/openclaw/openclaw/actions/runs/25620603418/job/75206336280
  - check-test-types: failure - https://github.com/openclaw/openclaw/actions/runs/25620603418/job/75206336327
  - checks-node-auto-reply-reply-state-routing: failure - https://github.com/openclaw/openclaw/actions/runs/25620603418/job/75206336440
  - build-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25620603418/job/75206389906
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25620603418/job/75206412374
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25620603418/job/75206415104
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25620603418/job/75206443772
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431964
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431966
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431974
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431979
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431984
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431985
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431989
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431992
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431993
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431994
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431995
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206431999
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-xai, Native live xAI plugin, node .release-...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206432009
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206432014
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206432018
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206432021
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206565848
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206565853
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206565854
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206565857
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206565858
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206565859
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206565864
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75206667313
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25620603693/job/75209555852

## Notes

Automatically requested by Full Release Validation 25620598794 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


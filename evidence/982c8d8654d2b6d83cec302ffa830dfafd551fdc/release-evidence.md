# OpenClaw Release Evidence: 982c8d8654d2b6d83cec302ffa830dfafd551fdc

Generated: 2026-05-06T11:07:59.670Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `982c8d8654d2b6d83cec302ffa830dfafd551fdc` |
| Release ref input | `982c8d8654d2b6d83cec302ffa830dfafd551fdc` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `982c8d8654d2b6d83cec302ffa830dfafd551fdc` |
| Release ref SHA | `982c8d8654d2b6d83cec302ffa830dfafd551fdc` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/982c8d8654d2-1778064540693` | `982c8d8654d2` | 18m 35s | 42m 29s | 18m 6s | [25430812061](https://github.com/openclaw/openclaw/actions/runs/25430812061) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/982c8d8654d2-1778064540693` | `982c8d8654d2` | 5m 15s | 1h 24m 54s | 5m 11s | [25430837626](https://github.com/openclaw/openclaw/actions/runs/25430837626) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/982c8d8654d2-1778064540693` | `982c8d8654d2` | 18m 5s | 8h 3m 51s | 18m 1s | [25430838698](https://github.com/openclaw/openclaw/actions/runs/25430838698) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/982c8d8654d2-1778064540693` | `982c8d8654d2` | 1m 49s | 1m 34s | 14s | [25430936253](https://github.com/openclaw/openclaw/actions/runs/25430936253) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 17m 25s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430812061/job/74596322660) |
| 15m 23s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709413) |
| 15m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709841) |
| 14m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709835) |
| 14m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709826) |
| 14m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709855) |
| 14m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709787) |
| 14m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709810) |
| 14m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709812) |
| 14m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709814) |
| 14m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709825) |
| 13m 58s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430812061/job/74596322661) |
| 5m 45s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430812061/job/74596322655) |
| 3m 44s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430837626/job/74596416202) |
| 2m 39s | `normal-ci` | checks-node-core-runtime-infra-state | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430837626/job/74596416622) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 18m 6s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25430812061/job/74598958604) |
| 18m 1s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74599044540) |
| 17m 25s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598971165) |
| 12m 43s | 1m 37s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598074913) |
| 12m 42s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598055891) |
| 12m 42s | 1m 54s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598074880) |
| 12m 42s | 2m 14s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598074882) |
| 12m 42s | 2m 27s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598074899) |
| 12m 42s | 1m 20s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598074901) |
| 12m 42s | 1m 50s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598074910) |
| 12m 42s | 1m 32s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598074918) |
| 5m 11s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430837626/job/74597133068) |
| 4m 16s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430837626/job/74596994985) |
| 4m 5s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430837626/job/74596951592) |
| 4m 5s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25430837626/job/74596951612) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430812061
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430812061/job/74596322660
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25430812061/job/74598958604
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709413
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709777
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709786
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709787
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709810
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709812
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709814
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709825
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709826
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709833
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709835
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709838
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709841
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709855
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596709888
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74596980969
  - Run repo/live E2E validation / Docker live models (Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597035946
  - Run repo/live E2E validation / Docker live models (OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597035952
  - Run repo/live E2E validation / Docker live models (Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597035957
  - Run repo/live E2E validation / Docker live models (xAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597035962
  - Run repo/live E2E validation / Docker live models (MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597035970
  - Run repo/live E2E validation / Docker live models (OpenCode): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597035979
  - Run repo/live E2E validation / Docker live models (Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597035981
  - Run repo/live E2E validation / Docker live models (Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036003
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036022
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036025
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036037
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036048
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036058
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036062
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036074
  - Run repo/live E2E validation / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036095
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036136
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74597036201
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598055892
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74598971165
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25430838698/job/74599044540

## Notes

Automatically requested by Full Release Validation 25430812061 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


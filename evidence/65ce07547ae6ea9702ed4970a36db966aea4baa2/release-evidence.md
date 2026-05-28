# OpenClaw Release Evidence: 65ce07547ae6ea9702ed4970a36db966aea4baa2

Generated: 2026-05-06T11:22:52.165Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `65ce07547ae6ea9702ed4970a36db966aea4baa2` |
| Release ref input | `65ce07547ae6ea9702ed4970a36db966aea4baa2` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `65ce07547ae6ea9702ed4970a36db966aea4baa2` |
| Release ref SHA | `65ce07547ae6ea9702ed4970a36db966aea4baa2` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/65ce07547ae6-1778065671152` | `65ce07547ae6` | 14m 28s | 14m 5s | 14m 11s | [25431637307](https://github.com/openclaw/openclaw/actions/runs/25431637307) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/65ce07547ae6-1778065671152` | `65ce07547ae6` | 14m 14s | 6h 37m 2s | 14m 10s | [25431662009](https://github.com/openclaw/openclaw/actions/runs/25431662009) | 36 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 13m 41s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74599139302) |
| 11m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533042) |
| 11m 11s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599532990) |
| 11m 11s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533025) |
| 11m 11s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533075) |
| 11m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599532930) |
| 11m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599532971) |
| 11m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533016) |
| 11m 9s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599532354) |
| 11m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533010) |
| 11m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533047) |
| 16s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74601172083) |
| 8s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74599095102) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74599139857) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74599139962) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 14m 11s | 16s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74601172083) |
| 14m 10s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74601255577) |
| 13m 42s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74601186236) |
| 10m 34s | 2m 52s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74600553929) |
| 10m 34s | 1m 49s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74600553930) |
| 10m 34s | 1m 20s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74600553935) |
| 10m 34s | 1m 14s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74600553944) |
| 10m 34s | 1m 49s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74600553951) |
| 10m 34s | 1m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74600596021) |
| 10m 34s | 1m 28s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74600596023) |
| 10m 34s | 1m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74600596024) |
| 27s | 13m 41s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74599139302) |
| 19s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74599139857) |
| 19s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74599139962) |
| 19s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74599139996) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431637307
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74599139302
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25431637307/job/74601172083
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599532354
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599532930
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599532971
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599532975
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599532990
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533010
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533011
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533016
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533017
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533025
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533042
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533047
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533068
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533075
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599533104
  - Run repo/live E2E validation / Docker live models (Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803771
  - Run repo/live E2E validation / Docker live models (OpenCode): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803778
  - Run repo/live E2E validation / Docker live models (MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803781
  - Run repo/live E2E validation / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803788
  - Run repo/live E2E validation / Docker live models (OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803790
  - Run repo/live E2E validation / Docker live models (Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803792
  - Run repo/live E2E validation / Docker live models (Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803795
  - Run repo/live E2E validation / Docker live models (xAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803802
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803815
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803820
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803823
  - Run repo/live E2E validation / Docker live models (Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803828
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803838
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803839
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803869
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803888
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803890
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599803921
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599839109
  - cross_os_release_checks / Windows / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599839112
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74599839113
  - Run Docker release-path validation / Docker E2E (plugins/runtime install A): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74600553929
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74600596027
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74601186236
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25431662009/job/74601255577

## Notes

Automatically requested by Full Release Validation 25431637307 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 1d8add1c98240974e29806b4552bc054cb962be2

Generated: 2026-05-09T16:33:31.839Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `1d8add1c98240974e29806b4552bc054cb962be2` |
| Release ref input | `1d8add1c98240974e29806b4552bc054cb962be2` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `1d8add1c98240974e29806b4552bc054cb962be2` |
| Release ref SHA | `1d8add1c98240974e29806b4552bc054cb962be2` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/1d8add1c9824-1778343948677` | `1d8add1c9824` | 7m 20s | 25m 42s | 6m 51s | [25605946042](https://github.com/openclaw/openclaw/actions/runs/25605946042) | 1 |
| running | blocking | `normal-ci` | CI | `release-ci/1d8add1c9824-1778343948677` | `1d8add1c9824` | 5m 56s | 1h 18m 57s | 6m 13s | [25605955174](https://github.com/openclaw/openclaw/actions/runs/25605955174) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/1d8add1c9824-1778343948677` | `1d8add1c9824` | 6m 36s | 2h 35m 7s | 6m 32s | [25605955343](https://github.com/openclaw/openclaw/actions/runs/25605955343) | 17 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/1d8add1c9824-1778343948677` | `1d8add1c9824` | 3m 12s | 2m 59s | 12s | [25606010729](https://github.com/openclaw/openclaw/actions/runs/25606010729) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 6m 14s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605946042/job/75167762745) |
| 6m 14s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605946042/job/75167762764) |
| 6m 8s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605946042/job/75167762757) |
| 5m 56s | `normal-ci` | checks-node-agentic-control-plane-runtime | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955174/job/75167783776) |
| 3m 56s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167897916) |
| 3m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605946042/job/75167912941) |
| 3m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898121) |
| 3m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898136) |
| 3m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898139) |
| 3m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898143) |
| 3m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898149) |
| 3m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898190) |
| 3m 43s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898129) |
| 3m 43s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898135) |
| 3m 43s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898171) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6m 51s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25605946042/job/75168135725) |
| 6m 32s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168141239) |
| 6m 13s | 0s | `normal-ci` | checks-node-core | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955174/job/75168124058) |
| 6m 8s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168119691) |
| 6m 8s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168119711) |
| 6m 8s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168119732) |
| 6m 2s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168112367) |
| 5m 58s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / plan_docker_lane_groups | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168109961) |
| 5m 58s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / prepare_live_test_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168109989) |
| 5m 58s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / prepare_docker_e2e_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110071) |
| 5m 58s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110078) |
| 5m 58s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / validate_repo_e2e | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110098) |
| 2m 59s | 3m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605946042/job/75167912941) |
| 2m 5s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605955174/job/75167884926) |
| 2m 3s | 4s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25605955174/job/75167883456) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605946042
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605946042/job/75167762745
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605946042/job/75167762757
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605946042/job/75167762764
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25605946042/job/75168135725
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167897916
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898121
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898129
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898131
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898134
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898135
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898136
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898139
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898143
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898149
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898171
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167898190
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167963144
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167978649
  - Run repo/live E2E validation / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167978650
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167978653
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167978656
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167978658
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75167978660
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168023821
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168023825
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168023828
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168023829
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168023830
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168023831
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168023838
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168023839
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168023840
  - Run Docker release-path validation / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168061537
  - Run package acceptance / Docker product acceptance / validate_selected_ref: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168069293
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168069357
  - Run package acceptance / Docker product acceptance / plan_docker_lane_groups: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168109961
  - Run package acceptance / Docker product acceptance / prepare_live_test_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168109989
  - Run package acceptance / Docker product acceptance / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110071
  - Run package acceptance / Docker product acceptance / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110078
  - Run package acceptance / Docker product acceptance / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110098
  - Run package acceptance / Docker product acceptance / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110112
  - Run package acceptance / Docker product acceptance / validate_special_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110115
  - Run package acceptance / Docker product acceptance / Live media suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110118
  - Run package acceptance / Docker product acceptance / Docker live suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110120
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110121
  - Run package acceptance / Docker product acceptance / validate_live_provider_suites: cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110126
  - Run package acceptance / Docker product acceptance / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110137
  - Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110228
  - Run package acceptance / Docker product acceptance / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168110260
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168112367
  - Run Docker release-path validation / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168119691
  - Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168119711
  - Run Docker release-path validation / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168119732
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25605955343/job/75168141239

## Notes

Automatically requested by Full Release Validation 25605946042 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


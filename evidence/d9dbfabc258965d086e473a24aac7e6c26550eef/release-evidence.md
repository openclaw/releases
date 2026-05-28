# OpenClaw Release Evidence: d9dbfabc258965d086e473a24aac7e6c26550eef

Generated: 2026-05-10T04:49:02.879Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `d9dbfabc258965d086e473a24aac7e6c26550eef` |
| Release ref input | `d9dbfabc258965d086e473a24aac7e6c26550eef` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `d9dbfabc258965d086e473a24aac7e6c26550eef` |
| Release ref SHA | `d9dbfabc258965d086e473a24aac7e6c26550eef` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/d9dbfabc2589-1778388100000` | `d9dbfabc2589` | 7m 43s | 21m 37s | 7m 16s | [25619996248](https://github.com/openclaw/openclaw/actions/runs/25619996248) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/d9dbfabc2589-1778388100000` | `d9dbfabc2589` | 3m 10s | 1h 11m 19s | 2m 43s | [25620002482](https://github.com/openclaw/openclaw/actions/runs/25620002482) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/d9dbfabc2589-1778388100000` | `d9dbfabc2589` | 6m 4s | 1h 39m 4s | 6m 1s | [25620004128](https://github.com/openclaw/openclaw/actions/runs/25620004128) | 6 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/d9dbfabc2589-1778388100000` | `d9dbfabc2589` | 3m 9s | 2m 53s | 15s | [25620060757](https://github.com/openclaw/openclaw/actions/runs/25620060757) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 19s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619996248/job/75204753201) |
| 5m 11s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619996248/job/75204753180) |
| 3m 41s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619996248/job/75204753190) |
| 3m 32s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619996248/job/75204753184) |
| 3m 23s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204815154) |
| 3m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619996248/job/75204911405) |
| 2m 53s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620002482/job/75204768399) |
| 2m 53s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620060757/job/75204916501) |
| 2m 50s | `release-checks` | Run QA Lab parity lane (candidate) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204815173) |
| 2m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868410) |
| 2m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868398) |
| 2m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868401) |
| 2m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868405) |
| 2m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868409) |
| 2m 47s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868403) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 7m 16s | 26s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619996248/job/75205060115) |
| 6m 1s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75205030065) |
| 5m 0s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984923) |
| 4m 59s |  | `release-checks` | Run package acceptance / Telegram package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984916) |
| 4m 59s |  | `release-checks` | Run package acceptance / Docker product acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204985010) |
| 4m 58s |  | `release-checks` | Run Docker release-path validation / plan_docker_lane_groups | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984057) |
| 4m 58s |  | `release-checks` | Run Docker release-path validation / prepare_docker_e2e_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984062) |
| 4m 58s |  | `release-checks` | Run Docker release-path validation / validate_special_e2e | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984106) |
| 4m 58s |  | `release-checks` | Run Docker release-path validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984116) |
| 4m 58s |  | `release-checks` | Run Docker release-path validation / validate_live_provider_suites | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984144) |
| 4m 58s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984153) |
| 3m 52s | 3m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619996248/job/75204911405) |
| 2m 43s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620002482/job/75204876705) |
| 2m 31s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620002482/job/75204866975) |
| 2m 31s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620002482/job/75204866980) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619996248
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619996248/job/75204753180
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619996248/job/75204753201
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25619996248/job/75205060115
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128
  - install_smoke_release_checks / root_dockerfile_image: failure - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204824133
  - Run repo/live E2E validation / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868269
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868274
  - Run repo/live E2E validation / Live media suites (Native live media video plugins B): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868315
  - Run repo/live E2E validation / Live media suites (Native live media video plugins C): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868340
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868394
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868398
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868401
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868403
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868405
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868406
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868409
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868410
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868411
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868412
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868413
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868417
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868418
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868419
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868421
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204868426
  - Run QA Lab parity report: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204945102
  - Run repo/live E2E validation / Docker live models (MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968558
  - Run repo/live E2E validation / Docker live models (Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968560
  - Run repo/live E2E validation / Docker live models (xAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968561
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968562
  - Run repo/live E2E validation / Docker live models (Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968563
  - Run repo/live E2E validation / Docker live models (Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968564
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968565
  - Run repo/live E2E validation / Docker live models (OpenCode): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968566
  - Run repo/live E2E validation / Docker live models (OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968567
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968568
  - Run repo/live E2E validation / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968571
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968572
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968573
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968574
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968575
  - Run repo/live E2E validation / Docker live models (Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968576
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968579
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968580
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204968582
  - Run Docker release-path validation / validate_selected_ref: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204969465
  - Run package acceptance / Resolve package candidate: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204969548
  - cross_os_release_checks / prepare: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204969566
  - cross_os_release_checks / ${{ matrix.display_name }} / ${{ matrix.suite_label }}: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204983807
  - Run Docker release-path validation / plan_docker_lane_groups: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984057
  - Run Docker release-path validation / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984062
  - Run Docker release-path validation / validate_special_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984106
  - Run Docker release-path validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984116
  - Run Docker release-path validation / validate_live_provider_suites: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984144
  - Run Docker release-path validation / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984153
  - Run Docker release-path validation / prepare_live_test_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984156
  - Run Docker release-path validation / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984160
  - Run Docker release-path validation / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984178
  - Run Docker release-path validation / Live media suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984182
  - Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984214
  - Run Docker release-path validation / Docker live suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984280
  - Run Docker release-path validation / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984301
  - Run Docker release-path validation / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984326
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75204984923
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25620004128/job/75205030065

## Notes

Automatically requested by Full Release Validation 25619996248 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


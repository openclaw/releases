# OpenClaw Release Evidence: 83427ee9e7b252b922a48f5ddbfc4113120076c5

Generated: 2026-05-10T04:23:36.434Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `83427ee9e7b252b922a48f5ddbfc4113120076c5` |
| Release ref input | `83427ee9e7b252b922a48f5ddbfc4113120076c5` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `83427ee9e7b252b922a48f5ddbfc4113120076c5` |
| Release ref SHA | `83427ee9e7b252b922a48f5ddbfc4113120076c5` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/83427ee9e7b2-1778386543821` | `83427ee9e7b2` | 7m 34s | 24m 15s | 7m 2s | [25619571585](https://github.com/openclaw/openclaw/actions/runs/25619571585) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/83427ee9e7b2-1778386543821` | `83427ee9e7b2` | 3m 12s | 1h 12m 42s | 3m 8s | [25619578131](https://github.com/openclaw/openclaw/actions/runs/25619578131) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/83427ee9e7b2-1778386543821` | `83427ee9e7b2` | 7m 17s | 2h 47m 45s | 7m 14s | [25619578666](https://github.com/openclaw/openclaw/actions/runs/25619578666) | 17 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/83427ee9e7b2-1778386543821` | `83427ee9e7b2` | 3m 3s | 2m 46s | 16s | [25619634857](https://github.com/openclaw/openclaw/actions/runs/25619634857) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 6m 34s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619571585/job/75203606606) |
| 6m 33s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619571585/job/75203606607) |
| 4m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727755) |
| 4m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727794) |
| 4m 13s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727679) |
| 4m 13s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727762) |
| 4m 13s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727784) |
| 4m 13s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727795) |
| 4m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727759) |
| 4m 1s | `release-checks` | Run repo/live E2E validation / Live media suites (Native live media video plugins D) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727703) |
| 3m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727745) |
| 3m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727758) |
| 3m 44s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619571585/job/75203606600) |
| 3m 21s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619571585/job/75203606603) |
| 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619571585/job/75203756887) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 7m 14s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203944827) |
| 7m 2s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619571585/job/75203919600) |
| 6m 51s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203930557) |
| 6m 44s |  | `release-checks` | Run Docker release-path validation / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203925850) |
| 6m 44s |  | `release-checks` | Run Docker release-path validation / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203925865) |
| 6m 44s |  | `release-checks` | Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203925868) |
| 6m 40s |  | `release-checks` | Run package acceptance / Docker product acceptance / validate_repo_e2e | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922469) |
| 6m 40s |  | `release-checks` | Run package acceptance / Docker product acceptance / prepare_docker_e2e_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922551) |
| 6m 40s |  | `release-checks` | Run package acceptance / Docker product acceptance / validate_special_e2e | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922553) |
| 6m 40s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922564) |
| 6m 40s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922612) |
| 3m 40s | 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619571585/job/75203756887) |
| 3m 8s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619578131/job/75203748376) |
| 3m 5s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619578131/job/75203745213) |
| 3m 5s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619578131/job/75203745226) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619571585
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619571585/job/75203606606
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619571585/job/75203606607
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25619571585/job/75203919600
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25619578131
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25619578131/job/75203745243
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25619578131/job/75203748376
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727679
  - Run repo/live E2E validation / Live media suites (Native live media video plugins D): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727703
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727745
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727755
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727758
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727759
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727762
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727784
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-infra, Native live infra, OPENCLAW_LIVE_APNS_REACH...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727788
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727794
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203727795
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203796598
  - Run repo/live E2E validation / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203824376
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203824389
  - Run repo/live E2E validation / Docker live models (xAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203824398
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203824403
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203824405
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203824410
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203824412
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203824416
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203858667
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203858668
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203858671
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203858672
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203858673
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203858674
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203858675
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203858676
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203858678
  - Run Docker release-path validation / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203889022
  - Run package acceptance / Docker product acceptance / validate_selected_ref: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203892516
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203892532
  - Run package acceptance / Docker product acceptance / prepare_live_test_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922419
  - Run package acceptance / Docker product acceptance / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922420
  - Run package acceptance / Docker product acceptance / plan_docker_lane_groups: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922443
  - Run package acceptance / Docker product acceptance / validate_live_provider_suites: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922457
  - Run package acceptance / Docker product acceptance / Live media suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922465
  - Run package acceptance / Docker product acceptance / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922469
  - Run package acceptance / Docker product acceptance / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922551
  - Run package acceptance / Docker product acceptance / validate_special_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922553
  - Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922564
  - Run package acceptance / Docker product acceptance / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922612
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922625
  - Run package acceptance / Docker product acceptance / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922632
  - Run package acceptance / Docker product acceptance / Docker live suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922652
  - Run package acceptance / Docker product acceptance / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203922673
  - Run Docker release-path validation / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203925850
  - Run Docker release-path validation / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203925865
  - Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203925868
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203930557
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25619578666/job/75203944827

## Notes

Automatically requested by Full Release Validation 25619571585 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


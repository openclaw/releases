# OpenClaw Release Evidence: 40823f757e270861e2cc3bd4f7120bfa8c786995

Generated: 2026-05-09T20:07:11.927Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `40823f757e270861e2cc3bd4f7120bfa8c786995` |
| Release ref input | `40823f757e270861e2cc3bd4f7120bfa8c786995` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `40823f757e270861e2cc3bd4f7120bfa8c786995` |
| Release ref SHA | `40823f757e270861e2cc3bd4f7120bfa8c786995` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/40823f757e27-1778356797148` | `40823f757e27` | 6m 56s | 24m 52s | 6m 24s | [25610464695](https://github.com/openclaw/openclaw/actions/runs/25610464695) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/40823f757e27-1778356797148` | `40823f757e27` | 5m 45s | 1h 16m 34s | 2m 43s | [25610474004](https://github.com/openclaw/openclaw/actions/runs/25610474004) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/40823f757e27-1778356797148` | `40823f757e27` | 6m 23s | 2h 28m 51s | 6m 20s | [25610474229](https://github.com/openclaw/openclaw/actions/runs/25610474229) | 15 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/40823f757e27-1778356797148` | `40823f757e27` | 3m 10s | 2m 57s | 12s | [25610531964](https://github.com/openclaw/openclaw/actions/runs/25610531964) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 6m 7s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610464695/job/75179661902) |
| 6m 6s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610464695/job/75179661899) |
| 6m 6s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610464695/job/75179661921) |
| 5m 29s | `normal-ci` | macos-swift | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474004/job/75179689020) |
| 3m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811378) |
| 3m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811388) |
| 3m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811394) |
| 3m 32s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811211) |
| 3m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811387) |
| 3m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811390) |
| 3m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811392) |
| 3m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811400) |
| 3m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811401) |
| 3m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811389) |
| 3m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610464695/job/75179812450) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6m 24s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25610464695/job/75179994600) |
| 6m 20s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75180003304) |
| 5m 52s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179983583) |
| 5m 50s |  | `release-checks` | Run Docker release-path validation / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179982944) |
| 5m 49s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179982847) |
| 5m 49s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179982865) |
| 5m 46s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / plan_docker_lane_groups | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979610) |
| 5m 46s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / validate_live_provider_suites | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979612) |
| 5m 46s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Live media suites (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979638) |
| 5m 46s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / prepare_docker_e2e_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979665) |
| 5m 46s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker live models (${{ matrix.provider_label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979672) |
| 2m 59s | 3m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610464695/job/75179812450) |
| 2m 43s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610474004/job/75179820350) |
| 2m 8s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610474004/job/75179790804) |
| 2m 7s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25610474004/job/75179791055) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610464695
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610464695/job/75179661899
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610464695/job/75179661902
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610464695/job/75179661921
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25610464695/job/75179994600
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474004
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474004/job/75179689020
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811211
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811378
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811387
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811388
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811389
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811390
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811391
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811392
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811394
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811400
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811401
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811403
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811408
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811415
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179811421
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179869322
  - install_smoke_release_checks / root_dockerfile_smokes: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179869327
  - Run repo/live E2E validation / Docker live models (Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179883192
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179883194
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179883197
  - Run repo/live E2E validation / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179883200
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179883201
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179883205
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179883209
  - Run repo/live E2E validation / Docker live models (MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179883218
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179883222
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179923785
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179923791
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179923793
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179923794
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179923795
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179923799
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179923800
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179923803
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179923808
  - Run package acceptance / Docker product acceptance / validate_selected_ref: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179953692
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179953771
  - Run Docker release-path validation / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179954569
  - Run package acceptance / Docker product acceptance / plan_docker_lane_groups: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979610
  - Run package acceptance / Docker product acceptance / validate_live_provider_suites: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979612
  - Run package acceptance / Docker product acceptance / Live media suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979638
  - Run package acceptance / Docker product acceptance / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979665
  - Run package acceptance / Docker product acceptance / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979672
  - Run package acceptance / Docker product acceptance / prepare_live_test_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979673
  - Run package acceptance / Docker product acceptance / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979684
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979696
  - Run package acceptance / Docker product acceptance / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979697
  - Run package acceptance / Docker product acceptance / validate_special_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979728
  - Run package acceptance / Docker product acceptance / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979763
  - Run package acceptance / Docker product acceptance / Docker live suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979766
  - Run package acceptance / Docker product acceptance / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979769
  - Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179979770
  - Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179982847
  - Run Docker release-path validation / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179982865
  - Run Docker release-path validation / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179982944
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75179983583
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25610474229/job/75180003304

## Notes

Automatically requested by Full Release Validation 25610464695 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


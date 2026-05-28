# OpenClaw Release Evidence: a6639f1f899324dff2b4795addda20c2c31ed36e

Generated: 2026-05-10T00:07:47.429Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `a6639f1f899324dff2b4795addda20c2c31ed36e` |
| Release ref input | `a6639f1f899324dff2b4795addda20c2c31ed36e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `a6639f1f899324dff2b4795addda20c2c31ed36e` |
| Release ref SHA | `a6639f1f899324dff2b4795addda20c2c31ed36e` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/a6639f1f8993-1778371246356` | `a6639f1f8993` | 6m 41s | 20m 58s | 6m 9s | [25615053133](https://github.com/openclaw/openclaw/actions/runs/25615053133) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/a6639f1f8993-1778371246356` | `a6639f1f8993` | 2m 46s | 1h 5m 34s | 2m 40s | [25615059266](https://github.com/openclaw/openclaw/actions/runs/25615059266) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/a6639f1f8993-1778371246356` | `a6639f1f8993` | 5m 57s | 2h 12m 55s | 5m 54s | [25615058940](https://github.com/openclaw/openclaw/actions/runs/25615058940) | 15 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/a6639f1f8993-1778371246356` | `a6639f1f8993` | 3m 1s | 2m 56s | 4s | [25615106787](https://github.com/openclaw/openclaw/actions/runs/25615106787) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 39s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615053133/job/75191465984) |
| 5m 38s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615053133/job/75191465977) |
| 3m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615053133/job/75191592507) |
| 3m 12s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615053133/job/75191465989) |
| 3m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593010) |
| 3m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593030) |
| 3m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593035) |
| 3m 8s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593014) |
| 3m 7s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191592893) |
| 3m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593005) |
| 3m 0s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593048) |
| 2m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593019) |
| 2m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593023) |
| 2m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593025) |
| 2m 56s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615106787/job/75191598617) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6m 9s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615053133/job/75191746276) |
| 5m 54s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191746422) |
| 5m 22s | 7s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726657) |
| 5m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726303) |
| 5m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Live media suites (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726317) |
| 5m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker live models (${{ matrix.provider_label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726348) |
| 5m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726355) |
| 5m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker live suites (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726374) |
| 5m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker live models (selected providers) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726428) |
| 5m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726444) |
| 5m 21s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726546) |
| 2m 49s | 3m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615053133/job/75191592507) |
| 2m 40s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615059266/job/75191601216) |
| 1m 56s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615059266/job/75191565704) |
| 1m 55s | 3s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615059266/job/75191563825) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615053133
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615053133/job/75191465977
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615053133/job/75191465984
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25615053133/job/75191746276
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191592893
  - Run repo/live E2E validation / Live media suites (Native live media video plugins B): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191592910
  - Run repo/live E2E validation / Live media suites (Native live media video plugins C): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191592912
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593005
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593010
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593014
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593019
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593023
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593025
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593030
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593035
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593036
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593037
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593038
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593045
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593047
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191593048
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191639385
  - install_smoke_release_checks / root_dockerfile_smokes: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191639397
  - Run repo/live E2E validation / Docker live models (OpenCode): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650272
  - Run repo/live E2E validation / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650277
  - Run repo/live E2E validation / Docker live models (Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650282
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650286
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650289
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650293
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650299
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650301
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650302
  - Run repo/live E2E validation / Docker live models (Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650303
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650304
  - Run repo/live E2E validation / Docker live models (Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191650314
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191683340
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191683346
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191683348
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191683349
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191683350
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191683351
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191683352
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191683355
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191683364
  - Run package acceptance / Docker product acceptance / validate_selected_ref: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191716872
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191716921
  - Run Docker release-path validation / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191719024
  - Run package acceptance / Docker product acceptance / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726122
  - Run package acceptance / Docker product acceptance / plan_docker_lane_groups: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726191
  - Run package acceptance / Docker product acceptance / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726205
  - Run package acceptance / Docker product acceptance / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726208
  - Run package acceptance / Docker product acceptance / prepare_live_test_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726217
  - Run package acceptance / Docker product acceptance / validate_live_provider_suites: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726281
  - Run package acceptance / Docker product acceptance / validate_special_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726296
  - Run package acceptance / Docker product acceptance / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726303
  - Run package acceptance / Docker product acceptance / Live media suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726317
  - Run package acceptance / Docker product acceptance / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726348
  - Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726355
  - Run package acceptance / Docker product acceptance / Docker live suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726374
  - Run package acceptance / Docker product acceptance / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726428
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726444
  - Run Docker release-path validation / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726546
  - Run Docker release-path validation / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726555
  - Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726650
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191726657
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25615058940/job/75191746422

## Notes

Automatically requested by Full Release Validation 25615053133 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


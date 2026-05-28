# OpenClaw Release Evidence: d3043345ca142f43b45f733e880ca3abb9efd71c

Generated: 2026-05-03T22:25:38.066Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `d3043345ca142f43b45f733e880ca3abb9efd71c` |
| Release ref input | `d3043345ca142f43b45f733e880ca3abb9efd71c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `d3043345ca142f43b45f733e880ca3abb9efd71c` |
| Release ref SHA | `d3043345ca142f43b45f733e880ca3abb9efd71c` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/d3043345ca14-1777846893098` | `d3043345ca14` | 3m 30s | 11m 36s | 3m 7s | [25292493479](https://github.com/openclaw/openclaw/actions/runs/25292493479) | 0 |
| fail | blocking | `normal-ci` | CI | `release-ci/d3043345ca14-1777846893098` | `d3043345ca14` | 2m 42s | 1h 11m 21s | 2m 42s | [25292500901](https://github.com/openclaw/openclaw/actions/runs/25292500901) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/d3043345ca14-1777846893098` | `d3043345ca14` | 3m 28s | 29m 21s | 3m 23s | [25292501397](https://github.com/openclaw/openclaw/actions/runs/25292501397) | 3 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 2m 49s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146280862) |
| 2m 48s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146280867) |
| 2m 47s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146280871) |
| 2m 35s | `full-release-validation` | Prepare release package artifact | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146280859) |
| 2m 25s | `normal-ci` | check-additional-boundaries-a | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299315) |
| 2m 17s | `normal-ci` | checks-node-core-fast | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299441) |
| 2m 5s | `normal-ci` | build-artifacts | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299223) |
| 2m 0s | `normal-ci` | checks-node-core-runtime-infra-process | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299423) |
| 2m 0s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146361372) |
| 1m 57s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299274) |
| 1m 55s | `normal-ci` | checks-node-core-runtime-shared | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299467) |
| 1m 50s | `normal-ci` | checks-fast-contracts-plugins-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299278) |
| 1m 47s | `normal-ci` | checks-windows-node-test | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299263) |
| 1m 47s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299266) |
| 1m 41s | `release-checks` | Run QA Lab parity lane (candidate) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146347136) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 3m 23s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146465673) |
| 3m 21s | 0s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146465632) |
| 3m 21s | 0s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146465636) |
| 3m 21s | 0s | `release-checks` | install_smoke_release_checks / installer_smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146465709) |
| 3m 7s | 22s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146433228) |
| 3m 0s | 4s | `full-release-validation` | Run package Telegram E2E | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146422360) |
| 2m 47s |  | `release-checks` | Run QA Lab parity report | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146435859) |
| 2m 45s | 0s | `release-checks` | cross_os_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146434384) |
| 2m 45s | 0s | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146434407) |
| 2m 45s | 0s | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146434438) |
| 2m 42s | 0s | `normal-ci` | check-additional | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146430842) |
| 2m 36s |  | `release-checks` | Run repo/live E2E validation / Docker live models (${{ matrix.provider_label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146427573) |
| 2m 35s | 0s | `release-checks` | Run repo/live E2E validation / Docker live suites (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146427497) |
| 2m 34s | 0s | `normal-ci` | checks-node-core | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146425011) |
| 2m 29s | 0s | `normal-ci` | build-smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146420952) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292493479
  - Prepare release package artifact: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146280859
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146280862
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146280867
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146280871
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146422360
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25292493479/job/74146433228
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292500901
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299223
  - check-additional-boundaries-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299315
  - checks-node-core-fast: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146299441
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146420952
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146421004
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146421025
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146425011
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292500901/job/74146430842
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397
  - Run QA Lab parity lane (candidate): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146347136
  - Run QA Lab parity lane (baseline): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146347139
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146347140
  - Run QA Lab live Slack lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146347143
  - Prepare release package artifact: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146347144
  - install_smoke_release_checks / root_dockerfile_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146361372
  - Run repo/live E2E validation / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396281
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396284
  - Run repo/live E2E validation / validate_special_e2e (openai-ws-stream-live-e2e, OpenAI WebSocket live E2E, pnpm test:e2e src/age...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396300
  - Run repo/live E2E validation / validate_special_e2e (openshell-e2e, OpenShell repo E2E, pnpm test:e2e:openshell, 120, true, false): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396301
  - Run repo/live E2E validation / prepare_live_test_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396320
  - Run repo/live E2E validation / Live media suites (Native live media music MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396348
  - Run repo/live E2E validation / Live media suites (Native live media music Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396356
  - Run repo/live E2E validation / Live media suites (Native live media video plugins B): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396357
  - Run repo/live E2E validation / Live media suites (Native live media video plugins C): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396370
  - Run repo/live E2E validation / Live media suites (Native live media audio plugins): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396372
  - Run repo/live E2E validation / Live media suites (Native live media video plugins D): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396375
  - Run repo/live E2E validation / Live media suites (Native live plugins A-K): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396384
  - Run repo/live E2E validation / Live media suites (Native live media video plugins A): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396393
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-moonshot, Native live Moonshot plugin, node...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396497
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-backends, Native live gateway backends, no...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396498
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396500
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396506
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396516
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396518
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396519
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-l-n, Native live plugins L-N, node .release...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396523
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-o-z-other, Native live plugins O-Z other, n...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396524
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396525
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396526
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396531
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-core, Native live gateway core, node .rele...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396533
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-xai, Native live xAI plugin, node .release-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396534
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396535
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396536
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396538
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396540
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396541
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396542
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396544
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396545
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146396552
  - Run repo/live E2E validation / Docker live suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146427497
  - Run repo/live E2E validation / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146427518
  - Run repo/live E2E validation / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146427573
  - Run QA Lab parity report: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146435859
  - install_smoke_release_checks / root_dockerfile_smokes: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146465632
  - install_smoke_release_checks / bun_global_install_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146465636
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146465673
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292501397/job/74146465709

## Notes

Automatically requested by Full Release Validation 25292493479 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


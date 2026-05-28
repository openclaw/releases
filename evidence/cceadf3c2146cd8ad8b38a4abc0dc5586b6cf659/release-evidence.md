# OpenClaw Release Evidence: cceadf3c2146cd8ad8b38a4abc0dc5586b6cf659

Generated: 2026-05-09T19:29:02.130Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `cceadf3c2146cd8ad8b38a4abc0dc5586b6cf659` |
| Release ref input | `cceadf3c2146cd8ad8b38a4abc0dc5586b6cf659` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `cceadf3c2146cd8ad8b38a4abc0dc5586b6cf659` |
| Release ref SHA | `cceadf3c2146cd8ad8b38a4abc0dc5586b6cf659` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 3 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/cceadf3c2146-1778354516570` | `cceadf3c2146` | 6m 48s | 21m 51s | 6m 17s | [25609695674](https://github.com/openclaw/openclaw/actions/runs/25609695674) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/cceadf3c2146-1778354516570` | `cceadf3c2146` | 4m 43s | 1h 23m 3s | 4m 43s | [25609704063](https://github.com/openclaw/openclaw/actions/runs/25609704063) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/cceadf3c2146-1778354516570` | `cceadf3c2146` | 5m 32s | 1h 46m 27s | 5m 29s | [25609704435](https://github.com/openclaw/openclaw/actions/runs/25609704435) | 8 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/cceadf3c2146-1778354516570` | `cceadf3c2146` | 2m 55s | 2m 40s | 14s | [25609755495](https://github.com/openclaw/openclaw/actions/runs/25609755495) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 5s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609695674/job/75177665325) |
| 5m 4s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609695674/job/75177665322) |
| 5m 4s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609695674/job/75177665344) |
| 4m 29s | `normal-ci` | macos-node | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177682885) |
| 4m 29s | `normal-ci` | macos-swift | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177682899) |
| 4m 29s | `normal-ci` | checks-node-auto-reply-core-top-level | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177683073) |
| 3m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609695674/job/75177802780) |
| 3m 7s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177682914) |
| 2m 51s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177741500) |
| 2m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798832) |
| 2m 44s | `normal-ci` | android-test-third-party | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177682916) |
| 2m 40s | `postpublish-telegram` | Run package Telegram E2E | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609755495/job/75177809392) |
| 2m 36s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798803) |
| 2m 36s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798810) |
| 2m 36s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798817) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6m 17s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609695674/job/75177984009) |
| 5m 29s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177964153) |
| 5m 7s |  | `release-checks` | Run Docker release-path validation / prepare_docker_e2e_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945633) |
| 5m 7s |  | `release-checks` | Run Docker release-path validation / validate_special_e2e | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945658) |
| 5m 7s |  | `release-checks` | Run Docker release-path validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945661) |
| 5m 7s |  | `release-checks` | Run Docker release-path validation / plan_docker_lane_groups | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945668) |
| 5m 7s |  | `release-checks` | Run Docker release-path validation / prepare_live_test_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945707) |
| 5m 7s |  | `release-checks` | Run Docker release-path validation / validate_live_provider_suites | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945713) |
| 5m 7s |  | `release-checks` | Run Docker release-path validation / Live media suites (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945735) |
| 5m 7s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945844) |
| 5m 7s | 0s | `release-checks` | Run Docker release-path validation / Docker live models (selected providers) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945869) |
| 4m 43s | 0s | `normal-ci` | checks-node-core | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177922937) |
| 2m 57s | 3m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609695674/job/75177802780) |
| 2m 34s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177799608) |
| 1m 52s | 3s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177769031) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609695674
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609695674/job/75177665322
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609695674/job/75177665325
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609695674/job/75177665344
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25609695674/job/75177984009
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704063
  - checks-windows-node-test: failure - https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177682877
  - macos-node: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177682885
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177682899
  - checks-node-auto-reply-core-top-level: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177683073
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704063/job/75177922937
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798671
  - Run repo/live E2E validation / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798673
  - Run repo/live E2E validation / Live media suites (Native live media video plugins B): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798718
  - Run repo/live E2E validation / Live media suites (Native live media video plugins C): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798721
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798795
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798796
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798803
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798804
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798810
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798811
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798812
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798814
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798815
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798817
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798822
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798823
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798824
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798828
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798832
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177798843
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177865636
  - install_smoke_release_checks / root_dockerfile_smokes: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177865637
  - Run repo/live E2E validation / Docker live models (OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888832
  - Run repo/live E2E validation / Docker live models (MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888835
  - Run repo/live E2E validation / Docker live models (Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888838
  - Run repo/live E2E validation / Docker live models (Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888839
  - Run repo/live E2E validation / Docker live models (OpenCode): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888840
  - Run repo/live E2E validation / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888842
  - Run repo/live E2E validation / Docker live models (xAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888843
  - Run repo/live E2E validation / Docker live models (Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888844
  - Run repo/live E2E validation / Docker live models (Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888862
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888863
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888865
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888867
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888869
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888870
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888871
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888873
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888875
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888878
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177888887
  - Run Docker release-path validation / validate_selected_ref: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177895537
  - Run package acceptance / Resolve package candidate: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177895693
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177915524
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177915525
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177915527
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177915532
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177915534
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177915536
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177915537
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177915539
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177915541
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177926182
  - Run Docker release-path validation / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945633
  - Run Docker release-path validation / validate_special_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945658
  - Run Docker release-path validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945661
  - Run Docker release-path validation / plan_docker_lane_groups: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945668
  - Run Docker release-path validation / prepare_live_test_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945707
  - Run Docker release-path validation / validate_live_provider_suites: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945713
  - Run Docker release-path validation / Live media suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945735
  - Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945844
  - Run Docker release-path validation / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945869
  - Run Docker release-path validation / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945874
  - Run Docker release-path validation / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945916
  - Run Docker release-path validation / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945917
  - Run Docker release-path validation / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945950
  - Run Docker release-path validation / Docker live suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177945966
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25609704435/job/75177964153
- `postpublish-telegram`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609755495
  - Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609755495/job/75177809392

## Notes

Automatically requested by Full Release Validation 25609695674 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


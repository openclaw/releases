# OpenClaw Release Evidence: 81fabbb17689f94512be076178321d7648c2b916

Generated: 2026-05-09T19:23:02.768Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `81fabbb17689f94512be076178321d7648c2b916` |
| Release ref input | `81fabbb17689f94512be076178321d7648c2b916` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `81fabbb17689f94512be076178321d7648c2b916` |
| Release ref SHA | `81fabbb17689f94512be076178321d7648c2b916` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/81fabbb17689-1778354030092` | `81fabbb17689` | 8m 46s | 30m 23s | 8m 18s | [25609537275](https://github.com/openclaw/openclaw/actions/runs/25609537275) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/81fabbb17689-1778354030092` | `81fabbb17689` | 7m 39s | 1h 19m 32s | 2m 44s | [25609543425](https://github.com/openclaw/openclaw/actions/runs/25609543425) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/81fabbb17689-1778354030092` | `81fabbb17689` | 8m 21s | 3h 8m 49s | 8m 17s | [25609543643](https://github.com/openclaw/openclaw/actions/runs/25609543643) | 17 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/81fabbb17689-1778354030092` | `81fabbb17689` | 3m 8s | 2m 52s | 15s | [25609595898](https://github.com/openclaw/openclaw/actions/runs/25609595898) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 8m 0s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609537275/job/75177241210) |
| 7m 59s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609537275/job/75177241245) |
| 7m 49s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609537275/job/75177241258) |
| 7m 21s | `normal-ci` | macos-swift | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543425/job/75177260506) |
| 5m 38s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369677) |
| 5m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369891) |
| 5m 28s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369952) |
| 5m 16s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369899) |
| 4m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369889) |
| 4m 43s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369857) |
| 4m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369880) |
| 4m 28s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369879) |
| 4m 24s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369931) |
| 4m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369863) |
| 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609537275/job/75177382091) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 8m 18s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609537275/job/75177657919) |
| 8m 17s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177676456) |
| 7m 58s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177659626) |
| 7m 44s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177648861) |
| 7m 44s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177648863) |
| 7m 44s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177648973) |
| 7m 42s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177646839) |
| 7m 42s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177646888) |
| 7m 42s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177646933) |
| 6m 27s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / prepare_docker_e2e_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177570046) |
| 6m 18s | 8s | `release-checks` | Run package acceptance / Docker product acceptance / plan_docker_lane_groups | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177570045) |
| 2m 56s | 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609537275/job/75177382091) |
| 2m 44s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609543425/job/75177390291) |
| 2m 34s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609543425/job/75177376706) |
| 2m 6s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25609543425/job/75177352841) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609537275
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609537275/job/75177241210
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609537275/job/75177241245
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609537275/job/75177241258
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25609537275/job/75177657919
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543425
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543425/job/75177260506
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369677
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369891
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369899
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177369952
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177443354
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177443362
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177472665
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177472668
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177472671
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177472672
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177472673
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177472674
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177472678
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177472691
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177472695
  - Run Docker release-path validation / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177510600
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177510906
  - Run package acceptance / Docker product acceptance / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177570046
  - Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177646839
  - Run Docker release-path validation / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177646888
  - Run Docker release-path validation / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177646933
  - Run package acceptance / Docker product acceptance / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177648861
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177648863
  - Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177648973
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177659626
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25609543643/job/75177676456

## Notes

Automatically requested by Full Release Validation 25609537275 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


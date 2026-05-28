# OpenClaw Release Evidence: 0ccc408132843c92c702accead01a7f1320911e0

Generated: 2026-05-10T04:30:02.996Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `0ccc408132843c92c702accead01a7f1320911e0` |
| Release ref input | `0ccc408132843c92c702accead01a7f1320911e0` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `0ccc408132843c92c702accead01a7f1320911e0` |
| Release ref SHA | `0ccc408132843c92c702accead01a7f1320911e0` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/0ccc40813284-1778387000000` | `0ccc40813284` | 7m 27s | 20m 14s | 6m 59s | [25619681923](https://github.com/openclaw/openclaw/actions/runs/25619681923) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/0ccc40813284-1778387000000` | `0ccc40813284` | 2m 51s | 1h 9m 11s | 2m 47s | [25619687759](https://github.com/openclaw/openclaw/actions/runs/25619687759) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/0ccc40813284-1778387000000` | `0ccc40813284` | 5m 1s | 1h 27m 58s | 4m 57s | [25619687908](https://github.com/openclaw/openclaw/actions/runs/25619687908) | 5 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/0ccc40813284-1778387000000` | `0ccc40813284` | 3m 7s | 2m 47s | 19s | [25619746806](https://github.com/openclaw/openclaw/actions/runs/25619746806) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 4m 53s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619681923/job/75203905729) |
| 4m 53s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619681923/job/75203905739) |
| 3m 29s | `release-checks` | Prepare release package artifact | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75203976809) |
| 3m 23s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619681923/job/75203905753) |
| 3m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619681923/job/75204072702) |
| 3m 11s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619681923/job/75203905728) |
| 3m 1s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75203976816) |
| 2m 50s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75203976806) |
| 2m 47s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619746806/job/75204079265) |
| 2m 34s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75203983173) |
| 2m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032183) |
| 2m 24s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619687759/job/75203923536) |
| 2m 24s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032176) |
| 2m 24s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032189) |
| 2m 24s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032196) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6m 59s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619681923/job/75204228520) |
| 4m 57s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204151277) |
| 4m 50s | 0s | `release-checks` | cross_os_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204146919) |
| 4m 50s | 0s | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204146970) |
| 4m 50s | 0s | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204146978) |
| 4m 35s | 0s | `release-checks` | Run repo/live E2E validation / Docker live models (${{ matrix.provider_label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204134594) |
| 4m 35s | 0s | `release-checks` | Run repo/live E2E validation / Docker live models (selected providers) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204134654) |
| 4m 35s | 0s | `release-checks` | Run repo/live E2E validation / Docker live suites (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204134660) |
| 4m 4s | 50s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204110205) |
| 4m 4s | 35s | `release-checks` | install_smoke_release_checks / installer_smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204110210) |
| 4m 4s | 51s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204110215) |
| 3m 40s | 3m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619681923/job/75204072702) |
| 2m 47s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619687759/job/75204045178) |
| 2m 43s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619687759/job/75204041105) |
| 2m 43s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619687759/job/75204041108) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619681923
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619681923/job/75203905729
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619681923/job/75203905739
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25619681923/job/75204228520
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25619687759
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25619687759/job/75204041129
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25619687759/job/75204045178
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908
  - Prepare release package artifact: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75203976809
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032047
  - Run repo/live E2E validation / prepare_live_test_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032048
  - Run repo/live E2E validation / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032064
  - Run repo/live E2E validation / Live media suites (Native live media video plugins C): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032076
  - Run repo/live E2E validation / Live media suites (Native live media music MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032080
  - Run repo/live E2E validation / Live media suites (Native live media video plugins B): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032084
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032167
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032168
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032176
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032180
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032183
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032186
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032189
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032194
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032195
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032196
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032198
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032205
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032206
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032211
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032221
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204032229
  - Run QA Lab parity report: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204083824
  - install_smoke_release_checks / bun_global_install_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204110205
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204110210
  - install_smoke_release_checks / root_dockerfile_smokes: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204110215
  - Run repo/live E2E validation / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204134594
  - Run repo/live E2E validation / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204134654
  - Run repo/live E2E validation / Docker live suites (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204134660
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25619687908/job/75204151277

## Notes

Automatically requested by Full Release Validation 25619681923 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


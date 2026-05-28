# OpenClaw Release Evidence: 07985e70070da3d4cc416bb8e04b834d8239dc9e

Generated: 2026-05-09T22:46:19.611Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `07985e70070da3d4cc416bb8e04b834d8239dc9e` |
| Release ref input | `07985e70070da3d4cc416bb8e04b834d8239dc9e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `07985e70070da3d4cc416bb8e04b834d8239dc9e` |
| Release ref SHA | `07985e70070da3d4cc416bb8e04b834d8239dc9e` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/07985e70070d-1778365849873` | `07985e70070d` | 15m 4s | 40m 11s | 14m 37s | [25613456498](https://github.com/openclaw/openclaw/actions/runs/25613456498) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/07985e70070d-1778365849873` | `07985e70070d` | 3m 54s | 1h 12m 17s | 2m 46s | [25613463070](https://github.com/openclaw/openclaw/actions/runs/25613463070) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/07985e70070d-1778365849873` | `07985e70070d` | 6m 59s | 3h 11m 33s | 6m 58s | [25613462991](https://github.com/openclaw/openclaw/actions/runs/25613462991) | 22 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/07985e70070d-1778365849873` | `07985e70070d` | 3m 41s | 3m 28s | 12s | [25613535220](https://github.com/openclaw/openclaw/actions/runs/25613535220) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 14m 21s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25613456498/job/75187435986) |
| 12m 55s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613456498/job/75187436008) |
| 7m 11s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187553193) |
| 6m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187553181) |
| 5m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187553190) |
| 5m 2s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187663038) |
| 4m 54s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187553185) |
| 4m 53s | `release-checks` | Run QA Lab live Telegram lane | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187500423) |
| 4m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187553201) |
| 4m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187553174) |
| 4m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187553200) |
| 4m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187553142) |
| 4m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613456498/job/75187619259) |
| 4m 13s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613456498/job/75187435982) |
| 3m 50s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613456498/job/75187435997) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 14m 37s | 26s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25613456498/job/75188135857) |
| 6m 58s |  | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187761726) |
| 6m 58s | 1m 11s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187761747) |
| 6m 58s | 1m 40s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187761748) |
| 6m 58s | 1m 37s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187761750) |
| 6m 58s | 1m 43s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187761755) |
| 6m 58s | 1m 57s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187761758) |
| 6m 57s | 4m 6s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187761717) |
| 6m 57s | 1m 49s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187761721) |
| 6m 57s | 1m 27s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187761739) |
| 6m 57s | 1m 18s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613462991/job/75187761741) |
| 4m 7s | 4m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613456498/job/75187619259) |
| 2m 46s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613463070/job/75187573888) |
| 2m 15s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613463070/job/75187548592) |
| 1m 59s | 2s | `normal-ci` | check | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25613463070/job/75187536774) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25613456498
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25613456498/job/75187435986
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25613456498/job/75188135857
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25613463070
  - check-test-types: failure - https://github.com/openclaw/openclaw/actions/runs/25613463070/job/75187455558
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25613463070/job/75187536774
- `postpublish-telegram`: failure - https://github.com/openclaw/openclaw/actions/runs/25613535220
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25613535220/job/75187625589

## Notes

Automatically requested by Full Release Validation 25613456498 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


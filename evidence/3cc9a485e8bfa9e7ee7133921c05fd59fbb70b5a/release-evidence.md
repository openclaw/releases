# OpenClaw Release Evidence: 3cc9a485e8bfa9e7ee7133921c05fd59fbb70b5a

Generated: 2026-05-10T03:44:13.616Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `3cc9a485e8bfa9e7ee7133921c05fd59fbb70b5a` |
| Release ref input | `3cc9a485e8bfa9e7ee7133921c05fd59fbb70b5a` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `3cc9a485e8bfa9e7ee7133921c05fd59fbb70b5a` |
| Release ref SHA | `3cc9a485e8bfa9e7ee7133921c05fd59fbb70b5a` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/3cc9a485e8bf-1778383792113` | `3cc9a485e8bf` | 13m 51s (+1m 14s) | 20m 13s (-13m 47s) | 13m 28s | [25618772024](https://github.com/openclaw/openclaw/actions/runs/25618772024) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/3cc9a485e8bf-1778383792113` | `3cc9a485e8bf` | 2m 50s (-3m 22s) | 1h 7m 19s (-4m 28s) | 2m 47s | [25618804188](https://github.com/openclaw/openclaw/actions/runs/25618804188) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/3cc9a485e8bf-1778383792113` | `3cc9a485e8bf` | 7m 52s (-3m 37s) | 2h 24m 49s (-2h 24m 9s) | 12m 37s | [25618804442](https://github.com/openclaw/openclaw/actions/runs/25618804442) | 10 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 11m 52s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618772024/job/75201593592) |
| 5m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75201931306) |
| 4m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75201931300) |
| 4m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75201931319) |
| 4m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75201931295) |
| 4m 27s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75201915781) |
| 4m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75201931335) |
| 3m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75201931286) |
| 3m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75201931296) |
| 3m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75201931334) |
| 3m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75201949672) |
| 3m 25s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618772024/job/75201593600) |
| 3m 9s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618772024/job/75201593595) |
| 2m 30s | `normal-ci` | checks-node-core-runtime-shared | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804188/job/75201610366) |
| 2m 7s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804188/job/75201610265) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 13m 28s | 22s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25618772024/job/75202144608) |
| 12m 37s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75202176750) |
| 12m 37s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75202176755) |
| 12m 36s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75202176752) |
| 12m 30s |  | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75202168445) |
| 12m 30s |  | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75202168452) |
| 12m 30s |  | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75202168467) |
| 12m 30s |  | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75202168470) |
| 12m 29s |  | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75202168442) |
| 12m 29s |  | `release-checks` | Run Docker release-path validation / Docker E2E (core) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75202168444) |
| 12m 29s |  | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25618804442/job/75202168461) |
| 5m 1s | 6s | `full-release-validation` | Run package Telegram E2E | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25618772024/job/75201754822) |
| 2m 47s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804188/job/75201727979) |
| 2m 17s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804188/job/75201705416) |
| 2m 17s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25618804188/job/75201705417) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 11m 29s | 7m 52s | -3m 37s | -2h 24m 9s |
| `normal-ci` | 6m 12s | 2m 50s | -3m 22s | -4m 28s |
| `full-release-validation` | 12m 37s | 13m 51s | +1m 14s | -13m 47s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25618772024
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25618772024/job/75201754822
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25618772024/job/75202144608

## Notes

Automatically requested by Full Release Validation 25618772024 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 815af8036367a9774f2ea951275e34d3dd6b5efc

Generated: 2026-05-12T08:29:26.161Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `815af8036367a9774f2ea951275e34d3dd6b5efc` |
| Release ref input | `815af8036367a9774f2ea951275e34d3dd6b5efc` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `815af8036367a9774f2ea951275e34d3dd6b5efc` |
| Release ref SHA | `815af8036367a9774f2ea951275e34d3dd6b5efc` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/815af8036367-1778570980742` | `815af8036367` | 59m 21s | 1h 23m 56s | 58m 44s | [25720108097](https://github.com/openclaw/openclaw/actions/runs/25720108097) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/815af8036367-1778570980742` | `815af8036367` | 3m 36s | 1h 6m 44s | 3m 33s | [25720126159](https://github.com/openclaw/openclaw/actions/runs/25720126159) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/815af8036367-1778570980742` | `815af8036367` | 57m 33s | 14h 47m 31s | 57m 29s | [25720129803](https://github.com/openclaw/openclaw/actions/runs/25720129803) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/815af8036367-1778570980742` | `815af8036367` | 4m 9s | 3m 10s | 59s | [25720275537](https://github.com/openclaw/openclaw/actions/runs/25720275537) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 58m 17s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720108097/job/75519028037) |
| 50m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923954) |
| 50m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519924017) |
| 40m 40s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923976) |
| 35m 58s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923921) |
| 35m 56s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923886) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923892) |
| 35m 51s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923881) |
| 35m 51s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519924010) |
| 35m 49s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923927) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923890) |
| 12m 58s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720108097/job/75519028108) |
| 4m 24s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720108097/job/75519524732) |
| 4m 13s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720108097/job/75519028069) |
| 3m 15s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720108097/job/75519028106) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 58m 44s | 37s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720108097/job/75527967103) |
| 57m 29s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75527845177) |
| 17m 49s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75521668247) |
| 12m 13s | 3m 34s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520787380) |
| 12m 13s | 1m 20s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520787382) |
| 12m 12s | 1m 37s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520787357) |
| 12m 12s | 3m 37s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520787368) |
| 12m 12s | 1m 51s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520787385) |
| 12m 12s | 1m 28s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520787388) |
| 12m 12s | 2m 7s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520787409) |
| 12m 11s | 4m 29s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520787360) |
| 3m 36s | 4m 24s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720108097/job/75519524732) |
| 3m 33s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720126159/job/75519573808) |
| 3m 27s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720126159/job/75519544113) |
| 3m 27s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720126159/job/75519544191) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25720108097
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25720108097/job/75527967103
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25720129803
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519487034
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes...: failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519487333
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923875
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923877
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923881
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923886
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923887
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923888
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923889
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923890
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923892
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923904
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923919
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923921
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923927
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923930
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923944
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923954
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519923976
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519924010
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75519924017
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520502975
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520502994
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520503149
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520787380
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75520787383
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75521668247
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25720129803/job/75527845177

## Notes

Automatically requested by Full Release Validation 25720108097 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


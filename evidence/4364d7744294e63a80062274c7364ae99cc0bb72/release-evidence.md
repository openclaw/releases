# OpenClaw Release Evidence: 4364d7744294e63a80062274c7364ae99cc0bb72

Generated: 2026-05-06T08:55:33.050Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `4364d7744294e63a80062274c7364ae99cc0bb72` |
| Release ref input | `4364d7744294e63a80062274c7364ae99cc0bb72` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `4364d7744294e63a80062274c7364ae99cc0bb72` |
| Release ref SHA | `4364d7744294e63a80062274c7364ae99cc0bb72` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/4364d7744294-1778053825771` | `4364d7744294` | 1h 4m 38s | 1h 28m 28s | 1h 4m 5s | [25423050330](https://github.com/openclaw/openclaw/actions/runs/25423050330) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/4364d7744294-1778053825771` | `4364d7744294` | 4m 21s | 1h 23m 54s | 4m 18s | [25423069080](https://github.com/openclaw/openclaw/actions/runs/25423069080) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/4364d7744294-1778053825771` | `4364d7744294` | 1h 3m 4s | 13h 26m 57s | 1h 3m 0s | [25423069369](https://github.com/openclaw/openclaw/actions/runs/25423069369) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/4364d7744294-1778053825771` | `4364d7744294` | 1m 59s | 1m 40s | 18s | [25423163136](https://github.com/openclaw/openclaw/actions/runs/25423163136) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 3m 33s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423050330/job/74569631559) |
| 1h 0m 20s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74569980777) |
| 33m 8s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570768492) |
| 32m 4s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570206648) |
| 25m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74569981211) |
| 24m 11s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570293808) |
| 22m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74569981165) |
| 22m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74569981203) |
| 21m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74569981194) |
| 21m 5s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570293720) |
| 21m 3s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570293782) |
| 14m 49s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423050330/job/74569631451) |
| 4m 44s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423050330/job/74569631464) |
| 3m 55s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069080/job/74569698851) |
| 2m 24s | `normal-ci` | check-additional-extension-package-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069080/job/74569698921) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 4m 5s | 32s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423050330/job/74578547200) |
| 1h 3m 0s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74578451353) |
| 41m 52s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74575422126) |
| 11m 56s | 1m 35s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570790689) |
| 11m 33s | 7m 14s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570790702) |
| 11m 33s | 1m 29s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570790703) |
| 11m 33s | 1m 24s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570790706) |
| 11m 33s | 1m 38s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570790714) |
| 11m 33s | 1m 12s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570790718) |
| 11m 33s | 1m 23s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570790735) |
| 11m 33s | 6m 51s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570790737) |
| 4m 18s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069080/job/74570216432) |
| 3m 26s | 4s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423069080/job/74570087981) |
| 3m 13s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069080/job/74570072325) |
| 3m 12s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423069080/job/74570072313) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25423050330
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25423050330/job/74578547200
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25423069080
  - check-test-types: failure - https://github.com/openclaw/openclaw/actions/runs/25423069080/job/74569698870
  - checks-node-core-runtime-infra-process: failure - https://github.com/openclaw/openclaw/actions/runs/25423069080/job/74569699282
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25423069080/job/74569949949
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25423069080/job/74570087981
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25423069369
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74569980777
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570293726
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin): failure - https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74570768503
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74575422126
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25423069369/job/74578451353

## Notes

Automatically requested by Full Release Validation 25423050330 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


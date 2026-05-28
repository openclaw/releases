# OpenClaw Release Evidence: 06d46f7cf638a31c4852c068aeeaa76f5e949941

Generated: 2026-05-04T07:53:26.501Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `06d46f7cf638a31c4852c068aeeaa76f5e949941` |
| Release ref input | `06d46f7cf638a31c4852c068aeeaa76f5e949941` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `06d46f7cf638a31c4852c068aeeaa76f5e949941` |
| Release ref SHA | `06d46f7cf638a31c4852c068aeeaa76f5e949941` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/06d46f7cf638-1777879320347` | `06d46f7cf638` | 30m 54s | 55m 3s | 30m 27s | [25306336205](https://github.com/openclaw/openclaw/actions/runs/25306336205) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/06d46f7cf638-1777879320347` | `06d46f7cf638` | 6m 13s | 1h 28m 6s | 6m 10s | [25306356732](https://github.com/openclaw/openclaw/actions/runs/25306356732) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/06d46f7cf638-1777879320347` | `06d46f7cf638` | 29m 32s | 13h 30m 44s | 29m 29s | [25306352152](https://github.com/openclaw/openclaw/actions/runs/25306352152) | 38 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/06d46f7cf638-1777879320347` | `06d46f7cf638` | 1m 53s | 1m 35s | 17s | [25306433073](https://github.com/openclaw/openclaw/actions/runs/25306433073) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 30m 5s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306336205/job/74183068467) |
| 26m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183335467) |
| 22m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183335544) |
| 21m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183335578) |
| 21m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183335568) |
| 20m 27s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183335608) |
| 19m 59s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183592116) |
| 19m 57s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183335527) |
| 19m 8s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183592143) |
| 19m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183335569) |
| 18m 55s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183592114) |
| 13m 13s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306336205/job/74183068510) |
| 6m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306336205/job/74183068452) |
| 5m 50s | `normal-ci` | checks-node-agentic-control-plane-runtime | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306356732/job/74183124886) |
| 4m 5s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306356732/job/74183124590) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 30m 27s | 26s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25306336205/job/74186591240) |
| 29m 29s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74186528661) |
| 23m 5s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74185775733) |
| 14m 7s | 0s | `release-checks` | Run QA Lab parity report | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74184718883) |
| 11m 5s | 1m 2s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74184346074) |
| 11m 5s | 1m 52s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74184346101) |
| 11m 5s | 1m 41s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74184346103) |
| 11m 4s | 1m 27s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74184346043) |
| 11m 4s | 1m 52s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74184346058) |
| 11m 4s | 1m 22s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74184346100) |
| 11m 4s | 1m 18s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74184346106) |
| 6m 10s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306356732/job/74183800683) |
| 4m 25s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306356732/job/74183597895) |
| 2m 36s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306356732/job/74183374847) |
| 2m 35s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306356732/job/74183374926) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25306336205
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25306336205/job/74186591240
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25306352152
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183214982
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183215013
  - Run QA Lab parity lane (baseline): failure - https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183215020
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183592136
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): failure - https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183592139
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74183951069
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74185775733
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25306352152/job/74186528661

## Notes

Automatically requested by Full Release Validation 25306336205 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


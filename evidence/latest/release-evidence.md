# OpenClaw Release Evidence: latest

Generated: 2026-05-04T09:19:22.744Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `latest` |
| Release ref input | `v2026.5.3` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.3` |
| Release ref SHA | `06d46f7cf638a31c4852c068aeeaa76f5e949941` |
| Runs at release SHA | none |
| Package spec | `openclaw@latest` |
| npm status | published |
| npm resolved version | `2026.5.3` |
| npm dist-tags pointing here | `latest` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-04T07:46:24.298Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.3.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `da1e1435ad31` | 43m 15s | 1h 3m 59s | 42m 49s | [25309229437](https://github.com/openclaw/openclaw/actions/runs/25309229437) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `da1e1435ad31` | 4m 0s | 1h 12m 17s | 3m 55s | [25309247462](https://github.com/openclaw/openclaw/actions/runs/25309247462) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `da1e1435ad31` | 41m 56s | 13h 15m 57s | 41m 52s | [25309241629](https://github.com/openclaw/openclaw/actions/runs/25309241629) | 30 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `main` | `da1e1435ad31` | 1m 57s | 1m 41s | 16s | [25309246461](https://github.com/openclaw/openclaw/actions/runs/25309246461) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 42m 34s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309229437/job/74192009339) |
| 36m 43s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192554173) |
| 25m 28s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192312580) |
| 23m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192312563) |
| 22m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192312579) |
| 22m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192312680) |
| 21m 56s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192312604) |
| 21m 11s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192312684) |
| 21m 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192386412) |
| 20m 38s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192312690) |
| 20m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192312585) |
| 14m 24s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309229437/job/74192009324) |
| 4m 14s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309229437/job/74192009302) |
| 3m 29s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309247462/job/74192070238) |
| 2m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309229437/job/74192009659) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 42m 49s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25309229437/job/74197815813) |
| 41m 52s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74197708234) |
| 14m 9s | 0s | `release-checks` | Run QA Lab parity report | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74193898852) |
| 6m 54s | 1m 45s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192864402) |
| 6m 48s | 1m 22s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192864312) |
| 6m 46s | 1m 45s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192864285) |
| 6m 46s | 1m 50s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192864288) |
| 6m 46s | 1m 4s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192864291) |
| 6m 46s | 1m 34s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192864294) |
| 6m 46s | 2m 10s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192864302) |
| 6m 46s | 1m 52s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192864306) |
| 3m 55s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309247462/job/74192546201) |
| 2m 34s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309247462/job/74192376462) |
| 2m 30s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309247462/job/74192355094) |
| 2m 30s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25309247462/job/74192355117) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25309229437
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25309229437/job/74197815813
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25309241629
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192175986
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192176006
  - Run QA Lab parity lane (baseline): failure - https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192176007
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): failure - https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192386392
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192386406
  - Run package acceptance / Resolve package candidate: failure - https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192496848
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192554173
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74192661106
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25309241629/job/74197708234

## Notes

Automatically requested by Full Release Validation 25309229437 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


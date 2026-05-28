# OpenClaw Release Evidence: 2026.5.12-beta.3

Generated: 2026-05-13T02:43:49.372Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.12-beta.3` |
| Release ref input | `release/2026.5.12` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.5.12` |
| Release ref SHA | `ab9893a4f564039fb57670f710e0f2a8e3f0fccb` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | `openclaw@2026.5.12-beta.3` |
| npm status | published |
| npm resolved version | `2026.5.12-beta.3` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-12T23:38:06.518Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.12-beta.3.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.12` | `ab9893a4f564` | 36m 11s (+2m 29s) | 39m 50s (-9m 49s) | 35m 45s | [25773813660](https://github.com/openclaw/openclaw/actions/runs/25773813660) | 0 |
| pass | blocking | `normal-ci` | CI | `release/2026.5.12` | `ab9893a4f564` | 3m 15s (-8s) | 1h 0m 56s (+3m 6s) | 3m 10s | [25774253404](https://github.com/openclaw/openclaw/actions/runs/25774253404) | 4 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.12` | `ab9893a4f564` | 21m 26s (-10m 50s) | 4h 58m 5s (-7m 5s) | 21m 23s | [25774256677](https://github.com/openclaw/openclaw/actions/runs/25774256677) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release/2026.5.12` | `ab9893a4f564` | 3m 13s (+11s) | 3m 1s (+10s) | 11s | [25774256938](https://github.com/openclaw/openclaw/actions/runs/25774256938) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 22m 3s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75703517249) |
| 16m 46s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75703873557) |
| 11m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75704370827) |
| 9m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75703517252) |
| 8m 28s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75703773330) |
| 7m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75704370858) |
| 7m 0s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75703773323) |
| 6m 56s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75703773317) |
| 6m 53s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75703968451) |
| 6m 30s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75704001679) |
| 6m 6s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75703773313) |
| 5m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75703773327) |
| 3m 47s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75703517456) |
| 3m 40s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75703517250) |
| 3m 1s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256938/job/75703538884) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 35m 45s | 25s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75705636698) |
| 21m 23s | 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75705569938) |
| 20m 37s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75705503787) |
| 13m 41s | 3m 47s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75703517456) |
| 13m 40s | 22m 3s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75703517249) |
| 13m 35s | 3m 40s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75703517250) |
| 13m 34s | 9m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75703517252) |
| 13m 33s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75703517480) |
| 13m 20s | 12s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25773813660/job/75703494418) |
| 9m 0s | 1m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75704370831) |
| 9m 0s | 4m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75704370836) |
| 9m 0s | 1m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75704370869) |
| 8m 59s | 1m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75704370810) |
| 8m 59s | 1m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75704370815) |
| 8m 59s | 4m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25774256677/job/75704370823) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 32m 16s | 21m 26s | -10m 50s | -7m 5s |
| `full-release-validation` | 33m 42s | 36m 11s | +2m 29s | -9m 49s |
| `postpublish-telegram` | 3m 2s | 3m 13s | +11s | +10s |
| `normal-ci` | 3m 23s | 3m 15s | -8s | +3m 6s |

## Notes

Automatically requested by Full Release Validation 25773813660 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 665b164d4fc43e8d07b8fddaaf61ba1e09764143

Generated: 2026-05-06T09:07:45.068Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `665b164d4fc43e8d07b8fddaaf61ba1e09764143` |
| Release ref input | `665b164d4fc43e8d07b8fddaaf61ba1e09764143` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `665b164d4fc43e8d07b8fddaaf61ba1e09764143` |
| Release ref SHA | `665b164d4fc43e8d07b8fddaaf61ba1e09764143` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/665b164d4fc4-1778054375328` | `665b164d4fc4` | 1h 4m 46s | 1h 23m 7s | 1h 4m 5s | [25423419820](https://github.com/openclaw/openclaw/actions/runs/25423419820) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/665b164d4fc4-1778054375328` | `665b164d4fc4` | 4m 58s | 1h 25m 21s | 4m 46s | [25423437608](https://github.com/openclaw/openclaw/actions/runs/25423437608) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/665b164d4fc4-1778054375328` | `665b164d4fc4` | 1h 2m 55s | 13h 5m 29s | 1h 2m 51s | [25423434313](https://github.com/openclaw/openclaw/actions/runs/25423434313) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/665b164d4fc4-1778054375328` | `665b164d4fc4` | 1m 42s | 1m 35s | 6s | [25423535323](https://github.com/openclaw/openclaw/actions/runs/25423535323) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 3m 39s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423419820/job/74570830383) |
| 1h 0m 18s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571194846) |
| 32m 16s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571423582) |
| 27m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571882212) |
| 22m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571195244) |
| 22m 4s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571195224) |
| 21m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571195231) |
| 21m 20s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571195225) |
| 21m 18s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571195180) |
| 21m 10s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571500870) |
| 20m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571195235) |
| 8m 45s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423419820/job/74570830364) |
| 5m 16s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423419820/job/74570830365) |
| 3m 59s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423437608/job/74570900813) |
| 2m 29s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423437608/job/74570900789) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 4m 5s | 40s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423419820/job/74579939997) |
| 1h 2m 51s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74579823771) |
| 37m 40s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74576118093) |
| 10m 24s | 1m 47s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571778562) |
| 10m 20s | 2m 38s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571778572) |
| 10m 20s | 1m 49s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571778608) |
| 10m 20s | 1m 25s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571778623) |
| 10m 20s | 1m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571882102) |
| 10m 20s | 1m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571882127) |
| 10m 20s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571882140) |
| 10m 20s | 1m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571882144) |
| 4m 46s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25423437608/job/74571516888) |
| 4m 41s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423437608/job/74571490711) |
| 3m 59s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423437608/job/74571395362) |
| 3m 52s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25423437608/job/74571395337) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25423419820
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25423419820/job/74579939997
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25423437608
  - checks-node-core-runtime-infra-process: failure - https://github.com/openclaw/openclaw/actions/runs/25423437608/job/74570901310
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25423437608/job/74571516888
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25423434313
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571194846
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: failure - https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571195247
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571500870
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571500982
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin): failure - https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74571882127
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74576118093
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25423434313/job/74579823771

## Notes

Automatically requested by Full Release Validation 25423419820 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


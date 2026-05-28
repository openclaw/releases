# OpenClaw Release Evidence: d0497d13d18ec11fed3f616a2e0dac51eaa51b20

Generated: 2026-05-03T15:42:12.974Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `d0497d13d18ec11fed3f616a2e0dac51eaa51b20` |
| Release ref input | `d0497d13d18ec11fed3f616a2e0dac51eaa51b20` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `d0497d13d18ec11fed3f616a2e0dac51eaa51b20` |
| Release ref SHA | `d0497d13d18ec11fed3f616a2e0dac51eaa51b20` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/d0497d13d18e-1777821178129` | `d0497d13d18e` | 27m 46s | 44m 13s | 27m 17s | [25282802546](https://github.com/openclaw/openclaw/actions/runs/25282802546) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/d0497d13d18e-1777821178129` | `d0497d13d18e` | 3m 55s | 1h 8m 59s | 3m 52s | [25282812980](https://github.com/openclaw/openclaw/actions/runs/25282812980) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/d0497d13d18e-1777821178129` | `d0497d13d18e` | 26m 35s | 13h 25m 2s | 26m 31s | [25282813233](https://github.com/openclaw/openclaw/actions/runs/25282813233) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/d0497d13d18e-1777821178129` | `d0497d13d18e` | 1m 47s | 1m 35s | 11s | [25282873161](https://github.com/openclaw/openclaw/actions/runs/25282873161) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 26m 53s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282802546/job/74122598465) |
| 23m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122733422) |
| 21m 52s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122868203) |
| 21m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122733451) |
| 21m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122733489) |
| 21m 26s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122733432) |
| 20m 24s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122733443) |
| 20m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122733433) |
| 19m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122868136) |
| 19m 50s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122868142) |
| 19m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122733428) |
| 7m 41s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282802546/job/74122598463) |
| 4m 8s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282802546/job/74122598461) |
| 3m 34s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282812980/job/74122624883) |
| 2m 35s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282802546/job/74122598457) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 17s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25282802546/job/74124135082) |
| 26m 31s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74124114682) |
| 25m 5s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74124036580) |
| 6m 24s | 1m 19s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122973491) |
| 6m 23s | 1m 44s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122973444) |
| 6m 23s | 7m 38s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122973446) |
| 6m 23s | 2m 46s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122973448) |
| 6m 23s | 1m 40s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122973450) |
| 6m 23s | 59s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122973451) |
| 6m 23s | 7m 26s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122973455) |
| 6m 23s | 1m 53s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122973475) |
| 3m 52s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282812980/job/74122838902) |
| 2m 52s | 2m 19s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282802546/job/74122755551) |
| 2m 37s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282812980/job/74122765109) |
| 1m 59s | 2s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25282812980/job/74122720395) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25282802546
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25282802546/job/74124135082
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25282813233
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122733285
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: failure - https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74122733485
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25282813233/job/74124114682

## Notes

Manual rerun after making evidence ingestion wait for in-progress full validation.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


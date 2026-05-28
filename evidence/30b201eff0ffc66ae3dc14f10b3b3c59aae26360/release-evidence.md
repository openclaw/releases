# OpenClaw Release Evidence: 30b201eff0ffc66ae3dc14f10b3b3c59aae26360

Generated: 2026-05-04T02:54:11.200Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `30b201eff0ffc66ae3dc14f10b3b3c59aae26360` |
| Release ref input | `30b201eff0ffc66ae3dc14f10b3b3c59aae26360` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `30b201eff0ffc66ae3dc14f10b3b3c59aae26360` |
| Release ref SHA | `30b201eff0ffc66ae3dc14f10b3b3c59aae26360` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/30b201eff0ff-1777861521111` | `30b201eff0ff` | 28m 19s | 48m 38s | 27m 50s | [25298037947](https://github.com/openclaw/openclaw/actions/runs/25298037947) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/30b201eff0ff-1777861521111` | `30b201eff0ff` | 4m 4s | 1h 23m 53s | 4m 0s | [25298046495](https://github.com/openclaw/openclaw/actions/runs/25298046495) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/30b201eff0ff-1777861521111` | `30b201eff0ff` | 26m 59s | 13h 9m 17s | 26m 54s | [25298046651](https://github.com/openclaw/openclaw/actions/runs/25298046651) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/30b201eff0ff-1777861521111` | `30b201eff0ff` | 1m 52s | 1m 47s | 4s | [25298098792](https://github.com/openclaw/openclaw/actions/runs/25298098792) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 27m 28s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298037947/job/74160007439) |
| 24m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160139772) |
| 22m 27s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160139747) |
| 22m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160139782) |
| 21m 21s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160139758) |
| 20m 21s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160139781) |
| 20m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160139775) |
| 19m 36s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160215148) |
| 19m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160139771) |
| 19m 0s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160215144) |
| 18m 54s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160139791) |
| 11m 15s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298037947/job/74160007438) |
| 4m 39s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298037947/job/74160007440) |
| 3m 44s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046495/job/74160030766) |
| 2m 29s | `normal-ci` | checks-node-core-runtime-infra-state | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046495/job/74160030809) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 50s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25298037947/job/74161638805) |
| 26m 54s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74161607354) |
| 24m 9s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74161447271) |
| 6m 36s | 7m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160407558) |
| 6m 35s | 1m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160407560) |
| 6m 35s | 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160407564) |
| 6m 35s | 1m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160407567) |
| 6m 34s | 2m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160407562) |
| 6m 26s | 17m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160407568) |
| 6m 25s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160407646) |
| 6m 25s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160407774) |
| 4m 0s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046495/job/74160253061) |
| 2m 44s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046495/job/74160178714) |
| 2m 37s | 2m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298037947/job/74160147482) |
| 2m 25s | 3s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25298046495/job/74160159112) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25298037947
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25298037947/job/74161638805
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25298046651
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74160084735
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25298046651/job/74161607354

## Notes

Automatically requested by Full Release Validation 25298037947 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


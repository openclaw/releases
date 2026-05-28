# OpenClaw Release Evidence: 443f7035a2e5e31cab659de6b4927978eda5e3d8

Generated: 2026-05-04T00:45:24.169Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `443f7035a2e5e31cab659de6b4927978eda5e3d8` |
| Release ref input | `443f7035a2e5e31cab659de6b4927978eda5e3d8` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `443f7035a2e5e31cab659de6b4927978eda5e3d8` |
| Release ref SHA | `443f7035a2e5e31cab659de6b4927978eda5e3d8` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/443f7035a2e5-1777853797593` | `443f7035a2e5` | 28m 11s | 49m 10s | 27m 45s | [25294957520](https://github.com/openclaw/openclaw/actions/runs/25294957520) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/443f7035a2e5-1777853797593` | `443f7035a2e5` | 3m 52s | 1h 20m 6s | 3m 49s | [25294963317](https://github.com/openclaw/openclaw/actions/runs/25294963317) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/443f7035a2e5-1777853797593` | `443f7035a2e5` | 26m 55s | 12h 59m 21s | 26m 52s | [25294963514](https://github.com/openclaw/openclaw/actions/runs/25294963514) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/443f7035a2e5-1777853797593` | `443f7035a2e5` | 1m 47s | 1m 43s | 3s | [25295021859](https://github.com/openclaw/openclaw/actions/runs/25295021859) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 27m 31s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294957520/job/74152154317) |
| 24m 26s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152289132) |
| 23m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152289147) |
| 21m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152289160) |
| 21m 24s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152289134) |
| 21m 5s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152429726) |
| 21m 3s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152429725) |
| 19m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152289221) |
| 19m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152429727) |
| 18m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152289180) |
| 18m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152289152) |
| 12m 22s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294957520/job/74152154307) |
| 4m 12s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294957520/job/74152154311) |
| 3m 32s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963317/job/74152174487) |
| 2m 35s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963317/job/74152174509) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 45s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294957520/job/74153824626) |
| 26m 52s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74153789128) |
| 23m 9s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74153564679) |
| 6m 26s | 1m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152548397) |
| 6m 26s | 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152548398) |
| 6m 26s | 6m 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152548403) |
| 6m 26s | 1m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152548405) |
| 6m 26s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152548409) |
| 6m 25s | 1m 37s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152538252) |
| 6m 25s | 1m 50s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152538256) |
| 6m 25s | 16m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152548404) |
| 3m 49s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963317/job/74152388044) |
| 2m 48s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963317/job/74152323487) |
| 2m 43s | 2m 15s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294957520/job/74152297691) |
| 2m 14s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294963317/job/74152284608) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25294957520
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25294957520/job/74153824626
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25294963514
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152230972
  - Run QA Lab live Matrix lane: failure - https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152230978
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152410461
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74152429725
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25294963514/job/74153789128

## Notes

Automatically requested by Full Release Validation 25294957520 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: eb2748e5090a7ffcdb4a0b1ec0bec3bc06bb3699

Generated: 2026-05-03T23:11:25.133Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `eb2748e5090a7ffcdb4a0b1ec0bec3bc06bb3699` |
| Release ref input | `eb2748e5090a7ffcdb4a0b1ec0bec3bc06bb3699` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `eb2748e5090a7ffcdb4a0b1ec0bec3bc06bb3699` |
| Release ref SHA | `eb2748e5090a7ffcdb4a0b1ec0bec3bc06bb3699` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/eb2748e5090a-1777848196206` | `eb2748e5090a` | 27m 38s | 43m 47s | 27m 14s | [25292961487](https://github.com/openclaw/openclaw/actions/runs/25292961487) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/eb2748e5090a-1777848196206` | `eb2748e5090a` | 3m 56s | 1h 12m 57s | 3m 52s | [25292969777](https://github.com/openclaw/openclaw/actions/runs/25292969777) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/eb2748e5090a-1777848196206` | `eb2748e5090a` | 26m 27s | 13h 26m 16s | 26m 24s | [25292969602](https://github.com/openclaw/openclaw/actions/runs/25292969602) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/eb2748e5090a-1777848196206` | `eb2748e5090a` | 1m 46s | 1m 41s | 4s | [25293018507](https://github.com/openclaw/openclaw/actions/runs/25293018507) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 26m 54s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292961487/job/74147395380) |
| 23m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147520605) |
| 21m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147520587) |
| 21m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147520591) |
| 21m 9s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147636757) |
| 20m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147520576) |
| 20m 40s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147636762) |
| 20m 33s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147636798) |
| 20m 0s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147520612) |
| 19m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147520564) |
| 19m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147636745) |
| 7m 40s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292961487/job/74147395372) |
| 4m 9s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292961487/job/74147395374) |
| 3m 31s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969777/job/74147418205) |
| 2m 18s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292961487/job/74147395368) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 14s | 23s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292961487/job/74148747128) |
| 26m 24s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74148725361) |
| 23m 24s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74148572413) |
| 9m 55s | 10m 58s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147619651) |
| 7m 17s | 10m 49s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147619655) |
| 6m 22s | 2m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147725403) |
| 6m 22s | 17m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147725404) |
| 6m 22s | 1m 24s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147725405) |
| 6m 22s | 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147725407) |
| 6m 22s | 1m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147725408) |
| 6m 22s | 7m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147725412) |
| 3m 52s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969777/job/74147602959) |
| 2m 33s | 2m 15s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292961487/job/74147518845) |
| 2m 29s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969777/job/74147535803) |
| 2m 0s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292969777/job/74147506282) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25292961487
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25292961487/job/74148747128
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25292969602
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74147465191
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25292969602/job/74148725361

## Notes

Automatically requested by Full Release Validation 25292961487 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


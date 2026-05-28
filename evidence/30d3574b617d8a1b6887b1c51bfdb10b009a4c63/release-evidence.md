# OpenClaw Release Evidence: 30d3574b617d8a1b6887b1c51bfdb10b009a4c63

Generated: 2026-05-09T21:25:48.425Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `30d3574b617d8a1b6887b1c51bfdb10b009a4c63` |
| Release ref input | `30d3574b617d8a1b6887b1c51bfdb10b009a4c63` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `30d3574b617d8a1b6887b1c51bfdb10b009a4c63` |
| Release ref SHA | `30d3574b617d8a1b6887b1c51bfdb10b009a4c63` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 2 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/30d3574b617d-1778359979591` | `30d3574b617d` | 32m 26s | 1h 17m 29s | 31m 54s | [25611547346](https://github.com/openclaw/openclaw/actions/runs/25611547346) | 1 |
| running | blocking | `normal-ci` | CI | `release-ci/30d3574b617d-1778359979591` | `30d3574b617d` | 14s | 1h 12m 54s | 20m 56s | [25611554409](https://github.com/openclaw/openclaw/actions/runs/25611554409) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/30d3574b617d-1778359979591` | `30d3574b617d` | 4m 15s | 5h 0m 37s | 15m 14s | [25611556540](https://github.com/openclaw/openclaw/actions/runs/25611556540) | 42 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/30d3574b617d-1778359979591` | `30d3574b617d` | 2m 54s | 2m 49s | 5s | [25611608343](https://github.com/openclaw/openclaw/actions/runs/25611608343) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 31m 35s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611547346/job/75182528333) |
| 31m 28s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25611547346/job/75182528327) |
| 18m 32s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182888843) |
| 13m 49s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182757063) |
| 13m 48s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182757065) |
| 11m 54s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182757061) |
| 11m 33s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182757062) |
| 11m 23s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182757068) |
| 7m 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182898040) |
| 7m 44s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611547346/job/75182528331) |
| 7m 22s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182656970) |
| 6m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182656999) |
| 5m 26s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182747082) |
| 3m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611547346/job/75182663052) |
| 2m 49s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611608343/job/75182669925) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 31m 54s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25611547346/job/75184150611) |
| 20m 56s | 1m 14s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611554409/job/75182544628) |
| 15m 14s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75183320960) |
| 7m 20s | 7m 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182898040) |
| 7m 19s | 1m 4s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182898053) |
| 7m 19s | 4m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182898055) |
| 7m 18s | 2m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182898029) |
| 7m 17s | 2m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182898021) |
| 7m 16s | 4m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182898025) |
| 7m 16s | 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182898032) |
| 7m 16s | 4m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182898034) |
| 7m 16s | 5m 13s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611556540/job/75182898043) |
| 3m 1s | 3m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611547346/job/75182663052) |
| 2m 49s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611554409/job/75182670540) |
| 2m 3s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25611554409/job/75182632138) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611547346
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611547346/job/75182528327
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25611547346/job/75182528333
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25611547346/job/75184150611

## Notes

Automatically requested by Full Release Validation 25611547346 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


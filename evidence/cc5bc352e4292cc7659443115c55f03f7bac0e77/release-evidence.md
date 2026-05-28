# OpenClaw Release Evidence: cc5bc352e4292cc7659443115c55f03f7bac0e77

Generated: 2026-05-10T04:42:13.804Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `cc5bc352e4292cc7659443115c55f03f7bac0e77` |
| Release ref input | `cc5bc352e4292cc7659443115c55f03f7bac0e77` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `cc5bc352e4292cc7659443115c55f03f7bac0e77` |
| Release ref SHA | `cc5bc352e4292cc7659443115c55f03f7bac0e77` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/cc5bc352e429-1778387350000` | `cc5bc352e429` | 14m 29s | 37m 1s | 14m 2s | [25619769159](https://github.com/openclaw/openclaw/actions/runs/25619769159) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/cc5bc352e429-1778387350000` | `cc5bc352e429` | 3m 0s | 1h 16m 8s | 2m 50s | [25619774813](https://github.com/openclaw/openclaw/actions/runs/25619774813) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/cc5bc352e429-1778387350000` | `cc5bc352e429` | 14m 3s | 5h 36m 33s | 13m 59s | [25619774658](https://github.com/openclaw/openclaw/actions/runs/25619774658) | 45 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/cc5bc352e429-1778387350000` | `cc5bc352e429` | 3m 49s | 3m 37s | 12s | [25619835477](https://github.com/openclaw/openclaw/actions/runs/25619835477) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 13m 40s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619769159/job/75204150980) |
| 11m 48s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619769159/job/75204150974) |
| 11m 4s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204271398) |
| 8m 27s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386528) |
| 8m 27s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386541) |
| 8m 25s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386534) |
| 8m 13s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386540) |
| 8m 12s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386535) |
| 7m 49s | `release-checks` | cross_os_release_checks / Windows / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386537) |
| 7m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204271647) |
| 7m 28s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386530) |
| 7m 19s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386531) |
| 4m 19s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619769159/job/75204312005) |
| 3m 37s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619835477/job/75204317478) |
| 3m 27s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619769159/job/75204150977) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 14m 2s | 26s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619769159/job/75204757342) |
| 13m 59s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204773395) |
| 13m 51s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204768128) |
| 8m 56s | 2m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548061) |
| 8m 56s | 4m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548068) |
| 8m 56s | 4m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548074) |
| 8m 56s | 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548092) |
| 8m 55s | 1m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548055) |
| 8m 55s | 1m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548083) |
| 8m 54s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548054) |
| 8m 54s | 4m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548065) |
| 3m 43s | 4m 19s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619769159/job/75204312005) |
| 2m 50s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619774813/job/75204286561) |
| 2m 47s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619774813/job/75204282968) |
| 2m 46s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25619774813/job/75204282964) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619769159
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619769159/job/75204150980
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25619769159/job/75204757342
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204271398
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386528
  - cross_os_release_checks / Linux / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386529
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386530
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386531
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386534
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386535
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386537
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386540
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204386541
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204511010
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204511014
  - Run Docker release-path validation / Docker E2E (plugins/runtime install A): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204511030
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548065
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548066
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548068
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548070
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548071
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): cancelled - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204548079
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204768128
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25619774658/job/75204773395

## Notes

Automatically requested by Full Release Validation 25619769159 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


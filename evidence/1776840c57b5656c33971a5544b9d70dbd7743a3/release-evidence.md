# OpenClaw Release Evidence: 1776840c57b5656c33971a5544b9d70dbd7743a3

Generated: 2026-04-27T23:30:54.267Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `1776840c57b5656c33971a5544b9d70dbd7743a3` |
| Release ref input | `1776840c57b5656c33971a5544b9d70dbd7743a3` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `1776840c57b5656c33971a5544b9d70dbd7743a3` |
| Release ref SHA | `1776840c57b5656c33971a5544b9d70dbd7743a3` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `1776840c57b5` | 21m 59s | 25m 29s | [25024399875](https://github.com/openclaw/openclaw/actions/runs/25024399875) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `1776840c57b5` | 3m 13s | 53m 57s | [25024427812](https://github.com/openclaw/openclaw/actions/runs/25024427812) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `1776840c57b5` | 20m 29s | 5h 51m 26s | [25024428755](https://github.com/openclaw/openclaw/actions/runs/25024428755) | 32 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 21m 0s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024399875/job/73292213722) |
| 17m 15s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292552031) |
| 16m 41s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-core, Native live gateway core, node scrip... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292371616) |
| 16m 33s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-media, Native live media plugins, node scri... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292371717) |
| 14m 16s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292552030) |
| 13m 12s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292694526) |
| 12m 41s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292552044) |
| 11m 47s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292552020) |
| 11m 47s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292694498) |
| 11m 42s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292694557) |
| 10m 48s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292694555) |
| 3m 39s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024399875/job/73292213733) |
| 2m 54s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024427812/job/73292240772) |
| 1m 56s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024427812/job/73292240542) |
| 1m 56s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024427812/job/73292240747) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25024399875
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25024399875/job/73294450256
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25024428755
  - install_smoke_release_checks / install-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292307775
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-test, Native live test harnesses, node scripts/test-li...: failure - https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292371609
  - cross_os_release_checks / macOS / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292552044
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292552051
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292560886
  - live_and_e2e_release_checks / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73292694497
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73293455696
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25024428755/job/73294385762

## Notes

Automatically requested by Full Release Validation 25024399875 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 87345c066766537d3a4457a1b0d8f69cab708c48

Generated: 2026-04-27T23:15:16.871Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `87345c066766537d3a4457a1b0d8f69cab708c48` |
| Release ref input | `87345c066766537d3a4457a1b0d8f69cab708c48` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `87345c066766537d3a4457a1b0d8f69cab708c48` |
| Release ref SHA | `87345c066766537d3a4457a1b0d8f69cab708c48` |
| Runs at release SHA | `full-release-validation` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `87345c066766` | 21m 53s | 24m 28s | [25023845423](https://github.com/openclaw/openclaw/actions/runs/25023845423) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `ea2d95e23e87` | 2m 27s | 52m 46s | [25023875689](https://github.com/openclaw/openclaw/actions/runs/25023875689) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `ea2d95e23e87` | 20m 40s | 5h 27m 5s | [25023876003](https://github.com/openclaw/openclaw/actions/runs/25023876003) | 30 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 20m 55s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023845423/job/73290517947) |
| 16m 37s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290942364) |
| 15m 26s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-core, Native live gateway core, node scrip... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290691834) |
| 13m 31s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290942350) |
| 12m 32s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73291007689) |
| 11m 22s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73291007705) |
| 10m 53s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73291007700) |
| 10m 45s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290942386) |
| 10m 16s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290942420) |
| 10m 16s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73291007698) |
| 9m 44s | `release-checks` | cross_os_release_checks / Windows / installer fresh | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290942356) |
| 2m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023845423/job/73290517938) |
| 2m 6s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023875689/job/73290550220) |
| 2m 3s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023875689/job/73290550105) |
| 1m 54s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023875689/job/73290550256) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25023845423
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25023845423/job/73292785930
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25023875689
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25023875689/job/73290743925
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25023875689/job/73290788660
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25023876003
  - install_smoke_release_checks / install-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290621190
  - live_and_e2e_release_checks / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290691707
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-agents, Native live agents, node scripts/test-live...: failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290691768
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-test, Native live test harnesses, node scripts/test-li...: failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290691856
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290896889
  - cross_os_release_checks / Windows / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290942337
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290942356
  - cross_os_release_checks / macOS / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73290942364
  - live_and_e2e_release_checks / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73291007679
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73291772866
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25023876003/job/73292761147

## Notes

Automatically requested by Full Release Validation 25023845423 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


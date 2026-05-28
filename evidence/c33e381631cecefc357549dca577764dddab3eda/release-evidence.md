# OpenClaw Release Evidence: c33e381631cecefc357549dca577764dddab3eda

Generated: 2026-05-10T00:37:52.472Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `c33e381631cecefc357549dca577764dddab3eda` |
| Release ref input | `c33e381631cecefc357549dca577764dddab3eda` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `c33e381631cecefc357549dca577764dddab3eda` |
| Release ref SHA | `c33e381631cecefc357549dca577764dddab3eda` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/c33e381631ce-1778373031925` | `c33e381631ce` | 7m 3s | 22m 22s | 6m 30s | [25615573666](https://github.com/openclaw/openclaw/actions/runs/25615573666) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/c33e381631ce-1778373031925` | `c33e381631ce` | 3m 0s | 1h 4m 36s | 2m 55s | [25615580077](https://github.com/openclaw/openclaw/actions/runs/25615580077) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/c33e381631ce-1778373031925` | `c33e381631ce` | 6m 51s | 2h 37m 37s | 6m 50s | [25615579956](https://github.com/openclaw/openclaw/actions/runs/25615579956) | 16 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/c33e381631ce-1778373031925` | `c33e381631ce` | 3m 2s | 2m 58s | 3s | [25615628221](https://github.com/openclaw/openclaw/actions/runs/25615628221) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 6m 11s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615573666/job/75192883668) |
| 6m 9s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615573666/job/75192883672) |
| 3m 51s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193004379) |
| 3m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193004486) |
| 3m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193004489) |
| 3m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193004477) |
| 3m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193004503) |
| 3m 42s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193004479) |
| 3m 42s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193004497) |
| 3m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193004495) |
| 3m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193004505) |
| 3m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193004491) |
| 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615573666/job/75193017007) |
| 3m 16s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615573666/job/75192883670) |
| 2m 58s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615628221/job/75193024598) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6m 50s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193219409) |
| 6m 43s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193213939) |
| 6m 30s | 32s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615573666/job/75193184651) |
| 6m 11s |  | `release-checks` | Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193188581) |
| 6m 11s |  | `release-checks` | Run Docker release-path validation / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193188587) |
| 6m 10s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193188503) |
| 6m 1s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker live models (${{ matrix.provider_label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193180480) |
| 6m 0s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / plan_docker_lane_groups | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193180284) |
| 6m 0s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / validate_repo_e2e | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193180319) |
| 6m 0s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / validate_special_e2e | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193180329) |
| 6m 0s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / validate_live_provider_suites | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615579956/job/75193180333) |
| 3m 3s | 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615573666/job/75193017007) |
| 2m 55s | 4s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615580077/job/75193029842) |
| 2m 0s | 4s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615580077/job/75192985701) |
| 1m 55s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615580077/job/75192981424) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615573666
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615573666/job/75192883668
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615573666/job/75192883672
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25615573666/job/75193184651
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25615580077
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25615580077/job/75192970512
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25615580077/job/75193029842

## Notes

Automatically requested by Full Release Validation 25615573666 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


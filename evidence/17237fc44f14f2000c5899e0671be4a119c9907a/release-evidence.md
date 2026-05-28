# OpenClaw Release Evidence: 17237fc44f14f2000c5899e0671be4a119c9907a

Generated: 2026-05-12T11:00:49.804Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `17237fc44f14f2000c5899e0671be4a119c9907a` |
| Release ref input | `17237fc44f14f2000c5899e0671be4a119c9907a` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `17237fc44f14f2000c5899e0671be4a119c9907a` |
| Release ref SHA | `17237fc44f14f2000c5899e0671be4a119c9907a` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/17237fc44f14-1778578384905` | `17237fc44f14` | 1h 27m 24s | 2h 25m 16s | 1h 26m 47s | [25726008417](https://github.com/openclaw/openclaw/actions/runs/25726008417) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/17237fc44f14-1778578384905` | `17237fc44f14` | 6m 18s | 1h 10m 14s | 6m 15s | [25726024382](https://github.com/openclaw/openclaw/actions/runs/25726024382) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/17237fc44f14-1778578384905` | `17237fc44f14` | 1h 25m 56s | 16h 5m 23s | 1h 25m 52s | [25726024055](https://github.com/openclaw/openclaw/actions/runs/25726024055) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/17237fc44f14-1778578384905` | `17237fc44f14` | 15m 3s | 3m 12s | 11m 51s | [25726191616](https://github.com/openclaw/openclaw/actions/runs/25726191616) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 26m 23s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726008417/job/75538858213) |
| 50m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642157) |
| 50m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642093) |
| 40m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642116) |
| 35m 59s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642048) |
| 35m 56s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642095) |
| 35m 56s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642203) |
| 35m 47s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642026) |
| 35m 46s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642039) |
| 35m 46s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642071) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642034) |
| 32m 26s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726008417/job/75538858239) |
| 15m 32s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726008417/job/75539434503) |
| 6m 50s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726008417/job/75538858192) |
| 5m 46s | `normal-ci` | checks-node-agentic-control-plane-agent-chat | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726024382/job/75538933069) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 26m 47s | 36s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726008417/job/75553015252) |
| 1h 25m 52s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75552925949) |
| 40m 32s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75545449068) |
| 35m 1s | 30m 37s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642129) |
| 35m 0s | 35m 59s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642048) |
| 35m 0s | 35m 56s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642203) |
| 34m 59s | 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642063) |
| 34m 59s | 35m 46s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642071) |
| 34m 59s | 50m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642093) |
| 34m 59s | 30m 36s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642127) |
| 34m 59s | 50m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642157) |
| 11m 51s | 3m 12s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726191616/job/75539462936) |
| 6m 15s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726024382/job/75539909004) |
| 3m 40s | 15m 32s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726008417/job/75539434503) |
| 3m 16s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726024382/job/75539408033) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25726008417
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25726008417/job/75553015252
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25726024055
  - install_smoke_release_checks / bun_global_install_smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75539738870
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75541990798
  - Run Docker release-path validation / Docker E2E (plugins/runtime install D): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75541990811
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75541990851
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75543635575
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75543635581
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75543635606
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642014
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642026
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642034
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642039
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642043
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642048
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642063
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642071
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642092
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642093
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642095
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642115
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642116
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642125
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642127
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642129
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642157
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642163
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75544642203
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75545449068
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25726024055/job/75552925949

## Notes

Automatically requested by Full Release Validation 25726008417 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


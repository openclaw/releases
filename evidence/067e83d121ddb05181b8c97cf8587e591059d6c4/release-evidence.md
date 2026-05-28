# OpenClaw Release Evidence: 067e83d121ddb05181b8c97cf8587e591059d6c4

Generated: 2026-05-12T10:56:57.630Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `067e83d121ddb05181b8c97cf8587e591059d6c4` |
| Release ref input | `067e83d121ddb05181b8c97cf8587e591059d6c4` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `067e83d121ddb05181b8c97cf8587e591059d6c4` |
| Release ref SHA | `067e83d121ddb05181b8c97cf8587e591059d6c4` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/067e83d121dd-1778579512734` | `067e83d121dd` | 1h 4m 29s | 1h 40m 34s | 1h 3m 38s | [25726931242](https://github.com/openclaw/openclaw/actions/runs/25726931242) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/067e83d121dd-1778579512734` | `067e83d121dd` | 9m 1s | 1h 5m 55s | 7m 49s | [25726947361](https://github.com/openclaw/openclaw/actions/runs/25726947361) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/067e83d121dd-1778579512734` | `067e83d121dd` | 1h 2m 34s | 15h 57m 0s | 1h 2m 31s | [25726952800](https://github.com/openclaw/openclaw/actions/runs/25726952800) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/067e83d121dd-1778579512734` | `067e83d121dd` | 7m 43s | 3m 20s | 4m 22s | [25727117913](https://github.com/openclaw/openclaw/actions/runs/25727117913) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 3m 15s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726931242/job/75542012834) |
| 50m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897190) |
| 50m 28s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897052) |
| 40m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897047) |
| 35m 56s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896909) |
| 35m 56s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896949) |
| 35m 53s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896934) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896956) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896961) |
| 35m 50s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897005) |
| 35m 45s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896948) |
| 15m 56s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726931242/job/75542012898) |
| 9m 19s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726931242/job/75542012845) |
| 7m 52s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726931242/job/75542579357) |
| 3m 20s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727117913/job/75542626254) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 3m 38s | 50s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726931242/job/75552313138) |
| 1h 2m 31s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75552199103) |
| 23m 23s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75545964006) |
| 16m 6s | 4m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544196318) |
| 16m 5s | 4m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544195915) |
| 16m 5s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544195917) |
| 16m 5s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544195918) |
| 16m 5s | 1m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544195926) |
| 16m 5s | 1m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544195937) |
| 16m 5s | 4m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544195939) |
| 16m 5s | 5m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544195941) |
| 7m 49s | 1m 11s | `normal-ci` | checks-windows-node-test | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726947361/job/75542077893) |
| 4m 22s | 3m 20s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727117913/job/75542626254) |
| 4m 1s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726947361/job/75542698397) |
| 4m 0s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25726947361/job/75542698382) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25726931242
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25726931242/job/75552313138
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25726952800
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896909
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896934
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896938
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896948
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896949
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896956
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896957
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896961
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543896969
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897005
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897035
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897044
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897047
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897049
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897052
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897058
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897074
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897109
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543897190
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543905227
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543905251
  - Run Docker release-path validation / Docker E2E (plugins/runtime install A): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75543905276
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544195918
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544195962
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75544195968
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75545964006
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25726952800/job/75552199103

## Notes

Automatically requested by Full Release Validation 25726931242 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


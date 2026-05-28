# OpenClaw Release Evidence: 39005e6aa76090698291cbce15e6ab3882a0a28c

Generated: 2026-05-12T07:26:31.442Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `39005e6aa76090698291cbce15e6ab3882a0a28c` |
| Release ref input | `39005e6aa76090698291cbce15e6ab3882a0a28c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `39005e6aa76090698291cbce15e6ab3882a0a28c` |
| Release ref SHA | `39005e6aa76090698291cbce15e6ab3882a0a28c` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/39005e6aa760-1778567328043` | `39005e6aa760` | 57m 24s | 1h 16m 48s | 56m 50s | [25717562187](https://github.com/openclaw/openclaw/actions/runs/25717562187) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/39005e6aa760-1778567328043` | `39005e6aa760` | 2m 54s | 1h 1m 39s | 2m 38s | [25717574685](https://github.com/openclaw/openclaw/actions/runs/25717574685) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/39005e6aa760-1778567328043` | `39005e6aa760` | 55m 57s | 15h 21m 43s | 55m 54s | [25717574382](https://github.com/openclaw/openclaw/actions/runs/25717574382) | 44 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/39005e6aa760-1778567328043` | `39005e6aa760` | 3m 25s | 2m 57s | 27s | [25717707635](https://github.com/openclaw/openclaw/actions/runs/25717707635) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 56m 33s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717562187/job/75510866940) |
| 50m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480456) |
| 50m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480459) |
| 40m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480457) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480442) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480481) |
| 35m 45s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480484) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480472) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480477) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480531) |
| 35m 40s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480467) |
| 9m 18s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717562187/job/75510866973) |
| 3m 53s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717562187/job/75511272348) |
| 3m 12s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717562187/job/75510866935) |
| 3m 11s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717562187/job/75510866982) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 56m 50s | 34s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717562187/job/75518409057) |
| 55m 54s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75518315704) |
| 16m 16s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75512888595) |
| 9m 19s | 4m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511946820) |
| 9m 19s | 1m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511946841) |
| 9m 19s | 1m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511946854) |
| 9m 19s | 4m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511946885) |
| 9m 18s | 1m 39s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511946778) |
| 9m 18s | 1m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511946786) |
| 9m 18s | 1m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511946799) |
| 9m 18s | 4m 45s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511946806) |
| 3m 34s | 3m 53s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717562187/job/75511272348) |
| 2m 38s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717574685/job/75511212881) |
| 2m 4s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717574685/job/75511125787) |
| 2m 2s | 4s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717574685/job/75511122608) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25717562187
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25717562187/job/75518409057
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25717574382
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511057493
  - Run QA Lab live Telegram lane: failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511057498
  - Run QA Lab live Matrix lane: failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511057499
  - Run QA Lab parity lane (baseline): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511057527
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511216539
  - Run QA Lab parity report: failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511257169
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480425
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480426
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480428
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480434
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480435
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480442
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480444
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480446
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480456
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480457
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480459
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480467
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480472
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480476
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480477
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480481
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480484
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480499
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511480531
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511832708
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511832809
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75511946799
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75512888595
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25717574382/job/75518315704

## Notes

Automatically requested by Full Release Validation 25717562187 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


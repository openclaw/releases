# OpenClaw Release Evidence: 6eebba39203ef2f991d8bd329e243fee07589835

Generated: 2026-05-12T17:11:09.253Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `6eebba39203ef2f991d8bd329e243fee07589835` |
| Release ref input | `6eebba39203ef2f991d8bd329e243fee07589835` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `6eebba39203ef2f991d8bd329e243fee07589835` |
| Release ref SHA | `6eebba39203ef2f991d8bd329e243fee07589835` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/6eebba39203e-1778596157082` | `6eebba39203e` | 2h 41m 14s | 2h 40m 51s | 2h 40m 57s | [25741104424](https://github.com/openclaw/openclaw/actions/runs/25741104424) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/6eebba39203e-1778596157082` | `6eebba39203e` | 2h 40m 1s | 9h 6m 28s | 2h 39m 58s | [25741140556](https://github.com/openclaw/openclaw/actions/runs/25741140556) | 15 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 2h 40m 24s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25741104424/job/75591491757) |
| 50m 50s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637525) |
| 50m 40s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637234) |
| 40m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637255) |
| 30m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637032) |
| 30m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637134) |
| 30m 38s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637045) |
| 30m 35s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601636936) |
| 30m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601636985) |
| 30m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637013) |
| 30m 30s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637027) |
| 15s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25741104424/job/75623713391) |
| 12s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25741104424/job/75591414564) |
| 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25741104424/job/75591493527) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2h 40m 57s | 15s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25741104424/job/75623713391) |
| 2h 39m 58s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75623629223) |
| 1h 48m 59s | 50m 50s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637525) |
| 1h 48m 57s | 1m 30s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637102) |
| 1h 48m 49s | 1m 11s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601761842) |
| 1h 48m 42s | 30m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637032) |
| 1h 48m 30s | 2m 2s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601761970) |
| 1h 48m 16s | 1m 42s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601761977) |
| 1h 48m 15s | 2m 3s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601761862) |
| 1h 48m 15s | 4m 55s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601761963) |
| 1h 48m 14s | 2m 14s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601761890) |
| 30s | 2h 40m 24s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25741104424/job/75591491757) |
| 27s |  | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25741104424/job/75591492155) |
| 27s |  | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25741104424/job/75591492643) |
| 27s |  | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25741104424/job/75591493372) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25741104424
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25741104424/job/75623713391
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601636936
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601636985
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637013
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637027
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637032
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637045
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637134
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637234
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637255
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75601637525
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25741140556/job/75623629223

## Notes

Automatically requested by Full Release Validation 25741104424 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


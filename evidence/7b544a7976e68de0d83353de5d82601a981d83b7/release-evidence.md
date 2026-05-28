# OpenClaw Release Evidence: 7b544a7976e68de0d83353de5d82601a981d83b7

Generated: 2026-05-12T16:06:38.208Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `7b544a7976e68de0d83353de5d82601a981d83b7` |
| Release ref input | `7b544a7976e68de0d83353de5d82601a981d83b7` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `7b544a7976e68de0d83353de5d82601a981d83b7` |
| Release ref SHA | `7b544a7976e68de0d83353de5d82601a981d83b7` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/7b544a7976e6-1778592970635` | `7b544a7976e6` | 2h 29m 47s (+1h 1m 53s) | 2h 29m 19s (+1h 2m 4s) | 2h 29m 30s | [25738044541](https://github.com/openclaw/openclaw/actions/runs/25738044541) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/7b544a7976e6-1778592970635` | `7b544a7976e6` | 2h 28m 23s (+1h 2m 11s) | 9h 19m 34s (+8h 30m 47s) | 2h 28m 18s | [25738082562](https://github.com/openclaw/openclaw/actions/runs/25738082562) | 15 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 2h 28m 52s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75580407728) |
| 50m 46s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314710) |
| 50m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314658) |
| 40m 35s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314815) |
| 30m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314660) |
| 30m 34s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314674) |
| 30m 34s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314678) |
| 30m 34s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314683) |
| 30m 32s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314754) |
| 30m 32s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314794) |
| 30m 30s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314540) |
| 16s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75611603970) |
| 11s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75580334154) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75580408596) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75580408668) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2h 29m 30s | 16s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75611603970) |
| 2h 28m 18s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75611501554) |
| 1h 38m 19s | 30m 30s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314540) |
| 1h 38m 18s | 2m 6s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589244011) |
| 1h 38m 18s | 2m 27s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589244483) |
| 1h 38m 18s | 1m 47s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314584) |
| 1h 38m 18s | 30m 34s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314678) |
| 1h 38m 18s | 1m 35s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314698) |
| 1h 38m 18s | 4m 13s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314731) |
| 1h 38m 17s | 2m 10s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314795) |
| 1h 37m 31s | 30m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314660) |
| 35s | 2h 28m 52s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75580407728) |
| 25s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75580408596) |
| 25s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75580408668) |
| 25s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75580409099) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 1h 26m 12s | 2h 28m 23s | +1h 2m 11s | +8h 30m 47s |
| `full-release-validation` | 1h 27m 54s | 2h 29m 47s | +1h 1m 53s | +1h 2m 4s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25738044541
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25738044541/job/75611603970
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25738082562
  - Run repo/live E2E validation / Live media suites (Native live media audio plugins): failure - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75581055356
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75581056275
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314540
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314658
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314660
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314674
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314678
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314683
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314710
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314754
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314794
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75589314815
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25738082562/job/75611501554

## Notes

Automatically requested by Full Release Validation 25738044541 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


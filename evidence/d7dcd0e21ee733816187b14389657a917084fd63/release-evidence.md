# OpenClaw Release Evidence: d7dcd0e21ee733816187b14389657a917084fd63

Generated: 2026-04-27T22:08:36.910Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `d7dcd0e21ee733816187b14389657a917084fd63` |
| Release ref input | `d7dcd0e21ee733816187b14389657a917084fd63` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `d7dcd0e21ee733816187b14389657a917084fd63` |
| Release ref SHA | `d7dcd0e21ee733816187b14389657a917084fd63` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `d7dcd0e21ee7` | 7m 33s | 12m 39s | [25021883973](https://github.com/openclaw/openclaw/actions/runs/25021883973) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `d7dcd0e21ee7` | 4m 48s | 57m 37s | [25021918941](https://github.com/openclaw/openclaw/actions/runs/25021918941) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `d7dcd0e21ee7` | 6m 15s | 1h 49m 50s | [25021918662](https://github.com/openclaw/openclaw/actions/runs/25021918662) | 14 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 6m 34s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021883973/job/73284168772) |
| 5m 16s | `release-checks` | live_and_e2e_release_checks / Docker live models (Google) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021918662/job/73284377715) |
| 5m 16s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenRouter) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021918662/job/73284377760) |
| 5m 15s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25021883973/job/73284168797) |
| 5m 2s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenCode) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021918662/job/73284377704) |
| 5m 2s | `release-checks` | live_and_e2e_release_checks / Docker live models (Z.ai) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021918662/job/73284377800) |
| 5m 1s | `release-checks` | live_and_e2e_release_checks / Docker live models (MiniMax) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021918662/job/73284377712) |
| 5m 1s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021918662/job/73284377786) |
| 5m 1s | `release-checks` | live_and_e2e_release_checks / Docker live models (xAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021918662/job/73284377792) |
| 4m 57s | `release-checks` | live_and_e2e_release_checks / Docker live models (Anthropic) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021918662/job/73284377815) |
| 4m 48s | `release-checks` | live_and_e2e_release_checks / Docker live models (Fireworks) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021918662/job/73284377901) |
| 4m 17s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-cli-backend-docker, Docker live CLI backend, pnpm test:docker... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25021918662/job/73284377943) |
| 2m 48s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25021918941/job/73284214218) |
| 2m 3s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/25021918941/job/73284214004) |
| 2m 1s | `normal-ci` | checks-node-extensions-shard-5 | success | [job](https://github.com/openclaw/openclaw/actions/runs/25021918941/job/73284214064) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25021883973
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25021883973/job/73284168772
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25021883973/job/73285029719

## Notes

Automatically requested by Full Release Validation 25021883973 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


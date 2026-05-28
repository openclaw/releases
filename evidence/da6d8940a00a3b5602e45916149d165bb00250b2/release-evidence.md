# OpenClaw Release Evidence: da6d8940a00a3b5602e45916149d165bb00250b2

Generated: 2026-04-27T23:09:18.022Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `da6d8940a00a3b5602e45916149d165bb00250b2` |
| Release ref input | `da6d8940a00a3b5602e45916149d165bb00250b2` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `da6d8940a00a3b5602e45916149d165bb00250b2` |
| Release ref SHA | `da6d8940a00a3b5602e45916149d165bb00250b2` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `da6d8940a00a` | 6m 37s | 10m 14s | [25024183926](https://github.com/openclaw/openclaw/actions/runs/25024183926) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `ff2b2e769f5d` | 3m 14s | 53m 26s | [25024215545](https://github.com/openclaw/openclaw/actions/runs/25024215545) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `da6d8940a00a` | 5m 16s | 1h 55m 1s | [25024215278](https://github.com/openclaw/openclaw/actions/runs/25024215278) | 28 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 36s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024183926/job/73291556164) |
| 4m 22s | `release-checks` | Run QA Lab parity gate | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024215278/job/73291639291) |
| 4m 6s | `release-checks` | live_and_e2e_release_checks / Docker live models (Anthropic) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024215278/job/73291720156) |
| 4m 6s | `release-checks` | live_and_e2e_release_checks / Docker live models (MiniMax) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024215278/job/73291720167) |
| 4m 5s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenCode) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024215278/job/73291720155) |
| 4m 4s | `release-checks` | live_and_e2e_release_checks / Docker live models (Google) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024215278/job/73291720146) |
| 4m 4s | `release-checks` | live_and_e2e_release_checks / Docker live models (xAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024215278/job/73291720171) |
| 4m 4s | `release-checks` | live_and_e2e_release_checks / Docker live models (Fireworks) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024215278/job/73291720172) |
| 4m 4s | `release-checks` | live_and_e2e_release_checks / Docker live models (Z.ai) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024215278/job/73291720194) |
| 4m 3s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenRouter) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024215278/job/73291720178) |
| 3m 59s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-gateway-docker, Docker live gateway, pnpm test:docker:live-ga... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25024215278/job/73291720208) |
| 3m 45s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024183926/job/73291556162) |
| 2m 47s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024215545/job/73291594146) |
| 2m 4s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024215545/job/73291594019) |
| 1m 57s | `normal-ci` | checks-node-core-runtime-infra | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024215545/job/73291594156) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25024183926
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25024183926/job/73291556164
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25024183926/job/73292157277
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25024215545
  - check-test-types: failure - https://github.com/openclaw/openclaw/actions/runs/25024215545/job/73291594063
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25024215545/job/73291688691

## Notes

Automatically requested by Full Release Validation 25024183926 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


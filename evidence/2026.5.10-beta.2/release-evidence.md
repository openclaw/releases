# OpenClaw Release Evidence: 2026.5.10-beta.2

Generated: 2026-05-11T02:29:52.029Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.10-beta.2` |
| Release ref input | `release/2026.5.10` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.5.10` |
| Release ref SHA | `c9779652a2ee70f9c1b0a2eeb73ea21cbb97d8cc` |
| Runs at release SHA | none |
| Package spec | `openclaw@2026.5.10-beta.2` |
| npm status | published |
| npm resolved version | `2026.5.10-beta.2` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-10T18:15:07.481Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.10-beta.2.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `main` | `a41f1e8d6308` | 6m 17s (-33m 3s) | 6m 9s (-14m 15s) | 6m 10s | [25647009754](https://github.com/openclaw/openclaw/actions/runs/25647009754) | 0 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `main` | `a41f1e8d6308` | 5m 9s (-14m 21s) | 6m 57s (-16m 1s) | 5m 6s | [25647020421](https://github.com/openclaw/openclaw/actions/runs/25647020421) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 48s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647009754/job/75277733485) |
| 1m 48s | `release-checks` | Run repo/live E2E validation / prepare_live_test_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75277933437) |
| 1m 32s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75277933447) |
| 1m 19s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75277745306) |
| 1m 9s | `release-checks` | Run repo/live E2E validation / validate_selected_ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75277844784) |
| 15s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647009754/job/75277715420) |
| 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075489) |
| 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075492) |
| 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075496) |
| 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075497) |
| 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075498) |
| 6s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647009754/job/75278158086) |
| 6s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075482) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25647009754/job/75277733590) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25647009754/job/75277733597) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6m 10s | 6s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647009754/job/75278158086) |
| 5m 6s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278113376) |
| 4m 58s | 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075489) |
| 4m 58s | 6s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075490) |
| 4m 58s | 5s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075491) |
| 4m 58s | 6s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075493) |
| 4m 58s | 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075498) |
| 4m 58s | 6s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075499) |
| 4m 45s | 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075492) |
| 4m 45s | 7s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075496) |
| 4m 44s | 6s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647020421/job/75278075482) |
| 20s | 5m 48s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25647009754/job/75277733485) |
| 19s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25647009754/job/75277733590) |
| 19s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25647009754/job/75277733597) |
| 19s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25647009754/job/75277733703) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 39m 20s | 6m 17s | -33m 3s | -14m 15s |
| `release-checks` | 19m 30s | 5m 9s | -14m 21s | -16m 1s |

## Notes

Automatically requested by Full Release Validation 25647009754 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


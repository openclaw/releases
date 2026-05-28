# OpenClaw Release Evidence: f55220d6b9227b4f8450dd7c16f670e04cc91ec6

Generated: 2026-04-28T14:21:04.352Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `f55220d6b9227b4f8450dd7c16f670e04cc91ec6` |
| Release ref input | `f55220d6b9227b4f8450dd7c16f670e04cc91ec6` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `f55220d6b9227b4f8450dd7c16f670e04cc91ec6` |
| Release ref SHA | `f55220d6b9227b4f8450dd7c16f670e04cc91ec6` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.4.27` | `f55220d6b922` | 51m 22s | 54m 52s | [25055732933](https://github.com/openclaw/openclaw/actions/runs/25055732933) | 0 |
| fail | blocking | `normal-ci` | CI | `release/2026.4.27` | `f55220d6b922` | 3m 7s | 1h 3m 52s | [25055753051](https://github.com/openclaw/openclaw/actions/runs/25055753051) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.4.27` | `f55220d6b922` | 50m 10s | 6h 21m 58s | [25055754906](https://github.com/openclaw/openclaw/actions/runs/25055754906) | 37 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 50m 42s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055732933/job/73395416133) |
| 13m 34s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, OPENCLAW_LIVE_DOCKER_R... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400199206) |
| 13m 11s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go, Native live gateway ... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400199175) |
| 13m 3s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-gateway-docker, Docker live gateway, OPENCLAW_LIVE_DOCKER_REP... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400199183) |
| 12m 21s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-media-music-google, Native live media music... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400199373) |
| 10m 25s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73401976413) |
| 10m 9s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73401976403) |
| 10m 7s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73401976564) |
| 9m 45s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73401976438) |
| 9m 44s | `release-checks` | live_and_e2e_release_checks / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400198757) |
| 9m 8s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73401976472) |
| 3m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055732933/job/73395416097) |
| 2m 33s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055753051/job/73395509092) |
| 2m 33s | `normal-ci` | checks-node-auto-reply-reply-commands-state-routing | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055753051/job/73395509193) |
| 2m 16s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25055753051/job/73395508915) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25055732933
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25055732933/job/73405251271
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25055753051
  - checks-node-extensions-shard-5: failure - https://github.com/openclaw/openclaw/actions/runs/25055753051/job/73395509002
  - checks-node-extensions: failure - https://github.com/openclaw/openclaw/actions/runs/25055753051/job/73395964351
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906
  - Run QA Lab live Telegram lane: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73399737102
  - Run QA Lab live Matrix lane: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73399737204
  - install_smoke_release_checks / install-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73399777572
  - cross_os_release_checks / macOS / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400145356
  - cross_os_release_checks / macOS / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400145400
  - cross_os_release_checks / Linux / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400145407
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400145418
  - cross_os_release_checks / Windows / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400145444
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400145448
  - cross_os_release_checks / Linux / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400145476
  - cross_os_release_checks / Linux / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400145478
  - cross_os_release_checks / macOS / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400145486
  - live_and_e2e_release_checks / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400198643
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400199070
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-xai, Native live xAI plugin, node .release-...: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400199153
  - live_and_e2e_release_checks / validate_live_provider_suites (live-codex-harness-docker, Docker live Codex harness, OPENCLAW_LIV...: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400199171
  - live_and_e2e_release_checks / validate_live_provider_suites (live-cli-backend-docker, Docker live CLI backend, OPENCLAW_LIVE_DO...: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400199243
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73400311928
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73403914840
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25055754906/job/73405148258

## Notes

Automatically requested by Full Release Validation 25055732933 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


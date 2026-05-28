# OpenClaw Release Evidence: 72846084615384264a61a26cb9b1184c9f9ab871

Generated: 2026-05-12T12:51:01.772Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `72846084615384264a61a26cb9b1184c9f9ab871` |
| Release ref input | `72846084615384264a61a26cb9b1184c9f9ab871` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `72846084615384264a61a26cb9b1184c9f9ab871` |
| Release ref SHA | `72846084615384264a61a26cb9b1184c9f9ab871` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/728460846153-1778586639604` | `728460846153` | 59m 52s | 1h 24m 57s | 59m 22s | [25732555466](https://github.com/openclaw/openclaw/actions/runs/25732555466) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/728460846153-1778586639604` | `728460846153` | 4m 46s | 1h 11m 19s | 4m 43s | [25732613072](https://github.com/openclaw/openclaw/actions/runs/25732613072) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/728460846153-1778586639604` | `728460846153` | 57m 39s | 16h 19m 51s | 57m 35s | [25732613156](https://github.com/openclaw/openclaw/actions/runs/25732613156) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/728460846153-1778586639604` | `728460846153` | 4m 0s | 3m 22s | 37s | [25732774446](https://github.com/openclaw/openclaw/actions/runs/25732774446) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 58m 7s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732555466/job/75561346941) |
| 50m 50s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326237) |
| 50m 45s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326228) |
| 45m 28s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75561742089) |
| 40m 36s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326227) |
| 35m 59s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326250) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326202) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326449) |
| 35m 45s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326170) |
| 35m 45s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326215) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326184) |
| 12m 51s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732555466/job/75561346924) |
| 5m 15s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732555466/job/75561346961) |
| 4m 27s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732555466/job/75561877192) |
| 4m 12s | `normal-ci` | check-dependencies | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732613072/job/75561436254) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 59m 22s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25732555466/job/75571330935) |
| 57m 35s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75571223287) |
| 47m 48s | 0s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75569461853) |
| 47m 48s | 0s | `release-checks` | install_smoke_release_checks / installer_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75569461854) |
| 47m 48s | 0s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75569461962) |
| 24m 25s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75565407647) |
| 13m 11s | 11m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75563291006) |
| 13m 11s | 6m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75563291084) |
| 13m 11s | 1m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75563291229) |
| 13m 10s | 4m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75563290993) |
| 13m 10s | 1m 58s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75563291002) |
| 4m 43s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732613072/job/75562133115) |
| 4m 23s | 4m 27s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732555466/job/75561877192) |
| 3m 54s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732613072/job/75561981274) |
| 3m 42s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25732613072/job/75561944998) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25732555466
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25732555466/job/75571330935
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25732613156
  - install_smoke_release_checks / root_dockerfile_image: failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75561742089
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75561817573
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326170
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326176
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326184
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326199
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326202
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326207
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326209
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326215
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326216
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326217
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326218
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326219
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326227
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326228
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326237
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326250
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326296
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326345
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75562326449
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75563290972
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75565407647
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25732613156/job/75571223287

## Notes

Automatically requested by Full Release Validation 25732555466 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


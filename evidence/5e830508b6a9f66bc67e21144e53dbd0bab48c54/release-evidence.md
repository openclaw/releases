# OpenClaw Release Evidence: 5e830508b6a9f66bc67e21144e53dbd0bab48c54

Generated: 2026-05-03T15:52:47.555Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `5e830508b6a9f66bc67e21144e53dbd0bab48c54` |
| Release ref input | `5e830508b6a9f66bc67e21144e53dbd0bab48c54` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `5e830508b6a9f66bc67e21144e53dbd0bab48c54` |
| Release ref SHA | `5e830508b6a9f66bc67e21144e53dbd0bab48c54` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/5e830508b6a9-1777821871879` | `5e830508b6a9` | 27m 43s | 44m 5s | 27m 18s | [25283080356](https://github.com/openclaw/openclaw/actions/runs/25283080356) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/5e830508b6a9-1777821871879` | `5e830508b6a9` | 3m 54s | 1h 11m 55s | 3m 51s | [25283087312](https://github.com/openclaw/openclaw/actions/runs/25283087312) | 4 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/5e830508b6a9-1777821871879` | `5e830508b6a9` | 26m 35s | 13h 23m 55s | 26m 32s | [25283087347](https://github.com/openclaw/openclaw/actions/runs/25283087347) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/5e830508b6a9-1777821871879` | `5e830508b6a9` | 1m 55s | 1m 43s | 11s | [25283142414](https://github.com/openclaw/openclaw/actions/runs/25283142414) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 27m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283080356/job/74123279321) |
| 24m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123396883) |
| 23m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123396868) |
| 22m 14s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123506050) |
| 22m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123396921) |
| 22m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123396934) |
| 21m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123396924) |
| 20m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123396881) |
| 19m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123396925) |
| 19m 34s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123396864) |
| 19m 29s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123506082) |
| 7m 45s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283080356/job/74123279308) |
| 4m 12s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283080356/job/74123279302) |
| 3m 29s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087312/job/74123296482) |
| 2m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283080356/job/74123403574) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 18s | 24s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25283080356/job/74124779624) |
| 26m 32s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74124755933) |
| 25m 14s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74124680742) |
| 6m 26s | 2m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123626938) |
| 6m 25s | 1m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123626941) |
| 6m 25s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123626946) |
| 6m 24s | 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123626934) |
| 6m 24s | 3m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123626944) |
| 6m 24s | 18m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123626948) |
| 6m 19s | 1m 36s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123615402) |
| 6m 15s | 6m 43s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087347/job/74123615389) |
| 3m 51s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087312/job/74123488216) |
| 2m 36s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087312/job/74123428556) |
| 2m 30s | 2m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283080356/job/74123403574) |
| 1m 58s | 3s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25283087312/job/74123391417) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25283080356
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25283080356/job/74124779624

## Notes

Automatically requested by Full Release Validation 25283080356 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


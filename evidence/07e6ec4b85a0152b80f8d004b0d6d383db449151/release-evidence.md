# OpenClaw Release Evidence: 07e6ec4b85a0152b80f8d004b0d6d383db449151

Generated: 2026-05-03T18:39:52.734Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `07e6ec4b85a0152b80f8d004b0d6d383db449151` |
| Release ref input | `07e6ec4b85a0152b80f8d004b0d6d383db449151` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `07e6ec4b85a0152b80f8d004b0d6d383db449151` |
| Release ref SHA | `07e6ec4b85a0152b80f8d004b0d6d383db449151` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/07e6ec4b85a0-1777832043068` | `07e6ec4b85a0` | 25m 22s | 42m 55s | 24m 55s | [25286889124](https://github.com/openclaw/openclaw/actions/runs/25286889124) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/07e6ec4b85a0-1777832043068` | `07e6ec4b85a0` | 3m 51s | 1h 10m 47s | 3m 48s | [25286897553](https://github.com/openclaw/openclaw/actions/runs/25286897553) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/07e6ec4b85a0-1777832043068` | `07e6ec4b85a0` | 24m 17s | 11h 7m 24s | 24m 11s | [25286897373](https://github.com/openclaw/openclaw/actions/runs/25286897373) | 19 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/07e6ec4b85a0-1777832043068` | `07e6ec4b85a0` | 1m 55s | 1m 42s | 12s | [25286952176](https://github.com/openclaw/openclaw/actions/runs/25286952176) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 24m 33s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286889124/job/74132620154) |
| 21m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132745494) |
| 21m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132745493) |
| 21m 11s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132745485) |
| 20m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132745483) |
| 19m 57s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132844690) |
| 19m 54s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132745501) |
| 19m 22s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132745491) |
| 18m 40s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132745355) |
| 18m 25s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132844691) |
| 18m 13s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132745508) |
| 8m 49s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286889124/job/74132620148) |
| 4m 13s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286889124/job/74132620149) |
| 3m 32s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897553/job/74132637217) |
| 2m 28s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286889124/job/74132620150) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 24m 55s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25286889124/job/74133984263) |
| 24m 11s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74133968444) |
| 10m 21s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74133191140) |
| 10m 21s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74133191147) |
| 10m 21s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74133191196) |
| 7m 1s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74133010703) |
| 7m 0s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74133010709) |
| 7m 0s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74133010775) |
| 7m 0s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74133010965) |
| 6m 23s | 36s | `release-checks` | Run package acceptance / Docker product acceptance / prepare_docker_e2e_image | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132955557) |
| 6m 2s | 6s | `release-checks` | Run package acceptance / Docker product acceptance / plan_docker_lane_groups | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132955567) |
| 3m 48s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897553/job/74132833876) |
| 2m 57s | 2m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286889124/job/74132759336) |
| 2m 28s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897553/job/74132762600) |
| 1m 53s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25286897553/job/74132731673) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25286889124
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25286889124/job/74133984263
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25286897373
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132844678
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132844679
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132844680
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): failure - https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132844688
  - Run Docker release-path validation / prepare_docker_e2e_image: failure - https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132876437
  - Run package acceptance / Docker product acceptance / prepare_docker_e2e_image: failure - https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74132955557
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74133010703
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25286897373/job/74133968444

## Notes

Automatically requested by Full Release Validation 25286889124 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


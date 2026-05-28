# OpenClaw Release Evidence: 2026.5.9-beta.1

Generated: 2026-05-09T14:53:56.638Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.9-beta.1` |
| Release ref input | `6c9981e9bc5f79da78b081b37319c07c6df38b1c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `6c9981e9bc5f79da78b081b37319c07c6df38b1c` |
| Release ref SHA | `6c9981e9bc5f79da78b081b37319c07c6df38b1c` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | `openclaw@2026.5.9-beta.1` |
| npm status | published |
| npm resolved version | `2026.5.9-beta.1` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-09T13:27:37.091Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.9-beta.1.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/6c9981e9bc5f-1778336039433` | `6c9981e9bc5f` | 39m 29s (+31m 16s) | 1h 6m 50s (+43m 15s) | 39m 3s | [25603220476](https://github.com/openclaw/openclaw/actions/runs/25603220476) | 0 |
| fail | blocking | `normal-ci` | CI | `release-ci/6c9981e9bc5f-1778336039433` | `6c9981e9bc5f` | 11m 31s (+7m 8s) | 1h 29m 19s (+13m 28s) | 2m 42s | [25603228762](https://github.com/openclaw/openclaw/actions/runs/25603228762) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/6c9981e9bc5f-1778336039433` | `6c9981e9bc5f` | 38m 4s (+30m 14s) | 4h 49m 36s (+1h 46m 26s) | 37m 59s | [25603228934](https://github.com/openclaw/openclaw/actions/runs/25603228934) | 33 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/6c9981e9bc5f-1778336039433` | `6c9981e9bc5f` | 3m 15s (-13s) | 3m 3s (-11s) | 12s | [25603229239](https://github.com/openclaw/openclaw/actions/runs/25603229239) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 38m 41s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603220476/job/75160583425) |
| 32m 44s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160825049) |
| 23m 40s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160714883) |
| 11m 56s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603220476/job/75160583427) |
| 11m 46s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603220476/job/75160583416) |
| 11m 0s | `normal-ci` | macos-node | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603228762/job/75160603594) |
| 8m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160715121) |
| 7m 36s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160825058) |
| 7m 18s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160715149) |
| 7m 4s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160715129) |
| 6m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160715140) |
| 6m 6s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160953748) |
| 5m 51s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160795388) |
| 5m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160715091) |
| 3m 53s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603220476/job/75160583526) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 39m 3s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603220476/job/75162685182) |
| 37m 59s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75162650222) |
| 11m 21s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75161203374) |
| 11m 20s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75161203335) |
| 7m 48s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75161006663) |
| 7m 48s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75161006673) |
| 7m 5s | 1m 19s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160953734) |
| 7m 5s | 1m 58s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160953745) |
| 7m 5s | 6m 6s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160953748) |
| 7m 4s | 1m 19s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160953736) |
| 7m 4s | 1m 54s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160953741) |
| 2m 42s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228762/job/75160726476) |
| 2m 40s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228762/job/75160730323) |
| 2m 8s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228762/job/75160697592) |
| 2m 3s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603228762/job/75160697580) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 8m 13s | 39m 29s | +31m 16s | +43m 15s |
| `release-checks` | 7m 50s | 38m 4s | +30m 14s | +1h 46m 26s |
| `normal-ci` | 4m 23s | 11m 31s | +7m 8s | +13m 28s |
| `postpublish-telegram` | 3m 28s | 3m 15s | -13s | -11s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25603220476
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25603220476/job/75162685182
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25603228762
  - macos-node: failure - https://github.com/openclaw/openclaw/actions/runs/25603228762/job/75160603594
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25603228934
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160657349
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160714875
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160795381
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160795387
  - install_smoke_release_checks / installer_smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160811203
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160825045
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160825049
  - cross_os_release_checks / Windows / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160825058
  - Run QA Lab parity report: failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160827379
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160857613
  - Run package acceptance / Docker product acceptance / plan_docker_lane_groups: cancelled - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160918999
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160953705
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75160953748
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75161203374
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25603228934/job/75162650222

## Notes

Automatically requested by Full Release Validation 25603220476 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


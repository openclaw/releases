# OpenClaw Release Evidence: main

Generated: 2026-04-29T00:51:26.645Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `main` |
| Release ref input | `main` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `main` |
| Release ref SHA | `28ff82dcdae7f7fb11491deefe48bd82b68eb0bb` |
| Runs at release SHA | none |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `7229ec5e044d` | 20m 8s (+14m 23s) | 36m 6s (+28m 20s) | [25084845944](https://github.com/openclaw/openclaw/actions/runs/25084845944) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `8e5fcfff5026` | 18m 39s (+13m 21s) | 2h 55m 9s (+1h 53m 59s) | [25084875061](https://github.com/openclaw/openclaw/actions/runs/25084875061) | 24 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `8e5fcfff5026` | 16m 39s (+15m 0s) | 6h 3m 8s (+6h 2m 59s) | [25084872852](https://github.com/openclaw/openclaw/actions/runs/25084872852) | 37 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 18m 54s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084845944/job/73498048228) |
| 16m 49s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084845944/job/73498048223) |
| 13m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-media-music-minimax, Native live media musi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498228660) |
| 10m 50s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498228461) |
| 10m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (live-gateway-docker, Docker live gateway, OPENCLAW_LIVE_DOCKER_REP... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498228685) |
| 10m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go, Native live gateway ... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498228656) |
| 9m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, OPENCLAW_LIVE_DOCKER_R... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498228687) |
| 9m 27s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498680317) |
| 9m 25s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498680295) |
| 9m 15s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498680282) |
| 8m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498228645) |
| 8m 56s | `release-checks` | install_smoke_release_checks / install-smoke | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498165319) |
| 8m 51s | `normal-ci` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084875061/job/73498916742) |
| 8m 40s | `normal-ci` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-3) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084875061/job/73498916769) |
| 8m 38s | `normal-ci` | plugin-prerelease-docker-suite / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/25084875061/job/73498161927) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 1m 39s | 16m 39s | +15m 0s | +6h 2m 59s |
| `full-release-validation` | 5m 45s | 20m 8s | +14m 23s | +28m 20s |
| `normal-ci` | 5m 18s | 18m 39s | +13m 21s | +1h 53m 59s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25084845944
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25084845944/job/73499694744
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25084872852
  - install_smoke_release_checks / install-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498165319
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73498511254
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73499059353
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25084872852/job/73499500949

## Notes

Automatically requested by Full Release Validation 25084845944 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


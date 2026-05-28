# OpenClaw Release Evidence: release-2026.4.27

Generated: 2026-04-29T14:14:33.743Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `release-2026.4.27` |
| Release ref input | `release/2026.4.27` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.4.27` |
| Release ref SHA | `04101e42ebac4417c1a48133f33f8b7645f668b8` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `6bbacd14a366` | 22m 44s (+12m 38s) | 28m 30s (+4m 50s) | [25112918883](https://github.com/openclaw/openclaw/actions/runs/25112918883) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `66cdbccc8a2a` | 3m 10s (-4m 27s) | 52m 23s (+9m 43s) | [25112993923](https://github.com/openclaw/openclaw/actions/runs/25112993923) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `66cdbccc8a2a` | 20m 29s (+13m 28s) | 4h 22m 35s (+3h 54m 50s) | [25112996312](https://github.com/openclaw/openclaw/actions/runs/25112996312) | 21 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 21m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112918883/job/73591945647) |
| 15m 24s | `release-checks` | Run Docker release-path validation / prepare_docker_e2e_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592943741) |
| 14m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go, Native live gateway ... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592405063) |
| 11m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592404966) |
| 10m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592405281) |
| 9m 55s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73593091130) |
| 9m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592405046) |
| 9m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73593090961) |
| 9m 27s | `release-checks` | install_smoke_release_checks / docker-e2e-fast | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592259341) |
| 9m 17s | `release-checks` | install_smoke_release_checks / install-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592259336) |
| 7m 31s | `release-checks` | Run repo/live E2E validation / Live media suites (Native live media video plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592404540) |
| 3m 49s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112918883/job/73591945673) |
| 3m 11s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112918883/job/73591945754) |
| 2m 43s | `normal-ci` | checks-fast-contracts-plugins-legacy | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112993923/job/73592055991) |
| 2m 35s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25112993923/job/73592056345) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 7m 1s | 20m 29s | +13m 28s | +3h 54m 50s |
| `full-release-validation` | 10m 6s | 22m 44s | +12m 38s | +4m 50s |
| `normal-ci` | 7m 37s | 3m 10s | -4m 27s | +9m 43s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25112918883
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25112918883/job/73596054008
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25112996312
  - install_smoke_release_checks / docker-e2e-fast: failure - https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592259341
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592893147
  - Run Docker release-path validation / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73592943741
  - Run Docker release-path validation / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73595931525
  - Run Docker release-path validation / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73595931697
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73595932044
  - Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25112996312/job/73595932487

## Notes

Automatically requested by Full Release Validation 25112918883 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


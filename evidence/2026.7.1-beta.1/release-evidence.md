# OpenClaw Release Evidence: 2026.7.1-beta.1

Generated: 2026-07-02T07:35:25.201Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.7.1-beta.1` |
| Release ref input | `v2026.7.1-beta.1` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.7.1-beta.1` |
| Release ref SHA | `4eb1d333cfeca440b796b6a3f70d3c2bef996243` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `plugin-prerelease`, `release-checks`, `product-performance` |
| Package spec | `openclaw@2026.7.1-beta.1` |
| npm status | published |
| npm resolved version | `2026.7.1-beta.1` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-07-02T07:13:30.054Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.7.1-beta.1.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 2 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release/2026.7.1` | `4eb1d333cfec` | 38m 35s | 1h 30m 47s | 38m 3s | [28569693812](https://github.com/openclaw/openclaw/actions/runs/28569693812) | 1 |
| pass | blocking | `normal-ci` | CI | `release/2026.7.1` | `4eb1d333cfec` | 12m 14s | 3h 10m 45s | 12m 13s | [28569815685](https://github.com/openclaw/openclaw/actions/runs/28569815685) | 6 |
| pass | blocking | `plugin-prerelease` | Plugin Prerelease | `release/2026.7.1` | `4eb1d333cfec` | 34m 38s | 1h 42m 18s | 34m 36s | [28569816005](https://github.com/openclaw/openclaw/actions/runs/28569816005) | 12 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.7.1` | `4eb1d333cfec` | 30m 51s | 3h 21m 44s | 30m 45s | [28569815816](https://github.com/openclaw/openclaw/actions/runs/28569815816) | 38 |
| pass | advisory | `product-performance` | OpenClaw Performance full-release-validation-28569693812-1 | `release/2026.7.1` | `4eb1d333cfec` | 8m 42s | 8m 45s | 10s | [28569816262](https://github.com/openclaw/openclaw/actions/runs/28569816262) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 35m 11s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569693812/job/84704844160) |
| 31m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569693812/job/84704844144) |
| 27m 13s | `release-checks` | Run QA Lab runtime parity lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84704888209) |
| 20m 20s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84706281286) |
| 16m 38s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (update-channel-switch--kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569816005/job/84707360874) |
| 16m 1s | `plugin-prerelease` | plugin-prerelease-docker-suite / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569816005/job/84705115456) |
| 14m 42s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84705484397) |
| 13m 51s | `release-checks` | Run package acceptance / Docker product acceptance / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84705922485) |
| 13m 6s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84705484388) |
| 12m 23s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569693812/job/84704844174) |
| 10m 26s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84705484403) |
| 9m 54s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84704910930) |
| 8m 59s | `full-release-validation` | Run product performance evidence | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569693812/job/84704844162) |
| 8m 31s | `product-performance` | Kova mock provider performance | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569816262/job/84704858595) |
| 8m 29s | `normal-ci` | checks-node-core-tooling | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815685/job/84704910915) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 38m 3s | 31s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569693812/job/84709870308) |
| 34m 36s | 2s | `plugin-prerelease` | plugin-prerelease-suite | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569816005/job/84709784449) |
| 30m 45s | 5s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84709202294) |
| 27m 32s | 1m 9s | `release-checks` | Enforce QA Lab runtime tool coverage | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84708731578) |
| 27m 7s | 3s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84708673794) |
| 21m 44s | 3m 43s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84707883894) |
| 21m 43s | 2m 4s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84707883832) |
| 21m 43s | 4m 39s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84707883862) |
| 21m 43s | 4m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-binding-command-escape) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84707883867) |
| 21m 43s | 1m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84707883883) |
| 21m 43s | 1m 37s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84707883901) |
| 21m 43s | 2m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84707883902) |
| 17m 58s | 2m 30s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-22--bundled-plugin-install-uninstall-23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569816005/job/84707360894) |
| 17m 56s | 6m 23s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (npm-onboard-channel-agent--doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569816005/job/84707360830) |
| 17m 56s | 2m 28s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (kitchen-sink-rpc--gateway-network) | success | [job](https://github.com/openclaw/openclaw/actions/runs/28569816005/job/84707360836) |

## Performance Metrics

Run: [28569816262](https://github.com/openclaw/openclaw/actions/runs/28569816262)

### mock-provider

Kova summary:

| Scenario | State | Samples | Health ready | Listen | Agent p95 | Cold | Warm | RSS | CPU |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| agent-cold-warm-message | mock-openai-provider | 3 |  |  | 3,018 ms | 3,023 ms | 2,881 ms | 731 MB | 146 % |

Gateway startup:

| Case | Samples | readyz p50 | readyz p95 | health p50 | listen p50 | ready log p50 | RSS p95 | CPU core p95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| default | 3 | 3,479 ms | 3,487 ms | 3,479 ms | 3,334 ms | 3,422 ms | 728 MB | 1.2 cores |
| skipChannels | 3 | 3,369 ms | 3,404 ms | 3,369 ms | 3,307 ms | 3,339 ms | 687 MB | 1.2 cores |
| oneInternalHook | 3 | 3,429 ms | 3,452 ms | 3,429 ms | 3,376 ms | 3,410 ms | 707 MB | 1.2 cores |
| allInternalHooks | 3 | 3,388 ms | 3,395 ms | 3,382 ms | 3,327 ms | 3,359 ms | 668 MB | 1.2 cores |
| fiftyPlugins | 3 | 3,304 ms | 3,354 ms | 3,304 ms | 3,225 ms | 3,285 ms | 656 MB | 1.2 cores |
| fiftyStartupLazyPlugins | 3 | 3,093 ms | 3,115 ms | 3,088 ms | 3,014 ms | 3,075 ms | 686 MB | 1 cores |

CLI startup:

| Case | Samples | duration p50 | duration p95 | first output p50 | RSS p95 | Exit |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| gatewayHealthJson | 3 | 3,081 ms | 3,606 ms | 3,037 ms | 56.6 MB | code:0x3 |
| configGetGatewayPort | 3 | 1,044 ms | 1,137 ms | 992 ms | 56.6 MB | code:0x3 |


## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


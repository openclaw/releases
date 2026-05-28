# OpenClaw Release Evidence: 2026.5.26-beta.2

Generated: 2026-05-27T08:05:46.716Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.26-beta.2` |
| Release ref input | `v2026.5.26-beta.2` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.26-beta.2` |
| Release ref SHA | `7d89681bb0b5b65d06b969c0f14f313fec3fe434` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `plugin-prerelease`, `release-checks`, `product-performance` |
| Package spec | `openclaw@2026.5.26-beta.2` |
| npm status | published |
| npm resolved version | `2026.5.26-beta.2` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-27T07:52:33.751Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.26-beta.2.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 2 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.26` | `7d89681bb0b5` | 38m 10s | 1h 11m 39s | 37m 48s | [26495937332](https://github.com/openclaw/openclaw/actions/runs/26495937332) | 1 |
| pass | blocking | `normal-ci` | CI | `release/2026.5.26` | `7d89681bb0b5` | 6m 12s | 1h 27m 22s | 18s | [26496169823](https://github.com/openclaw/openclaw/actions/runs/26496169823) | 5 |
| pass | blocking | `plugin-prerelease` | Plugin Prerelease | `release/2026.5.26` | `7d89681bb0b5` | 19m 3s | 1h 11m 6s | 19m 0s | [26496168233](https://github.com/openclaw/openclaw/actions/runs/26496168233) | 12 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.26` | `7d89681bb0b5` | 31m 56s | 3h 21m 31s | 31m 53s | [26496168639](https://github.com/openclaw/openclaw/actions/runs/26496168639) | 32 |
| pass | advisory | `product-performance` | OpenClaw Performance | `release/2026.5.26` | `7d89681bb0b5` | 7m 2s | 7m 12s | 4s | [26496168067](https://github.com/openclaw/openclaw/actions/runs/26496168067) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 32m 33s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26495937332/job/78024765411) |
| 24m 39s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78025756435) |
| 19m 28s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26495937332/job/78024765461) |
| 17m 28s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78025756414) |
| 16m 18s | `release-checks` | Run QA Lab runtime parity lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78025023061) |
| 13m 31s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78026166193) |
| 12m 54s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78025756400) |
| 9m 14s | `plugin-prerelease` | plugin-prerelease-docker-suite / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168233/job/78025032083) |
| 8m 13s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78025048959) |
| 7m 52s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (update-channel-switch--kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168233/job/78026286686) |
| 7m 23s | `full-release-validation` | Run product performance evidence | success | [job](https://github.com/openclaw/openclaw/actions/runs/26495937332/job/78024765420) |
| 6m 57s | `product-performance` | Kova mock provider performance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168067/job/78024789833) |
| 6m 49s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/26495937332/job/78024765418) |
| 6m 28s | `release-checks` | Run QA Lab parity lane (baseline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78025023067) |
| 5m 56s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78025023107) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 37m 48s | 20s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26495937332/job/78029414614) |
| 31m 53s | 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78029329858) |
| 20m 50s | 4s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78027691332) |
| 19m 0s | 2s | `plugin-prerelease` | plugin-prerelease-suite | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168233/job/78027428211) |
| 18m 6s | 43s | `release-checks` | Enforce QA Lab runtime tool coverage | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78027296605) |
| 16m 0s | 3m 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78026987537) |
| 15m 59s | 1m 39s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78026987459) |
| 15m 59s | 2m 4s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78026987462) |
| 15m 59s | 4m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78026987464) |
| 15m 59s | 4m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-binding-command-escape) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78026987468) |
| 15m 59s | 4m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78026987471) |
| 15m 59s | 2m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168639/job/78026987472) |
| 11m 8s | 3m 27s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-2--bundled-plugin-install-uninstall-5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168233/job/78026286678) |
| 11m 6s | 3m 14s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-6--bundled-plugin-install-uninstall-9) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168233/job/78026286667) |
| 11m 6s | 3m 17s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-14--bundled-plugin-install-uninstall-17) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26496168233/job/78026286676) |

## Performance Metrics

Run: [26496168067](https://github.com/openclaw/openclaw/actions/runs/26496168067)

### mock-provider

Kova summary:

| Scenario | State | Samples | Health ready | Listen | Agent p95 | Cold | Warm | RSS | CPU |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| agent-cold-warm-message | mock-openai-provider | 3 |  |  | 2,849 ms | 2,872 ms | 2,401 ms | 671 MB | 138 % |

Gateway startup:

| Case | Samples | readyz p50 | readyz p95 | health p50 | listen p50 | ready log p50 | RSS p95 | CPU core p95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| default | 3 | 1,671 ms | 1,686 ms | 1,685 ms | 1,091 ms | 1,130 ms | 491 MB | 1.3 cores |
| skipChannels | 3 | 1,621 ms | 1,631 ms | 1,621 ms | 1,062 ms | 1,066 ms | 508 MB | 1.2 cores |
| oneInternalHook | 3 | 1,745 ms | 1,751 ms | 1,745 ms | 1,098 ms | 1,103 ms | 508 MB | 1.2 cores |
| allInternalHooks | 3 | 1,672 ms | 1,916 ms | 1,672 ms | 1,117 ms | 1,123 ms | 509 MB | 1.3 cores |
| fiftyPlugins | 3 | 1,813 ms | 1,819 ms | 1,813 ms | 1,220 ms | 1,225 ms | 509 MB | 1.1 cores |
| fiftyStartupLazyPlugins | 3 | 1,615 ms | 1,644 ms | 1,615 ms | 1,015 ms | 1,021 ms | 517 MB | 1.3 cores |

CLI startup:

| Case | Samples | duration p50 | duration p95 | first output p50 | RSS p95 | Exit |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| gatewayHealthJson | 3 | 684 ms | 689 ms | 660 ms | 56.3 MB | code:0x3 |
| configGetGatewayPort | 3 | 397 ms | 405 ms | 389 ms | 56.4 MB | code:1x3 |


## Notes

Generated after beta publish from Full Release Validation 26495937332; beta npm and plugin publish links are recorded on the public GitHub Release.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


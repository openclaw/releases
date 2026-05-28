# OpenClaw Release Evidence: 2026.5.24-beta.2

Generated: 2026-05-25T09:13:44.384Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.24-beta.2` |
| Release ref input | `v2026.5.24-beta.2` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.24-beta.2` |
| Release ref SHA | `abb43c997433697bc215560899d87110daca5a55` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `plugin-prerelease`, `release-checks`, `product-performance` |
| Package spec | `openclaw@2026.5.24-beta.2` |
| npm status | published |
| npm resolved version | `2026.5.24-beta.2` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-25T02:49:56.044Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.24-beta.2.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 2 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.24` | `abb43c997433` | 40m 41s (0s) | 53m 40s (0s) | 40m 22s | [26378909141](https://github.com/openclaw/openclaw/actions/runs/26378909141) | 1 |
| pass | blocking | `normal-ci` | CI | `release/2026.5.24` | `abb43c997433` | 5m 22s (0s) | 1h 29m 53s (0s) | 21s | [26379085065](https://github.com/openclaw/openclaw/actions/runs/26379085065) | 4 |
| pass | blocking | `plugin-prerelease` | Plugin Prerelease | `release/2026.5.24` | `abb43c997433` | 8m 39s (0s) | 49m 12s (0s) | 8m 35s | [26379086960](https://github.com/openclaw/openclaw/actions/runs/26379086960) | 12 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.24` | `abb43c997433` | 33m 2s (0s) | 3h 43m 31s (0s) | 32m 59s | [26379085576](https://github.com/openclaw/openclaw/actions/runs/26379085576) | 32 |
| pass | advisory | `product-performance` | OpenClaw Performance | `release/2026.5.24` | `abb43c997433` | 6m 54s | 7m 4s | 4s | [26392653537](https://github.com/openclaw/openclaw/actions/runs/26392653537) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 33m 31s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26378909141/job/77644752159) |
| 26m 2s | `release-checks` | Run QA Lab runtime parity lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77644883795) |
| 25m 41s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77645260622) |
| 25m 30s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77645260621) |
| 13m 43s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77645260630) |
| 11m 24s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77645436012) |
| 11m 2s | `release-checks` | Run QA Lab parity lane (baseline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77644883797) |
| 9m 18s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26378909141/job/77644752138) |
| 9m 6s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77644883801) |
| 8m 21s | `release-checks` | Run QA Lab parity lane (candidate) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77644883807) |
| 8m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-binding-command-escape) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77646021499) |
| 7m 56s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77644893692) |
| 6m 49s | `product-performance` | Kova mock provider performance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26392653537/job/77685829884) |
| 5m 39s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/26378909141/job/77644752143) |
| 5m 0s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085065/job/77644784625) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 40m 22s | 18s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26378909141/job/77647103978) |
| 32m 59s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77647070718) |
| 27m 42s | 43s | `release-checks` | Enforce QA Lab runtime tool coverage | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77646711770) |
| 26m 16s | 2s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77646613906) |
| 18m 2s | 2m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (root-managed-vps-upgrade) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77646021518) |
| 17m 57s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77646021481) |
| 17m 57s | 1m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77646021494) |
| 17m 57s | 2m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77646021495) |
| 17m 57s | 1m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77646021498) |
| 17m 57s | 8m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-binding-command-escape) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77646021499) |
| 17m 57s | 1m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379085576/job/77646021508) |
| 8m 35s | 3s | `plugin-prerelease` | plugin-prerelease-suite | success | [job](https://github.com/openclaw/openclaw/actions/runs/26379086960/job/77645360101) |
| 6m 50s | 9m 18s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26378909141/job/77644752138) |
| 6m 49s | 5m 39s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/26378909141/job/77644752143) |
| 6m 49s | 33m 31s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26378909141/job/77644752159) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 40m 41s | 40m 41s | 0s | 0s |
| `normal-ci` | 5m 22s | 5m 22s | 0s | 0s |
| `plugin-prerelease` | 8m 39s | 8m 39s | 0s | 0s |
| `release-checks` | 33m 2s | 33m 2s | 0s | 0s |

## Performance Metrics

Run: [26392653537](https://github.com/openclaw/openclaw/actions/runs/26392653537)

### mock-provider

Kova summary:

| Scenario | State | Samples | Health ready | Listen | Agent p95 | Cold | Warm | RSS | CPU |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| agent-cold-warm-message | mock-openai-provider | 3 |  |  | 4,725 ms | 4,746 ms | 4,268 ms | 671 MB | 134 % |

Gateway startup:

| Case | Samples | readyz p50 | readyz p95 | health p50 | listen p50 | ready log p50 | RSS p95 | CPU core p95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| default | 3 | 1,672 ms | 1,681 ms | 1,672 ms | 1,063 ms | 1,128 ms | 491 MB | 1.2 cores |
| skipChannels | 3 | 1,636 ms | 1,653 ms | 1,636 ms | 1,075 ms | 1,145 ms | 491 MB | 1.2 cores |
| oneInternalHook | 3 | 1,695 ms | 1,700 ms | 1,149 ms | 1,073 ms | 1,620 ms | 503 MB | 1.2 cores |
| allInternalHooks | 3 | 1,697 ms | 1,716 ms | 1,194 ms | 1,093 ms | 1,641 ms | 481 MB | 1.2 cores |
| fiftyPlugins | 3 | 1,756 ms | 1,775 ms | 1,756 ms | 1,178 ms | 1,253 ms | 475 MB | 1.2 cores |
| fiftyStartupLazyPlugins | 3 | 1,634 ms | 1,638 ms | 1,634 ms | 1,023 ms | 1,098 ms | 464 MB | 1.2 cores |

CLI startup:

| Case | Samples | duration p50 | duration p95 | first output p50 | RSS p95 | Exit |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| gatewayHealthJson | 3 | 745 ms | 751 ms | 717 ms | 56.3 MB | code:0x3 |
| configGetGatewayPort | 3 | 316 ms | 326 ms | 307 ms | 56.2 MB | code:1x3 |


## Notes

Post-publish Telegram beta E2E: https://github.com/openclaw/openclaw/actions/runs/26380673797

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


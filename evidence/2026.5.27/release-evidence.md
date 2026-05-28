# OpenClaw Release Evidence: 2026.5.27

Generated: 2026-05-28T12:32:07.503Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.27` |
| Release ref input | `v2026.5.27` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.27` |
| Release ref SHA | `27ae826f65256c7fbd1d78475fca87b674a53e7b` |
| Runs at release SHA | none |
| Package spec | `openclaw@2026.5.27` |
| npm status | published |
| npm resolved version | `2026.5.27` |
| npm expected version match | yes |
| npm dist-tags pointing here | `latest` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-28T11:41:30.934Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.27.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 2 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `main` | `3844e035bb0f` | 37m 25s | 1h 7m 36s | 37m 2s | [26569544553](https://github.com/openclaw/openclaw/actions/runs/26569544553) | 1 |
| pass | blocking | `normal-ci` | CI | `main` | `4bd711e1c424` | 5m 43s | 1h 26m 10s | 19s | [26569850872](https://github.com/openclaw/openclaw/actions/runs/26569850872) | 5 |
| pass | blocking | `plugin-prerelease` | Plugin Prerelease | `main` | `4bd711e1c424` | 16m 43s | 1h 8m 6s | 16m 39s | [26569851207](https://github.com/openclaw/openclaw/actions/runs/26569851207) | 12 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `main` | `4bd711e1c424` | 29m 34s | 3h 18m 4s | 29m 31s | [26569853272](https://github.com/openclaw/openclaw/actions/runs/26569853272) | 32 |
| pass | advisory | `product-performance` | OpenClaw Performance | `main` | `4bd711e1c424` | 6m 26s | 6m 36s | 11s | [26569850720](https://github.com/openclaw/openclaw/actions/runs/26569850720) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 30m 12s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569544553/job/78273880571) |
| 24m 6s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78274704621) |
| 18m 55s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78274704645) |
| 17m 20s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569544553/job/78273880711) |
| 16m 55s | `release-checks` | Run QA Lab runtime parity lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78274183134) |
| 16m 15s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78274704649) |
| 11m 42s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78275433344) |
| 8m 5s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78274212494) |
| 8m 2s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (update-channel-switch--kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569851207/job/78275171732) |
| 6m 53s | `full-release-validation` | Run product performance evidence | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569544553/job/78273880568) |
| 6m 40s | `plugin-prerelease` | plugin-prerelease-docker-suite / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569851207/job/78274168126) |
| 6m 24s | `full-release-validation` | Verify Docker runtime image assets | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569544553/job/78272914117) |
| 6m 22s | `product-performance` | Kova mock provider performance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569850720/job/78273905862) |
| 6m 12s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569544553/job/78273880595) |
| 6m 6s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78274183147) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 37m 2s | 22s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569544553/job/78278457617) |
| 29m 31s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78278365136) |
| 19m 0s | 4s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78276781832) |
| 18m 51s | 43s | `release-checks` | Enforce QA Lab runtime tool coverage | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78276759383) |
| 16m 39s | 4s | `plugin-prerelease` | plugin-prerelease-suite | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569851207/job/78276405035) |
| 14m 8s | 3m 58s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78276027302) |
| 14m 8s | 2m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78276027321) |
| 14m 8s | 4m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (root-managed-vps-upgrade) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78276027390) |
| 14m 8s | 3m 39s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78276027419) |
| 14m 7s | 4m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78276027266) |
| 14m 7s | 2m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78276027280) |
| 14m 7s | 1m 34s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569853272/job/78276027290) |
| 8m 35s | 3m 9s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-2--bundled-plugin-install-uninstall-5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569851207/job/78275171679) |
| 8m 35s | 3m 21s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-6--bundled-plugin-install-uninstall-9) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569851207/job/78275171699) |
| 8m 34s | 5m 14s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (npm-onboard-channel-agent--doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26569851207/job/78275171651) |

## Performance Metrics

Run: [26569850720](https://github.com/openclaw/openclaw/actions/runs/26569850720)

### mock-provider

Kova summary:

| Scenario | State | Samples | Health ready | Listen | Agent p95 | Cold | Warm | RSS | CPU |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| agent-cold-warm-message | mock-openai-provider | 3 |  |  | 2,550 ms | 2,561 ms | 2,303 ms | 652 MB | 135 % |

Gateway startup:

| Case | Samples | readyz p50 | readyz p95 | health p50 | listen p50 | ready log p50 | RSS p95 | CPU core p95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| default | 3 | 1,488 ms | 1,545 ms | 1,484 ms | 956 ms | 982 ms | 492 MB | 1.3 cores |
| skipChannels | 3 | 1,482 ms | 1,523 ms | 1,482 ms | 962 ms | 966 ms | 526 MB | 1.4 cores |
| oneInternalHook | 3 | 1,500 ms | 1,510 ms | 1,500 ms | 960 ms | 964 ms | 534 MB | 1.3 cores |
| allInternalHooks | 3 | 1,506 ms | 1,584 ms | 1,506 ms | 997 ms | 1,000 ms | 534 MB | 1.3 cores |
| fiftyPlugins | 3 | 1,691 ms | 1,768 ms | 1,691 ms | 1,112 ms | 1,116 ms | 540 MB | 1.2 cores |
| fiftyStartupLazyPlugins | 3 | 1,476 ms | 1,554 ms | 1,476 ms | 919 ms | 923 ms | 537 MB | 1.4 cores |

CLI startup:

| Case | Samples | duration p50 | duration p95 | first output p50 | RSS p95 | Exit |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| gatewayHealthJson | 3 | 595 ms | 607 ms | 573 ms | 56.3 MB | code:0x3 |
| configGetGatewayPort | 3 | 459 ms | 460 ms | 445 ms | 56.1 MB | code:0x3 |


## Notes

Automatically ingested from Full Release Validation 26569544553. Child runs: OpenClaw Performance: 26569850720; OpenClaw Release Checks: 26569853272; CI: 26569850872; Plugin Prerelease: 26569851207.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


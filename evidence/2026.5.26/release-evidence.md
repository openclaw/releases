# OpenClaw Release Evidence: 2026.5.26

Generated: 2026-05-27T12:53:51.430Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.26` |
| Release ref input | `v2026.5.26` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.26` |
| Release ref SHA | `10ad3aa16068baa84a1bd9ac4f7d42ae725cedb7` |
| Runs at release SHA | none |
| Package spec | `openclaw@2026.5.26` |
| npm status | published |
| npm resolved version | `2026.5.26` |
| npm expected version match | yes |
| npm dist-tags pointing here | `latest` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-27T12:38:41.427Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.26.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 2 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `main` | `f4b9d246216a` | 43m 11s | 1h 17m 32s | 42m 41s | [26508372964](https://github.com/openclaw/openclaw/actions/runs/26508372964) | 1 |
| pass | blocking | `normal-ci` | CI | `main` | `0503853c294b` | 5m 13s | 1h 19m 38s | 24s | [26508639898](https://github.com/openclaw/openclaw/actions/runs/26508639898) | 5 |
| pass | blocking | `plugin-prerelease` | Plugin Prerelease | `main` | `0503853c294b` | 19m 20s | 1h 16m 49s | 19m 17s | [26508639333](https://github.com/openclaw/openclaw/actions/runs/26508639333) | 12 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `main` | `0503853c294b` | 36m 38s | 4h 1m 25s | 36m 35s | [26508649633](https://github.com/openclaw/openclaw/actions/runs/26508649633) | 32 |
| pass | advisory | `product-performance` | OpenClaw Performance | `main` | `0503853c294b` | 8m 33s | 8m 43s | 10s | [26508639403](https://github.com/openclaw/openclaw/actions/runs/26508639403) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 36m 55s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508372964/job/78067524246) |
| 28m 40s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78068733376) |
| 19m 58s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508372964/job/78067524234) |
| 18m 18s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78068733371) |
| 17m 25s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78068733379) |
| 15m 30s | `release-checks` | Run QA Lab runtime parity lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78068160987) |
| 12m 50s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78069377350) |
| 9m 16s | `plugin-prerelease` | plugin-prerelease-docker-suite / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508639333/job/78067829202) |
| 9m 0s | `full-release-validation` | Run product performance evidence | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508372964/job/78067524295) |
| 8m 36s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78068217010) |
| 8m 29s | `product-performance` | Kova mock provider performance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508639403/job/78067553048) |
| 8m 11s | `release-checks` | Run package acceptance / Telegram package acceptance / Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78069121713) |
| 8m 9s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (update-channel-switch--kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508639333/job/78069122641) |
| 6m 14s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78068160934) |
| 6m 14s | `release-checks` | Run package acceptance / Docker product acceptance / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78069433703) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 42m 41s | 28s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508372964/job/78072691913) |
| 36m 35s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78072655213) |
| 25m 14s | 2s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78071017166) |
| 19m 19s | 4m 28s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78070181647) |
| 19m 19s | 3m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78070181652) |
| 19m 19s | 5m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78070181672) |
| 19m 19s | 5m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78070181776) |
| 19m 19s | 5m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78070181777) |
| 19m 19s | 5m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-binding-command-escape) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78070181794) |
| 19m 19s | 3m 39s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78070181796) |
| 19m 19s | 5m 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508649633/job/78070181802) |
| 19m 17s | 2s | `plugin-prerelease` | plugin-prerelease-suite | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508639333/job/78070150257) |
| 11m 6s | 3m 31s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (kitchen-sink-rpc--gateway-network) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508639333/job/78069122627) |
| 11m 6s | 3m 21s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-22--bundled-plugin-install-uninstall-23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508639333/job/78069122670) |
| 11m 5s | 4m 24s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-10--bundled-plugin-install-uninstall-13) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26508639333/job/78069122620) |

## Performance Metrics

Run: [26508639403](https://github.com/openclaw/openclaw/actions/runs/26508639403)

### mock-provider

Kova summary:

| Scenario | State | Samples | Health ready | Listen | Agent p95 | Cold | Warm | RSS | CPU |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| agent-cold-warm-message | mock-openai-provider | 3 |  |  | 2,703 ms | 2,724 ms | 2,308 ms | 669 MB | 139 % |

Gateway startup:

| Case | Samples | readyz p50 | readyz p95 | health p50 | listen p50 | ready log p50 | RSS p95 | CPU core p95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| default | 3 | 1,548 ms | 1,638 ms | 1,542 ms | 1,015 ms | 1,054 ms | 470 MB | 1.3 cores |
| skipChannels | 3 | 1,541 ms | 1,549 ms | 1,540 ms | 1,012 ms | 1,017 ms | 518 MB | 1.3 cores |
| oneInternalHook | 3 | 1,594 ms | 1,623 ms | 1,587 ms | 1,025 ms | 1,030 ms | 499 MB | 1.3 cores |
| allInternalHooks | 3 | 1,565 ms | 1,575 ms | 1,565 ms | 1,026 ms | 1,031 ms | 511 MB | 1.3 cores |
| fiftyPlugins | 3 | 1,648 ms | 1,650 ms | 1,648 ms | 1,099 ms | 1,104 ms | 526 MB | 1.2 cores |
| fiftyStartupLazyPlugins | 3 | 1,498 ms | 1,520 ms | 1,494 ms | 939 ms | 944 ms | 519 MB | 1.3 cores |

CLI startup:

| Case | Samples | duration p50 | duration p95 | first output p50 | RSS p95 | Exit |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| gatewayHealthJson | 3 | 611 ms | 670 ms | 591 ms | 56.2 MB | code:0x3 |
| configGetGatewayPort | 3 | 351 ms | 362 ms | 344 ms | 56.3 MB | code:1x3 |


## Notes

Stable release evidence generated from Full Release Validation 26508372964 after npm/latest publish verification.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


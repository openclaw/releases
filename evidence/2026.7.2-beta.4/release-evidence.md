# OpenClaw Release Evidence: 2026.7.2-beta.4

Generated: 2026-07-24T06:53:18.823Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.7.2-beta.4` |
| Release ref input | `v2026.7.2-beta.4` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.7.2-beta.4` |
| Release ref SHA | `5e63b365d4d3e62ef600b783fad7c5043b6f4738` |
| Runs at release SHA | none |
| Package spec | `openclaw@2026.7.2-beta.4` |
| npm status | published |
| npm resolved version | `2026.7.2-beta.4` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-07-24T06:11:58.181Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.7.2-beta.4.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 2 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release-ci/2b7622d9a3a7-1784869761362` | `2b7622d9a3a7` | 1m 21s | 1m 11s | 1m 8s | [30068669753](https://github.com/openclaw/openclaw/actions/runs/30068669753) | 2 |
| pass | blocking | `normal-ci` | CI full-release-validation-30065809940-1-ci | `release-ci/b88eeddeed15-1784865833044` | `b88eeddeed15` | 18m 7s | 5h 15m 57s | 18m 3s | [30065926582](https://github.com/openclaw/openclaw/actions/runs/30065926582) | 8 |
| pass | blocking | `plugin-prerelease` | Plugin Prerelease full-release-validation-30065809940-1-plugin-prerelease | `release-ci/b88eeddeed15-1784865833044` | `b88eeddeed15` | 15m 13s | 2h 16m 38s | 15m 10s | [30066300014](https://github.com/openclaw/openclaw/actions/runs/30066300014) | 20 |
| pass | blocking | `release-checks` | OpenClaw Release Checks full-release-validation-30065809940-1-release-checks | `release-ci/b88eeddeed15-1784865833044` | `b88eeddeed15` | 36m 13s | 3h 46m 9s | 36m 6s | [30066300466](https://github.com/openclaw/openclaw/actions/runs/30066300466) | 37 |
| pass | advisory | `product-performance` | OpenClaw Performance full-release-validation-30065809940-1 | `release-ci/b88eeddeed15-1784865833044` | `b88eeddeed15` | 8m 50s | 15m 15s | 8m 47s | [30065932302](https://github.com/openclaw/openclaw/actions/runs/30065932302) | 2 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 24m 35s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89398101048) |
| 23m 38s | `release-checks` | Run QA Lab runtime-pair lane (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89397913944) |
| 23m 22s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89399386115) |
| 18m 41s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89397913995) |
| 17m 22s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/30065926582/job/89396848906) |
| 14m 52s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89398101032) |
| 11m 54s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (plugins--kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300014/job/89398234367) |
| 11m 41s | `normal-ci` | checks-node-auto-reply-reply-dispatch | success | [job](https://github.com/openclaw/openclaw/actions/runs/30065926582/job/89396852119) |
| 11m 40s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89397943598) |
| 10m 54s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89398101041) |
| 9m 3s | `plugin-prerelease` | checks-node-extensions-shard-8 | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300014/job/89397875558) |
| 8m 36s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/30065926582/job/89396848991) |
| 8m 33s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (update-channel-switch--plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300014/job/89398234989) |
| 8m 28s | `product-performance` | Kova mock provider performance | success | [job](https://github.com/openclaw/openclaw/actions/runs/30065932302/job/89396805299) |
| 7m 42s | `normal-ci` | checks-node-agentic-agents-embedded | success | [job](https://github.com/openclaw/openclaw/actions/runs/30065926582/job/89396849913) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 36m 6s | 6s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89402209653) |
| 27m 15s | 1m 23s | `release-checks` | Enforce QA Lab runtime tool coverage | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89401165434) |
| 27m 7s | 5s | `release-checks` | Verify QA Lab runtime-pair lanes | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89401150085) |
| 18m 3s | 3s | `normal-ci` | openclaw/ci-gate | success | [job](https://github.com/openclaw/openclaw/actions/runs/30065926582/job/89399026518) |
| 18m 1s | 0s | `normal-ci` | ci-timings-summary | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/30065926582/job/89399027116) |
| 15m 10s | 2s | `plugin-prerelease` | plugin-prerelease-suite | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300014/job/89399683706) |
| 12m 47s | 3s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89399400276) |
| 12m 41s | 23m 22s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89399386115) |
| 12m 41s | 2m 42s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89399386130) |
| 12m 40s | 1m 55s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89399386111) |
| 12m 35s | 3s | `release-checks` | install_smoke_release_checks / root_dockerfile_image_ready | success | [job](https://github.com/openclaw/openclaw/actions/runs/30066300466/job/89399371931) |
| 11m 48s | 1m 25s | `normal-ci` | android-ktlint | success | [job](https://github.com/openclaw/openclaw/actions/runs/30065926582/job/89396848990) |
| 8m 47s | 2s | `product-performance` | Verify artifact-only report mode | success | [job](https://github.com/openclaw/openclaw/actions/runs/30065932302/job/89397904661) |
| 8m 44s | 0s | `product-performance` | Publish ${{ matrix.title }} report | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/30065932302/job/89397904768) |
| 8m 30s | 3m 16s | `normal-ci` | android-build-wear | success | [job](https://github.com/openclaw/openclaw/actions/runs/30065926582/job/89396849038) |

## Performance Metrics

Run: [30065932302](https://github.com/openclaw/openclaw/actions/runs/30065932302)

### mock-provider

### source

Gateway startup:

| Case | Samples | readyz p50 | readyz p95 | health p50 | listen p50 | ready log p50 | RSS p95 | CPU core p95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| default | 3 | 5,861 ms | 7,723 ms | 5,748 ms | 3,012 ms | 5,805 ms | 911 MB | 1.3 cores |
| skipChannels | 3 | 2,989 ms | 3,044 ms | 2,988 ms | 2,909 ms | 2,951 ms | 764 MB | 1.4 cores |
| oneInternalHook | 3 | 4,675 ms | 6,686 ms | 4,674 ms | 4,393 ms | 4,466 ms | 971 MB | 1.3 cores |
| allInternalHooks | 3 | 6,972 ms | 7,101 ms | 6,972 ms | 4,624 ms | 4,670 ms | 968 MB | 1.3 cores |
| fiftyPlugins | 3 | 8,763 ms | 8,767 ms | 8,763 ms | 4,357 ms | 4,443 ms | 1,121 MB | 1.3 cores |
| fiftyStartupLazyPlugins | 3 | 8,624 ms | 9,038 ms | 8,624 ms | 4,035 ms | 4,118 ms | 1,123 MB | 1.3 cores |

CLI startup:

| Case | Samples | duration p50 | duration p95 | first output p50 | RSS p95 | Exit |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| gatewayHealthJson | 3 | 3,858 ms | 3,898 ms | 3,797 ms | 61.6 MB | code:0x3 |
| configGetGatewayPort | 3 | 761 ms | 779 ms | 737 ms | 61.4 MB | code:0x3 |


## Notes

Beta 4 changelog-only validation reused green Code SHA c1ad6d278bba2d5345939b03ba43e532bb05066b evidence.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

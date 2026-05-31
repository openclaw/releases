# OpenClaw Release Evidence: 2026.5.30-beta.1

Generated: 2026-05-31T02:44:46.187Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.30-beta.1` |
| Release ref input | `v2026.5.30-beta.1` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.30-beta.1` |
| Release ref SHA | `effbaeb504e4320fe120b1d0af412c7538f386bd` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `plugin-prerelease`, `release-checks`, `product-performance` |
| Package spec | `openclaw@2026.5.30-beta.1` |
| npm status | published |
| npm resolved version | `2026.5.30-beta.1` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-31T02:29:00.103Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.30-beta.1.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 2 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.30` | `effbaeb504e4` | 30m 19s | 1h 4m 27s | 29m 50s | [26700348878](https://github.com/openclaw/openclaw/actions/runs/26700348878) | 1 |
| pass | blocking | `normal-ci` | CI | `release/2026.5.30` | `effbaeb504e4` | 6m 20s | 2h 3m 26s | 6m 3s | [26700453728](https://github.com/openclaw/openclaw/actions/runs/26700453728) | 6 |
| pass | blocking | `plugin-prerelease` | Plugin Prerelease | `release/2026.5.30` | `effbaeb504e4` | 19m 18s | 1h 16m 26s | 19m 14s | [26700453757](https://github.com/openclaw/openclaw/actions/runs/26700453757) | 12 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.30` | `effbaeb504e4` | 23m 24s | 2h 53m 27s | 23m 20s | [26700454170](https://github.com/openclaw/openclaw/actions/runs/26700454170) | 32 |
| pass | advisory | `product-performance` | OpenClaw Performance | `release/2026.5.30` | `effbaeb504e4` | 7m 28s | 7m 30s | 9s | [26700453640](https://github.com/openclaw/openclaw/actions/runs/26700453640) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 23m 53s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700348878/job/78692300099) |
| 19m 47s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700348878/job/78692300107) |
| 17m 13s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78692595148) |
| 15m 39s | `release-checks` | Run QA Lab runtime parity lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78692387775) |
| 11m 31s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78692804209) |
| 10m 30s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78692595159) |
| 10m 25s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (update-channel-switch--kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700453757/job/78692730894) |
| 8m 4s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78692397550) |
| 8m 4s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78692595152) |
| 7m 49s | `full-release-validation` | Run product performance evidence | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700348878/job/78692300093) |
| 7m 34s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78692387784) |
| 7m 18s | `product-performance` | Kova mock provider performance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700453640/job/78692304719) |
| 6m 51s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78692387790) |
| 6m 50s | `plugin-prerelease` | plugin-prerelease-docker-suite / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700453757/job/78692386175) |
| 6m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700348878/job/78692300102) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 29m 50s | 29s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700348878/job/78693473857) |
| 23m 20s | 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78693450359) |
| 19m 18s | 4s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78693259385) |
| 19m 14s | 4s | `plugin-prerelease` | plugin-prerelease-suite | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700453757/job/78693254978) |
| 17m 35s | 51s | `release-checks` | Enforce QA Lab runtime tool coverage | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78693172603) |
| 14m 31s | 4m 43s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78693020335) |
| 14m 31s | 2m 45s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78693020336) |
| 14m 30s | 2m 43s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78693020326) |
| 14m 30s | 1m 45s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78693020331) |
| 14m 30s | 3m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78693020332) |
| 14m 30s | 3m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78693020333) |
| 14m 30s | 1m 43s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700454170/job/78693020340) |
| 8m 47s | 4m 42s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-6--bundled-plugin-install-uninstall-9) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700453757/job/78692730921) |
| 8m 46s | 10m 25s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (update-channel-switch--kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700453757/job/78692730894) |
| 8m 46s | 4m 6s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-2--bundled-plugin-install-uninstall-5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26700453757/job/78692730895) |

## Performance Metrics

Run: [26700453640](https://github.com/openclaw/openclaw/actions/runs/26700453640)

### mock-provider

Kova summary:

| Scenario | State | Samples | Health ready | Listen | Agent p95 | Cold | Warm | RSS | CPU |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| agent-cold-warm-message | mock-openai-provider | 3 |  |  | 2,389 ms | 2,407 ms | 2,104 ms | 641 MB | 145 % |

Gateway startup:

| Case | Samples | readyz p50 | readyz p95 | health p50 | listen p50 | ready log p50 | RSS p95 | CPU core p95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| default | 3 | 1,483 ms | 1,505 ms | 1,483 ms | 1,087 ms | 1,127 ms | 488 MB | 1.3 cores |
| skipChannels | 3 | 1,475 ms | 1,515 ms | 1,474 ms | 1,083 ms | 1,087 ms | 516 MB | 1.3 cores |
| oneInternalHook | 3 | 1,514 ms | 1,563 ms | 1,514 ms | 1,100 ms | 1,103 ms | 549 MB | 1.3 cores |
| allInternalHooks | 3 | 1,538 ms | 1,541 ms | 1,537 ms | 1,146 ms | 1,150 ms | 532 MB | 1.3 cores |
| fiftyPlugins | 3 | 1,660 ms | 1,666 ms | 1,660 ms | 1,248 ms | 1,252 ms | 508 MB | 1.2 cores |
| fiftyStartupLazyPlugins | 3 | 1,428 ms | 1,461 ms | 1,427 ms | 1,021 ms | 1,025 ms | 524 MB | 0.7 cores |

CLI startup:

| Case | Samples | duration p50 | duration p95 | first output p50 | RSS p95 | Exit |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| gatewayHealthJson | 3 | 2,042 ms | 2,043 ms | 2,010 ms | 56.3 MB | code:0x3 |
| configGetGatewayPort | 3 | 451 ms | 462 ms | 438 ms | 56.3 MB | code:0x3 |


## Notes

Automatically ingested from Full Release Validation 26700348878. Child runs: OpenClaw Performance: 26700453640; OpenClaw Release Checks: 26700454170; CI: 26700453728; Plugin Prerelease: 26700453757.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


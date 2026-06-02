# OpenClaw Release Evidence: 2026.6.1-beta.2

Generated: 2026-06-02T15:21:49.519Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.6.1-beta.2` |
| Release ref input | `v2026.6.1-beta.2` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.6.1-beta.2` |
| Release ref SHA | `5ffec9056c906b3e697c70054360aed1b3560109` |
| Runs at release SHA | none |
| Package spec | `openclaw@2026.6.1-beta.2` |
| npm status | published |
| npm resolved version | `2026.6.1-beta.2` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-06-02T15:11:21.212Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.6.1-beta.2.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 4 | 0 | 0 | 0 |
| Advisory | 2 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `main` | `00d846daf767` | 48m 30s | 1h 37m 32s | 47m 49s | [26824750752](https://github.com/openclaw/openclaw/actions/runs/26824750752) | 2 |
| pass | blocking | `normal-ci` | CI | `main` | `00d846daf767` | 7m 42s | 2h 59m 31s | 7m 26s | [26825140257](https://github.com/openclaw/openclaw/actions/runs/26825140257) | 6 |
| pass | blocking | `plugin-prerelease` | Plugin Prerelease | `main` | `00d846daf767` | 21m 47s | 1h 30m 53s | 21m 42s | [26825140475](https://github.com/openclaw/openclaw/actions/runs/26825140475) | 12 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `main` | `00d846daf767` | 40m 55s | 10h 4m 43s | 40m 52s | [26825140388](https://github.com/openclaw/openclaw/actions/runs/26825140388) | 52 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `main` | `00d846daf767` | 3m 34s | 3m 14s | 18s | [26825363156](https://github.com/openclaw/openclaw/actions/runs/26825363156) | 1 |
| pass | advisory | `product-performance` | OpenClaw Performance | `main` | `00d846daf767` | 10m 54s | 10m 51s | 17s | [26825142116](https://github.com/openclaw/openclaw/actions/runs/26825142116) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 41m 19s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26824750752/job/79090291438) |
| 31m 22s | `release-checks` | Run QA Lab runtime parity lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79090757500) |
| 25m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627729) |
| 22m 1s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26824750752/job/79090291474) |
| 16m 48s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79091687319) |
| 16m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.22) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627589) |
| 15m 19s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.27) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627747) |
| 15m 13s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627798) |
| 14m 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.26) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627575) |
| 14m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.28) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627625) |
| 13m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627690) |
| 13m 18s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093436198) |
| 12m 19s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (update-channel-switch--kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140475/job/79092363060) |
| 11m 11s | `full-release-validation` | Run product performance evidence | success | [job](https://github.com/openclaw/openclaw/actions/runs/26824750752/job/79090291659) |
| 10m 36s | `product-performance` | Kova mock provider performance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825142116/job/79090354978) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 47m 49s | 40s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26824750752/job/79099488972) |
| 40m 52s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79099412603) |
| 40m 46s | 3s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79099392178) |
| 33m 25s | 1m 11s | `release-checks` | Enforce QA Lab runtime tool coverage | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79097738494) |
| 21m 42s | 4s | `plugin-prerelease` | plugin-prerelease-suite | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140475/job/79095102746) |
| 15m 9s | 1m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627545) |
| 15m 9s | 13m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627690) |
| 15m 9s | 5m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627789) |
| 15m 8s | 2m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627547) |
| 15m 8s | 3m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627554) |
| 15m 8s | 1m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627573) |
| 15m 8s | 14m 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.26) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140388/job/79093627575) |
| 10m 18s | 3m 58s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/26824750752/job/79091127356) |
| 9m 21s | 2m 41s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (kitchen-sink-rpc--gateway-network) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140475/job/79092362884) |
| 9m 21s | 4m 33s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (npm-onboard-channel-agent--doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26825140475/job/79092362924) |

## Performance Metrics

Run: [26825142116](https://github.com/openclaw/openclaw/actions/runs/26825142116)

### mock-provider

Kova summary:

| Scenario | State | Samples | Health ready | Listen | Agent p95 | Cold | Warm | RSS | CPU |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| agent-cold-warm-message | mock-openai-provider | 3 |  |  | 2,749 ms | 2,763 ms | 2,463 ms | 682 MB | 138 % |

Gateway startup:

| Case | Samples | readyz p50 | readyz p95 | health p50 | listen p50 | ready log p50 | RSS p95 | CPU core p95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| default | 3 | 1,666 ms | 1,687 ms | 1,665 ms | 1,194 ms | 1,235 ms | 494 MB | 1.2 cores |
| skipChannels | 3 | 1,651 ms | 1,671 ms | 1,646 ms | 1,183 ms | 1,186 ms | 512 MB | 1.2 cores |
| oneInternalHook | 3 | 1,745 ms | 1,750 ms | 1,745 ms | 1,226 ms | 1,229 ms | 504 MB | 1.2 cores |
| allInternalHooks | 3 | 1,665 ms | 1,667 ms | 1,659 ms | 1,233 ms | 1,236 ms | 513 MB | 1.3 cores |
| fiftyPlugins | 3 | 1,835 ms | 1,837 ms | 1,834 ms | 1,376 ms | 1,414 ms | 526 MB | 1.1 cores |
| fiftyStartupLazyPlugins | 3 | 1,591 ms | 1,613 ms | 1,591 ms | 1,147 ms | 1,182 ms | 520 MB | 1.3 cores |

CLI startup:

| Case | Samples | duration p50 | duration p95 | first output p50 | RSS p95 | Exit |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| gatewayHealthJson | 3 | 2,491 ms | 3,417 ms | 2,459 ms | 56.5 MB | code:0x3 |
| configGetGatewayPort | 3 | 574 ms | 581 ms | 559 ms | 56.3 MB | code:0x3 |


## Notes

Generated after beta publish from Full Release Validation 26824750752; beta npm, plugin npm, ClawHub, and Telegram publish/proof links are recorded on the public GitHub Release.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 2026.5.20

Generated: 2026-05-21T22:21:43.435Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.20` |
| Release ref input | `v2026.5.20` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.20` |
| Release ref SHA | `e510042870cf248c0e0461b6f8d427326266141d` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `plugin-prerelease`, `release-checks`, `npm-telegram` |
| Package spec | `openclaw@2026.5.20` |
| npm status | published |
| npm resolved version | `2026.5.20` |
| npm expected version match | yes |
| npm dist-tags pointing here | `latest` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-21T20:41:31.699Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.20.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 2 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.20` | `e510042870cf` | 52m 3s (0s) | 1h 7m 20s (0s) | 51m 39s | [26248546974](https://github.com/openclaw/openclaw/actions/runs/26248546974) | 1 |
| pass | blocking | `normal-ci` | CI | `release/2026.5.20` | `e510042870cf` | 5m 16s (0s) | 1h 27m 56s (0s) | 20s | [26248760810](https://github.com/openclaw/openclaw/actions/runs/26248760810) | 4 |
| pass | blocking | `plugin-prerelease` | Plugin Prerelease | `release/2026.5.20` | `e510042870cf` | 9m 27s | 48m 38s | 9m 22s | [26248761192](https://github.com/openclaw/openclaw/actions/runs/26248761192) | 12 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.20` | `e510042870cf` | 46m 47s (0s) | 3h 16m 9s (0s) | 46m 43s | [26248762847](https://github.com/openclaw/openclaw/actions/runs/26248762847) | 31 |
| pass | advisory | `npm-telegram` | NPM Telegram Beta E2E | `release/2026.5.20` | `e510042870cf` | 3m 18s | 3m 4s | 13s | [26252161788](https://github.com/openclaw/openclaw/actions/runs/26252161788) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 47m 26s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248546974/job/77253995562) |
| 39m 2s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77255349562) |
| 19m 36s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77255349671) |
| 17m 33s | `release-checks` | Run QA Lab runtime parity lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77254285723) |
| 16m 29s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77255349569) |
| 9m 45s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248546974/job/77253995572) |
| 8m 55s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77255733201) |
| 8m 11s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77254317441) |
| 6m 43s | `release-checks` | Run QA Lab parity lane (baseline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77254285755) |
| 6m 21s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77254285823) |
| 5m 47s | `release-checks` | Run QA Lab parity lane (candidate) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77254285824) |
| 5m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248546974/job/77253995581) |
| 5m 21s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77254285700) |
| 4m 57s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248760810/job/77254062195) |
| 4m 21s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248760810/job/77254062169) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 51m 39s | 23s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248546974/job/77262111804) |
| 46m 43s | 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77262004282) |
| 19m 10s | 53s | `release-checks` | Enforce QA Lab runtime tool coverage | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77257329928) |
| 16m 37s | 4s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77256895501) |
| 13m 51s | 1m 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77256394595) |
| 13m 50s | 1m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77256394564) |
| 13m 50s | 1m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77256394569) |
| 13m 50s | 2m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (root-managed-vps-upgrade) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77256394579) |
| 13m 50s | 1m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77256394588) |
| 13m 50s | 1m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77256394589) |
| 13m 50s | 1m 44s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248762847/job/77256394596) |
| 9m 22s | 4s | `plugin-prerelease` | plugin-prerelease-suite | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248761192/job/77255619186) |
| 5m 29s | 3m 50s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (update-channel-switch--kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248761192/job/77254928639) |
| 5m 21s | 1m 39s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-3--bundled-plugin-install-uninstall-6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248761192/job/77254928574) |
| 5m 21s | 1m 29s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-11--bundled-plugin-install-uninstall-14) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26248761192/job/77254928579) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 52m 3s | 52m 3s | 0s | 0s |
| `normal-ci` | 5m 16s | 5m 16s | 0s | 0s |
| `release-checks` | 46m 47s | 46m 47s | 0s | 0s |

## Notes

Backfilled after 2026.5.20 public release closeout. Public release verification links this durable evidence report instead of local Parallels proof paths.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


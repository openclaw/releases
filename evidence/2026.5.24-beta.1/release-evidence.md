# OpenClaw Release Evidence: 2026.5.24-beta.1

Generated: 2026-05-24T15:05:23.654Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.24-beta.1` |
| Release ref input | `refs/tags/v2026.5.24-beta.1` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.24-beta.1` |
| Release ref SHA | `0e2e7c66bd6a904518b9ca9efd54b9bb1a4c8c2c` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `plugin-prerelease`, `release-checks` |
| Package spec | `openclaw@2026.5.24-beta.1` |
| npm status | published |
| npm resolved version | `2026.5.24-beta.1` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-24T14:42:42.399Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.24-beta.1.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 4 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.24` | `0e2e7c66bd6a` | 37m 57s | 53m 14s | 37m 40s | [26362633403](https://github.com/openclaw/openclaw/actions/runs/26362633403) | 1 |
| pass | blocking | `normal-ci` | CI | `release/2026.5.24` | `0e2e7c66bd6a` | 4m 54s | 1h 25m 8s | 25s | [26362749005](https://github.com/openclaw/openclaw/actions/runs/26362749005) | 4 |
| pass | blocking | `plugin-prerelease` | Plugin Prerelease | `release/2026.5.24` | `0e2e7c66bd6a` | 9m 40s | 48m 52s | 9m 36s | [26362749297](https://github.com/openclaw/openclaw/actions/runs/26362749297) | 12 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.24` | `0e2e7c66bd6a` | 32m 2s | 3h 17m 26s | 31m 57s | [26362749149](https://github.com/openclaw/openclaw/actions/runs/26362749149) | 32 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `main` | `01c5ab8d138d` | 3m 24s | 3m 13s | 11s | [26364277200](https://github.com/openclaw/openclaw/actions/runs/26364277200) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 32m 27s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362633403/job/77601046211) |
| 25m 54s | `release-checks` | Run QA Lab runtime parity lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601150780) |
| 25m 22s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601443029) |
| 18m 19s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601443017) |
| 15m 7s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601443016) |
| 10m 40s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601643295) |
| 10m 17s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362633403/job/77601046207) |
| 10m 0s | `release-checks` | Run QA Lab parity lane (baseline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601150798) |
| 9m 37s | `release-checks` | Run QA Lab parity lane (candidate) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601150790) |
| 8m 18s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601150788) |
| 8m 0s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601162181) |
| 6m 17s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601150789) |
| 5m 10s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362633403/job/77601046196) |
| 4m 50s | `full-release-validation` | Verify Docker runtime-assets prune path | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362633403/job/77600749649) |
| 4m 34s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749005/job/77601069779) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 37m 40s | 17s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362633403/job/77602970672) |
| 31m 57s | 4s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77602940508) |
| 27m 38s | 57s | `release-checks` | Enforce QA Lab runtime tool coverage | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77602676599) |
| 14m 48s | 3s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601925066) |
| 11m 44s | 1m 19s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601741317) |
| 11m 44s | 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601741318) |
| 11m 44s | 1m 58s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601741319) |
| 11m 44s | 2m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (root-managed-vps-upgrade) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601741321) |
| 11m 44s | 1m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601741325) |
| 11m 44s | 1m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601741327) |
| 11m 44s | 3m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749149/job/77601741332) |
| 9m 36s | 3s | `plugin-prerelease` | plugin-prerelease-suite | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749297/job/77601626251) |
| 5m 24s | 1m 20s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (mcp-channels--bundled-plugin-install-uninstall-1) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749297/job/77601364283) |
| 5m 21s | 1m 37s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (bundled-plugin-install-uninstall-10--bundled-plugin-install-uninstall-13) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749297/job/77601364290) |
| 5m 20s | 4m 15s | `plugin-prerelease` | plugin-prerelease-docker-suite / Docker E2E targeted lanes (update-channel-switch--kitchen-sink-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26362749297/job/77601364286) |

## Notes

Backfilled after beta publish. Public Full Release Validation, child CI runs, and post-publish Telegram proof are authoritative.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


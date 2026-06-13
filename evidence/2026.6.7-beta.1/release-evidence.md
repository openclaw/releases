# OpenClaw Release Evidence: 2026.6.7-beta.1

Generated: 2026-06-13T11:25:43.307Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.6.7-beta.1` |
| Release ref input | `v2026.6.7-beta.1` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.6.7-beta.1` |
| Release ref SHA | `45a103a903872bcf6b26d5eba4cc2db0ff68bc69` |
| Runs at release SHA | `npm-preflight`, `npm-publish` |
| Package spec | `openclaw@2026.6.7-beta.1` |
| npm status | published |
| npm resolved version | `2026.6.7-beta.1` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-06-13T10:58:05.977Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.6.7-beta.1.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `npm-preflight` | OpenClaw NPM Release | `release/2026.6.7` | `45a103a90387` | 11m 20s | 11m 10s | 9s | [27463866154](https://github.com/openclaw/openclaw/actions/runs/27463866154) | 4 |
| pass | blocking | `full-release-validation` | Full Release Validation | `main` | `c9c19a110669` | 52m 9s | 1h 33m 11s | 51m 42s | [27463593355](https://github.com/openclaw/openclaw/actions/runs/27463593355) | 1 |
| pass | blocking | `npm-publish` | OpenClaw NPM Release | `release/2026.6.7` | `45a103a90387` | 3m 55s | 2m 47s | 1m 21s | [27464735158](https://github.com/openclaw/openclaw/actions/runs/27464735158) | 0 |
| pass | advisory | `package-acceptance` | Package Acceptance | `main` | `d3e7e0366907` | 24m 13s | 1h 7m 36s | 24m 10s | [27464849036](https://github.com/openclaw/openclaw/actions/runs/27464849036) | 17 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 36m 18s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463593355/job/81182714074) |
| 35m 36s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463593355/job/81182714071) |
| 13m 52s | `package-acceptance` | Docker product acceptance / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81185513324) |
| 11m 10s | `npm-preflight` | preflight_openclaw_npm | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463866154/job/81182573047) |
| 8m 21s | `full-release-validation` | Run product performance evidence | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463593355/job/81182714081) |
| 7m 5s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463593355/job/81182714076) |
| 6m 12s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335165) |
| 5m 8s | `full-release-validation` | Verify Docker runtime image assets | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463593355/job/81182425083) |
| 5m 4s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (root-managed-vps-upgrade) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335133) |
| 4m 57s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335125) |
| 3m 40s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335128) |
| 3m 32s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335127) |
| 3m 25s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335113) |
| 3m 14s | `package-acceptance` | Telegram package acceptance / Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81185421408) |
| 3m 3s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (openwebui) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335161) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 51m 42s | 27s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463593355/job/81184820732) |
| 24m 10s | 3s | `package-acceptance` | Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186689920) |
| 18m 2s | 3m 32s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335127) |
| 18m 2s | 2m 45s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (npm-onboard-channel-agent) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335139) |
| 18m 2s | 1m 39s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (cron-mcp-cleanup) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335207) |
| 17m 58s | 5m 4s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (root-managed-vps-upgrade) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335133) |
| 17m 56s | 3m 25s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335113) |
| 17m 56s | 4m 57s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335125) |
| 17m 56s | 3m 40s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335128) |
| 17m 56s | 1m 50s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335137) |
| 17m 56s | 1m 38s | `package-acceptance` | Docker product acceptance / Docker E2E targeted lanes (mcp-channels) | success | [job](https://github.com/openclaw/openclaw/actions/runs/27464849036/job/81186335149) |
| 15m 29s | 35m 36s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463593355/job/81182714071) |
| 15m 29s | 8m 21s | `full-release-validation` | Run product performance evidence | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463593355/job/81182714081) |
| 15m 23s | 36m 18s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463593355/job/81182714074) |
| 15m 23s | 7m 5s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/27463593355/job/81182714076) |

## Notes

OpenClaw 2026.6.7-beta.1 published to npm dist-tag beta. Registry verified openclaw@beta resolves to 2026.6.7-beta.1. GitHub prerelease target verified at 45a103a903872bcf6b26d5eba4cc2db0ff68bc69. Local provider-secret preflight was not possible from this shell because OPENAI_API_KEY, ANTHROPIC_API_KEY/ANTHROPIC_API_TOKEN, and FIREWORKS_API_KEY were absent; Full Release Validation covered the Actions secret-backed release lanes.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

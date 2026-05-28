# OpenClaw Release Evidence: 2026.5.7-beta.1

Generated: 2026-05-07T16:15:21.134Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.7-beta.1` |
| Release ref input | `release/2026.5.7` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.5.7` |
| Release ref SHA | `c5c7d102db0c66911335171d21718f5a7297af3f` |
| Runs at release SHA | none |
| Package spec | `openclaw@2026.5.7-beta.1` |
| npm status | published |
| npm resolved version | `2026.5.7-beta.1` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-07T15:34:57.240Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.7-beta.1.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `95a1c915312a` | 20m 51s (-7s) | 59m 12s (-18m 33s) | 19m 51s | [25506845795](https://github.com/openclaw/openclaw/actions/runs/25506845795) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `95a1c915312a` | 14m 3s (-4m 25s) | 8h 13m 2s (-2h 17m 58s) | 14m 2s | [25507123165](https://github.com/openclaw/openclaw/actions/runs/25507123165) | 1 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `95a1c915312a` | 13m 55s (-5m 24s) | 9h 4m 4s (-5h 17m 7s) | 13m 56s | [25507129170](https://github.com/openclaw/openclaw/actions/runs/25507129170) | 6 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `main` | `95a1c915312a` | 14m 4s (-4m 25s) | 14m 0s (-4m 22s) | 3s | [25507122810](https://github.com/openclaw/openclaw/actions/runs/25507122810) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 14m 35s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25506845795/job/74855678339) |
| 14m 31s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25506845795/job/74855677938) |
| 14m 29s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25506845795/job/74855677946) |
| 14m 27s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25506845795/job/74855677907) |
| 14m 0s | `postpublish-telegram` | Run package Telegram E2E | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507122810/job/74855722103) |
| 13m 36s | `normal-ci` | checks-windows-node-test | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794009) |
| 13m 36s | `normal-ci` | checks-fast-contracts-channels-c | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794047) |
| 13m 36s | `normal-ci` | checks-fast-contracts-channels-a | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794060) |
| 13m 36s | `normal-ci` | checks-fast-contracts-channels-b | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794158) |
| 13m 36s | `normal-ci` | checks-node-compat-node22 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794188) |
| 13m 36s | `normal-ci` | android-build-play | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794193) |
| 13m 36s | `normal-ci` | checks-fast-bundled | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794205) |
| 13m 36s | `normal-ci` | checks-fast-contracts-plugins-c | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794210) |
| 13m 36s | `normal-ci` | android-test-play | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794251) |
| 13m 36s | `normal-ci` | android-test-third-party | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794280) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 19m 51s | 59s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25506845795/job/74858444164) |
| 14m 2s |  | `normal-ci` | checks-fast-contracts-channels | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858356840) |
| 14m 2s |  | `normal-ci` | build-smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858356966) |
| 14m 2s |  | `normal-ci` | matrix.check_name | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858356971) |
| 14m 2s |  | `normal-ci` | matrix.check_name | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858356995) |
| 14m 2s | 0s | `normal-ci` | checks-fast-contracts-plugins | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858357029) |
| 14m 2s | 0s | `normal-ci` | check-additional | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858357113) |
| 14m 2s | 0s | `normal-ci` | checks-node-core | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858357226) |
| 14m 2s | 0s | `normal-ci` | check | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858357340) |
| 13m 56s |  | `release-checks` | Run QA Lab parity report | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507129170/job/74858359516) |
| 13m 56s | 0s | `release-checks` | Run package acceptance / Docker product acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25507129170/job/74858360123) |
| 13m 56s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507129170/job/74858360391) |
| 13m 56s | 0s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507129170/job/74858360456) |
| 13m 56s | 0s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507129170/job/74858360531) |
| 13m 56s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25507129170/job/74858360623) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 19m 19s | 13m 55s | -5m 24s | -5h 17m 7s |
| `normal-ci` | 18m 28s | 14m 3s | -4m 25s | -2h 17m 58s |
| `postpublish-telegram` | 18m 29s | 14m 4s | -4m 25s | -4m 22s |
| `full-release-validation` | 20m 58s | 20m 51s | -7s | -18m 33s |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25506845795
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25506845795/job/74855677907
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25506845795/job/74855677938
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25506845795/job/74855677946
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25506845795/job/74858444164
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794009
  - checks-fast-contracts-channels-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794047
  - checks-fast-contracts-channels-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794060
  - checks-fast-contracts-channels-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794158
  - checks-node-compat-node22: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794188
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794193
  - checks-fast-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794205
  - checks-fast-contracts-plugins-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794210
  - android-test-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794251
  - android-test-third-party: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794280
  - checks-fast-contracts-plugins-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794305
  - check-test-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794314
  - check-additional-runtime-topology-architecture: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794326
  - check-prod-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794335
  - checks-fast-contracts-plugins-d: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794340
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794343
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794382
  - check-additional-boundaries-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794393
  - check-additional-extension-channels: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794408
  - checks-fast-contracts-plugins-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794413
  - check-additional-boundaries-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794420
  - check-additional-extension-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794431
  - check-additional-boundaries-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794449
  - check-additional-boundaries-d: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794499
  - check-additional-extension-package-boundary: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794539
  - checks-node-agentic-control-plane-auth-node: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794606
  - checks-node-core-runtime-infra-state: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794650
  - checks-node-agentic-control-plane-runtime: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794659
  - checks-node-agentic-control-plane-http-models: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794671
  - checks-node-agentic-control-plane-http-plugin-ws: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794681
  - checks-node-agentic-control-plane-agent-chat: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794689
  - checks-node-agentic-control-plane-startup-runtime: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794708
  - checks-node-core-runtime-infra-process: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74855794720
  - checks-fast-contracts-channels: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858356840
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858356966
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858356971
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858356995
  - checks-fast-contracts-plugins: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858357029
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858357113
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858357226
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507123165/job/74858357340
- `postpublish-telegram`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507122810
  - Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25507122810/job/74855722103

## Notes

Automatically requested by Full Release Validation 25506845795 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


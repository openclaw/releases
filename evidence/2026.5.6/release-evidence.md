# OpenClaw Release Evidence: 2026.5.6

Generated: 2026-05-07T00:26:01.390Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.6` |
| Release ref input | `c97b9f79ec43b531a3472c3219ca51efbf7695a3` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `c97b9f79ec43b531a3472c3219ca51efbf7695a3` |
| Release ref SHA | `c97b9f79ec43b531a3472c3219ca51efbf7695a3` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `postpublish-telegram` |
| Package spec | `openclaw@2026.5.6` |
| npm status | published |
| npm resolved version | `2026.5.6` |
| npm expected version match | yes |
| npm dist-tags pointing here | `latest` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-06T17:33:28.172Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.6.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/c97b9f79ec43-1778091585276` | `c97b9f79ec43` | 6h 5m 45s | 17h 6m 19s | 6h 5m 25s | [25453157648](https://github.com/openclaw/openclaw/actions/runs/25453157648) | 0 |
| running | blocking | `normal-ci` | CI | `release-ci/c97b9f79ec43-1778091585276` | `c97b9f79ec43` | 34s | 1h 26m 10s | 5h 45m 43s | [25453175948](https://github.com/openclaw/openclaw/actions/runs/25453175948) | 4 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/c97b9f79ec43-1778091585276` | `c97b9f79ec43` | 5h 45m 50s | 1m 51s | 5h 43m 58s | [25453179719](https://github.com/openclaw/openclaw/actions/runs/25453179719) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 6h 5m 0s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531345) |
| 5h 0m 14s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531243) |
| 4h 0m 19s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531259) |
| 2h 0m 17s | `full-release-validation` | Run package Telegram E2E | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531703) |
| 3m 48s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649480) |
| 2m 28s | `normal-ci` | checks-node-core-runtime-infra-state | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649680) |
| 2m 14s | `normal-ci` | check-additional-extension-package-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649467) |
| 2m 12s | `normal-ci` | checks-node-core-runtime-shared | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649646) |
| 2m 7s | `normal-ci` | checks-node-core-runtime-infra-process | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649631) |
| 2m 6s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649380) |
| 1m 57s | `normal-ci` | checks-fast-contracts-channels-c | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649284) |
| 1m 54s | `normal-ci` | checks-node-agentic-gateway-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649822) |
| 1m 51s | `normal-ci` | checks-node-auto-reply-reply-agent-runner | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649697) |
| 1m 51s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453179719/job/74675594134) |
| 1m 50s | `normal-ci` | check-additional-extension-bundled | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649435) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6h 5m 25s | 19s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74727883806) |
| 5h 45m 43s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74725931189) |
| 5h 45m 11s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74725866690) |
| 5h 45m 11s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74725866695) |
| 5h 45m 10s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74725866700) |
| 5h 45m 4s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74725866701) |
| 5h 44m 27s | 3s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74725805555) |
| 5h 44m 25s | 4s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74725790308) |
| 5h 43m 58s | 1m 51s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453179719/job/74675594134) |
| 5h 43m 13s | 1m 12s | `normal-ci` | checks-fast-contracts-plugins-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649292) |
| 5h 43m 13s | 51s | `normal-ci` | checks-fast-bundled | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649297) |
| 5h 43m 13s | 42s | `normal-ci` | checks-fast-contracts-plugins-d | success | [job](https://github.com/openclaw/openclaw/actions/runs/25453175948/job/74675649317) |
| 23s | 6h 5m 0s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531345) |
| 23s | 2h 0m 17s | `full-release-validation` | Run package Telegram E2E | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531703) |
| 19s | 5h 0m 14s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531243) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25453157648
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531243
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531259
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531345
  - Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74675531703
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25453157648/job/74727883806

## Notes

Automatically requested by Full Release Validation 25453157648 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


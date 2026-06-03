# OpenClaw Release Evidence: 2026.6.1

Generated: 2026-06-03T21:31:48.382Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.6.1` |
| Release ref input | `v2026.6.1` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.6.1` |
| Release ref SHA | `2e08f0f4221f522b60423ed6ffd83427942b28de` |
| Runs at release SHA | `npm-preflight`, `plugin-npm-publish`, `plugin-clawhub-publish`, `openclaw-npm-publish` |
| Package spec | `openclaw@2026.6.1` |
| npm status | published |
| npm resolved version | `2026.6.1` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta`, `latest` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-06-03T19:35:05.903Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.6.1.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 9 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `full-release-validation` | Full Release Validation | `main` | `286e5ffe0767` | 42m 4s | 1h 31m 23s | 1h 57m 2s | [26900640419](https://github.com/openclaw/openclaw/actions/runs/26900640419) | 2 |
| pass | blocking | `npm-preflight` | OpenClaw NPM Release | `validation/release-2026.6.1-2e08f0f` | `2e08f0f4221f` | 11m 13s | 11m 3s | 9s | [26900686846](https://github.com/openclaw/openclaw/actions/runs/26900686846) | 4 |
| pass | blocking | `plugin-npm-publish` | Plugin NPM Release | `release/2026.6.1` | `2e08f0f4221f` | 7m 25s | 1h 11m 2s | 6m 6s | [26907235209](https://github.com/openclaw/openclaw/actions/runs/26907235209) | 0 |
| pass | blocking | `plugin-clawhub-publish` | Plugin ClawHub Release | `release/2026.6.1` | `2e08f0f4221f` | 17m 0s | 2h 58m 30s | 14m 3s | [26907239724](https://github.com/openclaw/openclaw/actions/runs/26907239724) | 0 |
| pass | blocking | `openclaw-npm-publish` | OpenClaw NPM Release | `release/2026.6.1` | `2e08f0f4221f` | 13m 13s | 2m 36s | 10m 44s | [26907625257](https://github.com/openclaw/openclaw/actions/runs/26907625257) | 0 |
| pass | blocking | `package-telegram-e2e` | NPM Telegram Beta E2E | `main` | `286e5ffe0767` | 3m 19s | 3m 12s | 6s | [26901214260](https://github.com/openclaw/openclaw/actions/runs/26901214260) | 1 |
| pass | blocking | `macos-preflight` | OpenClaw macOS Publish | `main` | `95ad48af06dd` | 42m 28s | 42m 14s | 17s | [26911870413](https://github.com/openclaw/releases/actions/runs/26911870413) | 2 |
| pass | blocking | `macos-validate` | OpenClaw macOS Validate | `main` | `95ad48af06dd` | 5m 16s | 5m 9s | 6s | [26911870392](https://github.com/openclaw/releases/actions/runs/26911870392) | 1 |
| pass | blocking | `macos-publish` | OpenClaw macOS Publish | `main` | `95ad48af06dd` | 2m 5s | 1m 55s | 13s | [26914060530](https://github.com/openclaw/releases/actions/runs/26914060530) | 2 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 42m 11s | `macos-preflight` | build_sign_and_package | success | [job](https://github.com/openclaw/releases/actions/runs/26911870413/job/79391760500) |
| 41m 5s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79366090377) |
| 18m 54s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79366091766) |
| 11m 3s | `npm-preflight` | preflight_openclaw_npm | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900686846/job/79351945323) |
| 8m 24s | `full-release-validation` | Run product performance evidence | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79366091741) |
| 7m 47s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79366091662) |
| 5m 45s | `full-release-validation` | Verify Docker runtime image assets | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79366091636) |
| 5m 9s | `macos-validate` | macos_validate | success | [job](https://github.com/openclaw/releases/actions/runs/26911870392/job/79391734432) |
| 4m 32s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79366091796) |
| 4m 11s | `plugin-clawhub-publish` | publish_plugins_clawhub (tlon, extensions/tlon, @openclaw/tlon, 2026.6.1, stable, latest, false) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184288) |
| 4m 3s | `plugin-clawhub-publish` | publish_plugins_clawhub (discord, extensions/discord, @openclaw/discord, 2026.6.1, stable, latest... | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184279) |
| 3m 54s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79366092001) |
| 3m 12s | `package-telegram-e2e` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/26901214260/job/79353822660) |
| 3m 4s | `plugin-clawhub-publish` | publish_plugins_clawhub (matrix, extensions/matrix, @openclaw/matrix, 2026.6.1, stable, latest, f... | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184210) |
| 3m 1s | `plugin-clawhub-publish` | publish_plugins_clawhub (slack, extensions/slack, @openclaw/slack, 2026.6.1, stable, latest, false) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184211) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 57m 2s | 47s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79373931357) |
| 1h 15m 55s | 41m 5s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79366090377) |
| 14m 3s | 2m 41s | `plugin-clawhub-publish` | publish_plugins_clawhub (zalo, extensions/zalo, @openclaw/zalo, 2026.6.1, stable, latest, false) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184172) |
| 14m 3s | 2m 56s | `plugin-clawhub-publish` | publish_plugins_clawhub (zalouser, extensions/zalouser, @openclaw/zalouser, 2026.6.1, stable, lat... | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184286) |
| 11m 0s | 3m 54s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79366092001) |
| 10m 49s | 4m 3s | `plugin-clawhub-publish` | publish_plugins_clawhub (discord, extensions/discord, @openclaw/discord, 2026.6.1, stable, latest... | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184279) |
| 10m 49s | 2m 36s | `plugin-clawhub-publish` | publish_plugins_clawhub (voice-call, extensions/voice-call, @openclaw/voice-call, 2026.6.1, stabl... | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184311) |
| 10m 49s | 2m 33s | `plugin-clawhub-publish` | publish_plugins_clawhub (nextcloud-talk, extensions/nextcloud-talk, @openclaw/nextcloud-talk, 202... | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184337) |
| 10m 48s | 2m 40s | `plugin-clawhub-publish` | publish_plugins_clawhub (openshell, extensions/openshell, @openclaw/openshell-sandbox, 2026.6.1, ... | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184219) |
| 10m 48s | 2m 36s | `plugin-clawhub-publish` | publish_plugins_clawhub (tokenjuice, extensions/tokenjuice, @openclaw/tokenjuice, 2026.6.1, stabl... | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184273) |
| 10m 48s | 2m 37s | `plugin-clawhub-publish` | publish_plugins_clawhub (msteams, extensions/msteams, @openclaw/msteams, 2026.6.1, stable, latest... | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184277) |
| 10m 48s | 4m 11s | `plugin-clawhub-publish` | publish_plugins_clawhub (tlon, extensions/tlon, @openclaw/tlon, 2026.6.1, stable, latest, false) | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184288) |
| 10m 48s | 2m 58s | `plugin-clawhub-publish` | publish_plugins_clawhub (feishu, extensions/feishu, @openclaw/feishu, 2026.6.1, stable, latest, f... | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907239724/job/79377184289) |
| 10m 44s | 2m 28s | `openclaw-npm-publish` | publish_openclaw_npm | success | [job](https://github.com/openclaw/openclaw/actions/runs/26907625257/job/79376800013) |
| 6m 25s | 7m 47s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/26900640419/job/79366091662) |

## Notes

Stable closeout repaired after initial publish left root npm latest on 2026.5.28. The openclaw/releases dist-tag workflow run 26911870143 failed because its stored NPM_TOKEN returned E401, so root openclaw dist-tags were updated locally with the documented 1Password/npm fallback and verified live: latest=2026.6.1, beta=2026.6.1. The original release-publish wrapper run 26907004505 is red because it was launched with beta dist-tag expectations; child npm/plugin/ClawHub publishes succeeded and are listed here. macOS publish uploaded assets and opened appcast PR 90024 after direct main push lost a race; PR 90024 was merged and appcast.xml now points at 2026.6.1 on main.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


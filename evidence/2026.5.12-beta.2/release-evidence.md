# OpenClaw Release Evidence: 2026.5.12-beta.2

Generated: 2026-05-12T23:16:50.877Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.12-beta.2` |
| Release ref input | `release/2026.5.12` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.5.12` |
| Release ref SHA | `cc46ca9bee27776a84fc585a28f6cec56e22a03e` |
| Runs at release SHA | none |
| Package spec | `openclaw@2026.5.12-beta.2` |
| npm status | published |
| npm resolved version | `2026.5.12-beta.2` |
| npm expected version match | yes |
| npm dist-tags pointing here | `beta` |
| npm gitHead | not recorded in npm metadata |
| npm published at | 2026-05-12T22:15:34.106Z |
| npm tarball | https://registry.npmjs.org/openclaw/-/openclaw-2026.5.12-beta.2.tgz |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `fd79013b8f37` | 58m 6s | 1h 15m 5s | 57m 40s | [25765528487](https://github.com/openclaw/openclaw/actions/runs/25765528487) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `29ba6f8312d3` | 4m 27s | 1h 5m 33s | 4m 24s | [25765545921](https://github.com/openclaw/openclaw/actions/runs/25765545921) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `29ba6f8312d3` | 56m 43s | 15h 36m 21s | 56m 40s | [25765546180](https://github.com/openclaw/openclaw/actions/runs/25765546180) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `main` | `29ba6f8312d3` | 3m 6s | 3m 3s | 3s | [25765545337](https://github.com/openclaw/openclaw/actions/runs/25765545337) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 57m 11s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765528487/job/75677041571) |
| 50m 40s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824148) |
| 50m 38s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824170) |
| 40m 30s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824202) |
| 35m 56s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824096) |
| 35m 45s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824088) |
| 35m 45s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824120) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824114) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824244) |
| 35m 40s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824089) |
| 35m 40s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824093) |
| 9m 14s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765528487/job/75677041573) |
| 4m 45s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765528487/job/75677041586) |
| 3m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765528487/job/75677041940) |
| 3m 17s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765545921/job/75677117896) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 57m 40s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765528487/job/75684237950) |
| 56m 40s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75684185830) |
| 16m 52s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75679292526) |
| 7m 41s | 4m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677940403) |
| 7m 41s | 1m 58s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677940446) |
| 7m 40s | 1m 44s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677940370) |
| 7m 40s | 2m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677940388) |
| 7m 40s | 2m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677940389) |
| 7m 40s | 4m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677940400) |
| 7m 40s | 4m 24s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677940402) |
| 7m 40s | 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677940405) |
| 4m 24s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765545921/job/75677617704) |
| 4m 23s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765545921/job/75677628688) |
| 4m 18s | 3s | `normal-ci` | checks-node-core-support-boundary | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25765545921/job/75677617647) |
| 4m 18s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25765545921/job/75677617680) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25765528487
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25765528487/job/75684237950
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25765545921
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25765545921/job/75677617647
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25765545921/job/75677628688
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25765546180
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824088
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824089
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824093
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824096
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824114
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824120
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824124
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824128
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824129
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824145
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824148
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824155
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824159
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824160
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824165
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824170
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824202
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824244
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677824355
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75677916696
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25765546180/job/75684185830

## Notes

Automatically requested by Full Release Validation 25765528487 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


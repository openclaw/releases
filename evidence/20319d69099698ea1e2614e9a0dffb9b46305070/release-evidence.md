# OpenClaw Release Evidence: 20319d69099698ea1e2614e9a0dffb9b46305070

Generated: 2026-05-12T10:01:34.593Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `20319d69099698ea1e2614e9a0dffb9b46305070` |
| Release ref input | `20319d69099698ea1e2614e9a0dffb9b46305070` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `20319d69099698ea1e2614e9a0dffb9b46305070` |
| Release ref SHA | `20319d69099698ea1e2614e9a0dffb9b46305070` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/20319d690996-1778576171237` | `20319d690996` | 1h 4m 58s | 1h 37m 1s | 1h 4m 16s | [25724178554](https://github.com/openclaw/openclaw/actions/runs/25724178554) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/20319d690996-1778576171237` | `20319d690996` | 3m 43s | 1h 5m 23s | 3m 40s | [25724215486](https://github.com/openclaw/openclaw/actions/runs/25724215486) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/20319d690996-1778576171237` | `20319d690996` | 1h 3m 11s | 16h 8m 22s | 1h 3m 7s | [25724202648](https://github.com/openclaw/openclaw/actions/runs/25724202648) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/20319d690996-1778576171237` | `20319d690996` | 4m 52s | 2m 59s | 1m 52s | [25724367803](https://github.com/openclaw/openclaw/actions/runs/25724367803) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 3m 50s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724178554/job/75532612024) |
| 50m 45s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080539) |
| 50m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080430) |
| 40m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080384) |
| 36m 10s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080326) |
| 36m 0s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080420) |
| 35m 53s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080306) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080472) |
| 35m 49s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080294) |
| 35m 46s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080373) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080313) |
| 19m 28s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724178554/job/75532612070) |
| 5m 22s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724178554/job/75533185451) |
| 4m 15s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724178554/job/75532612072) |
| 3m 18s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724178554/job/75532612095) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 4m 16s | 41s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724178554/job/75543444149) |
| 1h 3m 7s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75543325602) |
| 24m 52s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75536746244) |
| 15m 39s | 1m 8s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168461) |
| 15m 39s | 8m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168595) |
| 15m 38s | 1m 4s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168415) |
| 15m 38s | 7m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168419) |
| 15m 38s | 1m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168429) |
| 15m 38s | 1m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168436) |
| 15m 38s | 1m 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168450) |
| 15m 38s | 4m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168455) |
| 3m 43s | 5m 22s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724178554/job/75533185451) |
| 3m 40s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724215486/job/75533294792) |
| 3m 36s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724215486/job/75533279806) |
| 3m 36s | 3s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724215486/job/75533279810) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25724178554
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25724178554/job/75543444149
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25724202648
  - cross_os_release_checks / Windows / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75533570374
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080253
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080272
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080273
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080294
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080306
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080313
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080316
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080325
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080326
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080332
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080338
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080373
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080384
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080400
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080415
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080420
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080430
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080472
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534080539
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534946119
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75534946122
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168396
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168429
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75535168450
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75536746244
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25724202648/job/75543325602

## Notes

Automatically requested by Full Release Validation 25724178554 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


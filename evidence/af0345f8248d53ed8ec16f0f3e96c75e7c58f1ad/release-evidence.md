# OpenClaw Release Evidence: af0345f8248d53ed8ec16f0f3e96c75e7c58f1ad

Generated: 2026-05-12T07:24:44.262Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `af0345f8248d53ed8ec16f0f3e96c75e7c58f1ad` |
| Release ref input | `af0345f8248d53ed8ec16f0f3e96c75e7c58f1ad` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `af0345f8248d53ed8ec16f0f3e96c75e7c58f1ad` |
| Release ref SHA | `af0345f8248d53ed8ec16f0f3e96c75e7c58f1ad` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/af0345f8248d-1778567181003` | `af0345f8248d` | 57m 59s | 1h 17m 11s | 57m 21s | [25717465505](https://github.com/openclaw/openclaw/actions/runs/25717465505) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/af0345f8248d-1778567181003` | `af0345f8248d` | 3m 17s | 1h 2m 37s | 2m 39s | [25717483449](https://github.com/openclaw/openclaw/actions/runs/25717483449) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/af0345f8248d-1778567181003` | `af0345f8248d` | 56m 35s | 15h 26m 18s | 56m 32s | [25717480560](https://github.com/openclaw/openclaw/actions/runs/25717480560) | 44 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/af0345f8248d-1778567181003` | `af0345f8248d` | 3m 23s | 3m 17s | 5s | [25717616752](https://github.com/openclaw/openclaw/actions/runs/25717616752) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 56m 55s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717465505/job/75510570545) |
| 50m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261687) |
| 50m 40s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261696) |
| 40m 30s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261701) |
| 35m 50s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261671) |
| 35m 47s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261710) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261684) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261686) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261680) |
| 35m 41s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261718) |
| 35m 40s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261674) |
| 8m 48s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717465505/job/75510570547) |
| 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717465505/job/75510981263) |
| 3m 39s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717465505/job/75510570552) |
| 3m 17s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717616752/job/75511014721) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 57m 21s | 37s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717465505/job/75518131087) |
| 56m 32s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75518068904) |
| 18m 26s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75512860770) |
| 8m 45s | 2m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511624904) |
| 8m 42s | 5m 34s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511624816) |
| 8m 39s | 1m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511624793) |
| 8m 39s | 5m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511624805) |
| 8m 39s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511624848) |
| 8m 38s | 4m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511624803) |
| 8m 38s | 9m 46s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511624812) |
| 8m 38s | 6m 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511624813) |
| 3m 43s | 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717465505/job/75510981263) |
| 2m 39s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717483449/job/75510917066) |
| 2m 28s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717483449/job/75510881772) |
| 2m 27s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717483449/job/75510881759) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25717465505
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25717465505/job/75518131087
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25717480560
  - Run QA Lab live Matrix lane: failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75510771853
  - Run QA Lab live Telegram lane: failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75510771864
  - Run QA Lab parity lane (baseline): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75510771868
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75510771882
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75510914799
  - Run QA Lab parity report: failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75510935162
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261671
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261674
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261680
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261681
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261684
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261686
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261687
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261688
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261689
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261691
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261696
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261698
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261701
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261702
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261705
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261706
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261710
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261716
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511261718
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511582610
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511582626
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75511624799
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75512860770
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25717480560/job/75518068904

## Notes

Automatically requested by Full Release Validation 25717465505 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


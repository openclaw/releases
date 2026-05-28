# OpenClaw Release Evidence: e4498e0cd59a5a02d4b23e95e230634de7631490

Generated: 2026-05-12T09:54:07.846Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `e4498e0cd59a5a02d4b23e95e230634de7631490` |
| Release ref input | `e4498e0cd59a5a02d4b23e95e230634de7631490` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `e4498e0cd59a5a02d4b23e95e230634de7631490` |
| Release ref SHA | `e4498e0cd59a5a02d4b23e95e230634de7631490` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/e4498e0cd59a-1778575761759` | `e4498e0cd59a` | 1h 4m 19s | 1h 42m 9s | 1h 3m 44s | [25723838932](https://github.com/openclaw/openclaw/actions/runs/25723838932) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/e4498e0cd59a-1778575761759` | `e4498e0cd59a` | 3m 35s | 1h 5m 8s | 3m 16s | [25723865582](https://github.com/openclaw/openclaw/actions/runs/25723865582) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/e4498e0cd59a-1778575761759` | `e4498e0cd59a` | 1h 2m 56s | 15h 49m 28s | 1h 2m 53s | [25723865349](https://github.com/openclaw/openclaw/actions/runs/25723865349) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/e4498e0cd59a-1778575761759` | `e4498e0cd59a` | 6m 18s | 2m 57s | 3m 20s | [25724043639](https://github.com/openclaw/openclaw/actions/runs/25724043639) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 3m 8s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723838932/job/75531467899) |
| 50m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126831) |
| 50m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126895) |
| 41m 27s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126890) |
| 40m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126848) |
| 35m 54s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126804) |
| 35m 54s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126859) |
| 35m 53s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126814) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126849) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126797) |
| 35m 41s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126843) |
| 23m 30s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723838932/job/75531467872) |
| 6m 58s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723838932/job/75532070987) |
| 4m 14s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723838932/job/75531467882) |
| 3m 32s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723838932/job/75531467949) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 3m 44s | 34s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723838932/job/75542164749) |
| 1h 2m 53s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75542111854) |
| 31m 39s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75536769903) |
| 19m 5s | 12m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810708) |
| 19m 5s | 5m 19s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810710) |
| 19m 5s | 8m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810727) |
| 19m 5s | 5m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810747) |
| 19m 5s | 7m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810784) |
| 19m 5s | 8m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810785) |
| 19m 4s | 4m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810702) |
| 19m 4s | 9m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810721) |
| 4m 3s | 6m 58s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723838932/job/75532070987) |
| 3m 20s | 2m 57s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25724043639/job/75532102766) |
| 3m 16s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723865582/job/75532033982) |
| 3m 10s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723865582/job/75531996374) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25723838932
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25723838932/job/75542164749
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25723865349
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533070002
  - Run Docker release-path validation / Docker E2E (plugins/runtime install A): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533070016
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533070031
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126797
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126804
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126814
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126831
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126833
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126839
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126840
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126841
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126843
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126846
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126848
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126849
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126854
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126859
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126861
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126867
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126888
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126890
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533126895
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810710
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810747
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810775
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin): failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75533810783
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75536769903
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25723865349/job/75542111854

## Notes

Automatically requested by Full Release Validation 25723838932 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


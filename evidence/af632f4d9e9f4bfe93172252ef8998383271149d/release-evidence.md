# OpenClaw Release Evidence: af632f4d9e9f4bfe93172252ef8998383271149d

Generated: 2026-05-12T08:08:44.092Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `af632f4d9e9f4bfe93172252ef8998383271149d` |
| Release ref input | `af632f4d9e9f4bfe93172252ef8998383271149d` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `af632f4d9e9f4bfe93172252ef8998383271149d` |
| Release ref SHA | `af632f4d9e9f4bfe93172252ef8998383271149d` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/af632f4d9e9f-1778569662768` | `af632f4d9e9f` | 1h 0m 31s | 1h 21m 48s | 59m 56s | [25719162856](https://github.com/openclaw/openclaw/actions/runs/25719162856) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/af632f4d9e9f-1778569662768` | `af632f4d9e9f` | 4m 7s | 1h 3m 44s | 4m 3s | [25719181846](https://github.com/openclaw/openclaw/actions/runs/25719181846) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/af632f4d9e9f-1778569662768` | `af632f4d9e9f` | 58m 59s | 15h 41m 23s | 58m 56s | [25719178999](https://github.com/openclaw/openclaw/actions/runs/25719178999) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/af632f4d9e9f-1778569662768` | `af632f4d9e9f` | 3m 41s | 3m 7s | 33s | [25719323708](https://github.com/openclaw/openclaw/actions/runs/25719323708) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 59m 31s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719162856/job/75515921688) |
| 50m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027139) |
| 50m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027231) |
| 40m 30s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027132) |
| 36m 10s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027104) |
| 35m 56s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027234) |
| 35m 54s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027094) |
| 35m 46s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027133) |
| 35m 45s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027118) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027109) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027089) |
| 9m 17s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719162856/job/75515921775) |
| 4m 40s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719162856/job/75515921693) |
| 4m 19s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719162856/job/75516388849) |
| 3m 19s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719162856/job/75515921670) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 59m 56s | 32s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719162856/job/75524671752) |
| 58m 56s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75524590357) |
| 16m 29s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75518268243) |
| 9m 24s | 1m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517168670) |
| 9m 21s | 1m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517168515) |
| 9m 20s | 1m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517168514) |
| 9m 20s | 5m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517168523) |
| 9m 20s | 4m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517168536) |
| 9m 20s | 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517168540) |
| 9m 20s | 2m 4s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517168584) |
| 9m 19s | 2m 9s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517159648) |
| 4m 3s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719181846/job/75516513241) |
| 3m 58s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719181846/job/75516501315) |
| 3m 58s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719181846/job/75516501317) |
| 3m 58s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25719181846/job/75516501323) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25719162856
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25719162856/job/75524671752
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25719178999
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75516315828
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027089
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027094
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027103
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027104
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027108
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027109
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027115
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027117
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027118
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027132
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027133
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027139
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027142
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027148
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027162
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027190
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027231
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027234
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517027255
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517159632
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517159706
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517168514
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517168554
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75517168584
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75518268243
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25719178999/job/75524590357

## Notes

Automatically requested by Full Release Validation 25719162856 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


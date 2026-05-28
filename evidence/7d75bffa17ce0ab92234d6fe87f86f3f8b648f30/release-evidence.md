# OpenClaw Release Evidence: 7d75bffa17ce0ab92234d6fe87f86f3f8b648f30

Generated: 2026-05-12T08:44:35.610Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `7d75bffa17ce0ab92234d6fe87f86f3f8b648f30` |
| Release ref input | `7d75bffa17ce0ab92234d6fe87f86f3f8b648f30` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `7d75bffa17ce0ab92234d6fe87f86f3f8b648f30` |
| Release ref SHA | `7d75bffa17ce0ab92234d6fe87f86f3f8b648f30` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/7d75bffa17ce-1778571922274` | `7d75bffa17ce` | 58m 47s | 1h 17m 58s | 58m 10s | [25720811324](https://github.com/openclaw/openclaw/actions/runs/25720811324) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/7d75bffa17ce-1778571922274` | `7d75bffa17ce` | 3m 16s | 1h 4m 6s | 2m 57s | [25720828392](https://github.com/openclaw/openclaw/actions/runs/25720828392) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/7d75bffa17ce-1778571922274` | `7d75bffa17ce` | 57m 6s | 15h 41m 38s | 57m 2s | [25720832560](https://github.com/openclaw/openclaw/actions/runs/25720832560) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/7d75bffa17ce-1778571922274` | `7d75bffa17ce` | 3m 9s | 2m 56s | 12s | [25720972768](https://github.com/openclaw/openclaw/actions/runs/25720972768) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 57m 38s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720811324/job/75521325000) |
| 50m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151733) |
| 50m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151760) |
| 40m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151748) |
| 35m 54s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151629) |
| 35m 51s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151601) |
| 35m 50s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151594) |
| 35m 46s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151603) |
| 35m 45s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151607) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151680) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151602) |
| 9m 23s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720811324/job/75521325027) |
| 3m 44s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720811324/job/75521325030) |
| 3m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720811324/job/75521800776) |
| 3m 11s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720811324/job/75521325012) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 58m 10s | 36s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720811324/job/75530420308) |
| 57m 2s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75530330841) |
| 17m 50s | 4s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75524071955) |
| 10m 3s | 4m 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794575) |
| 10m 3s | 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794598) |
| 10m 2s | 3m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794514) |
| 10m 2s | 4m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794528) |
| 10m 2s | 3m 39s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794529) |
| 10m 2s | 1m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794532) |
| 10m 2s | 4m 19s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794545) |
| 10m 2s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794555) |
| 3m 34s | 3m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720811324/job/75521800776) |
| 2m 57s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720828392/job/75521766681) |
| 2m 52s | 4s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720828392/job/75521752627) |
| 2m 52s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25720828392/job/75521752628) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25720811324
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25720811324/job/75530420308
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25720832560
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75521728259
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151594
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151595
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151601
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151602
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151603
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151607
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151626
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151629
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151648
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151654
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151669
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151670
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151678
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151680
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151699
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151733
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151741
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151748
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522151760
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522580578
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522580579
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794529
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794532
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75522794569
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75524071955
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25720832560/job/75530330841

## Notes

Automatically requested by Full Release Validation 25720811324 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


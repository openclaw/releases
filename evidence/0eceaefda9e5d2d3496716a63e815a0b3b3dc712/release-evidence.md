# OpenClaw Release Evidence: 0eceaefda9e5d2d3496716a63e815a0b3b3dc712

Generated: 2026-05-12T06:47:19.190Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `0eceaefda9e5d2d3496716a63e815a0b3b3dc712` |
| Release ref input | `0eceaefda9e5d2d3496716a63e815a0b3b3dc712` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `0eceaefda9e5d2d3496716a63e815a0b3b3dc712` |
| Release ref SHA | `0eceaefda9e5d2d3496716a63e815a0b3b3dc712` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/0eceaefda9e5-1778564919513` | `0eceaefda9e5` | 58m 6s | 1h 18m 37s | 57m 34s | [25716061445](https://github.com/openclaw/openclaw/actions/runs/25716061445) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/0eceaefda9e5-1778564919513` | `0eceaefda9e5` | 3m 3s | 1h 1m 49s | 2m 38s | [25716070617](https://github.com/openclaw/openclaw/actions/runs/25716070617) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/0eceaefda9e5-1778564919513` | `0eceaefda9e5` | 56m 45s | 15h 31m 24s | 56m 42s | [25716071773](https://github.com/openclaw/openclaw/actions/runs/25716071773) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/0eceaefda9e5-1778564919513` | `0eceaefda9e5` | 3m 51s | 3m 1s | 49s | [25716195381](https://github.com/openclaw/openclaw/actions/runs/25716195381) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 57m 20s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716061445/job/75506203158) |
| 50m 38s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775429) |
| 50m 29s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775443) |
| 40m 32s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775449) |
| 36m 13s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775420) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775435) |
| 35m 51s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775415) |
| 35m 50s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775426) |
| 35m 48s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775413) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775412) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775414) |
| 9m 15s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716061445/job/75506203159) |
| 4m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716061445/job/75506576822) |
| 3m 40s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716061445/job/75506203148) |
| 3m 25s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716061445/job/75506203155) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 57m 34s | 32s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716061445/job/75512995147) |
| 56m 42s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75512910918) |
| 16m 33s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75508081629) |
| 9m 27s | 2m 7s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506787090) |
| 8m 36s | 1m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75507086751) |
| 8m 36s | 1m 45s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75507086765) |
| 8m 35s | 4m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75507086729) |
| 8m 35s | 7m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75507086744) |
| 8m 35s | 4m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75507086745) |
| 8m 35s | 1m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75507086747) |
| 8m 35s | 1m 24s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75507086749) |
| 3m 38s | 4m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716061445/job/75506576822) |
| 2m 38s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716070617/job/75506499668) |
| 2m 20s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716070617/job/75506457592) |
| 2m 6s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716070617/job/75506432621) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25716061445
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25716061445/job/75512995147
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25716071773
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775412
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775413
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775414
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775415
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775416
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775420
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775421
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775424
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775426
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775429
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775431
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775434
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775435
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775436
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775438
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775443
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775447
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775449
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75506775452
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75507037087
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75507037091
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75507086749
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75508081629
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25716071773/job/75512910918

## Notes

Automatically requested by Full Release Validation 25716061445 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


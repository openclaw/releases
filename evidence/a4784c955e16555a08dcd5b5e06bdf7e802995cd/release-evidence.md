# OpenClaw Release Evidence: a4784c955e16555a08dcd5b5e06bdf7e802995cd

Generated: 2026-05-12T07:31:14.153Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `a4784c955e16555a08dcd5b5e06bdf7e802995cd` |
| Release ref input | `a4784c955e16555a08dcd5b5e06bdf7e802995cd` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `a4784c955e16555a08dcd5b5e06bdf7e802995cd` |
| Release ref SHA | `a4784c955e16555a08dcd5b5e06bdf7e802995cd` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/a4784c955e16-1778567566946` | `a4784c955e16` | 58m 4s | 1h 18m 9s | 57m 33s | [25717721290](https://github.com/openclaw/openclaw/actions/runs/25717721290) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/a4784c955e16-1778567566946` | `a4784c955e16` | 3m 33s | 1h 1m 13s | 2m 47s | [25717735146](https://github.com/openclaw/openclaw/actions/runs/25717735146) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/a4784c955e16-1778567566946` | `a4784c955e16` | 56m 42s | 15h 57m 29s | 56m 39s | [25717740011](https://github.com/openclaw/openclaw/actions/runs/25717740011) | 44 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/a4784c955e16-1778567566946` | `a4784c955e16` | 3m 57s | 3m 12s | 44s | [25717876249](https://github.com/openclaw/openclaw/actions/runs/25717876249) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 57m 9s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717721290/job/75511371884) |
| 50m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039090) |
| 50m 28s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039082) |
| 40m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039088) |
| 35m 57s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039031) |
| 35m 55s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039013) |
| 35m 54s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039011) |
| 35m 45s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039036) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039073) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039027) |
| 35m 41s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039034) |
| 8m 51s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717721290/job/75511371887) |
| 4m 22s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717721290/job/75511789109) |
| 3m 41s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717721290/job/75511371870) |
| 3m 26s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717721290/job/75511371864) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 57m 33s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717721290/job/75519090059) |
| 56m 39s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75519004238) |
| 34m 2s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75515826601) |
| 8m 25s | 7m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512387240) |
| 8m 24s | 4m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512387157) |
| 8m 24s | 4m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512387161) |
| 8m 24s | 4m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512387169) |
| 8m 24s | 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512387175) |
| 8m 24s | 25m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512387177) |
| 8m 24s | 4m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512387179) |
| 8m 24s | 2m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512387185) |
| 3m 49s | 4m 22s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717721290/job/75511789109) |
| 2m 47s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717735146/job/75511706583) |
| 2m 7s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717735146/job/75511624637) |
| 2m 5s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25717735146/job/75511618384) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25717721290
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25717721290/job/75519090059
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25717740011
  - Run QA Lab live Matrix lane: failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75511575429
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75511575434
  - Run QA Lab live Telegram lane: failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75511575441
  - Run QA Lab parity lane (baseline): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75511575445
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75511698987
  - Run QA Lab parity report: failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75511771397
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039011
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039013
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039016
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039023
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039026
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039027
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039031
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039032
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039034
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039035
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039036
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039041
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039043
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039061
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039073
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039082
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039088
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039090
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512039105
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512362713
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512362716
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512387148
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75512387177
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75515826601
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25717740011/job/75519004238

## Notes

Automatically requested by Full Release Validation 25717721290 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


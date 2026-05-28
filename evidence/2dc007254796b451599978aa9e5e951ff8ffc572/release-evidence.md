# OpenClaw Release Evidence: 2dc007254796b451599978aa9e5e951ff8ffc572

Generated: 2026-05-12T06:51:19.774Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2dc007254796b451599978aa9e5e951ff8ffc572` |
| Release ref input | `2dc007254796b451599978aa9e5e951ff8ffc572` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `2dc007254796b451599978aa9e5e951ff8ffc572` |
| Release ref SHA | `2dc007254796b451599978aa9e5e951ff8ffc572` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/2dc007254796-1778565118375` | `2dc007254796` | 59m 4s | 1h 17m 22s | 58m 29s | [25716180433](https://github.com/openclaw/openclaw/actions/runs/25716180433) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/2dc007254796-1778565118375` | `2dc007254796` | 3m 4s | 1h 0m 44s | 2m 41s | [25716194903](https://github.com/openclaw/openclaw/actions/runs/25716194903) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/2dc007254796-1778565118375` | `2dc007254796` | 57m 45s | 15h 37m 26s | 57m 40s | [25716198335](https://github.com/openclaw/openclaw/actions/runs/25716198335) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/2dc007254796-1778565118375` | `2dc007254796` | 3m 21s | 3m 5s | 16s | [25716320334](https://github.com/openclaw/openclaw/actions/runs/25716320334) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 58m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716180433/job/75506573091) |
| 50m 40s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306685) |
| 50m 29s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306705) |
| 40m 40s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306679) |
| 35m 49s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306639) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306623) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306633) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306644) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306649) |
| 35m 41s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306619) |
| 35m 41s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306621) |
| 7m 44s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716180433/job/75506573055) |
| 3m 49s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716180433/job/75506950919) |
| 3m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716180433/job/75506573079) |
| 3m 25s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716180433/job/75506573088) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 58m 29s | 34s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716180433/job/75513529737) |
| 57m 40s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75513483799) |
| 19m 17s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75508805348) |
| 11m 11s | 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507826354) |
| 11m 10s | 3m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507826361) |
| 11m 10s | 1m 39s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507826365) |
| 11m 10s | 5m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507826370) |
| 11m 10s | 4m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507826376) |
| 11m 10s | 1m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507826377) |
| 11m 9s | 1m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507826342) |
| 11m 9s | 4m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507826344) |
| 3m 45s | 3m 49s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716180433/job/75506950919) |
| 2m 41s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716194903/job/75506856297) |
| 2m 27s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716194903/job/75506841476) |
| 2m 27s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25716194903/job/75506844460) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25716180433
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25716180433/job/75513529737
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25716198335
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75506864673
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507205273
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306616
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306619
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306621
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306623
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306631
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306633
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306639
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306644
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306645
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306649
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306650
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306656
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306663
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306670
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306679
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306680
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306684
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306685
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507306705
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507528602
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507528629
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75507826346
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75508805348
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25716198335/job/75513483799

## Notes

Automatically requested by Full Release Validation 25716180433 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


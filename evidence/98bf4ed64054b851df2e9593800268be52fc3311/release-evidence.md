# OpenClaw Release Evidence: 98bf4ed64054b851df2e9593800268be52fc3311

Generated: 2026-05-12T09:54:21.753Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `98bf4ed64054b851df2e9593800268be52fc3311` |
| Release ref input | `98bf4ed64054b851df2e9593800268be52fc3311` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `98bf4ed64054b851df2e9593800268be52fc3311` |
| Release ref SHA | `98bf4ed64054b851df2e9593800268be52fc3311` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/98bf4ed64054-1778575910007` | `98bf4ed64054` | 1h 2m 6s | 1h 54m 57s | 1h 1m 30s | [25723960437](https://github.com/openclaw/openclaw/actions/runs/25723960437) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/98bf4ed64054-1778575910007` | `98bf4ed64054` | 30m 31s | 1h 6m 27s | 29m 18s | [25723987617](https://github.com/openclaw/openclaw/actions/runs/25723987617) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/98bf4ed64054-1778575910007` | `98bf4ed64054` | 1h 0m 29s | 17h 3m 10s | 1h 0m 24s | [25723988927](https://github.com/openclaw/openclaw/actions/runs/25723988927) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/98bf4ed64054-1778575910007` | `98bf4ed64054` | 4m 21s | 3m 11s | 1m 9s | [25724152896](https://github.com/openclaw/openclaw/actions/runs/25724152896) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 0m 53s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723960437/job/75531867346) |
| 50m 45s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421538) |
| 50m 28s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421573) |
| 40m 45s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421500) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421600) |
| 35m 50s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421440) |
| 35m 46s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421496) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421459) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421548) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421464) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421501) |
| 30m 45s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723960437/job/75531867389) |
| 14m 30s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723960437/job/75531867354) |
| 4m 52s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723960437/job/75532442133) |
| 4m 50s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723987617/job/75531963476) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 1m 30s | 35s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723960437/job/75542202046) |
| 1h 0m 24s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75542112272) |
| 32m 46s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75537218979) |
| 29m 18s | 1m 13s | `normal-ci` | checks-windows-node-test | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723987617/job/75531963359) |
| 19m 53s | 7m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699659) |
| 19m 53s | 1m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699672) |
| 19m 52s | 11m 19s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699594) |
| 19m 52s | 1m 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699623) |
| 19m 52s | 7m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699718) |
| 19m 52s | 1m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699836) |
| 19m 51s | 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699706) |
| 16m 37s | 4m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699539) |
| 7m 44s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723987617/job/75533215830) |
| 7m 37s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723987617/job/75533178332) |
| 7m 37s | 4s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25723987617/job/75533178425) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25723960437
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25723960437/job/75542202046
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25723988927
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75532153647
  - install_smoke_release_checks / installer_smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533183639
  - Run QA Lab parity report: failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533234699
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421440
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421459
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421463
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421464
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421468
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421478
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421479
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421496
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421500
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421501
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421512
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421538
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421548
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421559
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421564
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421573
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421600
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421609
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75533421656
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534305823
  - Run Docker release-path validation / Docker E2E (plugins/runtime install B): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534305902
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534305922
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699539
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699581
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75534699623
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75537218979
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25723988927/job/75542112272

## Notes

Automatically requested by Full Release Validation 25723960437 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


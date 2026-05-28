# OpenClaw Release Evidence: release-2026.5.12

Generated: 2026-05-12T21:18:09.676Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `release-2026.5.12` |
| Release ref input | `release/2026.5.12` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.5.12` |
| Release ref SHA | `bc6090502cef4638d20dea2160d414ebc0fcd360` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.12` | `bc6090502cef` | 59m 29s (+51m 32s) | 59m 0s (+51m 27s) | 59m 14s | [25759781472](https://github.com/openclaw/openclaw/actions/runs/25759781472) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.12` | `bc6090502cef` | 57m 54s (+51m 16s) | 9h 42m 31s (+9h 34m 40s) | 57m 51s | [25759817595](https://github.com/openclaw/openclaw/actions/runs/25759817595) | 48 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 58m 33s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759781472/job/75657713643) |
| 50m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924812) |
| 40m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924795) |
| 30m 38s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924696) |
| 30m 37s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924703) |
| 30m 37s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924706) |
| 30m 37s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924708) |
| 30m 36s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924694) |
| 30m 29s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924743) |
| 30m 28s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924740) |
| 14m 21s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658369254) |
| 15s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25759781472/job/75667825168) |
| 12s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759781472/job/75657650399) |
| 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25759781472/job/75657714996) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 59m 14s | 15s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25759781472/job/75667825168) |
| 57m 51s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75667709040) |
| 16m 51s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75660469530) |
| 13m 8s | 1m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75659056406) |
| 7m 53s | 4m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75659056259) |
| 7m 38s | 2m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75659056366) |
| 7m 37s | 5m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75659056270) |
| 7m 36s | 1m 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75659056217) |
| 7m 36s | 7m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75659056228) |
| 7m 36s | 4m 58s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75659056243) |
| 7m 36s | 3m 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75659056263) |
| 32s | 58m 33s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25759781472/job/75657713643) |
| 23s |  | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25759781472/job/75657714497) |
| 23s |  | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25759781472/job/75657714669) |
| 23s |  | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25759781472/job/75657714677) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 7m 57s | 59m 29s | +51m 32s | +51m 27s |
| `release-checks` | 6m 38s | 57m 54s | +51m 16s | +9h 34m 40s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25759781472
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25759781472/job/75667825168
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25759817595
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924694
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924696
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924703
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924706
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924708
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924740
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924743
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924795
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75658924812
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25759817595/job/75667709040

## Notes

Automatically requested by Full Release Validation 25759781472 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


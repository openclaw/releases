# OpenClaw Release Evidence: ed40ef0a6868dc157f6284d38c059448f250b889

Generated: 2026-05-10T16:13:03.774Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `ed40ef0a6868dc157f6284d38c059448f250b889` |
| Release ref input | `ed40ef0a6868dc157f6284d38c059448f250b889` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `ed40ef0a6868dc157f6284d38c059448f250b889` |
| Release ref SHA | `ed40ef0a6868dc157f6284d38c059448f250b889` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release-ci/ed40ef0a6868-1778426800394` | `ed40ef0a6868` | 45m 55s | 1h 12m 51s | 45m 23s | [25632502252](https://github.com/openclaw/openclaw/actions/runs/25632502252) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/ed40ef0a6868-1778426800394` | `ed40ef0a6868` | 3m 8s | 1h 23m 51s | 2m 59s | [25632509496](https://github.com/openclaw/openclaw/actions/runs/25632509496) | 4 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/ed40ef0a6868-1778426800394` | `ed40ef0a6868` | 44m 57s | 5h 48m 37s | 44m 54s | [25632509633](https://github.com/openclaw/openclaw/actions/runs/25632509633) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/ed40ef0a6868-1778426800394` | `ed40ef0a6868` | 3m 23s | 3m 11s | 11s | [25632587422](https://github.com/openclaw/openclaw/actions/runs/25632587422) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 45m 5s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632502252/job/75238643063) |
| 38m 47s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75238963064) |
| 27m 49s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75238797528) |
| 16m 19s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632502252/job/75238643058) |
| 10m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239128663) |
| 8m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239128657) |
| 8m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75238797735) |
| 7m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75238797738) |
| 7m 14s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75238905373) |
| 6m 57s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239106147) |
| 6m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75238797723) |
| 5m 54s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75238905416) |
| 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632502252/job/75238850523) |
| 3m 39s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632502252/job/75238643072) |
| 3m 19s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632502252/job/75238643062) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 45m 23s | 31s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632502252/job/75241223911) |
| 44m 54s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75241216452) |
| 18m 30s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239719908) |
| 8m 23s | 8m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239128657) |
| 8m 23s | 1m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239128659) |
| 8m 22s | 10m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239128663) |
| 8m 22s | 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239128708) |
| 8m 21s | 1m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239128658) |
| 8m 21s | 4m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239128662) |
| 8m 21s | 1m 46s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239128664) |
| 8m 21s | 1m 10s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509633/job/75239128665) |
| 3m 43s | 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632502252/job/75238850523) |
| 2m 59s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509496/job/75238821356) |
| 2m 29s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509496/job/75238787485) |
| 2m 27s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25632509496/job/75238785839) |

## Notes

Automatically requested by Full Release Validation 25632502252 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


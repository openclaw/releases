# OpenClaw Release Evidence: d62fb9eac315148ad2891169157b89bd9fe0a27e

Generated: 2026-05-03T23:21:29.153Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `d62fb9eac315148ad2891169157b89bd9fe0a27e` |
| Release ref input | `d62fb9eac315148ad2891169157b89bd9fe0a27e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `d62fb9eac315148ad2891169157b89bd9fe0a27e` |
| Release ref SHA | `d62fb9eac315148ad2891169157b89bd9fe0a27e` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/d62fb9eac315-1777848796784` | `d62fb9eac315` | 27m 40s | 43m 3s | 27m 14s | [25293179846](https://github.com/openclaw/openclaw/actions/runs/25293179846) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/d62fb9eac315-1777848796784` | `d62fb9eac315` | 3m 48s | 1h 11m 18s | 3m 44s | [25293185576](https://github.com/openclaw/openclaw/actions/runs/25293185576) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/d62fb9eac315-1777848796784` | `d62fb9eac315` | 26m 29s | 13h 21m 11s | 26m 26s | [25293186089](https://github.com/openclaw/openclaw/actions/runs/25293186089) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/d62fb9eac315-1777848796784` | `d62fb9eac315` | 1m 40s | 1m 36s | 3s | [25293234039](https://github.com/openclaw/openclaw/actions/runs/25293234039) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 26m 58s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293179846/job/74147904436) |
| 24m 8s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007616) |
| 23m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007599) |
| 22m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007609) |
| 22m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007607) |
| 22m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007605) |
| 20m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007596) |
| 19m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007604) |
| 19m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007622) |
| 19m 30s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007601) |
| 18m 58s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148062217) |
| 6m 42s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293179846/job/74147904434) |
| 4m 10s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293179846/job/74147904433) |
| 3m 25s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293185576/job/74147917772) |
| 2m 23s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293179846/job/74147904435) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 14s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293179846/job/74149273037) |
| 26m 26s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74149245653) |
| 24m 58s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74149167424) |
| 7m 7s | 1m 58s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148234788) |
| 7m 7s | 2m 37s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148234795) |
| 7m 6s | 17m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148234784) |
| 7m 6s | 1m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148234786) |
| 7m 5s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148234778) |
| 6m 57s | 1m 32s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148234785) |
| 6m 56s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148234906) |
| 6m 56s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148234921) |
| 3m 44s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293185576/job/74148081154) |
| 2m 39s | 2m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293179846/job/74148017755) |
| 2m 30s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293185576/job/74148024293) |
| 1m 56s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293185576/job/74147999161) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25293179846
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25293179846/job/74149273037
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25293186089
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74147959961
  - Run repo/live E2E validation / validate_release_live_cache: failure - https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007507
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148007625
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74148234784
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74149167424
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25293186089/job/74149245653

## Notes

Automatically requested by Full Release Validation 25293179846 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


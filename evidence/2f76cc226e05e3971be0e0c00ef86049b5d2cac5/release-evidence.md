# OpenClaw Release Evidence: 2f76cc226e05e3971be0e0c00ef86049b5d2cac5

Generated: 2026-05-03T17:19:21.379Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2f76cc226e05e3971be0e0c00ef86049b5d2cac5` |
| Release ref input | `2f76cc226e05e3971be0e0c00ef86049b5d2cac5` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `2f76cc226e05e3971be0e0c00ef86049b5d2cac5` |
| Release ref SHA | `2f76cc226e05e3971be0e0c00ef86049b5d2cac5` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/2f76cc226e05-1777827053628` | `2f76cc226e05` | 27m 57s | 43m 42s | 27m 32s | [25285018418](https://github.com/openclaw/openclaw/actions/runs/25285018418) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/2f76cc226e05-1777827053628` | `2f76cc226e05` | 3m 46s | 1h 9m 47s | 3m 41s | [25285025643](https://github.com/openclaw/openclaw/actions/runs/25285025643) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/2f76cc226e05-1777827053628` | `2f76cc226e05` | 26m 39s | 13h 22m 33s | 26m 36s | [25285026102](https://github.com/openclaw/openclaw/actions/runs/25285026102) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/2f76cc226e05-1777827053628` | `2f76cc226e05` | 1m 37s | 1m 34s | 3s | [25285077878](https://github.com/openclaw/openclaw/actions/runs/25285077878) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 27m 9s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285018418/job/74128082363) |
| 22m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128202891) |
| 22m 26s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128301997) |
| 21m 38s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128202845) |
| 21m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128202854) |
| 20m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128202889) |
| 20m 47s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128301954) |
| 20m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128202876) |
| 20m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128301981) |
| 20m 19s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128301979) |
| 20m 9s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128301988) |
| 7m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285018418/job/74128082317) |
| 4m 13s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285018418/job/74128082310) |
| 3m 25s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285025643/job/74128098717) |
| 2m 17s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285018418/job/74128082308) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 32s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285018418/job/74129585242) |
| 26m 36s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74129561639) |
| 26m 7s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74129532740) |
| 6m 59s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128456274) |
| 6m 59s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128456278) |
| 6m 58s | 7m 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128456266) |
| 6m 57s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128456273) |
| 6m 57s | 1m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128456284) |
| 6m 57s | 19m 8s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128456289) |
| 6m 48s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128456330) |
| 6m 48s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128456435) |
| 3m 41s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285025643/job/74128283793) |
| 2m 33s | 1m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285018418/job/74128206348) |
| 2m 31s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285025643/job/74128222045) |
| 1m 58s | 2s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25285025643/job/74128191890) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25285018418
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25285018418/job/74129585242
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25285026102
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128301997
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74128456289
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74129532740
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25285026102/job/74129561639

## Notes

Automatically requested by Full Release Validation 25285018418 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: 9c373aed44553b264980ece56bc97bd56820f566

Generated: 2026-05-04T07:46:00.939Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `9c373aed44553b264980ece56bc97bd56820f566` |
| Release ref input | `9c373aed44553b264980ece56bc97bd56820f566` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `9c373aed44553b264980ece56bc97bd56820f566` |
| Release ref SHA | `9c373aed44553b264980ece56bc97bd56820f566` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/9c373aed4455-1777879051077` | `9c373aed4455` | 28m 5s | 44m 36s | 27m 39s | [25306171239](https://github.com/openclaw/openclaw/actions/runs/25306171239) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/9c373aed4455-1777879051077` | `9c373aed4455` | 4m 5s | 1h 22m 1s | 4m 0s | [25306188535](https://github.com/openclaw/openclaw/actions/runs/25306188535) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/9c373aed4455-1777879051077` | `9c373aed4455` | 26m 37s | 13h 23m 16s | 26m 32s | [25306185714](https://github.com/openclaw/openclaw/actions/runs/25306185714) | 38 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/9c373aed4455-1777879051077` | `9c373aed4455` | 1m 54s | 1m 35s | 19s | [25306281685](https://github.com/openclaw/openclaw/actions/runs/25306281685) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 27m 10s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306171239/job/74182554596) |
| 23m 54s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74182831991) |
| 22m 11s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74182832013) |
| 22m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74182831987) |
| 21m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74182831956) |
| 21m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74182831981) |
| 20m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74182831963) |
| 20m 16s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74182831960) |
| 19m 52s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183098264) |
| 19m 34s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183098270) |
| 18m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183098256) |
| 7m 17s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306171239/job/74182554613) |
| 4m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306171239/job/74182554591) |
| 3m 36s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306188535/job/74182601826) |
| 2m 32s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306171239/job/74182554593) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 39s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25306171239/job/74185716849) |
| 26m 32s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74185643201) |
| 25m 51s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74185568895) |
| 14m 23s | 0s | `release-checks` | Run QA Lab parity report | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74184236379) |
| 7m 28s | 1m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183401961) |
| 7m 28s | 2m 13s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183401975) |
| 7m 28s | 18m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183401998) |
| 7m 28s | 1m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183401999) |
| 7m 27s | 2m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183401997) |
| 7m 26s | 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183401930) |
| 7m 16s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183402243) |
| 4m 0s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306188535/job/74183033517) |
| 2m 56s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25306188535/job/74182903829) |
| 2m 54s | 2m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306171239/job/74182850537) |
| 2m 44s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25306188535/job/74182879133) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25306171239
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25306171239/job/74185716849
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25306188535
  - checks-node-core-runtime-infra-process: failure - https://github.com/openclaw/openclaw/actions/runs/25306188535/job/74182602012
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25306188535/job/74182903829
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25306185714
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74182714772
  - Run QA Lab parity lane (baseline): failure - https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74182714788
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74182714802
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): failure - https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183098323
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183098395
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74183401998
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74185568895
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25306185714/job/74185643201

## Notes

Automatically requested by Full Release Validation 25306171239 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


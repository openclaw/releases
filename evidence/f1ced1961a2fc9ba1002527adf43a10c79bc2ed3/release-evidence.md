# OpenClaw Release Evidence: f1ced1961a2fc9ba1002527adf43a10c79bc2ed3

Generated: 2026-05-10T06:22:05.422Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `f1ced1961a2fc9ba1002527adf43a10c79bc2ed3` |
| Release ref input | `f1ced1961a2fc9ba1002527adf43a10c79bc2ed3` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `f1ced1961a2fc9ba1002527adf43a10c79bc2ed3` |
| Release ref SHA | `f1ced1961a2fc9ba1002527adf43a10c79bc2ed3` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/f1ced1961a2f-1778390465` | `f1ced1961a2f` | 1h 0m 40s | 1h 25m 16s | 1h 0m 8s | [25620666683](https://github.com/openclaw/openclaw/actions/runs/25620666683) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/f1ced1961a2f-1778390465` | `f1ced1961a2f` | 4m 11s | 1h 11m 41s | 2m 42s | [25620671928](https://github.com/openclaw/openclaw/actions/runs/25620671928) | 1 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/f1ced1961a2f-1778390465` | `f1ced1961a2f` | 59m 25s | 8h 6m 39s | 59m 22s | [25620672436](https://github.com/openclaw/openclaw/actions/runs/25620672436) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/f1ced1961a2f-1778390465` | `f1ced1961a2f` | 3m 14s | 3m 2s | 11s | [25620733315](https://github.com/openclaw/openclaw/actions/runs/25620733315) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 59m 48s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620666683/job/75206514828) |
| 52m 7s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206853071) |
| 42m 25s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206753186) |
| 24m 18s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627042) |
| 17m 5s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206853067) |
| 14m 30s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206753194) |
| 14m 24s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206765625) |
| 14m 6s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206753190) |
| 13m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627166) |
| 12m 46s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620666683/job/75206514831) |
| 11m 55s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206753193) |
| 11m 32s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206753187) |
| 4m 41s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620666683/job/75206514825) |
| 3m 56s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620671928/job/75206528556) |
| 3m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620666683/job/75206680571) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 0m 8s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620666683/job/75209485744) |
| 59m 22s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75209467188) |
| 14m 30s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75207242049) |
| 7m 29s | 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206863025) |
| 7m 28s | 4m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206862994) |
| 7m 28s | 4m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206863000) |
| 7m 28s | 1m 24s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206863001) |
| 7m 28s | 2m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206863005) |
| 7m 28s | 1m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206863006) |
| 7m 28s | 1m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206863007) |
| 7m 28s | 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206863008) |
| 3m 55s | 3m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620666683/job/75206680571) |
| 2m 42s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620671928/job/75206639567) |
| 1m 55s | 3s | `normal-ci` | check-additional | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25620671928/job/75206603393) |
| 1m 49s | 3s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25620671928/job/75206598005) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25620666683
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25620666683/job/75209485744
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25620671928
  - build-artifacts: failure - https://github.com/openclaw/openclaw/actions/runs/25620671928/job/75206528505
  - checks-node-auto-reply-reply-state-routing: failure - https://github.com/openclaw/openclaw/actions/runs/25620671928/job/75206528744
  - build-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25620671928/job/75206575917
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25620671928/job/75206603393
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25620671928/job/75206639567
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627126
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627136
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627143
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627146
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627149
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627150
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627152
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627155
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627156
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627157
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627162
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627164
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627166
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627167
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src...: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206627172
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206765623
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206765626
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206765630
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206765631
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206765633
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206765638
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206765646
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206853067
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75206853071
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25620672436/job/75209467188

## Notes

Automatically requested by Full Release Validation 25620666683 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


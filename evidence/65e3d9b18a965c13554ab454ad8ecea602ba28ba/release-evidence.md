# OpenClaw Release Evidence: 65e3d9b18a965c13554ab454ad8ecea602ba28ba

Generated: 2026-05-10T01:04:12.942Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `65e3d9b18a965c13554ab454ad8ecea602ba28ba` |
| Release ref input | `65e3d9b18a965c13554ab454ad8ecea602ba28ba` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `65e3d9b18a965c13554ab454ad8ecea602ba28ba` |
| Release ref SHA | `65e3d9b18a965c13554ab454ad8ecea602ba28ba` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/65e3d9b18a96-1778374417413` | `65e3d9b18a96` | 10m 14s | 27m 42s | 9m 42s | [25615979372](https://github.com/openclaw/openclaw/actions/runs/25615979372) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/65e3d9b18a96-1778374417413` | `65e3d9b18a96` | 2m 41s | 1h 7m 51s | 2m 38s | [25615985335](https://github.com/openclaw/openclaw/actions/runs/25615985335) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/65e3d9b18a96-1778374417413` | `65e3d9b18a96` | 9m 40s | 4h 32m 23s | 9m 35s | [25615985621](https://github.com/openclaw/openclaw/actions/runs/25615985621) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/65e3d9b18a96-1778374417413` | `65e3d9b18a96` | 3m 14s | 3m 8s | 5s | [25616029335](https://github.com/openclaw/openclaw/actions/runs/25616029335) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 9m 21s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615979372/job/75194008110) |
| 8m 13s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615979372/job/75194008102) |
| 6m 54s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194126082) |
| 6m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194126174) |
| 6m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194126186) |
| 6m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194126192) |
| 5m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194126165) |
| 5m 3s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212595) |
| 5m 3s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212604) |
| 5m 2s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212592) |
| 4m 49s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212613) |
| 4m 49s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212634) |
| 3m 51s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615979372/job/75194125027) |
| 3m 8s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615979372/job/75194008122) |
| 3m 8s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25616029335/job/75194133142) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 9m 42s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615979372/job/75194470178) |
| 9m 35s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194484473) |
| 9m 22s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194473905) |
| 6m 57s | 2m 22s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340118) |
| 6m 57s | 2m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340134) |
| 6m 57s | 1m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340138) |
| 6m 57s | 1m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340149) |
| 6m 56s | 2m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340119) |
| 6m 56s | 2m 24s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340120) |
| 6m 56s | 1m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340121) |
| 6m 56s | 2m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340125) |
| 2m 48s | 3m 51s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615979372/job/75194125027) |
| 2m 38s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615985335/job/75194136584) |
| 2m 20s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615985335/job/75194121973) |
| 2m 20s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25615985335/job/75194121974) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615979372
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615979372/job/75194008110
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25615979372/job/75194470178
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194126082
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194126174
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194126186
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194126192
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212592
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212595
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212598
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212599
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212600
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212603
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212604
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212613
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194212634
  - Run repo/live E2E validation / Docker live models (xAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194225737
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194225747
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194225750
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194337958
  - Run Docker release-path validation / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194337971
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194337982
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340118
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340119
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340120
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340122
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340125
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340126
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340132
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340133
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194340134
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194473905
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25615985621/job/75194484473

## Notes

Automatically requested by Full Release Validation 25615979372 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


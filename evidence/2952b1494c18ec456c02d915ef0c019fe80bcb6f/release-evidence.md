# OpenClaw Release Evidence: 2952b1494c18ec456c02d915ef0c019fe80bcb6f

Generated: 2026-05-09T15:04:29.904Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2952b1494c18ec456c02d915ef0c019fe80bcb6f` |
| Release ref input | `2952b1494c18ec456c02d915ef0c019fe80bcb6f` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `2952b1494c18ec456c02d915ef0c019fe80bcb6f` |
| Release ref SHA | `2952b1494c18ec456c02d915ef0c019fe80bcb6f` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/2952b1494c18-1778336672608` | `2952b1494c18` | 39m 38s | 1h 12m 47s | 39m 3s | [25603433467](https://github.com/openclaw/openclaw/actions/runs/25603433467) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/2952b1494c18-1778336672608` | `2952b1494c18` | 11m 50s | 1h 26m 14s | 2m 42s | [25603439576](https://github.com/openclaw/openclaw/actions/runs/25603439576) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/2952b1494c18-1778336672608` | `2952b1494c18` | 38m 16s | 5h 39m 14s | 38m 12s | [25603439839](https://github.com/openclaw/openclaw/actions/runs/25603439839) | 46 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/2952b1494c18-1778336672608` | `2952b1494c18` | 3m 11s | 2m 54s | 16s | [25603494720](https://github.com/openclaw/openclaw/actions/runs/25603494720) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 38m 47s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603433467/job/75161145656) |
| 32m 40s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161402672) |
| 23m 56s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161289067) |
| 14m 26s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603433467/job/75161145651) |
| 12m 23s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603433467/job/75161145654) |
| 12m 18s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161368088) |
| 11m 0s | `normal-ci` | macos-node | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439576/job/75161166160) |
| 10m 1s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161402674) |
| 9m 36s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161542207) |
| 8m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556486) |
| 7m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161289224) |
| 7m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556491) |
| 6m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161289227) |
| 6m 41s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161542222) |
| 3m 47s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603433467/job/75161298379) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 39m 3s | 34s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603433467/job/75163252117) |
| 38m 12s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75163223962) |
| 16m 23s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75162054193) |
| 7m 28s | 4m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556481) |
| 7m 28s | 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556485) |
| 7m 28s | 4m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556488) |
| 7m 28s | 7m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556491) |
| 7m 27s | 1m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556475) |
| 7m 27s | 1m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556480) |
| 7m 27s | 8m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556486) |
| 7m 27s | 4m 4s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556490) |
| 2m 58s | 3m 47s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603433467/job/75161298379) |
| 2m 42s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439576/job/75161301311) |
| 2m 19s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439576/job/75161279864) |
| 2m 3s | 3s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25603439576/job/75161266217) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25603433467
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25603433467/job/75163252117
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25603439576
  - macos-node: failure - https://github.com/openclaw/openclaw/actions/runs/25603439576/job/75161166160
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161229127
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161289071
  - install_smoke_release_checks / installer_smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161353986
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161368082
  - cross_os_release_checks / Windows / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161402658
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161402669
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161402672
  - cross_os_release_checks / macOS / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161402674
  - Run QA Lab parity report: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161420644
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161453256
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161542219
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161542222
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556473
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556479
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556481
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556486
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556487
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556488
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75161556490
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75162054193
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25603439839/job/75163223962

## Notes

Automatically requested by Full Release Validation 25603433467 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


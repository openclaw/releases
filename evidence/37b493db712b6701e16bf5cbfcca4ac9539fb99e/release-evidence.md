# OpenClaw Release Evidence: 37b493db712b6701e16bf5cbfcca4ac9539fb99e

Generated: 2026-05-09T18:07:59.801Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `37b493db712b6701e16bf5cbfcca4ac9539fb99e` |
| Release ref input | `37b493db712b6701e16bf5cbfcca4ac9539fb99e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `37b493db712b6701e16bf5cbfcca4ac9539fb99e` |
| Release ref SHA | `37b493db712b6701e16bf5cbfcca4ac9539fb99e` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/37b493db712b-1778349366416` | `37b493db712b` | 11m 28s | 36m 39s | 11m 1s | [25607908181](https://github.com/openclaw/openclaw/actions/runs/25607908181) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/37b493db712b-1778349366416` | `37b493db712b` | 10m 30s | 1h 16m 29s | 8m 39s | [25607916877](https://github.com/openclaw/openclaw/actions/runs/25607916877) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/37b493db712b-1778349366416` | `37b493db712b` | 10m 59s | 4h 15m 45s | 10m 54s | [25607916890](https://github.com/openclaw/openclaw/actions/runs/25607916890) | 33 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/37b493db712b-1778349366416` | `37b493db712b` | 3m 3s | 2m 51s | 11s | [25607976644](https://github.com/openclaw/openclaw/actions/runs/25607976644) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 10m 36s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607908181/job/75172886269) |
| 10m 35s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607908181/job/75172886275) |
| 8m 44s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607908181/job/75172886281) |
| 8m 11s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173019770) |
| 7m 57s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75172966536) |
| 7m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173019861) |
| 7m 2s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173019887) |
| 6m 9s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143272) |
| 6m 8s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143289) |
| 6m 7s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143276) |
| 6m 6s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143282) |
| 6m 5s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143285) |
| 5m 35s | `release-checks` | cross_os_release_checks / Windows / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143273) |
| 3m 21s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607908181/job/75173036017) |
| 2m 53s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607916877/job/75172905076) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 11m 1s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607908181/job/75173486251) |
| 10m 54s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173505289) |
| 10m 36s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173490549) |
| 10m 18s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173475643) |
| 10m 18s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173475674) |
| 10m 18s | 0s | `release-checks` | Run Docker release-path validation / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173475755) |
| 9m 26s | 1m 26s | `release-checks` | install_smoke_release_checks / installer_smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173423227) |
| 9m 22s | 55s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173423222) |
| 9m 22s | 1m 12s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173423226) |
| 8m 39s | 1m 50s | `normal-ci` | macos-swift | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916877/job/75172905080) |
| 8m 1s | 2m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173334358) |
| 8m 1s | 1m 44s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173334367) |
| 3m 4s | 3m 21s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607908181/job/75173036017) |
| 2m 51s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607916877/job/75173045382) |
| 2m 16s | 3s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607916877/job/75173012983) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607908181
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607908181/job/75172886269
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607908181/job/75172886275
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25607908181/job/75173486251
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916877
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916877/job/75172905080
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173019770
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173127028
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143272
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143273
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143276
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143280
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143281
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143282
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143285
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143286
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173143289
  - Run Docker release-path validation / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173169804
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173334332
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173334337
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173334352
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173334355
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173334358
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173334361
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173334376
  - install_smoke_release_checks / bun_global_install_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173423222
  - install_smoke_release_checks / root_dockerfile_smokes: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173423226
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173423227
  - Run Docker release-path validation / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173475643
  - Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173475674
  - Run Docker release-path validation / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173475755
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173490549
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25607916890/job/75173505289

## Notes

Automatically requested by Full Release Validation 25607908181 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


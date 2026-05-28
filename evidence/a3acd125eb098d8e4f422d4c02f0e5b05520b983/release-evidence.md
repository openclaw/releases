# OpenClaw Release Evidence: a3acd125eb098d8e4f422d4c02f0e5b05520b983

Generated: 2026-05-09T15:59:45.646Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `a3acd125eb098d8e4f422d4c02f0e5b05520b983` |
| Release ref input | `a3acd125eb098d8e4f422d4c02f0e5b05520b983` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `a3acd125eb098d8e4f422d4c02f0e5b05520b983` |
| Release ref SHA | `a3acd125eb098d8e4f422d4c02f0e5b05520b983` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/a3acd125eb09-1778340987027` | `a3acd125eb09` | 22m 57s | 52m 52s | 22m 27s | [25604904899](https://github.com/openclaw/openclaw/actions/runs/25604904899) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/a3acd125eb09-1778340987027` | `a3acd125eb09` | 11m 34s | 1h 26m 31s | 2m 48s | [25604911000](https://github.com/openclaw/openclaw/actions/runs/25604911000) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/a3acd125eb09-1778340987027` | `a3acd125eb09` | 22m 14s | 5h 12m 54s | 22m 11s | [25604910848](https://github.com/openclaw/openclaw/actions/runs/25604910848) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/a3acd125eb09-1778340987027` | `a3acd125eb09` | 2m 54s | 2m 49s | 4s | [25604963141](https://github.com/openclaw/openclaw/actions/runs/25604963141) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 22m 5s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25604904899/job/75165041270) |
| 19m 34s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165173570) |
| 17m 17s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165270545) |
| 14m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412599) |
| 13m 55s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165255832) |
| 12m 18s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604904899/job/75165041267) |
| 11m 59s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604904899/job/75165041279) |
| 11m 0s | `normal-ci` | macos-node | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604911000/job/75165060025) |
| 8m 28s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165173696) |
| 7m 48s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165402512) |
| 7m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412587) |
| 6m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165173681) |
| 5m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412578) |
| 5m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412602) |
| 4m 36s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604911000/job/75165060014) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 22m 27s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604904899/job/75166206973) |
| 22m 11s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75166216309) |
| 22m 4s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75166210181) |
| 7m 10s | 4m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412590) |
| 7m 10s | 4m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412593) |
| 7m 10s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412597) |
| 7m 10s | 5m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412602) |
| 7m 9s | 2m 19s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412574) |
| 7m 9s | 5m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412578) |
| 7m 9s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412589) |
| 7m 9s | 4m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412596) |
| 2m 50s | 3m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604904899/job/75165173444) |
| 2m 48s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25604911000/job/75165184732) |
| 2m 45s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604911000/job/75165186776) |
| 1m 55s | 4s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25604911000/job/75165144342) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25604904899
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25604904899/job/75165041270
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25604904899/job/75166206973
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25604911000
  - macos-node: failure - https://github.com/openclaw/openclaw/actions/runs/25604911000/job/75165060025
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25604911000/job/75165133955
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25604911000/job/75165184732
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25604910848
  - Run QA Lab parity lane (baseline): failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165114779
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165173570
  - Run QA Lab parity report: failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165189152
  - install_smoke_release_checks / installer_smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165248068
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165255839
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165270545
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165270547
  - cross_os_release_checks / Windows / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165270548
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165316617
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165402502
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165402509
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412578
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412587
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412590
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412593
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412596
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): cancelled - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412599
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75165412602
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75166210181
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25604910848/job/75166216309

## Notes

Automatically requested by Full Release Validation 25604904899 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


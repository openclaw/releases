# OpenClaw Release Evidence: b2f7cda9c521c38233c0df8cf66e63fe6e75a118

Generated: 2026-05-09T21:50:15.334Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `b2f7cda9c521c38233c0df8cf66e63fe6e75a118` |
| Release ref input | `b2f7cda9c521c38233c0df8cf66e63fe6e75a118` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `b2f7cda9c521c38233c0df8cf66e63fe6e75a118` |
| Release ref SHA | `b2f7cda9c521c38233c0df8cf66e63fe6e75a118` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/b2f7cda9c521-1778362622441` | `b2f7cda9c521` | 12m 48s | 43m 0s | 12m 20s | [25612419570](https://github.com/openclaw/openclaw/actions/runs/25612419570) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/b2f7cda9c521-1778362622441` | `b2f7cda9c521` | 11m 43s | 1h 22m 48s | 9m 1s | [25612425520](https://github.com/openclaw/openclaw/actions/runs/25612425520) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/b2f7cda9c521-1778362622441` | `b2f7cda9c521` | 12m 20s | 5h 4m 1s | 12m 16s | [25612425719](https://github.com/openclaw/openclaw/actions/runs/25612425719) | 45 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/b2f7cda9c521-1778362622441` | `b2f7cda9c521` | 3m 12s | 2m 58s | 13s | [25612483994](https://github.com/openclaw/openclaw/actions/runs/25612483994) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 11m 58s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612419570/job/75184767891) |
| 11m 57s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612419570/job/75184767870) |
| 11m 57s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612419570/job/75184767871) |
| 11m 18s | `normal-ci` | macos-swift | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425520/job/75184791706) |
| 9m 35s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184894677) |
| 7m 51s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184972866) |
| 7m 34s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999257) |
| 7m 33s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999246) |
| 7m 33s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999251) |
| 7m 17s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999263) |
| 7m 9s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999250) |
| 7m 4s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184894764) |
| 7m 3s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184894766) |
| 6m 47s | `release-checks` | cross_os_release_checks / Windows / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999252) |
| 3m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612419570/job/75184907251) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 12m 20s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25612419570/job/75185364444) |
| 12m 16s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185381073) |
| 12m 4s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185372761) |
| 11m 9s | 50s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999259) |
| 10m 53s | 1m 6s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999255) |
| 9m 1s | 1m 12s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425520/job/75184791726) |
| 7m 4s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185114103) |
| 7m 4s | 1m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185114104) |
| 7m 4s | 4m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185114110) |
| 7m 4s | 2m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185114111) |
| 7m 4s | 4m 34s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185114113) |
| 7m 4s | 3m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185114114) |
| 3m 8s | 3m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612419570/job/75184907251) |
| 2m 52s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425520/job/75184909464) |
| 2m 40s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612425520/job/75184903711) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612419570
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612419570/job/75184767870
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612419570/job/75184767871
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612419570/job/75184767891
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25612419570/job/75185364444
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425520
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425520/job/75184791706
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184894677
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184972866
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184972867
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999246
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999250
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999251
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999252
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999255
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999257
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999258
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999259
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75184999263
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185105632
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185105643
  - Run Docker release-path validation / Docker E2E (plugins/runtime install E): cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185105657
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185114108
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185114115
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185372761
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25612425719/job/75185381073

## Notes

Automatically requested by Full Release Validation 25612419570 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


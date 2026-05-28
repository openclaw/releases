# OpenClaw Release Evidence: aed6ccf09043d2a1426989402caa47e0ac82a148

Generated: 2026-04-27T22:39:12.543Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `aed6ccf09043d2a1426989402caa47e0ac82a148` |
| Release ref input | `aed6ccf09043d2a1426989402caa47e0ac82a148` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `aed6ccf09043d2a1426989402caa47e0ac82a148` |
| Release ref SHA | `aed6ccf09043d2a1426989402caa47e0ac82a148` |
| Runs at release SHA | none |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 0 | 0 | 2 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `d2320e4d4b42` | 4m 11s | 7m 9s | [25023177325](https://github.com/openclaw/openclaw/actions/runs/25023177325) | 0 |
| running | blocking | `normal-ci` | CI | `main` | `d2320e4d4b42` | 2m 59s | 52m 55s | [25023209209](https://github.com/openclaw/openclaw/actions/runs/25023209209) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `d2320e4d4b42` | 3m 13s | 12m 18s | [25023209272](https://github.com/openclaw/openclaw/actions/runs/25023209272) | 5 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 3m 9s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25023177325/job/73288404308) |
| 3m 8s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25023177325/job/73288404298) |
| 2m 30s | `release-checks` | cross_os_release_checks / prepare | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209272/job/73288500817) |
| 2m 9s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209209/job/73288449367) |
| 2m 3s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209209/job/73288449040) |
| 2m 1s | `normal-ci` | checks-node-core-runtime-infra | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209209/job/73288449350) |
| 1m 57s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209209/job/73288449131) |
| 1m 56s | `normal-ci` | checks-node-extensions-shard-5 | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209209/job/73288449228) |
| 1m 50s | `normal-ci` | checks-node-auto-reply-reply-commands-state-routing | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209209/job/73288449380) |
| 1m 46s | `normal-ci` | checks-node-core-runtime-media-ui | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209209/job/73288449347) |
| 1m 45s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209209/job/73288449216) |
| 1m 41s | `normal-ci` | check-additional-extension-package-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209209/job/73288449249) |
| 1m 31s | `normal-ci` | checks-node-auto-reply-reply-dispatch | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209209/job/73288449371) |
| 1m 31s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25023209272/job/73288500619) |
| 1m 5s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25023209272/job/73288590662) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25023177325
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25023177325/job/73288404298
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25023177325/job/73288404308
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25023177325/job/73288776765

## Notes

Automatically requested by Full Release Validation 25023177325 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


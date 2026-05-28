# OpenClaw Release Evidence: 1ba689376acc91f38c2e6b782f3f0f6859b517d8

Generated: 2026-05-11T17:35:28.813Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `1ba689376acc91f38c2e6b782f3f0f6859b517d8` |
| Release ref input | `1ba689376acc91f38c2e6b782f3f0f6859b517d8` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `1ba689376acc91f38c2e6b782f3f0f6859b517d8` |
| Release ref SHA | `1ba689376acc91f38c2e6b782f3f0f6859b517d8` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/1ba689376acc-1778518724699` | `1ba689376acc` | 36m 0s | 2h 19m 25s | 35m 5s | [25684672546](https://github.com/openclaw/openclaw/actions/runs/25684672546) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/1ba689376acc-1778518724699` | `1ba689376acc` | 34m 12s | 19h 8m 15s | 34m 12s | [25684699432](https://github.com/openclaw/openclaw/actions/runs/25684699432) | 0 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/1ba689376acc-1778518724699` | `1ba689376acc` | 34m 10s | 27h 51m 47s | 34m 12s | [25684699961](https://github.com/openclaw/openclaw/actions/runs/25684699961) | 6 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/1ba689376acc-1778518724699` | `1ba689376acc` | 31m 0s | 30m 58s | 1s | [25684872652](https://github.com/openclaw/openclaw/actions/runs/25684872652) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 34m 36s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684672546/job/75405147329) |
| 34m 36s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684672546/job/75405147362) |
| 34m 35s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684672546/job/75405147348) |
| 33m 45s | `normal-ci` | checks-fast-bundled | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274006) |
| 33m 45s | `normal-ci` | checks-node-compat-node22 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274030) |
| 33m 45s | `normal-ci` | build-artifacts | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274066) |
| 33m 45s | `normal-ci` | checks-fast-contracts-plugins-b | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274076) |
| 33m 45s | `normal-ci` | checks-fast-contracts-plugins-d | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274092) |
| 33m 45s | `normal-ci` | checks-fast-contracts-plugins-a | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274106) |
| 33m 45s | `normal-ci` | checks-fast-contracts-channels-b | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274117) |
| 33m 45s | `normal-ci` | checks-fast-contracts-plugins-c | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274118) |
| 33m 45s | `normal-ci` | checks-fast-contracts-channels-a | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274170) |
| 33m 45s | `normal-ci` | checks-fast-contracts-channels-c | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274179) |
| 32m 49s | `release-checks` | Run QA Lab parity lane (candidate) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699961/job/75405456043) |
| 32m 49s | `release-checks` | Run QA Lab live Matrix lane | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699961/job/75405456113) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 35m 5s | 54s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25684672546/job/75411455829) |
| 34m 12s |  | `normal-ci` | checks-fast-contracts-plugins | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411396083) |
| 34m 12s |  | `normal-ci` | checks-node-core | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411396149) |
| 34m 12s |  | `normal-ci` | check | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411396221) |
| 34m 12s |  | `normal-ci` | check-additional | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411396300) |
| 34m 12s |  | `release-checks` | Run Docker release-path validation / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699961/job/75411399165) |
| 34m 12s |  | `release-checks` | Run package acceptance / Verify package acceptance |  | [job](https://github.com/openclaw/openclaw/actions/runs/25684699961/job/75411399435) |
| 34m 12s |  | `release-checks` | Run repo/live E2E validation / Docker live models (selected providers) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699961/job/75411399758) |
| 34m 12s |  | `release-checks` | Run repo/live E2E validation / Docker live models (${{ matrix.provider_label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699961/job/75411399886) |
| 34m 12s |  | `release-checks` | Run repo/live E2E validation / Docker live suites (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699961/job/75411400052) |
| 34m 11s | 0s | `normal-ci` | checks-fast-contracts-channels | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411395415) |
| 34m 11s | 0s | `normal-ci` | matrix.check_name | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411395476) |
| 34m 11s | 0s | `normal-ci` | matrix.check_name | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411395703) |
| 34m 11s | 0s | `normal-ci` | build-smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411395762) |
| 34m 11s | 0s | `release-checks` | Run QA Lab parity report | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25684699961/job/75411398087) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684672546
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684672546/job/75405147329
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684672546/job/75405147348
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684672546/job/75405147362
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25684672546/job/75411455829
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432
  - checks-fast-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274006
  - checks-node-compat-node22: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274030
  - checks-fast-protocol: failure - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274043
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274066
  - checks-fast-contracts-plugins-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274076
  - checks-fast-contracts-plugins-d: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274092
  - checks-fast-contracts-plugins-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274106
  - checks-fast-contracts-channels-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274117
  - checks-fast-contracts-plugins-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274118
  - checks-fast-contracts-channels-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274170
  - checks-fast-contracts-channels-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274179
  - android-test-third-party: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274203
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274223
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274232
  - android-test-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274257
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274330
  - check-test-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274379
  - check-additional-extension-package-boundary: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274391
  - check-additional-extension-channels: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274411
  - check-prod-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274418
  - check-additional-boundaries-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274426
  - check-additional-boundaries-d: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274444
  - check-dependencies: failure - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274448
  - check-additional-extension-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274460
  - check-additional-runtime-topology-architecture: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274481
  - check-additional-boundaries-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274565
  - check-additional-boundaries-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274609
  - checks-node-agentic-control-plane-agent-chat: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274728
  - checks-node-agentic-control-plane-runtime: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274735
  - checks-node-core-runtime-infra-state: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274740
  - checks-node-core-runtime-infra-process: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274759
  - checks-node-agentic-control-plane-startup-runtime: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274769
  - checks-node-agentic-control-plane-http-plugin-ws: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274770
  - checks-node-agentic-control-plane-auth-node: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274829
  - checks-node-agentic-control-plane-http-models: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75405274840
  - checks-fast-contracts-channels: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411395415
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411395476
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411395703
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411395762
  - checks-fast-contracts-plugins: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411396083
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411396149
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411396221
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684699432/job/75411396300
- `postpublish-telegram`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684872652
  - Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25684872652/job/75405808252

## Notes

Automatically requested by Full Release Validation 25684672546 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


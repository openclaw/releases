# OpenClaw Release Evidence: release-2026.5.7

Generated: 2026-05-07T22:38:14.648Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `release-2026.5.7` |
| Release ref input | `release/2026.5.7` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.5.7` |
| Release ref SHA | `627a80f9d67fb8c4652dbd0c6dc767e713d2a020` |
| Runs at release SHA | none |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `95a1c915312a` | 6h 7m 18s (+5h 48m 48s) | 15h 6m 32s (+14h 19m 18s) | 6h 6m 52s | [25508750969](https://github.com/openclaw/openclaw/actions/runs/25508750969) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `95a1c915312a` | 4h 0m 32s (+3h 45m 34s) | 132h 44m 7s (+124h 4m 35s) | 4h 0m 31s | [25508845614](https://github.com/openclaw/openclaw/actions/runs/25508845614) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 6h 5m 0s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799180) |
| 5h 0m 18s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799205) |
| 4h 0m 37s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799165) |
| 4h 0m 17s | `normal-ci` | check-additional-extension-bundled | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872244) |
| 4h 0m 17s | `normal-ci` | check-additional-extension-package-boundary | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872331) |
| 4h 0m 17s | `normal-ci` | check-additional-runtime-topology-architecture | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872431) |
| 4h 0m 17s | `normal-ci` | checks-node-agentic-control-plane-runtime | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872692) |
| 4h 0m 17s | `normal-ci` | checks-node-agentic-control-plane-startup-runtime | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872724) |
| 4h 0m 17s | `normal-ci` | checks-node-agentic-control-plane-http-plugin-ws | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872738) |
| 4h 0m 16s | `normal-ci` | build-artifacts | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872009) |
| 4h 0m 16s | `normal-ci` | checks-node-compat-node22 | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872021) |
| 4h 0m 16s | `normal-ci` | checks-fast-bundled | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872023) |
| 4h 0m 16s | `normal-ci` | checks-fast-contracts-plugins-d | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872066) |
| 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74921230460) |
| 12s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861737216) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6h 6m 52s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74921230460) |
| 4h 0m 31s | 0s | `normal-ci` | matrix.check_name | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929381) |
| 4h 0m 31s | 0s | `normal-ci` | build-smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929451) |
| 4h 0m 31s | 0s | `normal-ci` | matrix.check_name | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929781) |
| 4h 0m 31s | 0s | `normal-ci` | checks-fast-contracts-channels | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929786) |
| 4h 0m 31s | 0s | `normal-ci` | checks-fast-contracts-plugins | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929819) |
| 4h 0m 31s | 0s | `normal-ci` | check | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929905) |
| 4h 0m 31s | 0s | `normal-ci` | check-additional | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929908) |
| 4h 0m 31s | 0s | `normal-ci` | checks-node-core | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902930181) |
| 1m 50s | 5h 0m 18s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799205) |
| 1m 44s | 4h 0m 37s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799165) |
| 1m 43s | 6h 5m 0s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799180) |
| 1m 39s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799863) |
| 1m 39s | 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799971) |
| 1m 27s | 12s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861737216) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 18m 30s | 6h 7m 18s | +5h 48m 48s | +14h 19m 18s |
| `normal-ci` | 14m 58s | 4h 0m 32s | +3h 45m 34s | +124h 4m 35s |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508750969
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799165
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799180
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74861799205
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25508750969/job/74921230460
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872009
  - checks-node-compat-node22: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872021
  - checks-fast-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872023
  - checks-fast-contracts-plugins-d: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872066
  - checks-fast-contracts-plugins-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872073
  - checks-fast-contracts-plugins-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872085
  - android-test-third-party: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872119
  - android-test-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872144
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872146
  - checks-fast-contracts-plugins-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872165
  - checks-fast-contracts-channels-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872182
  - checks-fast-contracts-channels-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872188
  - checks-fast-contracts-channels-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872211
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872240
  - check-additional-extension-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872244
  - check-test-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872253
  - check-additional-extension-channels: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872259
  - check-prod-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872261
  - check-additional-boundaries-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872267
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872292
  - check-additional-boundaries-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872326
  - check-additional-extension-package-boundary: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872331
  - check-additional-boundaries-d: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872382
  - check-additional-boundaries-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872393
  - check-additional-runtime-topology-architecture: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872431
  - checks-node-agentic-control-plane-runtime: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872692
  - checks-node-core-runtime-infra-process: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872699
  - checks-node-agentic-control-plane-startup-runtime: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872724
  - checks-node-agentic-control-plane-http-models: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872732
  - checks-node-agentic-control-plane-http-plugin-ws: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872738
  - checks-node-agentic-control-plane-agent-chat: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872745
  - checks-node-agentic-control-plane-auth-node: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872796
  - checks-node-core-runtime-infra-state: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74861872947
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929381
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929451
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929781
  - checks-fast-contracts-channels: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929786
  - checks-fast-contracts-plugins: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929819
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929905
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902929908
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25508845614/job/74902930181

## Notes

Automatically requested by Full Release Validation 25508750969 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


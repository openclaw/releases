# OpenClaw Release Evidence: 41df8191c5380ca34e7a8047812b8f1c71a4442e

Generated: 2026-05-03T22:19:31.882Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `41df8191c5380ca34e7a8047812b8f1c71a4442e` |
| Release ref input | `41df8191c5380ca34e7a8047812b8f1c71a4442e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `41df8191c5380ca34e7a8047812b8f1c71a4442e` |
| Release ref SHA | `41df8191c5380ca34e7a8047812b8f1c71a4442e` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/41df8191c538-1777846623975` | `41df8191c538` | 1m 55s | 5m 24s | 1m 36s | [25292398352](https://github.com/openclaw/openclaw/actions/runs/25292398352) | 0 |
| fail | blocking | `normal-ci` | CI | `release-ci/41df8191c538-1777846623975` | `41df8191c538` | 1m 21s | 56m 42s | 1m 21s | [25292406103](https://github.com/openclaw/openclaw/actions/runs/25292406103) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/41df8191c538-1777846623975` | `41df8191c538` | 1m 8s | 1m 1s | 1m 3s | [25292406484](https://github.com/openclaw/openclaw/actions/runs/25292406484) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1m 20s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146033385) |
| 1m 13s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146033379) |
| 1m 13s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146033387) |
| 1m 8s | `normal-ci` | android-build-play | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054012) |
| 1m 7s | `normal-ci` | checks-node-core-runtime-infra-state | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054313) |
| 1m 6s | `normal-ci` | checks-fast-contracts-plugins-a | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053986) |
| 1m 6s | `normal-ci` | checks-node-agentic-control-plane-runtime | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054249) |
| 1m 6s | `normal-ci` | checks-node-core-runtime-infra-process | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054259) |
| 1m 5s | `full-release-validation` | Prepare release package artifact | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146033382) |
| 1m 5s | `normal-ci` | checks-fast-bundled | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053965) |
| 1m 5s | `normal-ci` | checks-fast-contracts-plugins-d | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053982) |
| 1m 3s | `normal-ci` | check-additional-extension-package-boundary | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054068) |
| 1m 2s | `normal-ci` | checks-fast-contracts-channels-c | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053972) |
| 1m 2s | `normal-ci` | checks-fast-contracts-channels-a | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053977) |
| 57s | `release-checks` | resolve_target | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146046491) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1m 36s | 18s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146109674) |
| 1m 22s | 6s | `full-release-validation` | Run package Telegram E2E | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146094759) |
| 1m 21s |  | `normal-ci` | checks-node-core | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146118830) |
| 1m 19s | 0s | `normal-ci` | checks-fast-contracts-plugins | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146117463) |
| 1m 17s | 0s | `normal-ci` | check-additional | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146116029) |
| 1m 16s | 0s | `normal-ci` | check | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146114529) |
| 1m 16s | 0s | `normal-ci` | checks-fast-contracts-channels | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146114530) |
| 1m 7s |  | `normal-ci` | matrix.check_name | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146106034) |
| 1m 7s |  | `normal-ci` | build-smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146106120) |
| 1m 7s |  | `normal-ci` | matrix.check_name | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146106196) |
| 1m 3s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101829) |
| 1m 2s |  | `release-checks` | Run QA Lab parity lane (${{ matrix.lane }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101839) |
| 1m 2s |  | `release-checks` | Run QA Lab parity report | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101880) |
| 1m 2s |  | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101943) |
| 1m 2s |  | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101946) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292398352
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146033379
  - Prepare release package artifact: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146033382
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146033385
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146033387
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146094759
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25292398352/job/74146109674
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103
  - checks-fast-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053965
  - checks-node-compat-node22: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053969
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053970
  - checks-fast-contracts-channels-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053972
  - checks-fast-contracts-channels-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053977
  - checks-fast-contracts-channels-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053978
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053981
  - checks-fast-contracts-plugins-d: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053982
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053984
  - android-test-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053985
  - checks-fast-contracts-plugins-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053986
  - checks-fast-contracts-plugins-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053989
  - check-docs: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146053994
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054012
  - check-test-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054024
  - check-additional-boundaries-d: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054044
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054047
  - check-additional-extension-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054048
  - check-prod-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054059
  - check-policy-guards: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054061
  - check-additional-extension-channels: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054063
  - check-dependencies: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054064
  - check-additional-extension-package-boundary: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054068
  - check-additional-runtime-topology-architecture: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054075
  - check-additional-boundaries-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054081
  - checks-node-agentic-control-plane-runtime: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054249
  - checks-node-auto-reply-reply-session: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054251
  - checks-node-core-fast: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054255
  - checks-node-agentic-commands-doctor: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054258
  - checks-node-core-runtime-infra-process: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054259
  - checks-node-agentic-gateway-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054260
  - checks-node-core-support: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054264
  - checks-node-agentic-plugin-sdk: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054266
  - checks-node-auto-reply-reply-dispatch: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054269
  - checks-node-auto-reply-reply-agent-runner: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054271
  - checks-node-agentic-commands-status-tools: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054272
  - checks-node-core-runtime-shared: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054275
  - checks-node-core-ui: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054279
  - checks-node-auto-reply-reply-commands: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054292
  - checks-node-agentic-gateway-methods: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054294
  - checks-node-auto-reply-reply-state-routing: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054297
  - checks-node-agentic-commands-onboard-config: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054298
  - checks-node-auto-reply-core-top-level: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054300
  - checks-node-agentic-commands-models: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054305
  - checks-node-core-src-security: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054307
  - checks-node-agentic-cli: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054308
  - checks-node-core-runtime-infra-state: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054313
  - checks-node-core-runtime-media-ui: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054314
  - checks-node-agentic-commands-agent-channel: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146054315
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146106034
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146106120
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146106196
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146114529
  - checks-fast-contracts-channels: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146114530
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146116029
  - checks-fast-contracts-plugins: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146117463
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406103/job/74146118830
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406484
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146046491
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101693
  - Prepare release package artifact: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101752
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101798
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101829
  - Run QA Lab parity lane (${{ matrix.lane }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101839
  - Run QA Lab parity report: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292406484/job/74146101880

## Notes

Automatically requested by Full Release Validation 25292398352 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


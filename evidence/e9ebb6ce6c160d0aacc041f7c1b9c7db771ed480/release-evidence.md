# OpenClaw Release Evidence: e9ebb6ce6c160d0aacc041f7c1b9c7db771ed480

Generated: 2026-05-05T03:18:21.596Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `e9ebb6ce6c160d0aacc041f7c1b9c7db771ed480` |
| Release ref input | `e9ebb6ce6c160d0aacc041f7c1b9c7db771ed480` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `e9ebb6ce6c160d0aacc041f7c1b9c7db771ed480` |
| Release ref SHA | `e9ebb6ce6c160d0aacc041f7c1b9c7db771ed480` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/e9ebb6ce6c16-1777950963059` | `e9ebb6ce6c16` | 1m 57s | 3m 36s | 1m 28s | [25355912948](https://github.com/openclaw/openclaw/actions/runs/25355912948) | 0 |
| fail | blocking | `normal-ci` | CI | `release-ci/e9ebb6ce6c16-1777950963059` | `e9ebb6ce6c16` | 1m 23s | 8m 34s | 1m 22s | [25355925977](https://github.com/openclaw/openclaw/actions/runs/25355925977) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/e9ebb6ce6c16-1777950963059` | `e9ebb6ce6c16` | 27s | 19s | 24s | [25355926222](https://github.com/openclaw/openclaw/actions/runs/25355926222) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1m 5s | `normal-ci` | checks-node-agentic-commands-agent-channel | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082881) |
| 53s | `full-release-validation` | Prepare release package artifact | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345039914) |
| 46s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345039916) |
| 45s | `normal-ci` | checks-node-agentic-command-support | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082895) |
| 38s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345039920) |
| 38s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345039931) |
| 34s | `normal-ci` | checks-fast-contracts-plugins-b | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082499) |
| 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345144002) |
| 17s | `release-checks` | resolve_target | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345064346) |
| 12s | `normal-ci` | security-scm-fast | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345061957) |
| 12s | `normal-ci` | checks-fast-contracts-plugins-d | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082482) |
| 11s | `normal-ci` | preflight | success | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345061992) |
| 10s | `normal-ci` | security-dependency-audit | success | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345062029) |
| 10s | `normal-ci` | check-prod-types | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082445) |
| 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345024502) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1m 28s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345144002) |
| 1m 22s | 4s | `full-release-validation` | Run package Telegram E2E | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345128003) |
| 1m 22s | 0s | `normal-ci` | checks-node-core | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345174794) |
| 52s |  | `normal-ci` | checks-fast-contracts-plugins | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345132306) |
| 27s | 0s | `normal-ci` | check | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345098766) |
| 25s | 0s | `normal-ci` | checks-fast-contracts-channels | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345096599) |
| 24s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092275) |
| 23s |  | `normal-ci` | matrix.check_name | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345092784) |
| 23s | 0s | `normal-ci` | check-additional | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345092999) |
| 22s | 0s | `normal-ci` | security-fast | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345091445) |
| 22s | 0s | `normal-ci` | matrix.check_name | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345092530) |
| 22s | 0s | `normal-ci` | build-smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345092610) |
| 22s | 0s | `release-checks` | Run repo/live E2E validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092004) |
| 22s | 0s | `release-checks` | Run QA Lab parity lane (${{ matrix.lane }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092006) |
| 22s | 0s | `release-checks` | Run QA Lab live Slack lane | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092018) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355912948
  - Prepare release package artifact: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345039914
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345039916
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345039920
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345039931
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345128003
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25355912948/job/74345144002
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977
  - security-scm-fast: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345061957
  - checks-fast-protocol: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082340
  - checks-node-compat-node22: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082343
  - checks-fast-contracts-channels-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082350
  - checks-fast-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082351
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082352
  - checks-fast-contracts-channels-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082354
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082376
  - check-docs: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082381
  - checks-fast-contracts-channels-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082390
  - check-strict-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082439
  - macos-node: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082440
  - checks-fast-contracts-plugins-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082443
  - check-prod-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082445
  - skills-python: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082450
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082456
  - check-test-types: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082457
  - check-policy-guards: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082464
  - android-test-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082471
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082472
  - check-dependencies: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082473
  - checks-fast-contracts-plugins-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082478
  - android-test-third-party: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082481
  - checks-fast-contracts-plugins-d: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082482
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082483
  - checks-fast-contracts-plugins-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082499
  - check-preflight-guards: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082509
  - check-additional-boundaries-d: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082523
  - check-additional-boundaries-a: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082524
  - check-additional-extension-package-boundary: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082526
  - check-additional-boundaries-b: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082528
  - check-additional-boundaries-c: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082529
  - check-additional-extension-channels: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082533
  - check-additional-extension-bundled: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082537
  - check-additional-runtime-topology-architecture: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082560
  - checks-node-core-src-security: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082827
  - checks-node-core-runtime-infra-process: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082834
  - checks-node-core-runtime-shared: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082839
  - checks-node-core-ui: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082840
  - checks-node-core-runtime-infra-state: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082853
  - checks-node-core-runtime-media-ui: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082863
  - checks-node-agentic-control-plane-http-plugin-ws: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082864
  - checks-node-agentic-control-plane-agent-chat: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082866
  - checks-node-agentic-control-plane-auth-node: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082869
  - checks-node-core-fast: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082872
  - checks-node-agentic-control-plane-http-models: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082873
  - checks-node-agentic-control-plane-runtime: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082874
  - checks-node-core-support: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082876
  - checks-node-agentic-commands-agent-channel: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082881
  - checks-node-agentic-control-plane-startup-runtime: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082883
  - checks-node-agentic-commands-doctor: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082890
  - checks-node-agentic-commands-status-tools: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082891
  - checks-node-agentic-commands-models: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082893
  - checks-node-agentic-cli: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082894
  - checks-node-agentic-command-support: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082895
  - checks-node-agentic-commands-doctor-shared: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082896
  - checks-node-agentic-gateway-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082899
  - checks-node-auto-reply-reply-commands: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082900
  - checks-node-agentic-commands-onboard-config: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082901
  - checks-node-agentic-agents: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082910
  - checks-node-agentic-gateway-methods: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082912
  - checks-node-auto-reply-core-top-level: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082915
  - checks-node-auto-reply-reply-state-routing: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082916
  - checks-node-agentic-plugin-sdk: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082917
  - checks-node-auto-reply-reply-dispatch: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082923
  - checks-node-auto-reply-reply-session: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082929
  - checks-node-auto-reply-reply-agent-runner: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345082930
  - security-fast: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345091445
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345092530
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345092610
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345092784
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345092999
  - checks-fast-contracts-channels: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345096599
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345098766
  - checks-fast-contracts-plugins: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345132306
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355925977/job/74345174794
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355926222
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345064346
  - Run QA Lab parity lane (${{ matrix.lane }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092006
  - Run QA Lab live Slack lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092018
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092025
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092097
  - Prepare release package artifact: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092128
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092275
  - Run QA Lab parity report: cancelled - https://github.com/openclaw/openclaw/actions/runs/25355926222/job/74345092394

## Notes

Automatically requested by Full Release Validation 25355912948 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


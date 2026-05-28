# OpenClaw Release Evidence: a2cab17ff057bfeaf5ce49aa960a00059300f35f

Generated: 2026-05-02T04:27:07.315Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `a2cab17ff057bfeaf5ce49aa960a00059300f35f` |
| Release ref input | `a2cab17ff057bfeaf5ce49aa960a00059300f35f` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `a2cab17ff057bfeaf5ce49aa960a00059300f35f` |
| Release ref SHA | `a2cab17ff057bfeaf5ce49aa960a00059300f35f` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 3 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/a2cab17ff057-1777695761281` | `a2cab17ff057` | 4m 15s | 8m 40s | 4m 1s | [25243652151](https://github.com/openclaw/openclaw/actions/runs/25243652151) | 0 |
| fail | blocking | `normal-ci` | CI | `release-ci/a2cab17ff057-1777695761281` | `a2cab17ff057` | 3m 5s | 57m 51s | 3m 2s | [25243657921](https://github.com/openclaw/openclaw/actions/runs/25243657921) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/a2cab17ff057-1777695761281` | `a2cab17ff057` | 20s | 6s | 16s | [25243658123](https://github.com/openclaw/openclaw/actions/runs/25243658123) | 0 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/a2cab17ff057-1777695761281` | `a2cab17ff057` | 38s | 26s | 11s | [25243672078](https://github.com/openclaw/openclaw/actions/runs/25243672078) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 3m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243652151/job/74023944956) |
| 3m 12s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243652151/job/74023944962) |
| 2m 43s | `normal-ci` | checks-node-core-runtime-infra | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023961056) |
| 2m 14s | `normal-ci` | checks-node-core-runtime-media-ui | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023961046) |
| 1m 57s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960921) |
| 1m 46s | `normal-ci` | checks-node-core-fast-support | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023961072) |
| 1m 36s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960944) |
| 1m 34s | `normal-ci` | checks-fast-contracts-channels-c | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960925) |
| 1m 34s | `normal-ci` | checks-node-agentic-commands-status-tools | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023961077) |
| 1m 31s | `normal-ci` | checks-node-auto-reply-reply-dispatch | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023961081) |
| 1m 30s | `normal-ci` | checks-fast-contracts-channels-b | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960904) |
| 1m 25s | `normal-ci` | checks-fast-contracts-channels-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960917) |
| 43s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243652151/job/74023975456) |
| 40s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243652151/job/74023944986) |
| 26s | `postpublish-telegram` | Run package Telegram E2E | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25243672078/job/74023984666) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 4m 1s | 13s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25243652151/job/74024102301) |
| 3m 2s | 2s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74024075629) |
| 1m 52s | 3s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74024027778) |
| 1m 36s | 3s | `normal-ci` | check-additional | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74024015486) |
| 1m 35s | 3s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74024015061) |
| 1m 25s | 2s | `normal-ci` | check | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74024004737) |
| 1m 3s | 43s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243652151/job/74023975456) |
| 58s | 2s | `normal-ci` | build-smoke | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023986237) |
| 50s | 0s | `normal-ci` | matrix.check_name | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023986309) |
| 50s | 0s | `normal-ci` | matrix.check_name | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023986353) |
| 41s | 1m 7s | `normal-ci` | checks-windows-node-test | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960903) |
| 29s | 34s | `normal-ci` | macos-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960939) |
| 16s | 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243658123/job/74023959866) |
| 15s | 3m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243652151/job/74023944956) |
| 15s | 3m 12s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25243652151/job/74023944962) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25243652151
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25243652151/job/74024102301
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921
  - build-artifacts: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960900
  - checks-node-compat-node22: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960905
  - check-prod-types: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960940
  - check-dependencies: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960942
  - check-lint: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960943
  - check-additional-extension-package-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960948
  - check-strict-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960950
  - check-additional-extension-channels: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960953
  - check-test-types: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960954
  - check-additional-extension-bundled: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023960974
  - build-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74023986237
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74024004737
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74024015486
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25243657921/job/74024075629
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25243658123
  - resolve_target: failure - https://github.com/openclaw/openclaw/actions/runs/25243658123/job/74023951905
- `postpublish-telegram`: failure - https://github.com/openclaw/openclaw/actions/runs/25243672078
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25243672078/job/74023984666

## Notes

Automatically requested by Full Release Validation 25243652151 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


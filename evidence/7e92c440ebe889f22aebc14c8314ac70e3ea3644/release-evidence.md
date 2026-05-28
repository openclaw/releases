# OpenClaw Release Evidence: 7e92c440ebe889f22aebc14c8314ac70e3ea3644

Generated: 2026-05-03T22:54:10.919Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `7e92c440ebe889f22aebc14c8314ac70e3ea3644` |
| Release ref input | `7e92c440ebe889f22aebc14c8314ac70e3ea3644` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `7e92c440ebe889f22aebc14c8314ac70e3ea3644` |
| Release ref SHA | `7e92c440ebe889f22aebc14c8314ac70e3ea3644` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 0 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/7e92c440ebe8-1777847941351` | `7e92c440ebe8` | 14m 39s | 29m 38s | 14m 9s | [25292866438](https://github.com/openclaw/openclaw/actions/runs/25292866438) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/7e92c440ebe8-1777847941351` | `7e92c440ebe8` | 3m 57s | 1h 12m 41s | 3m 54s | [25292872958](https://github.com/openclaw/openclaw/actions/runs/25292872958) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/7e92c440ebe8-1777847941351` | `7e92c440ebe8` | 7m 21s | 1h 48m 24s | 7m 20s | [25292873331](https://github.com/openclaw/openclaw/actions/runs/25292873331) | 28 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/7e92c440ebe8-1777847941351` | `7e92c440ebe8` | 1m 38s | 1m 34s | 3s | [25292928549](https://github.com/openclaw/openclaw/actions/runs/25292928549) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 13m 51s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292866438/job/74147179342) |
| 6m 45s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292866438/job/74147179345) |
| 6m 15s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147401296) |
| 4m 25s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147355650) |
| 4m 13s | `release-checks` | Run QA Lab live Slack lane | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147241834) |
| 4m 12s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292866438/job/74147179346) |
| 3m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147291981) |
| 3m 37s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292872958/job/74147196232) |
| 3m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147401312) |
| 3m 2s | `release-checks` | Run repo/live E2E validation / Live media suites (Native live media video plugins B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147291868) |
| 2m 57s | `release-checks` | Run repo/live E2E validation / Live media suites (Native live media video plugins C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147291865) |
| 2m 54s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147291948) |
| 2m 35s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147511905) |
| 2m 26s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292866438/job/74147179337) |
| 2m 25s | `release-checks` | Run repo/live E2E validation / validate_repo_e2e | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147291815) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 14m 9s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292866438/job/74147889194) |
| 7m 20s | 1m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147555870) |
| 7m 20s | 1m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147555871) |
| 7m 20s | 1m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147555872) |
| 7m 19s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147555863) |
| 7m 19s | 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147555873) |
| 7m 9s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147555861) |
| 7m 8s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147555958) |
| 7m 8s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147556043) |
| 6m 43s | 1m 21s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147511954) |
| 6m 42s | 1m 7s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292873331/job/74147511904) |
| 3m 54s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292872958/job/74147381655) |
| 2m 43s | 1m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292866438/job/74147304947) |
| 2m 37s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292872958/job/74147311973) |
| 2m 15s | 3s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292872958/job/74147298037) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292866438
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292866438/job/74147179342
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25292866438/job/74147889194

## Notes

Automatically requested by Full Release Validation 25292866438 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


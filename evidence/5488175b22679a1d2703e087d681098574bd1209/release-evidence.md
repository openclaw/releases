# OpenClaw Release Evidence: 5488175b22679a1d2703e087d681098574bd1209

Generated: 2026-04-27T22:29:45.124Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `5488175b22679a1d2703e087d681098574bd1209` |
| Release ref input | `5488175b22679a1d2703e087d681098574bd1209` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `5488175b22679a1d2703e087d681098574bd1209` |
| Release ref SHA | `5488175b22679a1d2703e087d681098574bd1209` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `5488175b2267` | 21m 22s | 24m 55s | [25022172895](https://github.com/openclaw/openclaw/actions/runs/25022172895) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `61a18e5596c8` | 3m 12s | 55m 39s | [25022207041](https://github.com/openclaw/openclaw/actions/runs/25022207041) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `5488175b2267` | 19m 55s | 4h 50m 37s | [25022206695](https://github.com/openclaw/openclaw/actions/runs/25022206695) | 26 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 20m 24s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022172895/job/73285107671) |
| 15m 46s | `release-checks` | install_smoke_release_checks / install-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285221634) |
| 14m 23s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-core, Native live gateway core, node scrip... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285301406) |
| 11m 36s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285955428) |
| 11m 9s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-gateway-docker, Docker live gateway, pnpm test:docker:live-ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285301397) |
| 10m 55s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285301414) |
| 10m 12s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285540303) |
| 9m 44s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285955395) |
| 9m 40s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285955427) |
| 9m 20s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285955416) |
| 8m 54s | `release-checks` | live_and_e2e_release_checks / Docker E2E (bundled channels) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285955418) |
| 3m 40s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022172895/job/73285107668) |
| 2m 50s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022207041/job/73285148743) |
| 1m 59s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022207041/job/73285148559) |
| 1m 58s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022207041/job/73285148851) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25022172895
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25022172895/job/73287645894
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25022206695
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285540311
  - live_and_e2e_release_checks / Docker E2E (bundled channels): failure - https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73285955418
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25022206695/job/73287589417

## Notes

Automatically requested by Full Release Validation 25022172895 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


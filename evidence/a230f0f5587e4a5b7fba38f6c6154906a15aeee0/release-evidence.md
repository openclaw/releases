# OpenClaw Release Evidence: a230f0f5587e4a5b7fba38f6c6154906a15aeee0

Generated: 2026-04-27T23:52:22.383Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `a230f0f5587e4a5b7fba38f6c6154906a15aeee0` |
| Release ref input | `a230f0f5587e4a5b7fba38f6c6154906a15aeee0` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `a230f0f5587e4a5b7fba38f6c6154906a15aeee0` |
| Release ref SHA | `a230f0f5587e4a5b7fba38f6c6154906a15aeee0` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.4.26` | `a230f0f5587e` | 27m 33s | 31m 7s | [25024934600](https://github.com/openclaw/openclaw/actions/runs/25024934600) | 0 |
| pass | blocking | `normal-ci` | CI | `release/2026.4.26` | `a230f0f5587e` | 3m 7s | 56m 46s | [25024963931](https://github.com/openclaw/openclaw/actions/runs/25024963931) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.4.26` | `a230f0f5587e` | 26m 23s | 4h 34m 28s | [25024963397](https://github.com/openclaw/openclaw/actions/runs/25024963397) | 22 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 26m 35s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024934600/job/73293903381) |
| 20m 51s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294425424) |
| 16m 48s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway, Native live gateway, node scripts/test-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294067733) |
| 14m 52s | `release-checks` | live_and_e2e_release_checks / Docker E2E (bundled channels) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294425415) |
| 14m 21s | `release-checks` | install_smoke_release_checks / install-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294001335) |
| 12m 44s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294425421) |
| 9m 54s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294243481) |
| 9m 9s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-l-z, Native live plugins L-Z, node scripts/... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294067731) |
| 8m 50s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-agents, Native live agents, node scripts/test-live... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294067732) |
| 8m 27s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-gateway-docker, Docker live gateway, pnpm test:docker:live-ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294067739) |
| 8m 19s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294067753) |
| 3m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024934600/job/73293903379) |
| 2m 24s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963931/job/73293944053) |
| 2m 16s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963931/job/73293944298) |
| 2m 6s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25024963931/job/73293944314) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25024934600
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25024934600/job/73296682812
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25024963397
  - live_and_e2e_release_checks / Docker E2E (bundled channels): failure - https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73294425415
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25024963397/job/73296658041

## Notes

Automatically requested by Full Release Validation 25024934600 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


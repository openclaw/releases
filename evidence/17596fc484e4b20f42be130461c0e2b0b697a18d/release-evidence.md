# OpenClaw Release Evidence: 17596fc484e4b20f42be130461c0e2b0b697a18d

Generated: 2026-04-27T22:39:21.024Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `17596fc484e4b20f42be130461c0e2b0b697a18d` |
| Release ref input | `17596fc484e4b20f42be130461c0e2b0b697a18d` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `17596fc484e4b20f42be130461c0e2b0b697a18d` |
| Release ref SHA | `17596fc484e4b20f42be130461c0e2b0b697a18d` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.4.26` | `17596fc484e4` | 20m 56s | 24m 25s | [25022553843](https://github.com/openclaw/openclaw/actions/runs/25022553843) | 0 |
| pass | blocking | `normal-ci` | CI | `release/2026.4.26` | `17596fc484e4` | 3m 6s | 56m 3s | [25022590450](https://github.com/openclaw/openclaw/actions/runs/25022590450) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.4.26` | `17596fc484e4` | 11m 7s | 4h 7m 40s | [25022591792](https://github.com/openclaw/openclaw/actions/runs/25022591792) | 21 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 19m 50s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25022553843/job/73286390010) |
| 16m 36s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway, Native live gateway, node scripts/test-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022591792/job/73286588990) |
| 13m 1s | `release-checks` | install_smoke_release_checks / install-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022591792/job/73286507213) |
| 11m 41s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022591792/job/73287063875) |
| 10m 31s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-l-z, Native live plugins L-Z, node scripts/... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25022591792/job/73286588925) |
| 9m 35s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022591792/job/73286589027) |
| 9m 20s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022591792/job/73286846601) |
| 8m 33s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-gateway-docker, Docker live gateway, pnpm test:docker:live-ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022591792/job/73286589000) |
| 8m 29s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-agents, Native live agents, node scripts/test-live... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022591792/job/73286588991) |
| 7m 48s | `release-checks` | live_and_e2e_release_checks / Docker E2E (bundled channels) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25022591792/job/73287063876) |
| 7m 31s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022591792/job/73286846577) |
| 3m 38s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022553843/job/73286389997) |
| 2m 44s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022590450/job/73286434420) |
| 2m 10s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022590450/job/73286434438) |
| 1m 57s | `normal-ci` | checks-node-core-runtime-infra | success | [job](https://github.com/openclaw/openclaw/actions/runs/25022590450/job/73286434394) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25022553843
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25022553843/job/73286390010
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25022553843/job/73288785825

## Notes

Automatically requested by Full Release Validation 25022553843 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


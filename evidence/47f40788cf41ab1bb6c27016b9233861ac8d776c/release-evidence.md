# OpenClaw Release Evidence: 47f40788cf41ab1bb6c27016b9233861ac8d776c

Generated: 2026-04-28T00:23:42.829Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `47f40788cf41ab1bb6c27016b9233861ac8d776c` |
| Release ref input | `47f40788cf41ab1bb6c27016b9233861ac8d776c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `47f40788cf41ab1bb6c27016b9233861ac8d776c` |
| Release ref SHA | `47f40788cf41ab1bb6c27016b9233861ac8d776c` |
| Runs at release SHA | `full-release-validation` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `47f40788cf41` | 25m 36s | 25m 27s | [25026046281](https://github.com/openclaw/openclaw/actions/runs/25026046281) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `32d76e2429ab` | 24m 14s | 4h 31m 30s | [25026076913](https://github.com/openclaw/openclaw/actions/runs/25026076913) | 12 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 24m 36s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026046281/job/73297341982) |
| 22m 38s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-other, Native live gateway profil... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297502929) |
| 14m 38s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297883346) |
| 14m 29s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297502946) |
| 14m 9s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297883323) |
| 12m 49s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297883341) |
| 11m 11s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-gateway-docker, Docker live gateway, pnpm test:docker:live-ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297502955) |
| 11m 5s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297502921) |
| 9m 54s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297883340) |
| 9m 45s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297883334) |
| 9m 38s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297502941) |
| 45s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026046281/job/73297268459) |
| 6s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25026046281/job/73299836006) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25026046281
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25026046281/job/73299836006
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25026076913
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: failure - https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297502921
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: failure - https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297502938
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: failure - https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73297502946
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25026076913/job/73299797808

## Notes

Automatically requested by Full Release Validation 25026046281 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


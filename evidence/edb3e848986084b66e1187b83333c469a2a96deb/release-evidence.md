# OpenClaw Release Evidence: edb3e848986084b66e1187b83333c469a2a96deb

Generated: 2026-04-27T11:36:59.657Z
Release ref: `edb3e848986084b66e1187b83333c469a2a96deb`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 3 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `edb3e8489860` | [24990481836](https://github.com/openclaw/openclaw/actions/runs/24990481836) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `edb3e8489860` | [24990522452](https://github.com/openclaw/openclaw/actions/runs/24990522452) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `edb3e8489860` | [24990522914](https://github.com/openclaw/openclaw/actions/runs/24990522914) | 21 |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/24990481836
  - Run release/live/Docker/QA validation: failure - https://github.com/openclaw/openclaw/actions/runs/24990481836/job/73174673297
  - Run normal full CI: failure - https://github.com/openclaw/openclaw/actions/runs/24990481836/job/73174673329
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24990481836/job/73181988423
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/24990522452
  - checks-node-agentic-agents: failure - https://github.com/openclaw/openclaw/actions/runs/24990522452/job/73174715635
  - checks-node-core-runtime-infra: failure - https://github.com/openclaw/openclaw/actions/runs/24990522452/job/73174715654
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/24990522452/job/73175182605
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/24990522914
  - live_and_e2e_release_checks / validate_live_provider_suites (live-all, pnpm test:live, pnpm test:live, 180, false): failure - https://github.com/openclaw/openclaw/actions/runs/24990522914/job/73174903216
  - live_and_e2e_release_checks / Docker E2E (plugins/integrations): failure - https://github.com/openclaw/openclaw/actions/runs/24990522914/job/73175920052
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/24990522914/job/73181840786

## Notes

Automatically requested by Full Release Validation 24990481836 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


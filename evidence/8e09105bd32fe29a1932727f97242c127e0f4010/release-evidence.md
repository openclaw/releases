# OpenClaw Release Evidence: 8e09105bd32fe29a1932727f97242c127e0f4010

Generated: 2026-04-27T13:32:59.465Z
Release ref: `8e09105bd32fe29a1932727f97242c127e0f4010`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `73ba282b54cd` | [24997848265](https://github.com/openclaw/openclaw/actions/runs/24997848265) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `73ba282b54cd` | [24997892747](https://github.com/openclaw/openclaw/actions/runs/24997892747) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `73ba282b54cd` | [24997894431](https://github.com/openclaw/openclaw/actions/runs/24997894431) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997848265
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997848265/job/73199617713
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997848265/job/73199617749
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24997848265/job/73200273199
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997892747
  - checks-fast-protocol: failure - https://github.com/openclaw/openclaw/actions/runs/24997892747/job/73199677988
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997892747/job/73199678080
  - check-lint: failure - https://github.com/openclaw/openclaw/actions/runs/24997892747/job/73199678189
  - checks-node-agentic-agents: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997892747/job/73199678323
  - checks-node-core-fast-support: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997892747/job/73199678381
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/24997892747/job/73199825639
  - checks-node-channels: failure - https://github.com/openclaw/openclaw/actions/runs/24997892747/job/73199998799
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997892747/job/73200193403
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431
  - Run QA Lab parity gate: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200098690
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200098728
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200098785
  - live_and_e2e_release_checks / validate_selected_ref: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200098884
  - cross_os_release_checks / prepare: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200099075
  - Run package acceptance / Resolve package candidate: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200099141
  - install_smoke_release_checks / docker-e2e-fast: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200132629
  - install_smoke_release_checks / install-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200132669
  - cross_os_release_checks / ${{ matrix.display_name }} / ${{ matrix.suite_label }}: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200219047
  - live_and_e2e_release_checks / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200246955
  - live_and_e2e_release_checks / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200247277
  - live_and_e2e_release_checks / validate_special_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200247299
  - live_and_e2e_release_checks / validate_live_provider_suites: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200247364
  - live_and_e2e_release_checks / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200247380
  - live_and_e2e_release_checks / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200247388
  - live_and_e2e_release_checks / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200247487
  - live_and_e2e_release_checks / Docker E2E targeted lanes: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200247488
  - live_and_e2e_release_checks / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200247493
  - live_and_e2e_release_checks / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200247794
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200266500
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/24997894431/job/73200311275

## Notes

Automatically requested by Full Release Validation 24997848265 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


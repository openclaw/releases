# OpenClaw Release Evidence: 2026.4.24

Generated: 2026-04-27T05:14:02.747Z
Release ref: `v2026.4.24`
Package spec: `openclaw@2026.4.24`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 4 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `6987132aed84` | [24977011361](https://github.com/openclaw/openclaw/actions/runs/24977011361) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `6987132aed84` | [24977031325](https://github.com/openclaw/openclaw/actions/runs/24977031325) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `6987132aed84` | [24977032095](https://github.com/openclaw/openclaw/actions/runs/24977032095) | 15 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `main` | `6987132aed84` | [24977031342](https://github.com/openclaw/openclaw/actions/runs/24977031342) | 0 |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/24977011361
  - Run post-publish Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/24977011361/job/73130835710
  - Run release/live/Docker/QA validation: failure - https://github.com/openclaw/openclaw/actions/runs/24977011361/job/73130835712
  - Run normal full CI: failure - https://github.com/openclaw/openclaw/actions/runs/24977011361/job/73130835721
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24977011361/job/73132869407
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/24977031325
  - macos-swift: failure - https://github.com/openclaw/openclaw/actions/runs/24977031325/job/73130857058
  - checks-node-agentic-plugin-sdk: failure - https://github.com/openclaw/openclaw/actions/runs/24977031325/job/73130857140
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/24977031325/job/73131004310
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/24977032095
  - Run QA Lab live Matrix lane: failure - https://github.com/openclaw/openclaw/actions/runs/24977032095/job/73130894881
  - live_and_e2e_release_checks / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/24977032095/job/73130946608
  - live_and_e2e_release_checks / prepare_docker_e2e_image: failure - https://github.com/openclaw/openclaw/actions/runs/24977032095/job/73130946609
  - live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-...: failure - https://github.com/openclaw/openclaw/actions/runs/24977032095/job/73130946615
  - live_and_e2e_release_checks / validate_live_provider_suites (live-all, pnpm test:live, pnpm test:live, 180, false): failure - https://github.com/openclaw/openclaw/actions/runs/24977032095/job/73130946621
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/24977032095/job/73131051726
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes: failure - https://github.com/openclaw/openclaw/actions/runs/24977032095/job/73131301893
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/24977032095/job/73131370108
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/24977032095/job/73132833956
- `postpublish-telegram`: failure - https://github.com/openclaw/openclaw/actions/runs/24977031342
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/24977031342/job/73130841851

## Notes

Manual ingest for Full Release Validation 24977011361. This run was started before automatic repository_dispatch evidence wiring landed, so it did not self-dispatch.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


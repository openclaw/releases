# OpenClaw Release Evidence: 2026.4.20

Generated: 2026-04-27T04:55:59.736Z
Release ref: `v2026.4.20`
Package spec: `openclaw@2026.4.20`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 5 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| pass | blocking | `npm-preflight` | OpenClaw NPM Release | `release/2026.4.20` | `115f05d5952a` | [24741753647](https://github.com/openclaw/openclaw/actions/runs/24741753647) | 1 |
| pass | blocking | `npm-publish` | OpenClaw NPM Release | `release/2026.4.20` | `6c54231bbd25` | [24743354114](https://github.com/openclaw/openclaw/actions/runs/24743354114) | 0 |
| pass | advisory | `public-macos-release` | macOS Release | `release/2026.4.20` | `6c54231bbd25` | [24741938232](https://github.com/openclaw/openclaw/actions/runs/24741938232) | 0 |
| pass | blocking | `macos-validate` | OpenClaw macOS Validate | `main` | `53a638d5a1d6` | [24741765175](https://github.com/openclaw/releases-private/actions/runs/24741765175) | 1 |
| pass | blocking | `macos-preflight` | OpenClaw macOS Publish | `main` | `624ac4ff37e8` | [24741938154](https://github.com/openclaw/releases-private/actions/runs/24741938154) | 2 |
| pass | blocking | `macos-publish` | OpenClaw macOS Publish | `main` | `624ac4ff37e8` | [24743353647](https://github.com/openclaw/releases-private/actions/runs/24743353647) | 2 |

## Notes

Backfilled on 2026-04-27 from existing Actions history. This records the successful npm and macOS release automation runs visible for the shipped release train.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


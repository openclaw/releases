# OpenClaw Release Evidence: 2026.4.24

Generated: 2026-04-27T04:42:49.304Z
Release ref: `v2026.4.24`
Package spec: `openclaw@2026.4.24`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 5 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| pass | blocking | `npm-preflight` | OpenClaw NPM Release | `release/2026.4.24` | `cbcfdf62c729` | [24937044224](https://github.com/openclaw/openclaw/actions/runs/24937044224) | 1 |
| pass | blocking | `npm-publish` | OpenClaw NPM Release | `release/2026.4.24` | `cbcfdf62c729` | [24937293696](https://github.com/openclaw/openclaw/actions/runs/24937293696) | 0 |
| pass | advisory | `public-macos-release` | macOS Release | `release/2026.4.24` | `cbcfdf62c729` | [24938395023](https://github.com/openclaw/openclaw/actions/runs/24938395023) | 0 |
| pass | blocking | `macos-validate` | OpenClaw macOS Validate | `main` | `b1cd149b3f54` | [24938444053](https://github.com/openclaw/releases-private/actions/runs/24938444053) | 1 |
| pass | blocking | `macos-preflight` | OpenClaw macOS Publish | `main` | `b1cd149b3f54` | [24938518217](https://github.com/openclaw/releases-private/actions/runs/24938518217) | 2 |
| pass | blocking | `macos-publish` | OpenClaw macOS Publish | `main` | `b1cd149b3f54` | [24938996336](https://github.com/openclaw/releases-private/actions/runs/24938996336) | 2 |

## Notes

Latest stable as of 2026-04-27: npm latest resolves to openclaw@2026.4.24 and GitHub release v2026.4.24 is the latest non-prerelease. Package Acceptance was not found on the release/2026.4.24 branch; this evidence records the release automation runs that exist for that release train.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


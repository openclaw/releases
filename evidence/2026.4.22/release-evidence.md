# OpenClaw Release Evidence: 2026.4.22

Generated: 2026-04-27T04:55:52.773Z
Release ref: `v2026.4.22`
Package spec: `openclaw@2026.4.22`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 5 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| pass | blocking | `npm-preflight` | OpenClaw NPM Release | `release/2026.4.22` | `2756d5f5641d` | [24840032131](https://github.com/openclaw/openclaw/actions/runs/24840032131) | 1 |
| pass | blocking | `npm-publish` | OpenClaw NPM Release | `release/2026.4.22` | `2756d5f5641d` | [24840545331](https://github.com/openclaw/openclaw/actions/runs/24840545331) | 0 |
| pass | blocking | `macos-validate` | OpenClaw macOS Validate | `main` | `b1cd149b3f54` | [24842109157](https://github.com/openclaw/releases/actions/runs/24842109157) | 1 |
| pass | blocking | `macos-preflight` | OpenClaw macOS Publish | `main` | `b1cd149b3f54` | [24842110669](https://github.com/openclaw/releases/actions/runs/24842110669) | 2 |
| pass | blocking | `macos-publish` | OpenClaw macOS Publish | `main` | `b1cd149b3f54` | [24843374044](https://github.com/openclaw/releases/actions/runs/24843374044) | 2 |

## Notes

Backfilled on 2026-04-27 from existing Actions history. Earlier release-check/mac attempts existed for this branch, including cancelled or failed attempts; this report records the successful release automation runs that map to the shipped train.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


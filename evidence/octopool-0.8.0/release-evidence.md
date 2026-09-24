# OpenClaw Release Evidence: octopool-0.8.0

Generated: 2026-09-24T20:30:54.852Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.8.0` |
| Release ref input | not recorded |
| Release ref status | not-recorded |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `ci` | CI | `main` | `56dd03c66a21` | 7m 31s | 12m 33s | 3s | [36051642807](https://github.com/openclaw/octopool/actions/runs/36051642807) | 0 |
| pass | blocking | `release` | release | `v0.8.0` | `56dd03c66a21` | 1m 24s | 1m 20s | 3s | [36051689337](https://github.com/openclaw/octopool/actions/runs/36051689337) | 0 |
| pass | blocking | `tap` | Update octopool for v0.8.0 (request-id=octopool-0.8.0-38193832379e; source-tag-object=d3b30314207c5821ed91d18a2d4c7a9f5fdb63c3; source-tag-commit=56dd03c66a2171c0a6737ffbe1cf9673e0c52e36) | `main` | `a67952ca969f` | 1m 32s | 1m 24s | 7s | [36053438184](https://github.com/openclaw/homebrew-tap/actions/runs/36053438184) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 7m 28s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/36051642807/job/107808382931) |
| 5m 5s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/36051642807/job/107808382605) |
| 1m 24s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/36053438184/job/107814458988) |
| 1m 20s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/36051689337/job/107808547635) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 7s | 1m 24s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/36053438184/job/107814458988) |
| 3s | 7m 28s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/36051642807/job/107808382931) |
| 3s | 1m 20s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/36051689337/job/107808547635) |
| 2s | 5m 5s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/36051642807/job/107808382605) |

## Notes

Octopool 0.8.0 (Go CLI + Cloudflare Worker).
Tag: v0.8.0 (annotated, SSH-signed; tag object d3b30314207c5821ed91d18a2d4c7a9f5fdb63c3, commit 56dd03c66a2171c0a6737ffbe1cf9673e0c52e36).
Release: https://github.com/openclaw/octopool/releases/tag/v0.8.0 (body verified identical to the CHANGELOG 0.8.0 section).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, secure timestamp; notarization Accepted (arm64 0fc07fd7-be1f-4bdb-a86a-67d7e977c0c6, amd64 92a6636e-53a9-4ede-88b5-582d0921c434); spctl: Notarized Developer ID on the re-downloaded release asset.
Final checksums.txt (post-signing): darwin_arm64 07a6be3c75f81d1920db4310aa13d4a1361849ab698e009ee7905de4aa00ccd7, darwin_amd64 9356b11d1ff45f312aa5f51d748e7fd9792042b80ce763c195a8ff86bf84e620; all six assets re-verified with shasum -c after upload.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb 0.8.0 (commit 161f9aa) with the final hashes.
Worker: octopool + octopool-public-proxy deployed from 56dd03c (versions 6092cac8-ac48-41c3-9eb0-3210b46c0e2f, 23557a55-5f73-40e0-b89d-936ef347c215).

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


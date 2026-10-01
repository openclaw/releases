# OpenClaw Release Evidence: octopool-0.9.3

Generated: 2026-10-01T20:46:56.919Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.3` |
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
| pass | blocking | `ci` | CI | `main` | `72415ef0e220` | 9m 5s | 12m 55s | 5s | [36921312604](https://github.com/openclaw/octopool/actions/runs/36921312604) | 0 |
| pass | blocking | `release` | release | `v0.9.3` | `72415ef0e220` | 1m 35s | 1m 31s | 3s | [36921341049](https://github.com/openclaw/octopool/actions/runs/36921341049) | 0 |
| pass | blocking | `tap` | Update octopool for v0.9.3 (request-id=octopool-0.9.3-68c0d1f45fd3; source-tag-object=0e44154ba218814dc627064bbe46ade49bdb0a6d; source-tag-commit=72415ef0e2208f598ea1420a23cc823cde4978ca) | `main` | `84bb057533e4` | 1m 30s | 1m 21s | 8s | [36922951164](https://github.com/openclaw/homebrew-tap/actions/runs/36922951164) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 9m 2s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/36921312604/job/110567789056) |
| 3m 53s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/36921312604/job/110567789711) |
| 1m 31s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/36921341049/job/110567883906) |
| 1m 21s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/36922951164/job/110573222718) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 8s | 1m 21s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/36922951164/job/110573222718) |
| 5s | 3m 53s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/36921312604/job/110567789711) |
| 3s | 9m 2s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/36921312604/job/110567789056) |
| 3s | 1m 31s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/36921341049/job/110567883906) |

## Notes

Octopool 0.9.3 (Go CLI; Worker changes already deployed).
Tag: v0.9.3 (annotated, SSH-signed; tag object 0e44154ba218814dc627064bbe46ade49bdb0a6d, commit 72415ef0e2208f598ea1420a23cc823cde4978ca).
Release: https://github.com/openclaw/octopool/releases/tag/v0.9.3 (body verified identical to the CHANGELOG 0.9.3 section).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, secure timestamp; notarization Accepted (arm64 835ccbd1-7a75-4638-8af9-82b77626b010, amd64 9d50f99a-2f0e-45bf-a05a-ea0b77b2df2b); spctl: Notarized Developer ID on the re-downloaded asset.
Final checksums (post-signing): darwin_arm64 f990f2957abf0e2d0bfa2832de08b02fe5ca393d690255045b15689f8c73c0e3, darwin_amd64 0b88e9ba1e07b52818b2b65b31d37f65fcb09a2424304a765aa6a048d7b2a88f; all six archives re-verified with shasum -c.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb 0.9.3 (commit b75fdbb), all four platform sha256 values verified.
Worker: deployed from main 64f1bba (cache_created_at, same-repo GraphQL aliases, six-hour terminal CI TTL); no D1 migrations; the release commit changes only CHANGELOG.md. Live proof: production graphql_read relay of the Codex-app batch shape with local viewer splice and shared-cache hits; new terminal job entries written with 21600 s TTL.
Fleet: clawstudio, steipete-studio-sf, steipete-mini-sf, megaclaw, miniclaw, steipete-studio-sf-worker report octopool 0.9.3 (72415ef) and relay with OCTOPOOL_NO_FALLBACK=1; steipete-mbp unreachable over SSH at release time (pending).

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


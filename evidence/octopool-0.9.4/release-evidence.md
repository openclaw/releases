# OpenClaw Release Evidence: octopool-0.9.4

Generated: 2026-10-02T18:53:59.807Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.4` |
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
| pass | blocking | `ci` | CI | `main` | `5e80b005abec` | 8m 30s | 13m 39s | 4s | [37048615590](https://github.com/openclaw/octopool/actions/runs/37048615590) | 0 |
| pass | blocking | `release` | release | `v0.9.4` | `5e80b005abec` | 1m 43s | 1m 38s | 4s | [37048647937](https://github.com/openclaw/octopool/actions/runs/37048647937) | 0 |
| pass | blocking | `tap` | Update octopool for v0.9.4 (request-id=octopool-0.9.4-aa6e8fd34b17; source-tag-object=2bc8295cfaf551c71e5672407061ea8dc7b8b3cb; source-tag-commit=5e80b005abecba628d0d991cd07451ebe723055f) | `main` | `445b061f4e51` | 1m 44s | 1m 35s | 9s | [37049472542](https://github.com/openclaw/homebrew-tap/actions/runs/37049472542) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 8m 26s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37048615590/job/110976135213) |
| 5m 13s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37048615590/job/110976135434) |
| 1m 38s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/37048647937/job/110976240721) |
| 1m 35s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/37049472542/job/110978958827) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 9s | 1m 35s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/37049472542/job/110978958827) |
| 4s | 8m 26s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37048615590/job/110976135213) |
| 4s | 1m 38s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/37048647937/job/110976240721) |
| 3s | 5m 13s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37048615590/job/110976135434) |

## Notes

Octopool 0.9.4 (Go CLI; Worker change already deployed).
Tag: v0.9.4 (annotated, SSH-signed; tag object 2bc8295cfaf551c71e5672407061ea8dc7b8b3cb, commit 5e80b005abecba628d0d991cd07451ebe723055f).
Release: https://github.com/openclaw/octopool/releases/tag/v0.9.4 (body verified identical to the CHANGELOG 0.9.4 section).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, secure timestamp; notarization Accepted (arm64 f4973687-6145-4f59-911d-7d82e5d70c55, amd64 828b1388-49ed-49f6-9de6-e68c6431b4ab); spctl: Notarized Developer ID on the re-downloaded asset.
Final checksums (post-signing): darwin_arm64 e625272be8ea9b1e3a7b300f8f59e799c74018517ac787e532fe31a9ec5cdc67, darwin_amd64 b18af42a06258ae032df5274e09c08e78760dc5ffb478f1ed242b62832cb697a; all six archives re-verified with shasum -c.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb 0.9.4 (commit f81e086), all four platform sha256 values verified.
Worker: deployed from main d40157d (admission RPC retry and fallback); no D1 migrations; the release commit changes only CHANGELOG.md.
CLI proof: with cache writes denied via sandbox-exec, a 30-way relay-eligible GraphQL burst gave v0.9.3 8 relayed / 22 relay_overloaded fallbacks and the fixed build 30/30 relayed.
Fleet: clawstudio, steipete-studio-sf, steipete-mini-sf, megaclaw, miniclaw, steipete-studio-sf-worker report octopool 0.9.4 (5e80b00) and relay with OCTOPOOL_NO_FALLBACK=1; steipete-mbp unreachable over SSH (pending manual brew upgrade).

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


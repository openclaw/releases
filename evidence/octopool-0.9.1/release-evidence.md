# OpenClaw Release Evidence: octopool-0.9.1

Generated: 2026-09-28T16:51:50.029Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.1` |
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
| pass | blocking | `ci` | CI | `main` | `a8f2e6fd0e4a` | 8m 39s | 13m 36s | 3s | [36452303463](https://github.com/openclaw/octopool/actions/runs/36452303463) | 0 |
| pass | blocking | `release` | release | `v0.9.1` | `a8f2e6fd0e4a` | 1m 36s | 1m 32s | 3s | [36452324054](https://github.com/openclaw/octopool/actions/runs/36452324054) | 0 |
| pass | blocking | `tap` | Update octopool for v0.9.1 (request-id=octopool-0.9.1-a7291ea71170; source-tag-object=a8a65f26f1db401d5ab7c9457ee0c2f2db0b9b40; source-tag-commit=a8f2e6fd0e4a3c95f7257a122213288c728e3108) | `main` | `7ae946fd728a` | 1m 33s | 1m 23s | 9s | [36453341203](https://github.com/openclaw/homebrew-tap/actions/runs/36453341203) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 8m 36s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/36452303463/job/109029814709) |
| 5m 0s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/36452303463/job/109029815165) |
| 1m 32s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/36452324054/job/109029881790) |
| 1m 23s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/36453341203/job/109033307248) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 9s | 1m 23s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/36453341203/job/109033307248) |
| 3s | 5m 0s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/36452303463/job/109029815165) |
| 3s | 1m 32s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/36452324054/job/109029881790) |
| 2s | 8m 36s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/36452303463/job/109029814709) |

## Notes

Octopool 0.9.1 (Go CLI; Worker side already deployed).
Tag: v0.9.1 (annotated, SSH-signed; tag object a8a65f26f1db401d5ab7c9457ee0c2f2db0b9b40, commit a8f2e6fd0e4a3c95f7257a122213288c728e3108).
Release: https://github.com/openclaw/octopool/releases/tag/v0.9.1 (body verified identical to the CHANGELOG 0.9.1 section).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, secure timestamp; notarization Accepted (arm64 6f37e361-1482-4644-aa3a-f2d04fa39c38, amd64 d456e427-fd97-4d54-8813-dccddad121f7); spctl: Notarized Developer ID on the re-downloaded asset.
Final checksums (post-signing): darwin_arm64 ea161308867b999cfb761c029353b15e5d921730cf72d2189e3412fe50c66816, darwin_amd64 16526f6c29becf48deb65b2ab926d3c5fe6073db5930b97a7a8253dc391b7f7a; all six assets re-verified with shasum -c.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb 0.9.1 (commit 253ad79), all four platform sha256 values verified.
Worker: deployed from main e3b6968 (version ec50b67a-ad5d-43b0-be3d-ac8417c67a7f); the release commit changes only CHANGELOG.md.
Fleet: clawstudio, steipete-studio-sf, steipete-mbp-4, steipete-mini-sf, megaclaw, miniclaw, steipete-studio-sf-worker report octopool 0.9.1 (a8f2e6f) and relay with OCTOPOOL_NO_FALLBACK=1.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


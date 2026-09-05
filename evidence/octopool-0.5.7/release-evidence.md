# OpenClaw Release Evidence: octopool-0.5.7

Generated: 2026-08-27T06:57:39.856Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.5.7` |
| Release ref input | `v0.5.7` |
| Release ref status | not-found |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | `octopool@0.5.7` |
| npm status | invalid |
| npm error | only openclaw package specs are supported |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `release` | release | `v0.5.7` | `7ba4b49b4de9` | 1m 4s | 1m 0s | 3s | [33046470900](https://github.com/openclaw/octopool/actions/runs/33046470900) | 0 |
| pass | blocking | `release-ci` | CI | `main` | `7ba4b49b4de9` | 3m 6s | 3m 3s | 2s | [33046136622](https://github.com/openclaw/octopool/actions/runs/33046136622) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.5.7 (request-id=octopool-0.5.7-0f40ad0d4326; source-tag-object=a5df57f9d5418d394dde988d1c19ea32e2fc8d6f; source-tag-commit=7ba4b49b4de97ddeebe0e602af3d3996f597a56c) | `main` | `834bcfd8829e` | 45s | 41s | 3s | [33047059239](https://github.com/openclaw/homebrew-tap/actions/runs/33047059239) | 0 |
| fail | advisory | `evidence-publish` | OpenClaw Release Evidence | `main` | `a16c18008aaf` | 1m 34s | 1m 28s | 5s | [33047288038](https://github.com/openclaw/releases/actions/runs/33047288038) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 3m 3s | `release-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33046136622/job/98430461568) |
| 1m 28s | `evidence-publish` | write_evidence | failure | [job](https://github.com/openclaw/releases/actions/runs/33047288038/job/98434168109) |
| 1m 0s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33046470900/job/98431522439) |
| 41s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33047059239/job/98433421819) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 5s | 1m 28s | `evidence-publish` | write_evidence | failure | [job](https://github.com/openclaw/releases/actions/runs/33047288038/job/98434168109) |
| 3s | 1m 0s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33046470900/job/98431522439) |
| 3s | 41s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33047059239/job/98433421819) |
| 2s | 3m 3s | `release-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33046136622/job/98430461568) |

## Failures

- `evidence-publish`: failure - https://github.com/openclaw/releases/actions/runs/33047288038
  - write_evidence: failure - https://github.com/openclaw/releases/actions/runs/33047288038/job/98434168109

## Notes

Octopool v0.5.7: https://github.com/openclaw/octopool/releases/tag/v0.5.7

Source commit: 7ba4b49b4de97ddeebe0e602af3d3996f597a56c. Annotated tag object: a5df57f9d5418d394dde988d1c19ea32e2fc8d6f.

The workflow release_ref resolver targets openclaw/openclaw; a not-found result for v0.5.7 there is expected. The Octopool source tag and commit above were independently verified.

All six final archives and checksums.txt were downloaded and verified against SHA-256 and GitHub asset digests. The GitHub Release body exactly matches the tagged 0.5.7 changelog section.

Both Darwin binaries are signed by Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), notarized by Apple, and accepted by Gatekeeper as Notarized Developer ID.

Darwin amd64 notarization: 6b6f442f-0cde-4131-983d-38433c96a006 (Accepted).

Darwin arm64 notarization: 9289c988-7ead-4e70-920a-9d2726f5693b (Accepted).

octopool_0.5.7_darwin_amd64.tar.gz: sha256=05e4321eff591dae5044dcb392a1b2f78ef1fe21363d7eada208e85deedf5952

octopool_0.5.7_darwin_arm64.tar.gz: sha256=2b1b2491b62793bde35619c65ca21cda9c24ec8c0302c39eeb0d0ff18bd897d2

octopool_0.5.7_linux_amd64.tar.gz: sha256=b0ca0b3d6513b6f8ad3d6a75f0316fe01e9fd475dcc85968455db69c55e5a962

octopool_0.5.7_linux_arm64.tar.gz: sha256=1f3fb5a4236ce7727cd1bac34e31f78d1fd4425ea413d7d564ef1603bb119b5f

octopool_0.5.7_windows_amd64.zip: sha256=3743fa9cbc07ba40d855859a2ab44bbc6ff3e0c88132848ece5b1bfd6d17b6fd

octopool_0.5.7_windows_arm64.zip: sha256=f29b8666d18b321bf342070df1028dd33eb05a591a83b801aea0b1046b45496a

Local deterministic pnpm check passed: 277 unit tests, 99 Worker integration tests, format/lint/generated checks, TypeScript builds, Go tests and vet. Formatting and docs site build also passed for the release notes.

The networked compiled CLI -> local Workerd/D1/Durable Object -> public GitHub gate passed a token-free miss then cache hit, with isolated HOME, fake local auth, and fallback disabled.

Published Darwin arm64 CLI version: octopool 0.5.7 (7ba4b49, 2026-08-27T06:36:26Z). Published CLI live smoke passed copied-shim skipping, direct copied-gh invocation, explicit real-gh acceptance and explicit-shim rejection.

Public Go module metadata resolves v0.5.7 to the release commit, and go install of that tag into a temporary GOBIN succeeded.

package_spec is an evidence label. package.json is private tooling metadata; no npm publication was performed.

Fleet upgrades and Worker deployments were intentionally not performed; no installed shims or stored credentials were changed. Temporary notarization credential copies were removed.

The shared evidence workflow generated its report but could not push because its stored GitHub credential was rejected. This evidence was regenerated with the official generator and published through the documented maintainer fallback; no credentials or workflow configuration were changed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


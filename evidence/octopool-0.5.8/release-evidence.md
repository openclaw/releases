# OpenClaw Release Evidence: octopool-0.5.8

Generated: 2026-08-28T21:10:55.749Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.5.8` |
| Release ref input | `v0.5.8` |
| Release ref status | not-found |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | `octopool@0.5.8` |
| npm status | invalid |
| npm error | only openclaw package specs are supported |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 5 | 0 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `release` | release | `v0.5.8` | `7a0f0b05136b` | 1m 27s | 1m 22s | 4s | [33208831124](https://github.com/openclaw/octopool/actions/runs/33208831124) | 0 |
| pass | blocking | `release-ci` | CI | `main` | `7a0f0b05136b` | 3m 53s | 3m 46s | 6s | [33208431857](https://github.com/openclaw/octopool/actions/runs/33208431857) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.5.8 (request-id=octopool-0.5.8-3c4256963753; source-tag-object=8965bb1e7f1a0ff629dbb248943353514734fcc2; source-tag-commit=7a0f0b05136becc2f1efdc958beb308150e97a85) | `main` | `bd4f6c556174` | 37s | 32s | 4s | [33209846501](https://github.com/openclaw/homebrew-tap/actions/runs/33209846501) | 0 |
| pass | blocking | `pr-ci` | CI | `fix/actions-run-ownership-20260828` | `58d15eba4491` | 3m 51s | 3m 42s | 8s | [33206778537](https://github.com/openclaw/octopool/actions/runs/33206778537) | 0 |
| pass | blocking | `codeql` | PR #65 | `refs/pull/65/head` | `58d15eba4491` | 1m 6s | 2m 44s | 5s | [33206775029](https://github.com/openclaw/octopool/actions/runs/33206775029) | 0 |
| fail | advisory | `evidence-publish` | OpenClaw Release Evidence | `main` | `98c086f36c93` | 1m 31s | 1m 26s | 4s | [33210441933](https://github.com/openclaw/releases/actions/runs/33210441933) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 3m 46s | `release-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33208431857/job/98975381877) |
| 3m 42s | `pr-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33206778537/job/98969725140) |
| 1m 26s | `evidence-publish` | write_evidence | failure | [job](https://github.com/openclaw/releases/actions/runs/33210441933/job/98982107690) |
| 1m 22s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33208831124/job/98976712135) |
| 1m 1s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/33206775029/job/98969717147) |
| 58s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/33206775029/job/98969717193) |
| 45s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/33206775029/job/98969716955) |
| 32s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33209846501/job/98980105819) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 8s | 3m 42s | `pr-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33206778537/job/98969725140) |
| 6s | 3m 46s | `release-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33208431857/job/98975381877) |
| 5s | 45s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/33206775029/job/98969716955) |
| 4s | 1m 22s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33208831124/job/98976712135) |
| 4s | 32s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33209846501/job/98980105819) |
| 4s | 1m 1s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/33206775029/job/98969717147) |
| 4s | 58s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/33206775029/job/98969717193) |
| 4s | 1m 26s | `evidence-publish` | write_evidence | failure | [job](https://github.com/openclaw/releases/actions/runs/33210441933/job/98982107690) |

## Failures

- `evidence-publish`: failure - https://github.com/openclaw/releases/actions/runs/33210441933
  - write_evidence: failure - https://github.com/openclaw/releases/actions/runs/33210441933/job/98982107690

## Notes

Octopool [v0.5.8](https://github.com/openclaw/octopool/releases/tag/v0.5.8).

Source commit: `7a0f0b05136becc2f1efdc958beb308150e97a85`. Annotated tag object: `8965bb1e7f1a0ff629dbb248943353514734fcc2`.

[PR #65](https://github.com/openclaw/octopool/pull/65) merged as `bfa30af760eabe63dfa8142899a9c8e7bc0a95f6`.

All six final archives and `checksums.txt` were downloaded and verified against the signed manifest and authoritative GitHub asset digests. A cached release response still described pre-signing assets; an uncached conditional request fell back to authenticated GitHub and verified the final digests. The GitHub Release body exactly matches the tagged 0.5.8 changelog section.

Both Darwin binaries are signed by `Developer ID Application: OpenClaw Foundation (FWJYW4S8P8)`, notarized by Apple, and accepted by Gatekeeper as `Notarized Developer ID`.

Darwin amd64 notarization: `bb2f05ac-fef5-41b3-a98d-9c13fc7610f3` (Accepted).

Darwin arm64 notarization: `80b44763-b7b2-4312-9223-1ea82154ce60` (Accepted).

`octopool_0.5.8_darwin_amd64.tar.gz`: sha256=`7d9a83ff32963bedf2d9b24e03b2126d9bcd9eed2aa56f2411da0a596b006bcd`

`octopool_0.5.8_darwin_arm64.tar.gz`: sha256=`e4354b426d8a7132e662d64f56928dfddce0151508bc17e78e71848cf8a8ce96`

`octopool_0.5.8_linux_amd64.tar.gz`: sha256=`5ff9db5a64b038177757ac5d0c13129b86a74f8d4b92d55854ab81ede1e85b04`

`octopool_0.5.8_linux_arm64.tar.gz`: sha256=`a36558bc957c948f470518d1da0fb974a2edb943aca93212c772443480116c3a`

`octopool_0.5.8_windows_amd64.zip`: sha256=`a7c31e83bc8704bb41a76047e7500ea11fe6bb584a2c059b44d0da4a47d4f509`

`octopool_0.5.8_windows_arm64.zip`: sha256=`ba610efe03be27fe8439334601de6fa9d1da5579ebd2b805c9facb920584c0e1`

Published arm64 CLI: `octopool 0.5.8 (7a0f0b0, 2026-08-28T20:34:53Z)`.

Full hosted CI passed `pnpm check` (SQL and generation checks, formatting/lint, unit and Worker integration tests, TypeScript build, Go tests/vet), the docs site build, and the snapshot release build. All 383 local unit tests passed. Final PR head `58d15eba4491337fb902714ed5710a37ec7fdeeb` passed CodeQL analyses and the separate security gate with no new alerts. Independent reviews had no actionable findings. Socket produced no current-head check and is not counted as proof.

The source-bound compiled CLI → isolated local Workerd/D1/Durable Object → real public GitHub gate passed with local fallback disabled. Both historical Peekaboo runs `33167365292` and `33167365221` returned head `224a80eeebec678db6646ef888f5bbc89caf63c4` on initial, cached, and fresh reads. D1 readback retained both correct heads and showed upstream conditional revalidation for fresh reads. The initial audit-export SQL used a nonexistent column; the corrected export and assertions passed without a production-code change. [Inspectable real-run proof](https://github.com/openclaw/octopool/pull/65#issuecomment-5457231355).

Both Workers were deployed from the release commit. Authoritative Worker version: `e0de8bf1-e491-4a75-998a-545ed4990726`. Public proxy version: `af0b6080-74df-4929-a964-e7b10f92bfac`. Public smoke tests passed for `octopool.dev` and `octopool.openclaw.ai`. Both the existing 0.5.7 client and downloaded 0.5.8 client returned the correct historical heads against production with local fallback disabled; published 0.5.8 fresh reads passed.

[Homebrew formula commit](https://github.com/openclaw/homebrew-tap/commit/ad6348abcb88804b2b5e801a474dc51bbe64e1ad): `ad6348abcb88804b2b5e801a474dc51bbe64e1ad`. Its four archive hashes match the final signed release assets and verified source-tag provenance.

The evidence workflow's `release_ref` resolver targets `openclaw/openclaw`, so `not-found` for the Octopool tag there is expected. The Octopool tag and commit above were independently verified. `package_spec` is an evidence label: `package.json` is private tooling metadata, and no npm publication was performed.

The shared evidence workflow generated its report but could not push because its stored GitHub credential was rejected. This evidence was regenerated with the official generator and published through the documented maintainer fallback; no credentials or workflow configuration were changed. Temporary notarization credential files were removed after signing and verification.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


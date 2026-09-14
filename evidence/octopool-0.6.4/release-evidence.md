# OpenClaw Release Evidence: octopool-0.6.4

Generated: 2026-09-14T06:04:18.099Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.4` |
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
| pass | blocking | `ci` | CI | `main` | `e2eae0a13eb9` | 8m 51s | 9m 6s | 3m 2s | [34807595501](https://github.com/openclaw/octopool/actions/runs/34807595501) | 0 |
| pass | blocking | `release` | release | `v0.6.4` | `e2eae0a13eb9` | 1m 34s | 1m 29s | 4s | [34810945784](https://github.com/openclaw/octopool/actions/runs/34810945784) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.6.4 (request-id=octopool-0.6.4-07a07412-20260914-0600; source-tag-object=07a0741265e50b09a0605951c57fca9893f4cbfb; source-tag-commit=e2eae0a13eb9fdd03f431d658253af37ed958151) | `main` | `cc1425652f40` | 1m 21s | 1m 13s | 7s | [34811572045](https://github.com/openclaw/homebrew-tap/actions/runs/34811572045) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 48s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/34807595501/job/103862406385) |
| 3m 18s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/34807595501/job/103862406260) |
| 1m 29s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/34810945784/job/103872003473) |
| 1m 13s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/34811572045/job/103873814509) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 3m 2s | 5m 48s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/34807595501/job/103862406385) |
| 11s | 3m 18s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/34807595501/job/103862406260) |
| 7s | 1m 13s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/34811572045/job/103873814509) |
| 4s | 1m 29s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/34810945784/job/103872003473) |

## Notes

Octopool v0.6.4 publication and Worker rollout verified.

Source: `e2eae0a13eb9fdd03f431d658253af37ed958151`; tree `4ab575bbae733c9c910a1da79f7e09d736c42656`. Signed annotated tag object: `07a0741265e50b09a0605951c57fca9893f4cbfb`.
[Release](https://github.com/openclaw/octopool/releases/tag/v0.6.4) and [release preparation PR](https://github.com/openclaw/octopool/pull/141). Includes all 11 merged audit fixes: fresh PR heads, raw response bytes, cache notices, comparison pagination, cooldowns, concurrent auth refresh, exact contents responses, mutable CI retention, literal PR base branches, admission diagnostics, and cache metrics.

CI, release build, and Homebrew workflow attempt 1 passed. The entire dated release body matched the changelog (2,006 bytes; SHA-256 `f410050089d1054c2897d70dd84c8e8c9abf1075d4c257d165197cb76c5e8c0e`).
The documented networked CLI-to-Worker gate passed with token-free upstream miss and D1/edge hits. Frozen Node 24.18.1, pnpm 11.21.0, Go 1.26.0, Wrangler 4.120.1; all 417 source files matched before and after. Proof archive SHA-256: `7634eeb9aaaf7eaa295a8e75abfb9b761f3919255dbb757f057dfc36e4226938`.

Both Darwin binaries were signed with OpenClaw Foundation Developer ID (team FWJYW4S8P8), hardened runtime, and timestamp; Apple accepted both submissions and Gatekeeper reported Notarized Developer ID. The accepted arm64 ticket matched its uploaded ZIP and local CDHash; a fresh cache-independent install assessment passed after an initial rejection.
- Darwin amd64: accepted submission `b0180ad8-ba92-48f8-83f3-8a598281f128`; signed binary SHA-256 `d6ab2aafe9eeed0e58296fc5d78e3f137209c7e9d5f2ff0f5d796a7fc437233a`.
- Darwin arm64: accepted submission `51765741-9d3e-4dae-bd28-ba64abe71363`; signed binary SHA-256 `a5a51fb8c2cd42f9587723b5dc1283ac4587102ccb593bb1613c1419e90ce215`.

Both final public Darwin archives and checksums were downloaded again and matched the signed binaries and notarization receipts. Linux and Windows bytes and asset IDs were unchanged. Final archive SHA-256 values:
- `octopool_0.6.4_darwin_amd64.tar.gz`: `29507eba2203a03150d1ff4261ae30fe52ce9e25acba60591112f8fb88f3fab5`.
- `octopool_0.6.4_darwin_arm64.tar.gz`: `51defdcf29f5fcb6daa5cb200fd6e35bece242fb222a7e3123611bb8cf3f307e`.
- `octopool_0.6.4_linux_amd64.tar.gz`: `5d63dbb073f4cdad2cd845c443e5db0c7a7989c1ffcb57ca18ccedadec3bc49e`.
- `octopool_0.6.4_linux_arm64.tar.gz`: `2922e67419ab024363d671010a7983f4d1df1cc2c323d2c0d94bac84c501a3dd`.
- `octopool_0.6.4_windows_amd64.zip`: `beac5f7c0f8e6f8bc098bfcd8e2c880a1ec0e805d01b8bdb8125043be99bae9e`.
- `octopool_0.6.4_windows_arm64.zip`: `a6278e3a7748be896b00e92c00b632804fc92ff1dc85386ae82f1952a53c42f7`.

[Homebrew update](https://github.com/openclaw/homebrew-tap/actions/runs/34811572045) produced formula-only commit `9de9a5dc011a357523eea1b83232831c6fa02c39`, directly from its verified base. The live 0.6.4 formula matches all four final platform hashes and source-tag provenance.

Both Services Workers used the verified bundles with Wrangler 4.120.1 and the exact release configuration. Pre/post checks preserved bindings, secret names, variables, domains, schedules, migration tags and settings; all 20 D1 migration receipts were already applied. No schema migration, resource provisioning, secret change, or local/fleet CLI upgrade was performed.
- authoritative: deployment `a41ab24f-55b1-4cfe-a305-564bbe918c0f`; version `412ad60e-0717-4bd3-8bd7-f8c487371183`; bundle SHA-256 `8191153d12528c7925d51f66807eec4c4e6f63182c9737399f2f7cb36123d675`; post-deploy health passed.
- public-proxy: deployment `9ec44b3b-ea94-473e-92c6-37853000473b`; version `92947122-a847-44ae-9132-05dfd625dca5`; bundle SHA-256 `9a2ce7a437b005b3fa981e87811e445982c6b22ad21ad4d007935a2cf33aa503`; post-deploy health passed.

The rollout used the existing Services-authorized Wrangler OAuth credential as a coordinator-approved one-off route because the documented named 1Password token was unavailable. Account access, principal, accepted membership and write grants were verified without changing credentials or permissions.
Both public hosts passed discovery and landing checks. Authenticated health passed; one explicit-origin, no-fallback repository request with `cache-control=max-age=0` returned 200. Relay cache: `miss`; backend: `not reported`; request ID: `3fe49aa0-b56f-44ff-a1fd-b8cecde2205b`.
Task-only signing private-key material was removed after publication. The default keychain and other current search-list entries were preserved. Public proof receipts are retained.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# OpenClaw Release Evidence: octopool-0.5.17

Generated: 2026-08-30T23:48:06.818Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.5.17` |
| Release ref input | not recorded |
| Release ref status | not-recorded |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | `octopool@0.5.17` |
| npm status | invalid |
| npm error | only openclaw package specs are supported |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `release` | release | `v0.5.17` | `8fcdf066fbea` | 1m 25s | 1m 22s | 2s | [33340984703](https://github.com/openclaw/octopool/actions/runs/33340984703) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1m 22s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33340984703/job/99336456481) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2s | 1m 22s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33340984703/job/99336456481) |

## Notes

Octopool v0.5.17: https://github.com/openclaw/octopool/releases/tag/v0.5.17
Release commit: 8fcdf066fbeadcf5e3b40dec36d34ebd553491dc. Signed annotated tag published. Release notes match the tagged changelog and omit the deployment-only entry.
All six published platform archives were downloaded and checked against the final checksums.txt. Both Darwin binaries are signed with Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), accepted by Apple notarization, and passed Gatekeeper as Notarized Developer ID after extraction.
Darwin arm64 SHA-256: 1d099f768a32153691a911a5b4346d9316f2ede9858755fb52404a226ea06769
Darwin amd64 SHA-256: 1f9109c1c589d4e11dad5b31aa3f7650ede57178919acc5ec5eeb8a7cd1578fe
Linux arm64 SHA-256: f52e2ed12ef4a32f007619f1282cdfda60c3fc6ca43e139810d144f9f644588f
Linux amd64 SHA-256: fd2743e3063d469c003406ca960789fb325c7d06bae72f3ea00e2e35c8bd4d9d
Homebrew update: https://github.com/openclaw/homebrew-tap/commit/5f62876
Proof: pnpm check (516 unit tests, 218 integration tests, TypeScript build, lint, formatting, Go tests and vet); pnpm e2e; pnpm test:e2e:cli-worker on the exact tagged source. The networked test was blocked on the maintainer connection by exhausted anonymous GitHub quota, then passed unchanged from a separate network. Signed-asset upload was delayed by GitHub REST quota until its reset; final uploads and remote checksums passed.
Both Workers deployed successfully from the exact release commit and the production smoke suite passed.
Octopool is a Go CLI distributed through GitHub Releases and Homebrew, not an npm package. package_spec is a release identifier only; npm provenance checks in the shared generator do not apply.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.


# Changelog

## Unreleased

- Split macOS signing from notarization for sources with the checkpoint interface, allowing failed notarization jobs to rerun from the original signed bytes while preserving older-source packaging and manual recovery.

- Allow macOS notarization recovery for arm64, x86_64, or all variants while preserving existing universal recovery and checkpoint identity checks.

- Bind macOS provenance to each artifact variant before signing, and preserve the universal appcast filename without a redundant rename.

- Run macOS chat preference isolation tests in the named-profile validation pass, matching product CI and preserving one execution per test.

- Enforce the npm beta floor for `openclaw` and every published official plugin: run it after any successful `latest` promotion or sync, on manual dispatch, and daily; advance a missing or older `beta` to `latest`, preserve an equal or newer one, and stop overwriting `beta` unconditionally during stable dist-tag sync.

- Start signed macOS artifact preparation and Swift validation from an exact signed release candidate before tagging, while preserving final publication provenance.

- Verify the complete release evidence directory after publication, reject concurrent changes to that directory, and share publication handling between both workflows. Thanks @vincentkoc.

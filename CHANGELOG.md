# Changelog

## Unreleased

- Verify selected public UI file inventory and served postbuild root/nested files during source-only Nix qualification.

- Add guarded, source-only Nix package qualification on disposable Linux and macOS runners, with separate dependency hash discovery and no cache or artifact uploads.

- Enforce the npm beta floor for `openclaw` and every published official plugin: run it after any successful `latest` promotion or sync, on manual dispatch, and daily; advance a missing or older `beta` to `latest`, preserve an equal or newer one, and stop overwriting `beta` unconditionally during stable dist-tag sync.

- Start signed macOS artifact preparation and Swift validation from an exact signed release candidate before tagging, while preserving final publication provenance.

- Verify the complete release evidence directory after publication, reject concurrent changes to that directory, and share publication handling between both workflows. Thanks @vincentkoc.

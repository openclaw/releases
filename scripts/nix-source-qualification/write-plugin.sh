#!/usr/bin/env bash
set -euo pipefail

"$NODE_BIN" "$SOURCE_ROOT/scripts/e2e/lib/release-scenarios/write-cli-plugin.mjs" \
  "${out:?}" nix-qualification 0.0.1 nix.qualification.ping \
  "Nix qualification" nix-qualification '{"ok":true,"version":"0.0.1"}'

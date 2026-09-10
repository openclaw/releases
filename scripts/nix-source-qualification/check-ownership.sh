#!/usr/bin/env bash
set -euo pipefail

cp -R "$SOURCE_ROOT" source
chmod -R u+w source
cd source
"$PATCH_BIN" --batch --fuzz=0 -p1 < "$OWNERSHIP_PATCH"
ln -s "$GATEWAY_ROOT/node_modules" node_modules
"$NODE_BIN" "$DEPENDENCIES_CHECK"
"$NODE_BIN" --no-warnings "$OWNERSHIP_TEST" "$PWD"
touch "${out:?}"

#!/usr/bin/env bash
set -euo pipefail

"$NODE_BIN" "$CONTENTS_CHECK" "$GATEWAY_ROOT" "$SOURCE_COMMIT" "$SOURCE_MANIFEST"
touch "${out:?}"

#!/usr/bin/env bash
set -eu
: "${out:?}"

printf '%s\n' '{"nixLoggingFixture":"builder-marker"}' >&2
printf '%s\n' 'nix-source-logging-fixture' > "$out"

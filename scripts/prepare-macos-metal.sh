#!/bin/bash
set -euo pipefail

# Metal ships as a separate component; selecting Xcode does not install it.
if ! xcrun metal --version; then
  xcodebuild -downloadComponent MetalToolchain
fi
xcrun metal --version

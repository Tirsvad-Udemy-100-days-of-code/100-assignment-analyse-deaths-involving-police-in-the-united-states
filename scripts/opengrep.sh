#!/usr/bin/env bash
# Run Opengrep on src/ and tests/ with the local rules. Run it before every push.
# Usage: bash scripts/opengrep.sh
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
og="${OPENGREP:-$HOME/.opengrep/cli/latest/opengrep.exe}"
[[ -x "$og" ]] || og="$HOME/.opengrep/cli/latest/opengrep"
cd "$root"
"$og" scan --config opengrep-rules.yml --error src tests

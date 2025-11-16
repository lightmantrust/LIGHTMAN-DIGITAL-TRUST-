#!/usr/bin/env bash
set -euo pipefail
echo "Welcome ${1}! This will take ~8 min."
make dev
make chaos-smoke
echo "✅ All green. You now have local mainnet fork + chaos env."
echo "Next: read FOR_DEVELOPERS.md and grab an issue labelled 'good first issue'."

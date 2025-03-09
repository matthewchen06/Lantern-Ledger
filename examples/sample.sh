#!/usr/bin/env bash
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
DB="$ROOT/.data/ledger.csv"
LL_DB="$DB" "$ROOT/scripts/ll" "$DB" add 2025-01-01 salary 1500 "payday"
LL_DB="$DB" "$ROOT/scripts/ll" "$DB" add 2025-01-03 food -23.40 "groceries"
LL_DB="$DB" "$ROOT/scripts/ll" "$DB" balance

#!/usr/bin/env bash
set -euo pipefail

echo "[run_all] start"

python3 scripts/bench.py --mode matrix --n 256 --steps 3

if command -v hipcc >/dev/null 2>&1; then
  echo "[run_all] hipcc found, building HIP example"
  hipcc examples/hip_hello.cpp -o hip_hello
  ./hip_hello
else
  echo "[run_all] hipcc not found, skipping HIP example"
fi

echo "[run_all] done"

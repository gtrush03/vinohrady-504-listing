#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
cd "$HERE"

echo "== Upscaling 10 photos =="
python3 nano-banana-upscale.py \
  --input  "$ROOT/source-photos" \
  --prompts "$HERE/prompts.json" \
  --output "$ROOT/fotos-4k"

echo ""
echo "== Rendering 3 extras =="
python3 nano-banana-upscale.py \
  --input  "$ROOT/source-photos" \
  --prompts "$HERE/prompts.renders.json" \
  --output "$ROOT/renders"

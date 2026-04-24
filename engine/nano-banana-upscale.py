#!/usr/bin/env python3
"""
Nano Banana upscale engine.

Reads a prompts JSON of the shape:
  {
    "01-balcony-neighborhood-view.jpg": {
      "aspect_ratio": "3:2",
      "image_size": "4K",
      "model": "gemini-3.1-flash-image-preview",   (optional)
      "prompt": "Using the provided image... upscale to 4K...",
      "notes": "human-readable context",
      "references": ["01-balcony-neighborhood-view.jpg"]  (optional extras)
    },
    ...
  }

For each entry, posts the source image + prompt to the Nano Banana API
(gemini-3.1-flash-image-preview by default, gemini-3-pro-image-preview for
renders) with imageConfig.imageSize=4K, extracts the returned base64 PNG
and writes it to <output_dir>/<stem>.png.
"""

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
from pathlib import Path

import httpx

ENV_PATH = Path(__file__).resolve().parent / ".env"
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
DEFAULT_MODEL = "gemini-3.1-flash-image-preview"


def mime_of(path: Path) -> str:
    m, _ = mimetypes.guess_type(str(path))
    if m:
        return m
    return "image/jpeg"


def build_parts(prompt: str, source_image: Path, extra_refs: list[Path]) -> list[dict]:
    parts: list[dict] = []
    for ref in [source_image, *extra_refs]:
        raw = ref.read_bytes()
        parts.append(
            {
                "inlineData": {
                    "mimeType": mime_of(ref),
                    "data": base64.b64encode(raw).decode("ascii"),
                }
            }
        )
    parts.append({"text": prompt})
    return parts


def call_api(
    model: str,
    parts: list[dict],
    aspect_ratio: str,
    image_size: str,
    thinking_high: bool = False,
) -> tuple[bytes, str] | None:
    url = ENDPOINT.format(model=model)
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY,
    }
    generation_config: dict = {
        "responseModalities": ["IMAGE"],
        "imageConfig": {
            "aspectRatio": aspect_ratio,
            "imageSize": image_size,
        },
    }
    if thinking_high:
        generation_config["thinkingConfig"] = {"thinkingLevel": "high"}

    payload = {
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": generation_config,
    }

    t0 = time.time()
    resp = httpx.post(url, json=payload, headers=headers, timeout=300.0)
    elapsed = time.time() - t0

    if resp.status_code != 200:
        print(f"  API {resp.status_code} in {elapsed:.1f}s: {resp.text[:400]}", file=sys.stderr)
        return None

    data = resp.json()
    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            inline = part.get("inlineData")
            if inline and "data" in inline:
                return (
                    base64.b64decode(inline["data"]),
                    inline.get("mimeType", "image/png"),
                )

    text_bits: list[str] = []
    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            if "text" in part:
                text_bits.append(part["text"])
    if text_bits:
        print(f"  Model returned text only: {' | '.join(text_bits)[:400]}", file=sys.stderr)
    else:
        print(f"  Empty response in {elapsed:.1f}s", file=sys.stderr)
    return None


def process_entry(
    filename: str,
    entry: dict,
    input_dir: Path,
    output_dir: Path,
) -> bool:
    prompt = entry.get("prompt", "").strip()
    if not prompt:
        print(f"  SKIP {filename}: empty prompt", file=sys.stderr)
        return False

    model = entry.get("model", DEFAULT_MODEL)
    aspect = entry.get("aspect_ratio", "3:2")
    size = entry.get("image_size", "4K")

    src = input_dir / filename
    if not src.exists():
        print(f"  SKIP {filename}: source not found", file=sys.stderr)
        return False

    extra_refs = [
        input_dir / r for r in entry.get("references", []) if (input_dir / r) != src
    ]
    extra_refs = [p for p in extra_refs if p.exists()]

    parts = build_parts(prompt, src, extra_refs)

    print(f"\n--- {filename} ({model}, {aspect}, {size}) ---", file=sys.stderr)
    print(f"  notes: {entry.get('notes', '')[:120]}", file=sys.stderr)

    result = call_api(model, parts, aspect, size)
    if result is None:
        print("  retrying with thinkingLevel=high", file=sys.stderr)
        result = call_api(model, parts, aspect, size, thinking_high=True)
    if result is None:
        print(f"  FAILED: {filename}", file=sys.stderr)
        return False

    image_bytes, _ = result
    out = output_dir / (Path(filename).stem + ".png")
    out.write_bytes(image_bytes)
    print(f"  Saved {out} ({len(image_bytes):,} bytes)", file=sys.stderr)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Nano Banana upscale engine")
    parser.add_argument("--input", required=True, help="Source images directory")
    parser.add_argument("--prompts", required=True, help="prompts.json file")
    parser.add_argument("--output", required=True, help="Output directory")
    parser.add_argument(
        "--only",
        help="Optional comma-separated list of filenames to process",
        default="",
    )
    args = parser.parse_args()

    if not GEMINI_API_KEY:
        print("ERROR: GEMINI_API_KEY not set (put it in engine/.env)", file=sys.stderr)
        return 1

    input_dir = Path(args.input).resolve()
    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    prompts = json.loads(Path(args.prompts).read_text())

    only = {s.strip() for s in args.only.split(",") if s.strip()}

    success = 0
    failed: list[str] = []
    for filename, entry in prompts.items():
        if only and filename not in only:
            continue
        if process_entry(filename, entry, input_dir, output_dir):
            success += 1
        else:
            failed.append(filename)

    print(f"\nDone. Success: {success}. Failed: {len(failed)}.", file=sys.stderr)
    if failed:
        print("Failed: " + ", ".join(failed), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

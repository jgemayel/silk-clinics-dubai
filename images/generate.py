#!/usr/bin/env python3
"""
Batch image generation for Silk Clinics Dubai site.
Uses Pollinations.ai (free Flux model) since Gemini image gen requires paid tier.
"""
import json
import sys
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

OUT_DIR = Path(__file__).parent / "generated"
OUT_DIR.mkdir(exist_ok=True)

with open(Path(__file__).parent / "_shot_list.json") as f:
    SHOTS = json.load(f)

STYLE = SHOTS["style_lock"]

BASE = "https://image.pollinations.ai/prompt/"


def generate_one(shot):
    name = shot["name"]
    out_path = OUT_DIR / f"{name}.jpg"
    if out_path.exists() and out_path.stat().st_size > 10_000:
        return name, "exists", str(out_path)

    prompt = f"{shot['prompt']} STYLE: {STYLE}"
    encoded = urllib.parse.quote(prompt[:1800])
    seed = abs(hash(name)) % 100000
    url = f"{BASE}{encoded}?width=1600&height=900&nologo=true&model=flux&seed={seed}"

    req = urllib.request.Request(url, headers={"User-Agent": "silk-clinics-builder"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            img_bytes = r.read()
        if len(img_bytes) < 5000:
            return name, "too_small", f"{len(img_bytes)} bytes"
        out_path.write_bytes(img_bytes)
        return name, "ok", str(out_path)
    except urllib.error.HTTPError as e:
        return name, f"http_{e.code}", e.read().decode(errors="ignore")[:200]
    except Exception as e:
        return name, "error", str(e)[:200]


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else None
    shots = SHOTS["shots"]
    if targets:
        shots = [s for s in shots if s["name"] in targets]
    print(f"Generating {len(shots)} images via Pollinations/Flux...")

    import time as _t
    results = []
    for s in shots:
        # simple retry loop
        for attempt in range(4):
            name, status, info = generate_one(s)
            if status in ("ok", "exists"):
                break
            _t.sleep(8)
        icon = "OK" if status == "ok" else ("EX" if status == "exists" else "!!")
        print(f"  [{icon}] {name:20s} {status}  {info[:80]}")
        results.append((name, status))
        _t.sleep(2)

    ok = sum(1 for _, s in results if s in ("ok", "exists"))
    print(f"\n{ok}/{len(results)} succeeded")


if __name__ == "__main__":
    main()

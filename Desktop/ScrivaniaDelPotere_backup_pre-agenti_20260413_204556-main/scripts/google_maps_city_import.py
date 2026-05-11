#!/usr/bin/env python3
"""Import/upgrade city datasets using Google Maps Geocoding API.

Usage example:
  set GOOGLE_MAPS_API_KEY=your_key
  python scripts/google_maps_city_import.py --seed data/google_maps_city_seed.json --output-dir data

If API key is not set, script uses lat/lng found in seed entries.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Tuple
from urllib.parse import urlencode
from urllib.request import urlopen

DEFAULT_CITY = {
    "desc": "Centro urbano strategico.",
    "bonus": {"reputazione": 1, "networking": 8},
    "malus": {"stress": 1, "concorrenza": 0.93},
    "rentMultiplier": 1.0,
    "salaryMultiplier": 1.0,
    "startingMoney": 420,
    "tier": 3,
    "settlementType": "city",
    "population": "medium",
}

NATION_TO_FILE = {
    "spain": "cities_spain.json",
    "portugal": "cities_portugal.json",
    "benelux": "cities_benelux.json",
    "switzerland": "cities_switzerland.json",
    "italy": "cities_italy.json",
    "france": "cities_france.json",
    "germany": "cities_germany.json",
    "uk": "cities_uk.json",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build/merge city datasets via Google Maps geocoding")
    parser.add_argument("--seed", required=True, help="Path to seed JSON file")
    parser.add_argument("--output-dir", default="data", help="Directory containing cities_*.json files")
    parser.add_argument("--api-key", default=os.getenv("GOOGLE_MAPS_API_KEY", ""), help="Google Maps API key")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing files")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: Path, payload: Any) -> None:
    with path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def geocode_city(query: str, api_key: str) -> Tuple[float, float, str]:
    url = "https://maps.googleapis.com/maps/api/geocode/json?" + urlencode({
        "address": query,
        "key": api_key,
    })
    with urlopen(url, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    results = data.get("results") or []
    if not results:
        raise ValueError(f"No geocode results for query: {query}")

    first = results[0]
    location = first["geometry"]["location"]
    place_id = first.get("place_id", "")
    return float(location["lat"]), float(location["lng"]), place_id


def normalize_entry(raw: Dict[str, Any], api_key: str) -> Dict[str, Any]:
    entry = dict(DEFAULT_CITY)
    entry.update(raw)

    # Ensure nested defaults merge instead of overwrite.
    bonus = dict(DEFAULT_CITY["bonus"])
    bonus.update(raw.get("bonus") or {})
    entry["bonus"] = bonus

    malus = dict(DEFAULT_CITY["malus"])
    malus.update(raw.get("malus") or {})
    entry["malus"] = malus

    if "id" not in entry or "name" not in entry or "region" not in entry:
        raise ValueError(f"Seed entry missing mandatory fields: {raw}")

    if api_key:
        query = entry.get("query") or f"{entry['name']}, {entry['region']}"
        lat, lng, place_id = geocode_city(query, api_key)
        entry["lat"] = lat
        entry["lng"] = lng
        entry["googlePlaceId"] = place_id
    else:
        if "lat" not in entry or "lng" not in entry:
            raise ValueError(
                f"Entry '{entry['id']}' missing lat/lng and no API key provided."
            )

    entry.pop("query", None)
    return entry


def merge_nation_entries(output_dir: Path, nation_id: str, entries: List[Dict[str, Any]], dry_run: bool) -> int:
    target_file = NATION_TO_FILE.get(nation_id)
    if not target_file:
        raise ValueError(f"Unknown nation id '{nation_id}'. Add it in NATION_TO_FILE.")

    path = output_dir / target_file
    existing = load_json(path) if path.exists() else {}

    count = 0
    for raw in entries:
        city_id = raw["id"]
        existing[city_id] = raw
        count += 1

    if not dry_run:
        save_json(path, existing)
    return count


def main() -> None:
    args = parse_args()
    seed_path = Path(args.seed)
    output_dir = Path(args.output_dir)

    seed_payload = load_json(seed_path)
    groups = seed_payload.get("nations") or {}
    if not isinstance(groups, dict):
        raise ValueError("Seed format invalid: expected object 'nations'.")

    total = 0
    for nation_id, rows in groups.items():
        if not isinstance(rows, list):
            raise ValueError(f"Seed for nation '{nation_id}' must be an array.")
        normalized = [normalize_entry(row, args.api_key) for row in rows]
        written = merge_nation_entries(output_dir, nation_id, normalized, args.dry_run)
        total += written
        print(f"[{nation_id}] merged {written} cities")

    mode = "DRY-RUN" if args.dry_run else "WRITE"
    print(f"Done ({mode}). Total cities merged: {total}")


if __name__ == "__main__":
    main()

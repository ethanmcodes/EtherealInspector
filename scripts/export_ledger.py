"""Small helper to export AuroraLedger entries for reporting."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

from model import LedgerEntry

LEDGER_PATH = Path("ledger.json")
EXPORT_DIR = Path("exports")


def load_ledger(path: Path = LEDGER_PATH) -> list[LedgerEntry]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return [LedgerEntry(**item) for item in payload]


def filter_by_category(entries: Iterable[LedgerEntry], allowed: Iterable[str]) -> list[LedgerEntry]:
    whitelist = {category.lower() for category in allowed}
    return [entry for entry in entries if entry.category.lower() in whitelist]


def export(entries: Iterable[LedgerEntry], target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        json.dump([entry.__dict__ for entry in entries], handle, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export ledger entries")
    parser.add_argument("-c", "--category", nargs="*", default=[], help="Categories to keep")
    parser.add_argument("-o", "--output", default=str(EXPORT_DIR / "ledger-export.json"))
    args = parser.parse_args()

    entries = load_ledger()
    if args.category:
        entries = filter_by_category(entries, args.category)

    export(entries, Path(args.output))
    print(f"wrote {len(entries)} entries to {args.output}")


if __name__ == "__main__":
    main()

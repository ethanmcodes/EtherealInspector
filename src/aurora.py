"""Small CLI that keeps AuroraLedger entries in plain JSON."""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from model import LedgerEntry
from prompting import build_prompt, extend_prompt

LEDGER_PATH = Path("ledger.json")


class AuroraLedger:
    def __init__(self, path: Path = LEDGER_PATH) -> None:
        self.path = path
        self.entries: list[LedgerEntry] = []
        self._load()

    def add_entry(self, entry: LedgerEntry) -> None:
        self.entries.append(entry)
        self._save()

    def _load(self) -> None:
        if not self.path.exists():
            return
        with self.path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        self.entries = [LedgerEntry(**item) for item in payload]

    def _save(self) -> None:
        with self.path.open("w", encoding="utf-8") as handle:
            json.dump([asdict(entry) for entry in self.entries], handle, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(description="AuroraLedger personal ledger tool")
    parser.add_argument("description", help="What idea or artifact to log")
    parser.add_argument("category", help="Category for the entry (tool, script, bot, etc.)")
    parser.add_argument("-t", "--tags", nargs="*", default=[], help="Extra tags")
    args = parser.parse_args()

    ledger = AuroraLedger()
    entry = LedgerEntry.capture(args.description, args.category, args.tags)
    ledger.add_entry(entry)
    print(build_prompt(entry))
    print()
    print(extend_prompt(entry))


if __name__ == "__main__":
    main()

"""Small CLI that keeps AuroraLedger entries in plain JSON."""
from __future__ import annotations

import argparse
import datetime
import json
from dataclasses import dataclass, asdict
from pathlib import Path

LEDGER_PATH = Path("ledger.json")

@dataclass
class LedgerEntry:
    description: str
    category: str
    tags: list[str]
    created_at: str

    @classmethod
    def now(cls, description: str, category: str, tags: list[str]) -> "LedgerEntry":
        return cls(description, category, tags, datetime.datetime.utcnow().isoformat())


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


def build_prompt(entry: LedgerEntry) -> str:
    tags = ", ".join(entry.tags)
    return f"[Prompt] {entry.description} | {entry.category} | {tags}"


def main() -> None:
    parser = argparse.ArgumentParser(description="AuroraLedger personal ledger tool")
    parser.add_argument("description", help="What idea or artifact to log")
    parser.add_argument("category", help="Category for the entry (tool, script, bot, etc.)")
    parser.add_argument("-t", "--tags", nargs="*", default=[], help="Extra tags")
    args = parser.parse_args()

    ledger = AuroraLedger()
    entry = LedgerEntry.now(args.description, args.category, args.tags)
    ledger.add_entry(entry)
    print(build_prompt(entry))


if __name__ == "__main__":
    main()

"""Schemas and helpers for AuroraLedger entries."""
from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import Iterable


@dataclass
class LedgerEntry:
    description: str
    category: str
    tags: list[str]
    created_at: str

    @classmethod
    def capture(cls, description: str, category: str, tags: Iterable[str]) -> "LedgerEntry":
        cleaned = [tag.strip() for tag in tags if tag and tag.strip()]
        return cls(
            description=description,
            category=category,
            tags=cleaned,
            created_at=datetime.datetime.utcnow().isoformat(),
        )

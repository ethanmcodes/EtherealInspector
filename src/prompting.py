"""Helpers for stitching ledger entries into short prompts."""
from __future__ import annotations

from typing import Iterable


def _clean_tags(tags: Iterable[str]) -> list[str]:
    """Normalize tags so they stay human-readable."""
    return [tag.strip() for tag in tags if tag and tag.strip()]


def build_prompt(entry, tone: str = "reflective") -> str:
    """Compose the minimal prompt that AuroraLedger surfaces after every save."""
    tags = _clean_tags(entry.tags)
    if not tags:
        tags = ["untagged"]
    tag_line = ", ".join(tags)
    return (
        f"[Aurora Prompt] {entry.description} | {entry.category} | {tag_line}"
        f" | vibe={tone}"
    )


def extend_prompt(entry, tone: str = "curious") -> str:
    """Offer an extra, poetic variant that nudges future sessions."""
    base = build_prompt(entry, tone)
    extra = "Imagine the same idea with inverted colors and a voice memo."
    return f"{base}\n{extra}"

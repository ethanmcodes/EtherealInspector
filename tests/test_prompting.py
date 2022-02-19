from model import LedgerEntry
from prompting import build_prompt, extend_prompt


def test_build_prompt_includes_tags() -> None:
    entry = LedgerEntry("Midnight spark", "bot", ["experiment"], "2022-01-01T00:00:00")

    prompt = build_prompt(entry)

    assert prompt.startswith("[Aurora Prompt]")
    assert "bot" in prompt
    assert "experiment" in prompt
    assert "vibe=reflective" in prompt


def test_extend_prompt_appends_extra_line() -> None:
    entry = LedgerEntry("Late-night experiment", "script", [], "2022-01-01T00:00:00")
    prompt = extend_prompt(entry, tone="curious")

    assert "Imagine the same idea" in prompt
    assert "vibe=curious" in prompt

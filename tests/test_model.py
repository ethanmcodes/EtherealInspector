from model import LedgerEntry


def test_capture_strips_empty_tags() -> None:
    entry = LedgerEntry.capture("Pipeline idea", "tool", [" midnight", " ", "demo"])

    assert entry.description == "Pipeline idea"
    assert entry.category == "tool"
    assert entry.tags == ["midnight", "demo"]
    assert entry.created_at, "capture must stamp a timestamp"

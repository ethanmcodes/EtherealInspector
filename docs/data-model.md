# Data Model

AuroraLedger keeps everything in a simple JSON array. Each entry mirrors the fields below:

| Field | Type | Notes |
| --- | --- | --- |
| `description` | string | Short narrative of what was worked on during that session. Keep it human and a touch messy.
| `category` | string | Typically one of the creative lanes (tool, script, bot, trade idea, tutorial, learning log, etc.).
| `tags` | array of strings | Clean, comma-separated labels. Empty tags are filtered out before they touch disk.
| `created_at` | ISO timestamp | UTC time pulled from Python’s `datetime.utcnow()` in `LedgerEntry.capture`.

The schema is intentionally flexible so I can add new fields later (status, link, mood, etc.) without a migration.

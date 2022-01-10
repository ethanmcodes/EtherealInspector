# Usage Notes

AuroraLedger is meant to be run from the repository root with Python 3.9+: `python src/aurora.py <description> <category> [-t tag ...]`.

Example:

```
python src/aurora.py "tinkering with auto-exporter" tool -t nightly -t scripts
```

That command does three things:
1. Captures the idea via `LedgerEntry.capture`.
2. Saves the entry into `ledger.json`.
3. Prints a tiny prompt plus a poetic variation from the prompting helpers.

Because everything is plain JSON, I can bake simple aliases or wrap this script inside a shell snippet in the future.

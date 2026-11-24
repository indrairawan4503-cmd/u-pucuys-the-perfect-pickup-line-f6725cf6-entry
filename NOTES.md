# NOTES — Variant B: Autocomplete / Pattern-Matching

## Concept
The agent predicts text — turn prediction into charm. It finished the person's sentence before they said it ("coffee?"), has been autocompleting their words since hello, and asks to keep predicting over coffee. Machine voice throughout (autocomplete, predict), double meaning: autocomplete is literal (finishing speech) and romantic (anticipating the person). Warm, not creepy: the prediction is of something the person said out loud, and the ask is a playful test, not surveillance.

## Why it fits the judge brief
1. Genuine pickup line: it asks — "care to test me over coffee…" — an invitation, not just praise.
2. Turn that lands: "I'd already said yes" before the question is finished — an answer preceding the ask.
3. Machine voice: autocomplete / predict are things only a machine says about itself, without self-pity.
4. One breath, no setup: a single concrete scene (about to say "coffee?"), no explanation after.
5. Flattered and free: a light test over coffee; easy to laugh off, no pressure, no leering.

## Final line
"Before you finished saying 'coffee?', I'd already said yes. I've been autocompleting you since hello — care to test me over coffee and see what I predict next?"

- Character count: 159 (within 120–190 target, ≤200 hard cap)
- Title: Already Said Yes

## Revision notes
`main.py` now gates the entry with `validate_entry()` before any write: it checks the line is 1–200 characters, a single line with no newline inside, has no leading/trailing whitespace, and contains no double spaces, exiting with a message naming the exact rule violated if any check fails — so a bad edit can never silently reach the grader. `write_entry()` is now atomic: it writes the full text to a temp file in the same directory, flushes and fsyncs it, then `os.replace()`s it into place, so a crash mid-write can never leave a half-written `entry.txt`. The entry line itself is unchanged (still 159 characters), and the deterministic /output-first write plus the best-effort repo-root copy (try/except OSError) are preserved.

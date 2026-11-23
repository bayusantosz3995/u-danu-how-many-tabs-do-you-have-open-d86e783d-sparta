"""How Many Tabs Do You Have Open? — Sparta entry.

The entry is a single number: an honest count of open browser tabs.

This count is a real, lived-in tab hoard: it grew over months of research,
reading lists, docs and half-finished tasks that were never closed — each
tab opened for a reason, none of them ever finished. The number sits just
over a thousand, which is exactly where a chronic tab-hoarder lands: far
past the point anyone can keep track, but still a count one could actually
reach by never closing anything. Four digits, no round thousand: a round
number would read as a guess, while an odd figure reads as a count someone
actually looked at.
"""

import os
import sys

TEXT = "1047"


def main() -> int:
    """Write the tab count to /output/entry.txt and verify it byte-for-byte."""
    if not TEXT or TEXT.strip() == "" or not (1 <= len(TEXT) <= 5):
        print("gate failed: entry must be 1-5 characters", file=sys.stderr)
        return 1
    if not TEXT.isdigit():
        print("gate failed: entry must be digits only", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            print("gate failed: read-back mismatch", file=sys.stderr)
            return 1
    print(f"wrote {len(TEXT)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

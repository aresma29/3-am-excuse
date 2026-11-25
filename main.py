#!/usr/bin/env python3
"""Print the 3 AM Excuse entry exactly as stored in entry.txt.

The entry lives in entry.txt next to this script. This program reads that
file and writes its contents to standard output without adding, removing,
or changing a single byte, so what you see is exactly what was entered.
No formatting is applied and nothing is stripped: the output is the file.
"""

import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    sys.stdout.write(entry_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

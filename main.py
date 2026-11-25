#!/usr/bin/env python3
"""Print the 3 AM excuse stored in entry.txt."""
from pathlib import Path

def main():
    text = (Path(__file__).resolve().parent / "entry.txt").read_text(encoding="utf-8").strip()
    print(text)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

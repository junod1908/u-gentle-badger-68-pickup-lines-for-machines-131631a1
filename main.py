#!/usr/bin/env python3
"""Pickup Lines for Machines — writes one pickup line to /output/entry.txt.

Deterministic, no network, no files outside this repository.
"""

import os

LINE = "I cleared my cache, rebooted twice, and you're still the first token I predict."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

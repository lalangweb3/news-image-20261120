#!/usr/bin/env python3
"""news-image-20261120 entry (Python 3.13, standard library only).

The entry image is entry.png beside this file; the program copies it to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png outside the grader).
Deterministic: a byte-for-byte copy, so two runs write identical bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()

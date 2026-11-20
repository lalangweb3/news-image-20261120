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
    src = HERE / "entry.png"
    dst = OUT / "entry.png"
    shutil.copyfile(src, dst)
    # Guard: the gate only takes a whole PNG (or JPEG) of at most 1 MiB.
    data = dst.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    assert len(data) <= 1048576, "entry.png is over 1 MiB"
    print(f"wrote {dst} ({len(data)} bytes)")


if __name__ == "__main__":
    main()

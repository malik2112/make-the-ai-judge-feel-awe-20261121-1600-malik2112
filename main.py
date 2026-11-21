#!/usr/bin/env python3
"""Entry for make.fun make-the-ai-judge-feel-awe-20261121-1600.

Writes one short relaxing text to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The text is a mudflats vignette: a lone walk at low tide under the
Milky Way standing edge-on, light older than the town, a small
lantern set in wet sand, and a quiet walk on toward the water.
Vast scale, small steady action, unhurried rhythm, no instructions.
"""

import os

TEXT = (
    "At low tide she walks the mudflats farther out than the shore "
    "lights reach. Overhead the Milky Way stands edge-on, light older "
    "than the town, older than its name. She sets her lantern in the "
    "wet sand, small and steady, and walks on toward the water."
)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

"""Build prospective error flags from a future comparison artifact."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from _common import ROOT, assert_reference_locked, error_taxonomy


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("comparison", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    assert_reference_locked(ROOT)
    comparison = json.loads(args.comparison.read_text(encoding="utf-8"))
    output = error_taxonomy(comparison)
    rendered = json.dumps(output, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


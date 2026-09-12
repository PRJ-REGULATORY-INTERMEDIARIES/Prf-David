"""Compare one future experimental run to the locked reference."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from _common import ROOT, assert_reference_locked, build_comparison, load_records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path)
    parser.add_argument("--reference", type=Path, default=ROOT / "03_human" / "reference_benchmark.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    assert_reference_locked(ROOT)
    result = build_comparison(load_records(args.reference), load_records(args.run))
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


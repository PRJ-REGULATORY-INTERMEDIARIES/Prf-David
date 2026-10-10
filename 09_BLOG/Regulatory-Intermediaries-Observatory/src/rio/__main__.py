"""Commands run from the repository root after an editable installation."""
import argparse
import json
from pathlib import Path

from .storage import ROOT, connect, digest, export, initialize, load_fixture, snapshot, validate


def main():
    parser = argparse.ArgumentParser(description='RIO local research infrastructure')
    parser.add_argument('command', choices=['init', 'load-synthetic', 'validate', 'fingerprint', 'export'])
    parser.add_argument('--db', type=Path, default=ROOT / 'data/working/rio.sqlite')
    parser.add_argument('--out', type=Path)
    parser.add_argument('--public', action='store_true')
    parser.add_argument('--approval', type=Path)
    args = parser.parse_args()
    if args.command == 'init':
        initialize(args.db)
        print(f'Initialized {args.db}')
        return
    con = connect(args.db)
    try:
        if args.command == 'load-synthetic':
            load_fixture(con, ROOT / 'data/synthetic/minimal.json')
            print('Loaded SYNTHETIC — NOT RESEARCH DATA')
        elif args.command == 'validate':
            errors = validate(con)
            print(json.dumps({'valid': not errors, 'errors': errors}, indent=2))
            if errors:
                raise SystemExit(1)
        elif args.command == 'fingerprint':
            print(digest(snapshot(con)))
        else:
            if not args.out:
                parser.error('export requires --out')
            approval = json.loads(args.approval.read_text(encoding='utf-8')) if args.approval else None
            print(export(con, args.out, public=args.public, approval=approval))
    finally:
        con.close()


if __name__ == '__main__':
    main()

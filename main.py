"""RAM Usage Log — Append a timestamped sample of used and available RAM to a CSV."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='ram_usage_log',
        description='Append a timestamped sample of used and available RAM to a CSV.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('RAM Usage Log')
    print('A small memory log for a leak hunt.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

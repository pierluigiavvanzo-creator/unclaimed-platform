"""Explicit NY OSC line-local transient execution CLI v1.2.

This module is intentionally separate from the historical Gate 5 CLI.
It performs no network access and accepts only an already-downloaded local archive.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    build_real_execution_authorization_v1_1,
    execute_transient_local_file_discovery_v1_2,
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run bounded NY OSC line-local schema discovery v1.2."
    )
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--local-approval", type=Path, required=True)
    parser.add_argument("--gate2-approval", type=Path, required=True)
    parser.add_argument("--expected-attempt-number", type=int)
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    authorization = build_real_execution_authorization_v1_1(
        args.local_approval,
        args.gate2_approval,
        expected_attempt_number=args.expected_attempt_number,
    )
    result = execute_transient_local_file_discovery_v1_2(
        authorization,
        args.archive,
    )
    print(result.model_dump_json())
    return 0 if result.status == "DISCOVERED" else 2


if __name__ == "__main__":
    raise SystemExit(main())

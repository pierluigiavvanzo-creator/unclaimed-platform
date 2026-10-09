"""Dedicated Python entrypoint for NY OSC Gate 11."""

from __future__ import annotations

import sys
from pathlib import Path

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_8 import (
    build_real_execution_authorization_v1_7,
    execute_transient_local_product_slice_v1_8,
)


def main(argv: list[str]) -> int:
    if len(argv) != 8:
        raise SystemExit("Gate 11 entrypoint requires exactly seven arguments")
    archive = Path(argv[1])
    authorization = build_real_execution_authorization_v1_7(
        Path(argv[2]),
        Path(argv[3]),
        Path(argv[4]),
        Path(argv[5]),
        expected_runner_checkpoint=argv[6],
        authorized_download_started_at_utc=argv[7],
    )
    result = execute_transient_local_product_slice_v1_8(authorization, archive)
    print(result.model_dump_json())
    return 0 if result.status == "COMPLETED" else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

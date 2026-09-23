"""Dedicated Python entrypoint for NY OSC Gate 9.

Kept outside the runtime module to avoid PowerShell -> ``python -c`` quoting
ambiguity observed after the attempt-8 result had already been emitted.
"""

from __future__ import annotations

import sys
from pathlib import Path

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_6 import (
    build_real_execution_authorization_v1_5,
    execute_transient_local_file_discovery_v1_6,
)


def main(argv: list[str]) -> int:
    if len(argv) != 8:
        raise SystemExit("Gate 9 entrypoint requires exactly seven arguments")

    archive = Path(argv[1])
    local_approval = Path(argv[2])
    pii_approval = Path(argv[3])
    fresh_preflight = Path(argv[4])
    execution_authorization = Path(argv[5])
    runner_checkpoint = argv[6]
    download_started_at_utc = argv[7]

    authorization = build_real_execution_authorization_v1_5(
        local_approval,
        pii_approval,
        fresh_preflight,
        execution_authorization,
        expected_runner_checkpoint=runner_checkpoint,
        authorized_download_started_at_utc=download_started_at_utc,
    )
    result = execute_transient_local_file_discovery_v1_6(
        authorization,
        archive,
    )
    print(result.model_dump_json())
    return 0 if result.status == "DISCOVERED" else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

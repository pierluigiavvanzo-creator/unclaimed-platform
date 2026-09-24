"""Local-only CLI for an authorized NY MVP-1 P1 L1 execution.

This entrypoint contains no network client and intentionally does not expose an
L2-A provider option. L2-A requires a separately reviewed provider adapter.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from unclaimed_platform.adapters.sources.ny_owner_name_p1_targetability_local import (
    execute_real_p1_targetability_local,
)
from unclaimed_platform.domain.ny_mvp1_p1_authorization import (
    build_p1_execution_authorization,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--local-file-gate", type=Path, required=True)
    parser.add_argument("--l1-pii-gate", type=Path, required=True)
    parser.add_argument("--preflight-gate", type=Path, required=True)
    parser.add_argument("--l1-execution-gate", type=Path, required=True)
    parser.add_argument("--preflight-receipt", type=Path, required=True)
    parser.add_argument("--runner-checkpoint", required=True)
    parser.add_argument("--authorized-download-started-at-utc", required=True)
    return parser


def main() -> int:
    args = _parser().parse_args()
    authorization = build_p1_execution_authorization(
        local_file_gate_path=args.local_file_gate,
        l1_pii_gate_path=args.l1_pii_gate,
        preflight_gate_path=args.preflight_gate,
        l1_execution_gate_path=args.l1_execution_gate,
        preflight_receipt_path=args.preflight_receipt,
        expected_runner_checkpoint=args.runner_checkpoint,
        authorized_download_started_at_utc=args.authorized_download_started_at_utc,
    )
    result = execute_real_p1_targetability_local(
        authorization,
        args.archive,
        l2a_provider=None,
    )
    print(result.model_dump_json())
    return 0 if result.status == "COMPLETED" else 2


if __name__ == "__main__":
    raise SystemExit(main())

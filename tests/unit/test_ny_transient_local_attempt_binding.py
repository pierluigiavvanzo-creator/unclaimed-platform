from __future__ import annotations

import json
from pathlib import Path

import pytest

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    GATE2_ID,
    LOCAL_APPROVAL_GATE,
    build_real_execution_authorization,
)


def _write(path: Path, payload: dict[str, object]) -> Path:
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _granted_approvals(tmp_path: Path) -> tuple[Path, Path]:
    local = {
        "authorization_gate": LOCAL_APPROVAL_GATE,
        "status": "GRANTED_NOT_CONSUMED",
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "attempt_number": 3,
        "execution_approval_ref": "SYNTHETIC_LOCAL_ATTEMPT_3",
        "scope": {"max_download_bytes": 450_000_000},
    }
    gate2 = {
        "authorization_gate": GATE2_ID,
        "status": "GRANTED_NOT_CONSUMED",
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "attempt_number": 3,
        "execution_approval_ref": "SYNTHETIC_PII_ATTEMPT_3",
        "execution_bounds": {
            "downloads_max": 1,
            "retries_max": 0,
            "max_download_bytes": 450_000_000,
            "max_uncompressed_bytes": 2_000_000_000,
            "max_archive_members": 1,
        },
    }
    return (
        _write(tmp_path / "local.json", local),
        _write(tmp_path / "gate2.json", gate2),
    )


def test_runtime_authorization_is_bound_to_expected_attempt(tmp_path: Path) -> None:
    local, gate2 = _granted_approvals(tmp_path)

    authorization = build_real_execution_authorization(
        local,
        gate2,
        expected_attempt_number=3,
    )

    assert authorization.attempt_number == 3


def test_runtime_rejects_wrong_expected_attempt(tmp_path: Path) -> None:
    local, gate2 = _granted_approvals(tmp_path)

    with pytest.raises(ValueError, match="does not match the requested attempt"):
        build_real_execution_authorization(
            local,
            gate2,
            expected_attempt_number=2,
        )

from __future__ import annotations

import json
import zipfile
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_7 import (
    EXPECTED_PROPOSAL_CHECKPOINT,
    build_real_execution_authorization_v1_6,
    execute_transient_local_product_slice_v1_7,
)

RUNNER = "b" * 40
PROPOSAL_REF = (
    "sources/proposals/ny_osc_owner_name_file_tenth_product_slice_authorization.v1.json"
)


def _stamp(value: datetime) -> str:
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


def _common() -> dict[str, object]:
    return {
        "attempt_number": 10,
        "proposal_ref": PROPOSAL_REF,
        "proposal_checkpoint": EXPECTED_PROPOSAL_CHECKPOINT,
        "runner_checkpoint": RUNNER,
        "runner_ci_conclusion": "SUCCESS",
    }


def _write(path: Path, payload: dict[str, object]) -> Path:
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _build(tmp_path: Path, *, start_offset_seconds: int = 60):
    performed = datetime(2026, 9, 22, 19, 24, 12, tzinfo=UTC)
    started = performed + timedelta(seconds=start_offset_seconds)
    local = {
        **_common(),
        "status": "GRANTED_NOT_CONSUMED",
        "execution_approval_ref": "local-ref",
    }
    pii = {
        **_common(),
        "status": "GRANTED_NOT_CONSUMED",
        "execution_approval_ref": "pii-ref",
    }
    preflight = {
        **_common(),
        "receipt_ref": "preflight-ref",
        "status": "EXACT_MATCH",
        "remote_preflight_performed": True,
        "performed_at_utc": _stamp(performed),
        "freshness_window_seconds": 900,
        "download_performed": False,
        "owner_file_opened": False,
        "owner_pii_processed": False,
        "contains_owner_pii": False,
    }
    execution = {
        **_common(),
        "status": "GRANTED_NOT_CONSUMED",
        "execution_approval_ref": "execution-ref",
        "fresh_preflight_receipt_ref": "preflight-ref",
        "download_authority": "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP",
        "execution_authority": "ONE_BOUND_GATE10_EXECUTION",
    }
    return build_real_execution_authorization_v1_6(
        _write(tmp_path / "local.json", local),
        _write(tmp_path / "pii.json", pii),
        _write(tmp_path / "preflight.json", preflight),
        _write(tmp_path / "execution.json", execution),
        expected_runner_checkpoint=RUNNER,
        authorized_download_started_at_utc=_stamp(started),
        now_utc=performed + timedelta(minutes=30),
    )


def _archive(tmp_path: Path) -> Path:
    fields = [
        b"ID",
        b"IN03",
        b"DESC",
        b"1",
        b"OWNER",
        b"ADDR",
        b"",
        b"",
        b"CITY",
        b"NY",
        b"ZIP",
        b"USA",
        b"HOLDER",
        b"2026",
    ]
    path = tmp_path / "FINDERS.zip"
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owners.txt", b"|".join(fields) + b"\r\n")
    return path


def test_builder_binds_freshness_to_download_start(tmp_path: Path) -> None:
    auth = _build(tmp_path)

    assert auth.attempt_number == 10
    assert auth.contract_version == "1.6.0"
    assert auth.tenth_execution_authorization_ref == "execution-ref"


def test_builder_rejects_download_start_after_freshness_window(
    tmp_path: Path,
) -> None:
    with pytest.raises(ValueError, match="outside fresh preflight window"):
        _build(tmp_path, start_offset_seconds=901)


def test_runtime_completes_product_slice_and_deletes_archive(
    tmp_path: Path,
) -> None:
    auth = _build(tmp_path)
    archive = _archive(tmp_path)

    result = execute_transient_local_product_slice_v1_7(auth, archive)

    assert result.status == "COMPLETED"
    assert result.reason_code == "PRODUCT_SLICE_COMPLETED"
    assert result.product_slice is not None
    assert result.product_slice.primary_in03_candidate_records == 1
    assert archive.exists() is False
    serialized = result.model_dump_json()
    assert "OWNER" not in serialized
    assert "ADDR" not in serialized

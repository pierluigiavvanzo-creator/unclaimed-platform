from __future__ import annotations

import io
import json
import tempfile
import zipfile
from pathlib import Path

import pytest

from unclaimed_platform.adapters.sources.ny_owner_name_schema_discovery import (
    NY_DOCUMENTED_FIELDS,
)
from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    NyTransientLocalExecutionAuthorization,
    build_real_execution_authorization,
    execute_transient_local_file_discovery,
)


def _zip_bytes() -> bytes:
    row = "|".join(
        [
            "1",
            "IN03",
            "Synthetic description",
            "1",
            "Synthetic Owner Alpha",
            "1 Synthetic Street",
            "",
            "",
            "Albany",
            "NY",
            "12207-0000",
            "USA",
            "Synthetic Holder",
            "2026",
        ]
    )
    payload = ("|".join(NY_DOCUMENTED_FIELDS) + "\n" + row + "\n").encode("utf-8")
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return buffer.getvalue()


def _auth(max_download_bytes: int = 100_000) -> NyTransientLocalExecutionAuthorization:
    return NyTransientLocalExecutionAuthorization(
        mode="SYNTHETIC_TEST",
        local_file_approval_ref="synthetic-local-approval",
        gate2_approval_ref="synthetic-gate2-approval",
        local_file_approval_granted=True,
        gate2_approval_granted=True,
        max_download_bytes=max_download_bytes,
        max_uncompressed_bytes=100_000,
        max_archive_members=1,
    )


def _dedicated_temp_file(contents: bytes) -> Path:
    root = Path(tempfile.mkdtemp(prefix="unclaimed-ny-osc-gate2-"))
    path = root / "FINDERS.zip"
    path.write_bytes(contents)
    return path


def test_success_deletes_local_file_and_returns_no_owner_values() -> None:
    path = _dedicated_temp_file(_zip_bytes())

    result = execute_transient_local_file_discovery(_auth(), path)

    assert result.status == "DISCOVERED"
    assert result.local_file_deleted is True
    assert result.logical_deletion_only is True
    assert result.physical_secure_erasure_guaranteed is False
    assert path.exists() is False
    serialized = result.model_dump_json()
    assert "Synthetic Owner Alpha" not in serialized
    assert "Synthetic Street" not in serialized


def test_oversize_file_is_blocked_and_deleted_before_schema_discovery() -> None:
    path = _dedicated_temp_file(_zip_bytes())

    result = execute_transient_local_file_discovery(
        _auth(max_download_bytes=10),
        path,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP"
    assert result.schema_result is None
    assert path.exists() is False


def test_path_outside_dedicated_temp_directory_is_rejected_without_reading(
    tmp_path: Path,
) -> None:
    path = tmp_path / "FINDERS.zip"
    path.write_bytes(_zip_bytes())

    with pytest.raises(ValueError, match="dedicated OS-temp"):
        execute_transient_local_file_discovery(_auth(), path)

    assert path.exists() is True


def test_real_authorization_requires_both_unconsumed_single_use_approvals(
    tmp_path: Path,
) -> None:
    local = tmp_path / "local.json"
    gate2 = tmp_path / "gate2.json"

    local.write_text(
        json.dumps(
            {
                "authorization_gate": (
                    "HUMAN_NY_OSC_FIRST_DOWNLOAD_TRANSIENT_LOCAL_FILE_RETENTION_AUTHORIZATION"
                ),
                "status": "GRANTED_NOT_CONSUMED",
                "single_use": True,
                "reusable": False,
                "retry_authorized": False,
                "attempt_number": 1,
                "execution_approval_ref": "local-approval-ref",
                "scope": {"max_download_bytes": 450_000_000},
            }
        ),
        encoding="utf-8",
    )
    gate2.write_text(
        json.dumps(
            {
                "authorization_gate": (
                    "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION"
                ),
                "status": "GRANTED_NOT_CONSUMED",
                "single_use": True,
                "reusable": False,
                "retry_authorized": False,
                "attempt_number": 1,
                "execution_approval_ref": "gate2-approval-ref",
                "execution_bounds": {
                    "downloads_max": 1,
                    "retries_max": 0,
                    "max_download_bytes": 450_000_000,
                    "max_uncompressed_bytes": 2_000_000_000,
                    "max_archive_members": 1,
                },
            }
        ),
        encoding="utf-8",
    )

    authorization = build_real_execution_authorization(local, gate2)

    assert authorization.mode == "AUTHORIZED_REAL_ONCE"
    assert authorization.attempt_number == 1
    assert authorization.max_download_bytes == 450_000_000
    assert authorization.max_uncompressed_bytes == 2_000_000_000
    assert authorization.max_archive_members == 1


def test_missing_gate2_approval_blocks_runner_construction(tmp_path: Path) -> None:
    local = tmp_path / "local.json"
    gate2 = tmp_path / "gate2.json"

    local.write_text(
        json.dumps(
            {
                "authorization_gate": (
                    "HUMAN_NY_OSC_FIRST_DOWNLOAD_TRANSIENT_LOCAL_FILE_RETENTION_AUTHORIZATION"
                ),
                "status": "GRANTED_NOT_CONSUMED",
                "single_use": True,
                "reusable": False,
                "execution_approval_ref": "local-approval-ref",
            }
        ),
        encoding="utf-8",
    )
    gate2.write_text(
        json.dumps(
            {
                "authorization_gate": (
                    "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION"
                ),
                "status": "NOT_GRANTED",
                "single_use": True,
                "reusable": False,
                "execution_approval_ref": "gate2-approval-ref",
                "execution_bounds": {
                    "max_download_bytes": 450_000_000,
                    "max_uncompressed_bytes": 2_000_000_000,
                    "max_archive_members": 1,
                },
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Gate 2 approval is not available"):
        build_real_execution_authorization(local, gate2)

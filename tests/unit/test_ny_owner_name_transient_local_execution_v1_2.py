from __future__ import annotations

import io
import json
import tempfile
import zipfile
from pathlib import Path

import pytest
from pydantic import ValidationError as PydanticValidationError

from unclaimed_platform.adapters.sources.ny_owner_name_schema_discovery import (
    NY_DOCUMENTED_FIELDS,
)
from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    NyTransientLocalExecutionAuthorizationV1_1,
    build_real_execution_authorization_v1_1,
    execute_transient_local_file_discovery_v1_2,
)


def _zip_payload(payload: bytes) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return buffer.getvalue()


def _row(owner_name: str = "Synthetic Owner Alpha") -> str:
    return "|".join(
        [
            "1",
            "IN03",
            "Synthetic description",
            "1",
            owner_name,
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


def _auth(
    max_download_bytes: int = 100_000,
) -> NyTransientLocalExecutionAuthorizationV1_1:
    return NyTransientLocalExecutionAuthorizationV1_1(
        mode="SYNTHETIC_TEST",
        local_file_approval_ref="synthetic-local",
        gate2_approval_ref="synthetic-gate2",
        local_file_approval_granted=True,
        gate2_approval_granted=True,
        max_download_bytes=max_download_bytes,
        max_uncompressed_bytes=100_000,
        max_archive_members=1,
        quote_dialect_mode="LINE_LOCAL_ARBITRATION",
    )


def _temp_archive(contents: bytes) -> Path:
    root = Path(tempfile.mkdtemp(prefix="unclaimed-ny-osc-gate2-"))
    path = root / "FINDERS.zip"
    path.write_bytes(contents)
    return path


def test_v1_2_discovers_plain_14_field_rows_and_deletes_file() -> None:
    payload = ("|".join(NY_DOCUMENTED_FIELDS) + "\n" + _row() + "\n").encode()
    path = _temp_archive(_zip_payload(payload))

    result = execute_transient_local_file_discovery_v1_2(_auth(), path)

    assert result.contract_version == "1.2.0"
    assert result.status == "DISCOVERED"
    assert result.schema_discovery_quote_dialect_mode == "LINE_LOCAL_ARBITRATION"
    assert result.structural_diagnostic is None
    assert result.quote_dialect_diagnostic is None
    assert path.exists() is False
    serialized = result.model_dump_json()
    assert "Synthetic Owner Alpha" not in serialized
    assert "Synthetic Street" not in serialized


def test_v1_2_quote_dialect_ambiguity_is_fail_closed_and_non_pii() -> None:
    payload = (_row('"Synthetic Owner|Alias"') + "\n").encode()
    path = _temp_archive(_zip_payload(payload))

    result = execute_transient_local_file_discovery_v1_2(_auth(), path)

    assert result.status == "BLOCKED"
    assert result.reason_code == "QUOTE_DIALECT_AMBIGUOUS"
    assert result.structural_diagnostic is None
    assert result.quote_dialect_diagnostic is not None
    assert result.quote_dialect_diagnostic.raw_field_count == 15
    assert result.quote_dialect_diagnostic.quote_aware_field_count == 14
    assert path.exists() is False
    serialized = result.model_dump_json()
    assert "Synthetic Owner" not in serialized
    assert "Alias" not in serialized


def test_v1_2_true_13_field_row_uses_only_structural_diagnostic() -> None:
    values = _row().split("|")[:-1]
    assert len(values) == 13
    path = _temp_archive(_zip_payload(("|".join(values) + "\n").encode()))

    result = execute_transient_local_file_discovery_v1_2(_auth(), path)

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.structural_diagnostic is not None
    assert result.quote_dialect_diagnostic is None
    assert result.structural_diagnostic.structural_field_count == 13
    assert path.exists() is False


def test_v1_2_oversize_archive_is_deleted_before_discovery() -> None:
    path = _temp_archive(_zip_payload((_row() + "\n").encode()))

    result = execute_transient_local_file_discovery_v1_2(
        _auth(max_download_bytes=10),
        path,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP"
    assert result.schema_result is None
    assert result.structural_diagnostic is None
    assert result.quote_dialect_diagnostic is None
    assert path.exists() is False


def test_v1_1_authorization_requires_explicit_line_local_mode() -> None:
    with pytest.raises(PydanticValidationError):
        NyTransientLocalExecutionAuthorizationV1_1(
            mode="SYNTHETIC_TEST",
            local_file_approval_ref="synthetic-local",
            gate2_approval_ref="synthetic-gate2",
            local_file_approval_granted=True,
            gate2_approval_granted=True,
            max_download_bytes=100_000,
            max_uncompressed_bytes=100_000,
            max_archive_members=1,
        )


def test_real_v1_1_builder_requires_versioned_line_local_bindings(
    tmp_path: Path,
) -> None:
    local = tmp_path / "local.json"
    gate2 = tmp_path / "gate2.json"
    local.write_text(
        json.dumps(
            {
                "authorization_gate": (
                    "HUMAN_NY_OSC_FIRST_DOWNLOAD_TRANSIENT_LOCAL_FILE_"
                    "RETENTION_AUTHORIZATION"
                ),
                "status": "GRANTED_NOT_CONSUMED",
                "single_use": True,
                "reusable": False,
                "retry_authorized": False,
                "attempt_number": 99,
                "execution_approval_ref": "future-local-ref",
                "scope": {
                    "expected_local_filename": "FINDERS.zip",
                    "max_download_bytes": 450_000_000,
                    "dedicated_os_temp_directory_required": True,
                    "immediate_logical_deletion_required": True,
                    "durable_raw_persistence_allowed": False,
                    "repository_persistence_allowed": False,
                    "cloud_sync_allowed": False,
                    "chat_upload_allowed": False,
                    "physical_secure_erasure_guaranteed": False,
                },
            }
        ),
        encoding="utf-8",
    )
    gate_payload = {
        "authorization_gate": (
            "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION"
        ),
        "status": "GRANTED_NOT_CONSUMED",
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "attempt_number": 99,
        "execution_approval_ref": "future-gate2-ref",
        "execution_bounds": {
            "downloads_max": 1,
            "retries_max": 0,
            "max_download_bytes": 450_000_000,
            "max_uncompressed_bytes": 2_000_000_000,
            "max_archive_members": 1,
            "required_transient_execution_authorization_contract_version": "1.1.0",
            "required_execution_result_contract_version": "1.2.0",
            "required_quote_dialect_mode": "LINE_LOCAL_ARBITRATION",
            "required_structural_diagnostic_contract_version": "1.0.0",
            "required_quote_dialect_diagnostic_contract_version": "1.0.0",
        },
        "processing_scope": {
            "transient_owner_pii_in_memory_allowed": True,
            "owner_rows_persistence_allowed": False,
            "owner_field_decoding_allowed": False,
            "owner_field_buffering_allowed": False,
            "owner_field_logging_allowed": False,
            "row_specific_human_inspection_allowed": False,
            "derived_non_pii_schema_metadata_persistence_allowed": True,
            "structural_diagnostic_persistence_allowed": True,
            "quote_dialect_diagnostic_persistence_allowed": True,
        },
    }
    gate2.write_text(json.dumps(gate_payload), encoding="utf-8")

    auth = build_real_execution_authorization_v1_1(
        local,
        gate2,
        expected_attempt_number=99,
    )
    assert auth.contract_version == "1.1.0"
    assert auth.quote_dialect_mode == "LINE_LOCAL_ARBITRATION"

    gate_payload["execution_bounds"][
        "required_execution_result_contract_version"
    ] = "1.1.0"
    gate2.write_text(json.dumps(gate_payload), encoding="utf-8")
    with pytest.raises(ValueError, match="line-local runtime binding mismatch"):
        build_real_execution_authorization_v1_1(
            local,
            gate2,
            expected_attempt_number=99,
        )

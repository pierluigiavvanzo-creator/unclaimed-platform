from __future__ import annotations

import io
import tempfile
import zipfile
from pathlib import Path

import pytest
from pydantic import ValidationError as PydanticValidationError

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_3 import (
    NyTransientLocalExecutionAuthorizationV1_2,
    NyTransientLocalExecutionResultV1_3,
    execute_transient_local_file_discovery_v1_3,
)


def _zip_payload(payload: bytes) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return buffer.getvalue()


def _row(
    *,
    owner_name: str = "Synthetic Owner Alpha",
    address1: str = "1 Synthetic Street",
) -> str:
    return "|".join(
        [
            "1",
            "IN03",
            "Synthetic description",
            "1",
            owner_name,
            address1,
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
) -> NyTransientLocalExecutionAuthorizationV1_2:
    return NyTransientLocalExecutionAuthorizationV1_2(
        mode="SYNTHETIC_TEST",
        local_file_approval_ref="synthetic-local",
        gate2_approval_ref="synthetic-gate2",
        local_file_approval_granted=True,
        gate2_approval_granted=True,
        max_download_bytes=max_download_bytes,
        max_uncompressed_bytes=100_000,
        max_archive_members=1,
        quote_dialect_mode="DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
    )


def _temp_archive(contents: bytes) -> Path:
    root = Path(tempfile.mkdtemp(prefix="unclaimed-ny-osc-gate2-"))
    path = root / "FINDERS.zip"
    path.write_bytes(contents)
    return path


def test_v1_3_sixth_shape_discovers_under_raw_literal_policy() -> None:
    payload = (
        _row(address1='"1 Synthetic Street')
        + "\n"
        + _row(owner_name="Synthetic Owner Beta", address1="2 Synthetic Street")
        + "\n"
    ).encode()
    path = _temp_archive(_zip_payload(payload))

    result = execute_transient_local_file_discovery_v1_3(_auth(), path)

    assert result.contract_version == "1.3.0"
    assert result.status == "DISCOVERED"
    assert result.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
    assert result.schema_discovery_quote_dialect_mode == (
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    )
    assert result.schema_result is not None
    assert result.schema_result.observed_data_field_count == 14
    assert result.schema_result.aggregate_complete_record_count == 2
    assert result.structural_diagnostic is None
    assert result.quote_dialect_diagnostic is None
    assert path.exists() is False

    serialized = result.model_dump_json()
    assert "Synthetic Owner Alpha" not in serialized
    assert "Synthetic Owner Beta" not in serialized
    assert "Synthetic Street" not in serialized


def test_v1_3_raw_15_quoted_pipe_blocks_fail_closed() -> None:
    path = _temp_archive(
        _zip_payload((_row(owner_name='"Synthetic | Owner"') + "\n").encode())
    )

    result = execute_transient_local_file_discovery_v1_3(_auth(), path)

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.schema_result is not None
    assert result.schema_result.observed_data_field_count == 15
    assert result.structural_diagnostic is not None
    assert result.structural_diagnostic.structural_field_count == 15
    assert result.quote_dialect_diagnostic is None
    assert path.exists() is False

    serialized = result.model_dump_json()
    assert "Synthetic | Owner" not in serialized


def test_v1_3_raw_13_blocks_fail_closed() -> None:
    row = _row()
    thirteen_fields = "|".join(row.split("|")[:-1])
    path = _temp_archive(_zip_payload((thirteen_fields + "\n").encode()))

    result = execute_transient_local_file_discovery_v1_3(_auth(), path)

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.schema_result is not None
    assert result.schema_result.observed_data_field_count == 13
    assert result.structural_diagnostic is not None
    assert result.structural_diagnostic.structural_field_count == 13
    assert result.quote_dialect_diagnostic is None
    assert path.exists() is False


def test_v1_3_local_archive_cap_blocks_before_schema_and_deletes() -> None:
    path = _temp_archive(_zip_payload((_row() + "\n").encode()))

    result = execute_transient_local_file_discovery_v1_3(
        _auth(max_download_bytes=10),
        path,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP"
    assert result.schema_result is None
    assert result.structural_diagnostic is None
    assert result.quote_dialect_diagnostic is None
    assert result.local_file_deleted is True
    assert result.logical_deletion_only is True
    assert result.physical_secure_erasure_guaranteed is False
    assert path.exists() is False


def test_v1_2_authorization_rejects_real_execution_mode() -> None:
    payload = _auth().model_dump()
    payload["mode"] = "AUTHORIZED_REAL_ONCE"

    with pytest.raises(PydanticValidationError):
        NyTransientLocalExecutionAuthorizationV1_2.model_validate(payload)


def test_v1_3_result_rejects_quote_dialect_diagnostic() -> None:
    path = _temp_archive(_zip_payload((_row() + "\n").encode()))
    result = execute_transient_local_file_discovery_v1_3(_auth(), path)
    payload = result.model_dump()
    payload["quote_dialect_diagnostic"] = {"unexpected": True}

    with pytest.raises(PydanticValidationError):
        NyTransientLocalExecutionResultV1_3.model_validate(payload)


def test_v1_3_rejects_non_temp_archive_without_deleting_it(tmp_path: Path) -> None:
    path = tmp_path / "FINDERS.zip"
    path.write_bytes(_zip_payload((_row() + "\n").encode()))

    with pytest.raises(ValueError, match="dedicated OS-temp"):
        execute_transient_local_file_discovery_v1_3(_auth(), path)

    assert path.exists() is True


def test_v1_3_no_real_builder_or_cli_surface() -> None:
    from unclaimed_platform.adapters.sources import (
        ny_owner_name_transient_local_execution_v1_3 as runtime,
    )

    assert not hasattr(runtime, "build_real_execution_authorization_v1_2")
    assert not hasattr(runtime, "main")

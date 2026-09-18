from __future__ import annotations

import io
import json
import zipfile

import pytest
from pydantic import ValidationError

from unclaimed_platform.adapters.sources.ny_owner_name_schema_discovery import (
    NY_DOCUMENTED_FIELDS,
    NyOwnerNameSchemaDiscoveryAuthorization,
    NyOwnerNameSchemaDiscoveryResult,
    discover_ny_owner_name_schema,
)


def _authorization(
    *,
    max_download_bytes: int = 100_000,
    max_uncompressed_bytes: int = 100_000,
    max_archive_members: int = 2,
) -> NyOwnerNameSchemaDiscoveryAuthorization:
    return NyOwnerNameSchemaDiscoveryAuthorization(
        mode="SYNTHETIC_TEST",
        approval_id="synthetic-gate2-approval",
        max_download_bytes=max_download_bytes,
        max_uncompressed_bytes=max_uncompressed_bytes,
        max_archive_members=max_archive_members,
        persist_raw_bytes=False,
        persist_owner_rows=False,
        owner_field_logging=False,
        row_specific_human_inspection=False,
    )


def _row(
    property_id: str,
    property_type_code: str,
    owner_name: str,
    owner_address: str,
) -> str:
    values = [
        property_id,
        property_type_code,
        "Synthetic property description",
        "1",
        owner_name,
        owner_address,
        "",
        "",
        "Albany",
        "NY",
        "12207-0000",
        "USA",
        "Synthetic Holder",
        "2026",
    ]
    assert len(values) == 14
    return "|".join(values)


def _zip_bytes(*, include_header: bool = True, rows: list[str] | None = None) -> bytes:
    rows = rows or [
        _row("1001", "IN03", "Synthetic Owner Alpha", "1 Synthetic Street"),
        _row("1002", "IN01", "Synthetic Owner Beta", "2 Synthetic Street"),
    ]
    lines: list[str] = []
    if include_header:
        lines.append("|".join(NY_DOCUMENTED_FIELDS))
    lines.extend(rows)
    payload = ("\n".join(lines) + "\n").encode("utf-8")

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return buffer.getvalue()


def test_discovers_documented_layout_without_returning_owner_values() -> None:
    result = discover_ny_owner_name_schema(_authorization(), _zip_bytes())

    assert result.status == "DISCOVERED"
    assert result.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
    assert result.observed_delimiter == "|"
    assert result.observed_data_field_count == 14
    assert result.observed_header_state == "EXACT_DOCUMENTED_HEADER"
    assert result.physical_header_names == NY_DOCUMENTED_FIELDS
    assert result.aggregate_complete_record_count == 2
    assert result.property_type_ascii_record_count == 2
    assert result.member_names_persisted is False
    assert result.raw_file_persisted is False
    assert result.owner_rows_persisted is False
    assert result.no_owner_values_returned is True

    serialized = json.dumps(result.model_dump(mode="json"))
    assert "Synthetic Owner Alpha" not in serialized
    assert "Synthetic Owner Beta" not in serialized
    assert "Synthetic Street" not in serialized


def test_no_header_case_never_persists_first_owner_row_as_header() -> None:
    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False),
    )

    assert result.status == "DISCOVERED"
    assert result.observed_header_state == "NO_HEADER_OBSERVED"
    assert result.physical_header_names == ()
    assert result.aggregate_complete_record_count == 2


def test_archive_cap_is_enforced_before_zip_parsing() -> None:
    archive = _zip_bytes()
    result = discover_ny_owner_name_schema(
        _authorization(max_download_bytes=len(archive) - 1),
        archive,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "ARCHIVE_EXCEEDS_DOWNLOAD_CAP"
    assert result.archive_member_count is None


def test_uncompressed_cap_is_enforced_before_member_read() -> None:
    result = discover_ny_owner_name_schema(
        _authorization(max_uncompressed_bytes=10),
        _zip_bytes(),
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNCOMPRESSED_TEXT_EXCEEDS_CAP"
    assert result.aggregate_complete_record_count is None


def test_wrong_field_count_fails_closed() -> None:
    bad_row = "1|IN03|too|few|fields"
    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False, rows=[bad_row]),
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.physical_header_names == ()


def test_multiple_text_members_fail_closed_without_persisting_names() -> None:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("one.txt", _row("1", "IN03", "A", "A") + "\n")
        archive.writestr("two.txt", _row("2", "IN01", "B", "B") + "\n")

    result = discover_ny_owner_name_schema(_authorization(), buffer.getvalue())

    assert result.status == "BLOCKED"
    assert result.reason_code == "AMBIGUOUS_TEXT_MEMBER_LAYOUT"
    assert result.member_names_persisted is False


def test_owner_field_safety_flags_cannot_be_enabled() -> None:
    with pytest.raises(ValidationError):
        NyOwnerNameSchemaDiscoveryAuthorization(
            mode="SYNTHETIC_TEST",
            approval_id="synthetic-gate2-approval",
            max_download_bytes=100,
            max_uncompressed_bytes=100,
            max_archive_members=1,
            persist_raw_bytes=True,
            persist_owner_rows=False,
            owner_field_logging=False,
            row_specific_human_inspection=False,
        )


def test_result_model_rejects_owner_value_return_flag_change() -> None:
    result = discover_ny_owner_name_schema(_authorization(), _zip_bytes()).model_dump()
    result["no_owner_values_returned"] = False

    with pytest.raises(ValidationError):
        NyOwnerNameSchemaDiscoveryResult.model_validate(result)

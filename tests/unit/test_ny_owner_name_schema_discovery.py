from __future__ import annotations

import io
import json
import zipfile

import pytest
from pydantic import ValidationError

from unclaimed_platform.adapters.sources.ny_owner_name_schema_discovery import (
    NY_DOCUMENTED_FIELDS,
    NyOwnerNameQuoteDialectDiagnosticResult,
    NyOwnerNameSchemaDiscoveryAuthorization,
    NyOwnerNameSchemaDiscoveryResult,
    NyOwnerNameStructuralDiagnosticResult,
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
    assert result.observed_delimiter == "|"
    assert result.observed_data_field_count == 5
    assert result.observed_header_state == "NO_HEADER_OBSERVED"
    assert result.aggregate_complete_record_count == 0
    assert result.property_type_ascii_record_count == 0
    assert result.physical_header_names == ()


def test_quoted_pipe_in_owner_field_does_not_change_structural_field_count() -> None:
    values = [
        "1001",
        "IN03",
        "Synthetic property description",
        "1",
        "Synthetic | Owner",
        "1 Synthetic Street",
        "",
        "",
        "Albany",
        "NY",
        "12207-0000",
        "USA",
        'Synthetic "Holder"',
        "2026",
    ]
    quoted_row = "|".join(f'"{value.replace(chr(34), chr(34) * 2)}"' for value in values)
    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=True, rows=[quoted_row]),
    )

    assert result.status == "DISCOVERED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 1
    assert result.property_type_ascii_record_count == 1
    assert "Synthetic | Owner" not in result.model_dump_json()
    assert 'Synthetic "Holder"' not in result.model_dump_json()


def test_unclosed_double_quote_fails_closed_without_returning_owner_values() -> None:
    bad_row = _row(
        "1001",
        "IN03",
        '"Synthetic Owner',
        "1 Synthetic Street",
    )
    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False, rows=[bad_row]),
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "MALFORMED_QUOTED_RECORD"
    assert result.aggregate_complete_record_count == 0
    assert "Synthetic Owner" not in result.model_dump_json()


def test_field_count_block_preserves_only_documented_header_metadata() -> None:
    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=True, rows=["1|IN03|too|few|fields"]),
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.observed_header_state == "EXACT_DOCUMENTED_HEADER"
    assert result.physical_header_names == NY_DOCUMENTED_FIELDS
    assert result.observed_data_field_count == 5


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



def _zip_raw_payload(payload: bytes) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return buffer.getvalue()


def test_normalized_header_accepts_utf8_bom_without_persisting_data_values() -> None:
    header = ("|".join(NY_DOCUMENTED_FIELDS) + "\n").encode("utf-8")
    row = (
        _row("1001", "IN03", "Synthetic Owner Alpha", "1 Synthetic Street") + "\n"
    ).encode("utf-8")
    archive = _zip_raw_payload(b"\xef\xbb\xbf" + header + row)

    result = discover_ny_owner_name_schema(_authorization(), archive)

    assert result.status == "DISCOVERED"
    assert result.observed_header_state == "NORMALIZED_DOCUMENTED_HEADER"
    assert result.physical_header_names == NY_DOCUMENTED_FIELDS
    assert result.aggregate_complete_record_count == 1
    assert "Synthetic Owner Alpha" not in result.model_dump_json()


def test_normalized_header_accepts_quoted_documented_field_names() -> None:
    quoted_header = "|".join(f'"{field}"' for field in NY_DOCUMENTED_FIELDS) + "\n"
    row = _row("1001", "IN03", "Synthetic Owner Alpha", "1 Synthetic Street") + "\n"
    archive = _zip_raw_payload((quoted_header + row).encode("utf-8"))

    result = discover_ny_owner_name_schema(_authorization(), archive)

    assert result.status == "DISCOVERED"
    assert result.observed_header_state == "NORMALIZED_DOCUMENTED_HEADER"
    assert result.aggregate_complete_record_count == 1


@pytest.mark.parametrize("code", ['"IN03"', " IN03 ", "'IN03'"])
def test_property_type_code_accepts_harmless_ascii_wrapping(code: str) -> None:
    archive = _zip_bytes(
        include_header=False,
        rows=[_row("1001", code, "Synthetic Owner Alpha", "1 Synthetic Street")],
    )

    result = discover_ny_owner_name_schema(_authorization(), archive)

    assert result.status == "DISCOVERED"
    assert result.property_type_ascii_record_count == 1


def test_property_type_code_still_rejects_non_alphanumeric_internal_shape() -> None:
    archive = _zip_bytes(
        include_header=False,
        rows=[
            _row(
                "1001",
                "IN 03",
                "Synthetic Owner Alpha",
                "1 Synthetic Street",
            )
        ],
    )

    result = discover_ny_owner_name_schema(_authorization(), archive)

    assert result.status == "BLOCKED"
    assert result.reason_code == "PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED"



@pytest.mark.parametrize("newline", ["\n", "\r\n"])
def test_multiline_quoted_owner_field_is_one_logical_record(newline: str) -> None:
    values = [
        "1001",
        "IN03",
        "Synthetic property description",
        "1",
        f'"Synthetic Owner Alpha{newline}Synthetic Owner Continuation"',
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
    payload = ("|".join(values) + newline).encode("utf-8")

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
    )

    assert result.status == "DISCOVERED"
    assert result.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 1
    assert result.property_type_ascii_record_count == 1
    assert result.observed_header_state == "NO_HEADER_OBSERVED"
    assert "Synthetic Owner" not in result.model_dump_json()


def test_multiline_quoted_pipe_and_doubled_quote_remain_non_structural() -> None:
    first = [
        "1001",
        "IN03",
        "Synthetic property description",
        "1",
        '"Synthetic | Owner\nwith ""quoted"" continuation"',
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
    second = _row(
        "1002",
        "IN01",
        "Synthetic Owner Beta",
        "2 Synthetic Street",
    )
    payload = ("|".join(first) + "\n" + second + "\n").encode("utf-8")

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
    )

    assert result.status == "DISCOVERED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 2
    assert result.property_type_ascii_record_count == 2
    serialized = result.model_dump_json()
    assert "Synthetic | Owner" not in serialized
    assert "quoted" not in serialized


def test_eof_inside_multiline_quote_still_fails_closed() -> None:
    payload = (
        b'1001|IN03|Synthetic description|1|"Synthetic Owner\n'
        b"continuation without closing quote"
    )

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "MALFORMED_QUOTED_RECORD"
    assert result.aggregate_complete_record_count == 0
    assert result.property_type_ascii_record_count == 0
    assert result.observed_delimiter == "|"
    assert "Synthetic Owner" not in result.model_dump_json()


def test_wrong_field_count_after_multiline_assembly_fails_closed() -> None:
    payload = (
        b'1001|IN03|Synthetic description|1|"Synthetic Owner\n'
        b'Continuation"|too|few\n'
    )

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.observed_data_field_count == 7
    assert result.aggregate_complete_record_count == 0
    assert "Synthetic Owner" not in result.model_dump_json()


def test_invalid_property_type_after_multiline_record_fails_closed() -> None:
    first = [
        "1001",
        "IN03",
        "Synthetic description",
        "1",
        '"Synthetic Owner\nContinuation"',
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
    second = _row(
        "1002",
        "IN 03",
        "Synthetic Owner Beta",
        "2 Synthetic Street",
    )
    payload = ("|".join(first) + "\n" + second + "\n").encode("utf-8")

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED"
    assert result.aggregate_complete_record_count == 1
    assert result.property_type_ascii_record_count == 1
    assert "Synthetic Owner" not in result.model_dump_json()



def _synthetic_tail_after_owner() -> bytes:
    return b"|1 Synthetic Street|||Albany|NY|12207|USA|Synthetic Holder|2026\n"


def test_doubled_quote_across_stream_chunk_boundary() -> None:
    prefix = b'1001|IN03|Synthetic description|1|"'
    padding = b"A" * ((64 * 1024 - 1) - len(prefix))
    payload = (
        prefix
        + padding
        + b'""continuation"'
        + _synthetic_tail_after_owner()
    )

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
    )

    assert result.status == "DISCOVERED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 1
    assert result.property_type_ascii_record_count == 1
    assert "continuation" not in result.model_dump_json()


def test_crlf_inside_quotes_across_stream_chunk_boundary() -> None:
    prefix = b'1001|IN03|Synthetic description|1|"'
    padding = b"A" * ((64 * 1024 - 1) - len(prefix))
    payload = (
        prefix
        + padding
        + b"\r\ncontinuation\""
        + _synthetic_tail_after_owner()
    )

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
    )

    assert result.status == "DISCOVERED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 1
    assert result.property_type_ascii_record_count == 1
    assert "continuation" not in result.model_dump_json()


def test_structural_diagnostic_true_13_field_row_reports_raw_shortage() -> None:
    row = _row("1001", "IN03", "Synthetic Owner Alpha", "1 Synthetic Street")
    thirteen_fields = "|".join(row.split("|")[:-1])
    diagnostics: list[NyOwnerNameStructuralDiagnosticResult] = []
    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False, rows=[thirteen_fields]),
        structural_diagnostic_sink=diagnostics.append,
    )
    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.observed_data_field_count == 13
    diagnostic = diagnostics[0]
    assert diagnostic.classification == "RAW_DELIMITER_COUNT_BELOW_DOCUMENTED"
    assert diagnostic.raw_pipe_count == 12
    assert diagnostic.structural_pipe_count == 12
    assert diagnostic.suppressed_pipe_count == 0
    assert diagnostic.quote_byte_count == 0


def test_structural_diagnostic_detects_quote_suppressed_separator() -> None:
    values = [
        "1001", "IN03", "Synthetic property description", "1",
        '"Synthetic Owner Alpha', '1 Synthetic Street"', "", "",
        "Albany", "NY", "12207-0000", "USA", "Synthetic Holder", "2026",
    ]
    diagnostics: list[NyOwnerNameStructuralDiagnosticResult] = []
    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False, rows=["|".join(values)]),
        structural_diagnostic_sink=diagnostics.append,
    )
    assert result.status == "BLOCKED"
    assert result.observed_data_field_count == 13
    diagnostic = diagnostics[0]
    assert diagnostic.classification == "QUOTE_SUPPRESSED_DELIMITER_OBSERVED"
    assert diagnostic.raw_pipe_count == 13
    assert diagnostic.structural_pipe_count == 12
    assert diagnostic.suppressed_pipe_count == 1
    assert diagnostic.quote_open_event_count == 1
    assert diagnostic.quote_close_event_count == 1
    serialized = diagnostic.model_dump_json()
    assert "Synthetic Owner Alpha" not in serialized
    assert "Synthetic Street" not in serialized


def test_structural_diagnostic_not_emitted_for_valid_quoted_pipe() -> None:
    values = [
        "1001", "IN03", "Synthetic property description", "1",
        '"Synthetic | Owner"', "1 Synthetic Street", "", "",
        "Albany", "NY", "12207-0000", "USA", "Synthetic Holder", "2026",
    ]
    diagnostics: list[NyOwnerNameStructuralDiagnosticResult] = []
    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False, rows=["|".join(values)]),
        structural_diagnostic_sink=diagnostics.append,
    )
    assert result.status == "DISCOVERED"
    assert result.observed_data_field_count == 14
    assert diagnostics == []


def test_structural_diagnostic_counts_multiline_quote_without_values() -> None:
    payload = (
        b'1001|IN03|Synthetic description|1|"Synthetic Owner\n'
        b'Continuation"|1 Synthetic Street|||Albany|NY|12207|USA|Holder\n'
    )
    diagnostics: list[NyOwnerNameStructuralDiagnosticResult] = []
    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
        structural_diagnostic_sink=diagnostics.append,
    )
    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    diagnostic = diagnostics[0]
    assert diagnostic.physical_line_breaks_inside_quotes == 1
    assert diagnostic.quote_open_event_count == 1
    assert diagnostic.quote_close_event_count == 1
    assert "Synthetic Owner" not in diagnostic.model_dump_json()



def test_line_local_arbitration_never_carries_open_quote_across_lines() -> None:
    first = _row(
        "1001",
        "IN03",
        '"Synthetic Owner Alpha',
        "1 Synthetic Street",
    )
    second = _row(
        "1002",
        "IN01",
        "Synthetic Owner Beta",
        "2 Synthetic Street",
    )
    payload = (first + "\n" + second + "\n").encode("utf-8")
    diagnostics: list[NyOwnerNameQuoteDialectDiagnosticResult] = []

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
        quote_dialect_mode="LINE_LOCAL_ARBITRATION",
        quote_dialect_diagnostic_sink=diagnostics.append,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "QUOTE_DIALECT_AMBIGUOUS"
    assert result.aggregate_complete_record_count == 0
    assert result.observed_data_field_count is None
    assert len(diagnostics) == 1
    diagnostic = diagnostics[0]
    assert diagnostic.ended_inside_quote is True
    assert diagnostic.raw_pipe_count == 13
    assert diagnostic.raw_field_count == 14
    assert diagnostic.quote_aware_structural_pipe_count == 4
    assert diagnostic.quote_aware_field_count == 5
    assert diagnostic.suppressed_pipe_count == 9
    assert "Synthetic Owner" not in diagnostic.model_dump_json()
    assert "Synthetic Street" not in diagnostic.model_dump_json()


def test_line_local_arbitration_blocks_same_line_quoted_pipe_as_ambiguous() -> None:
    values = [
        "1001",
        "IN03",
        "Synthetic property description",
        "1",
        '"Synthetic | Owner"',
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
    diagnostics: list[NyOwnerNameQuoteDialectDiagnosticResult] = []

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False, rows=["|".join(values)]),
        quote_dialect_mode="LINE_LOCAL_ARBITRATION",
        quote_dialect_diagnostic_sink=diagnostics.append,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "QUOTE_DIALECT_AMBIGUOUS"
    assert result.observed_data_field_count is None
    diagnostic = diagnostics[0]
    assert diagnostic.classification == (
        "RAW_AND_QUOTE_AWARE_FIELD_COUNTS_DIVERGE"
    )
    assert diagnostic.ended_inside_quote is False
    assert diagnostic.raw_pipe_count == 14
    assert diagnostic.raw_field_count == 15
    assert diagnostic.quote_aware_structural_pipe_count == 13
    assert diagnostic.quote_aware_field_count == 14
    assert diagnostic.suppressed_pipe_count == 1


def test_line_local_arbitration_accepts_balanced_quotes_without_pipe() -> None:
    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(
            include_header=False,
            rows=[
                _row(
                    "1001",
                    "IN03",
                    '"Synthetic Owner Alpha"',
                    "1 Synthetic Street",
                )
            ],
        ),
        quote_dialect_mode="LINE_LOCAL_ARBITRATION",
    )

    assert result.status == "DISCOVERED"
    assert result.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 1


def test_line_local_true_13_field_row_still_uses_field_count_fail_closed() -> None:
    row = _row("1001", "IN03", "Synthetic Owner Alpha", "1 Synthetic Street")
    thirteen_fields = "|".join(row.split("|")[:-1])
    structural: list[NyOwnerNameStructuralDiagnosticResult] = []
    quote_dialect: list[NyOwnerNameQuoteDialectDiagnosticResult] = []

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False, rows=[thirteen_fields]),
        structural_diagnostic_sink=structural.append,
        quote_dialect_mode="LINE_LOCAL_ARBITRATION",
        quote_dialect_diagnostic_sink=quote_dialect.append,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.observed_data_field_count == 13
    assert len(structural) == 1
    assert structural[0].classification == "RAW_DELIMITER_COUNT_BELOW_DOCUMENTED"
    assert quote_dialect == []



def test_line_local_unknown_mode_fails_closed_before_archive_processing() -> None:
    with pytest.raises(ValueError, match="unsupported quote dialect mode"):
        discover_ny_owner_name_schema(
            _authorization(max_download_bytes=1),
            b"not-a-zip",
            quote_dialect_mode="LINE_LOCAL_ARBITRATON",  # type: ignore[arg-type]
        )


def test_line_local_crlf_split_across_stream_chunk_boundary() -> None:
    chunk_size = 64 * 1024
    prefix = b"1001|IN03|Synthetic description|1|"
    tail = (
        b"|1 Synthetic Street|||Albany|NY|12207|USA|"
        b"Synthetic Holder|2026"
    )
    padding = b"A" * ((chunk_size - 1) - len(prefix) - len(tail))
    first = prefix + padding + tail
    assert len(first) == chunk_size - 1

    second = (
        _row(
            "1002",
            "IN01",
            "Synthetic Owner Beta",
            "2 Synthetic Street",
        )
        + "\r\n"
    ).encode("utf-8")
    payload = first + b"\r\n" + second

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
        quote_dialect_mode="LINE_LOCAL_ARBITRATION",
    )

    assert result.status == "DISCOVERED"
    assert result.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 2
    assert result.property_type_ascii_record_count == 2


def test_line_local_doubled_quote_split_across_stream_chunk_boundary() -> None:
    chunk_size = 64 * 1024
    prefix = b'1001|IN03|Synthetic description|1|"'
    padding = b"A" * ((chunk_size - 1) - len(prefix))
    tail = (
        b"|1 Synthetic Street|||Albany|NY|12207|USA|"
        b"Synthetic Holder|2026\n"
    )
    payload = prefix + padding + b'""continuation"' + tail

    assert payload[chunk_size - 1 : chunk_size + 1] == b'""'

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
        quote_dialect_mode="LINE_LOCAL_ARBITRATION",
    )

    assert result.status == "DISCOVERED"
    assert result.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 1
    assert result.property_type_ascii_record_count == 1



def test_raw_literal_policy_accepts_sixth_shape_without_quote_carry() -> None:
    first = _row(
        "1001",
        "IN03",
        '"Synthetic Owner Alpha',
        "1 Synthetic Street",
    )
    second = _row(
        "1002",
        "IN01",
        "Synthetic Owner Beta",
        "2 Synthetic Street",
    )
    quote_diagnostics: list[NyOwnerNameQuoteDialectDiagnosticResult] = []

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False, rows=[first, second]),
        quote_dialect_mode="DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
        quote_dialect_diagnostic_sink=quote_diagnostics.append,
    )

    assert result.status == "DISCOVERED"
    assert result.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 2
    assert result.property_type_ascii_record_count == 2
    assert quote_diagnostics == []
    serialized = result.model_dump_json()
    assert "Synthetic Owner Alpha" not in serialized
    assert "Synthetic Owner Beta" not in serialized


def test_raw_literal_policy_blocks_same_line_quoted_pipe_as_raw_15_fields() -> None:
    values = [
        "1001",
        "IN03",
        "Synthetic property description",
        "1",
        '"Synthetic | Owner"',
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
    structural: list[NyOwnerNameStructuralDiagnosticResult] = []
    quote_diagnostics: list[NyOwnerNameQuoteDialectDiagnosticResult] = []

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False, rows=["|".join(values)]),
        structural_diagnostic_sink=structural.append,
        quote_dialect_mode="DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
        quote_dialect_diagnostic_sink=quote_diagnostics.append,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.observed_data_field_count == 15
    assert len(structural) == 1
    diagnostic = structural[0]
    assert diagnostic.classification == "STRUCTURAL_MISMATCH_UNCLASSIFIED"
    assert diagnostic.raw_pipe_count == 14
    assert diagnostic.structural_pipe_count == 14
    assert diagnostic.suppressed_pipe_count == 0
    assert diagnostic.quote_byte_count == 0
    assert quote_diagnostics == []
    serialized = result.model_dump_json()
    assert "Synthetic | Owner" not in serialized
    assert "Synthetic Street" not in serialized


def test_raw_literal_policy_true_13_field_row_still_fails_closed() -> None:
    row = _row("1001", "IN03", "Synthetic Owner Alpha", "1 Synthetic Street")
    thirteen_fields = "|".join(row.split("|")[:-1])
    structural: list[NyOwnerNameStructuralDiagnosticResult] = []

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_bytes(include_header=False, rows=[thirteen_fields]),
        structural_diagnostic_sink=structural.append,
        quote_dialect_mode="DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.observed_data_field_count == 13
    assert len(structural) == 1
    assert structural[0].classification == "RAW_DELIMITER_COUNT_BELOW_DOCUMENTED"
    assert structural[0].suppressed_pipe_count == 0


def test_raw_literal_policy_crlf_is_hard_boundary_with_open_quote() -> None:
    first = _row(
        "1001",
        "IN03",
        '"Synthetic Owner Alpha',
        "1 Synthetic Street",
    )
    second = _row(
        "1002",
        "IN01",
        "Synthetic Owner Beta",
        "2 Synthetic Street",
    )
    payload = (first + "\r\n" + second + "\r\n").encode("utf-8")

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
        quote_dialect_mode="DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
    )

    assert result.status == "DISCOVERED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 2
    assert result.property_type_ascii_record_count == 2


def test_raw_literal_policy_crlf_split_across_stream_chunk_boundary() -> None:
    chunk_size = 64 * 1024
    prefix = b'1001|IN03|Synthetic description|1|"'
    tail = (
        b"|1 Synthetic Street|||Albany|NY|12207|USA|"
        b"Synthetic Holder|2026"
    )
    padding = b"A" * ((chunk_size - 1) - len(prefix) - len(tail))
    first = prefix + padding + tail
    assert len(first) == chunk_size - 1

    second = (
        _row(
            "1002",
            "IN01",
            "Synthetic Owner Beta",
            "2 Synthetic Street",
        )
        + "\r\n"
    ).encode("utf-8")
    payload = first + b"\r\n" + second

    result = discover_ny_owner_name_schema(
        _authorization(),
        _zip_raw_payload(payload),
        quote_dialect_mode="DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
    )

    assert result.status == "DISCOVERED"
    assert result.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
    assert result.observed_data_field_count == 14
    assert result.aggregate_complete_record_count == 2
    assert result.property_type_ascii_record_count == 2


def test_raw_literal_policy_preserves_quoted_header_normalization() -> None:
    quoted_header = "|".join(f'"{field}"' for field in NY_DOCUMENTED_FIELDS) + "\n"
    row = _row(
        "1001",
        "IN03",
        '"Synthetic Owner Alpha',
        "1 Synthetic Street",
    ) + "\n"
    archive = _zip_raw_payload((quoted_header + row).encode("utf-8"))

    result = discover_ny_owner_name_schema(
        _authorization(),
        archive,
        quote_dialect_mode="DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
    )

    assert result.status == "DISCOVERED"
    assert result.observed_header_state == "NORMALIZED_DOCUMENTED_HEADER"
    assert result.physical_header_names == NY_DOCUMENTED_FIELDS
    assert result.aggregate_complete_record_count == 1

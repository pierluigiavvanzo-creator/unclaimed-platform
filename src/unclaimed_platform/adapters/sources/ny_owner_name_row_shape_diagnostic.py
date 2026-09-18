"""Aggregate byte-level row-shape diagnostic for the NY OSC Owner Name File.

This diagnostic is deliberately narrower than a parser. It never decodes or returns
owner-field values. It compares raw pipe counts with a double-quote-aware structural
count so a later human review can distinguish likely quoting from a genuine layout
divergence without inspecting a real owner row.
"""

from __future__ import annotations

import io
import zipfile
from collections import Counter
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

NY_OWNER_NAME_SOURCE_ID = "ny.osc.unclaimed_funds.owner_name_file"


class NyOwnerNameRowShapeDiagnosticAuthorization(BaseModel):
    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    mode: Literal["SYNTHETIC_TEST", "AUTHORIZED_TRANSIENT_MEMORY_ONLY"]
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = NY_OWNER_NAME_SOURCE_ID
    approval_id: str = Field(min_length=1)
    max_download_bytes: int = Field(gt=0)
    max_uncompressed_bytes: int = Field(gt=0)
    max_archive_members: int = Field(gt=0)
    max_physical_lines_to_scan: int = Field(gt=0)
    persist_raw_bytes: Literal[False] = False
    persist_owner_rows: Literal[False] = False
    owner_field_logging: Literal[False] = False
    row_specific_human_inspection: Literal[False] = False


class NyOwnerNameRowShapeDiagnosticResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    status: Literal["DIAGNOSED", "BLOCKED"]
    reason_code: str = Field(min_length=3)
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = NY_OWNER_NAME_SOURCE_ID
    approval_id: str = Field(min_length=1)
    archive_byte_count: int = Field(ge=0)
    archive_member_count: int | None = Field(default=None, ge=0)
    selected_text_member_present: bool | None = None
    selected_member_uncompressed_bytes: int | None = Field(default=None, ge=0)
    physical_lines_scanned: int = Field(ge=0)
    raw_field_count_histogram: dict[str, int]
    quote_aware_field_count_histogram: dict[str, int]
    trailing_delimiter_line_count: int = Field(ge=0)
    unbalanced_double_quote_line_count: int = Field(ge=0)
    exact_14_raw_line_count: int = Field(ge=0)
    exact_14_quote_aware_line_count: int = Field(ge=0)
    member_names_persisted: Literal[False] = False
    raw_file_persisted: Literal[False] = False
    owner_rows_persisted: Literal[False] = False
    owner_field_logging: Literal[False] = False
    row_specific_human_inspection: Literal[False] = False
    no_owner_values_returned: Literal[True] = True


def _quote_aware_field_count(line: bytes) -> tuple[int, bool]:
    field_count = 1
    in_quotes = False
    index = 0

    while index < len(line):
        byte = line[index]

        if byte == 0x22:
            if in_quotes and index + 1 < len(line) and line[index + 1] == 0x22:
                index += 2
                continue
            in_quotes = not in_quotes
        elif byte == 0x7C and not in_quotes:
            field_count += 1

        index += 1

    return field_count, not in_quotes


def _blocked(
    authorization: NyOwnerNameRowShapeDiagnosticAuthorization,
    *,
    reason_code: str,
    archive_byte_count: int,
    archive_member_count: int | None = None,
    selected_text_member_present: bool | None = None,
    selected_member_uncompressed_bytes: int | None = None,
) -> NyOwnerNameRowShapeDiagnosticResult:
    return NyOwnerNameRowShapeDiagnosticResult(
        status="BLOCKED",
        reason_code=reason_code,
        approval_id=authorization.approval_id,
        archive_byte_count=archive_byte_count,
        archive_member_count=archive_member_count,
        selected_text_member_present=selected_text_member_present,
        selected_member_uncompressed_bytes=selected_member_uncompressed_bytes,
        physical_lines_scanned=0,
        raw_field_count_histogram={},
        quote_aware_field_count_histogram={},
        trailing_delimiter_line_count=0,
        unbalanced_double_quote_line_count=0,
        exact_14_raw_line_count=0,
        exact_14_quote_aware_line_count=0,
    )


def diagnose_ny_owner_name_row_shape(
    authorization: NyOwnerNameRowShapeDiagnosticAuthorization,
    archive_bytes: bytes,
) -> NyOwnerNameRowShapeDiagnosticResult:
    archive_byte_count = len(archive_bytes)
    if archive_byte_count > authorization.max_download_bytes:
        return _blocked(
            authorization,
            reason_code="ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
            archive_byte_count=archive_byte_count,
        )

    buffer = io.BytesIO(archive_bytes)
    if not zipfile.is_zipfile(buffer):
        return _blocked(
            authorization,
            reason_code="NOT_A_ZIP_ARCHIVE",
            archive_byte_count=archive_byte_count,
        )

    buffer.seek(0)
    with zipfile.ZipFile(buffer) as archive:
        file_members = [info for info in archive.infolist() if not info.is_dir()]
        member_count = len(file_members)

        if member_count == 0:
            return _blocked(
                authorization,
                reason_code="ARCHIVE_HAS_NO_FILES",
                archive_byte_count=archive_byte_count,
                archive_member_count=0,
            )

        if member_count > authorization.max_archive_members:
            return _blocked(
                authorization,
                reason_code="ARCHIVE_MEMBER_COUNT_EXCEEDS_CAP",
                archive_byte_count=archive_byte_count,
                archive_member_count=member_count,
            )

        text_members = [
            info for info in file_members if info.filename.lower().endswith(".txt")
        ]
        if len(text_members) != 1:
            return _blocked(
                authorization,
                reason_code="AMBIGUOUS_TEXT_MEMBER_LAYOUT",
                archive_byte_count=archive_byte_count,
                archive_member_count=member_count,
                selected_text_member_present=False,
            )

        selected = text_members[0]
        if selected.file_size > authorization.max_uncompressed_bytes:
            return _blocked(
                authorization,
                reason_code="UNCOMPRESSED_TEXT_EXCEEDS_CAP",
                archive_byte_count=archive_byte_count,
                archive_member_count=member_count,
                selected_text_member_present=True,
                selected_member_uncompressed_bytes=selected.file_size,
            )

        raw_histogram: Counter[int] = Counter()
        quote_histogram: Counter[int] = Counter()
        scanned = 0
        trailing_delimiter_count = 0
        unbalanced_quote_count = 0

        with archive.open(selected, "r") as stream:
            for raw_line in stream:
                line = raw_line.rstrip(b"\r\n")
                if not line:
                    continue

                raw_count = line.count(b"|") + 1
                quote_count, quotes_balanced = _quote_aware_field_count(line)

                raw_histogram[raw_count] += 1
                quote_histogram[quote_count] += 1
                trailing_delimiter_count += int(line.endswith(b"|"))
                unbalanced_quote_count += int(not quotes_balanced)

                scanned += 1
                if scanned >= authorization.max_physical_lines_to_scan:
                    break

        if scanned == 0:
            return _blocked(
                authorization,
                reason_code="TEXT_MEMBER_EMPTY",
                archive_byte_count=archive_byte_count,
                archive_member_count=member_count,
                selected_text_member_present=True,
                selected_member_uncompressed_bytes=selected.file_size,
            )

        return NyOwnerNameRowShapeDiagnosticResult(
            status="DIAGNOSED",
            reason_code="AGGREGATE_ROW_SHAPE_CAPTURED",
            approval_id=authorization.approval_id,
            archive_byte_count=archive_byte_count,
            archive_member_count=member_count,
            selected_text_member_present=True,
            selected_member_uncompressed_bytes=selected.file_size,
            physical_lines_scanned=scanned,
            raw_field_count_histogram={
                str(key): value for key, value in sorted(raw_histogram.items())
            },
            quote_aware_field_count_histogram={
                str(key): value for key, value in sorted(quote_histogram.items())
            },
            trailing_delimiter_line_count=trailing_delimiter_count,
            unbalanced_double_quote_line_count=unbalanced_quote_count,
            exact_14_raw_line_count=raw_histogram[14],
            exact_14_quote_aware_line_count=quote_histogram[14],
        )

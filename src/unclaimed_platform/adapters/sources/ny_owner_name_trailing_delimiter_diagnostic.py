"""Attempt-9 bounded byte-level diagnostic for a possible terminal pipe.

The diagnostic never decodes, stores, logs, or returns owner-field values.  It
streams the single TXT member and emits aggregate structural counters only.
"""

from __future__ import annotations

import zipfile
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class NyOwnerNameTrailingDelimiterDiagnosticResult(BaseModel):
    """Non-PII aggregate result for the attempt-9 structural hypothesis."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = (
        "ny.osc.unclaimed_funds.owner_name_file"
    )
    diagnostic_scope: Literal["TRAILING_DELIMITER_STRUCTURAL_ONLY"] = (
        "TRAILING_DELIMITER_STRUCTURAL_ONLY"
    )
    complete_records: int = Field(ge=0)
    records_with_exactly_14_pipes: int = Field(ge=0)
    records_ending_with_pipe: int = Field(ge=0)
    records_with_nonempty_15th_field: int = Field(ge=0)
    records_with_other_pipe_count: int = Field(ge=0)
    classification: Literal[
        "DOCUMENTED_14_FIELDS_WITH_TERMINAL_DELIMITER",
        "TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED",
    ]
    structural_normalization_allowed: bool
    raw_file_persisted: Literal[False] = False
    owner_rows_persisted: Literal[False] = False
    owner_field_logging: Literal[False] = False
    row_specific_human_inspection: Literal[False] = False
    no_raw_record_returned: Literal[True] = True
    no_owner_values_returned: Literal[True] = True


class _PhysicalRecordCounter:
    def __init__(self) -> None:
        self.complete_records = 0
        self.records_with_exactly_14_pipes = 0
        self.records_ending_with_pipe = 0
        self.records_with_nonempty_15th_field = 0
        self.records_with_other_pipe_count = 0
        self._pipe_count = 0
        self._bytes_after_14th_pipe = 0
        self._last_data_byte: int | None = None
        self._has_data = False
        self._pending_cr = False

    def consume(self, value: int) -> None:
        if self._pending_cr:
            self._pending_cr = False
            if value == ord("\n"):
                self._finish_record()
                return
            self._consume_data(ord("\r"))

        if value == ord("\r"):
            self._pending_cr = True
            return
        if value == ord("\n"):
            self._finish_record()
            return
        self._consume_data(value)

    def finish(self) -> None:
        if self._pending_cr:
            self._pending_cr = False
            self._finish_record()
            return
        if self._has_data:
            self._finish_record()

    def _consume_data(self, value: int) -> None:
        self._has_data = True
        if self._pipe_count >= 14:
            self._bytes_after_14th_pipe += 1
        if value == ord("|"):
            self._pipe_count += 1
        self._last_data_byte = value

    def _finish_record(self) -> None:
        if not self._has_data:
            self._reset_record()
            return

        self.complete_records += 1
        if self._pipe_count == 14:
            self.records_with_exactly_14_pipes += 1
        else:
            self.records_with_other_pipe_count += 1
        if self._last_data_byte == ord("|"):
            self.records_ending_with_pipe += 1
        if self._bytes_after_14th_pipe > 0:
            self.records_with_nonempty_15th_field += 1
        self._reset_record()

    def _reset_record(self) -> None:
        self._pipe_count = 0
        self._bytes_after_14th_pipe = 0
        self._last_data_byte = None
        self._has_data = False


def diagnose_ny_owner_name_trailing_delimiter(
    archive_path: Path,
    *,
    max_download_bytes: int = 450_000_000,
    max_uncompressed_bytes: int = 2_000_000_000,
    max_archive_members: int = 1,
) -> NyOwnerNameTrailingDelimiterDiagnosticResult:
    """Stream one bounded ZIP and test only the terminal-empty-field hypothesis."""

    archive_size = archive_path.stat().st_size
    if archive_size > max_download_bytes:
        raise ValueError("archive exceeds bounded download cap")
    if not zipfile.is_zipfile(archive_path):
        raise ValueError("not a ZIP archive")

    with zipfile.ZipFile(archive_path) as archive:
        members = [info for info in archive.infolist() if not info.is_dir()]
        if len(members) != max_archive_members:
            raise ValueError("archive member count mismatch")
        text_members = [
            info for info in members if info.filename.lower().endswith(".txt")
        ]
        if len(text_members) != 1:
            raise ValueError("expected exactly one TXT member")
        selected = text_members[0]
        if selected.file_size > max_uncompressed_bytes:
            raise ValueError("uncompressed TXT exceeds bounded cap")

        counter = _PhysicalRecordCounter()
        with archive.open(selected, "r") as stream:
            while chunk := stream.read(64 * 1024):
                for value in chunk:
                    counter.consume(value)
            counter.finish()

    confirmed = (
        counter.complete_records > 0
        and counter.records_with_exactly_14_pipes == counter.complete_records
        and counter.records_ending_with_pipe == counter.complete_records
        and counter.records_with_nonempty_15th_field == 0
        and counter.records_with_other_pipe_count == 0
    )
    classification: Literal[
        "DOCUMENTED_14_FIELDS_WITH_TERMINAL_DELIMITER",
        "TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED",
    ] = (
        "DOCUMENTED_14_FIELDS_WITH_TERMINAL_DELIMITER"
        if confirmed
        else "TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED"
    )
    return NyOwnerNameTrailingDelimiterDiagnosticResult(
        complete_records=counter.complete_records,
        records_with_exactly_14_pipes=counter.records_with_exactly_14_pipes,
        records_ending_with_pipe=counter.records_ending_with_pipe,
        records_with_nonempty_15th_field=(
            counter.records_with_nonempty_15th_field
        ),
        records_with_other_pipe_count=counter.records_with_other_pipe_count,
        classification=classification,
        structural_normalization_allowed=confirmed,
    )

from __future__ import annotations

import zipfile
from pathlib import Path

from unclaimed_platform.adapters.sources.ny_owner_name_trailing_delimiter_diagnostic import (
    diagnose_ny_owner_name_trailing_delimiter,
)


def _archive(tmp_path: Path, rows: list[bytes]) -> Path:
    path = tmp_path / "FINDERS.zip"
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", b"".join(rows))
    return path


def _fourteen_fields(*, trailing_pipe: bool, extra: bytes = b"") -> bytes:
    fields = [str(index).encode("ascii") for index in range(14)]
    row = b"|".join(fields)
    if trailing_pipe:
        row += b"|"
    return row + extra + b"\r\n"


def test_confirms_terminal_empty_field_for_every_record(tmp_path: Path) -> None:
    path = _archive(
        tmp_path,
        [
            _fourteen_fields(trailing_pipe=True),
            _fourteen_fields(trailing_pipe=True),
        ],
    )

    result = diagnose_ny_owner_name_trailing_delimiter(path)

    assert result.complete_records == 2
    assert result.records_with_exactly_14_pipes == 2
    assert result.records_ending_with_pipe == 2
    assert result.records_with_nonempty_15th_field == 0
    assert result.records_with_other_pipe_count == 0
    assert result.classification == "DOCUMENTED_14_FIELDS_WITH_TERMINAL_DELIMITER"
    assert result.structural_normalization_allowed is True


def test_rejects_nonempty_fifteenth_field(tmp_path: Path) -> None:
    path = _archive(
        tmp_path,
        [_fourteen_fields(trailing_pipe=True, extra=b"EXTRA")],
    )

    result = diagnose_ny_owner_name_trailing_delimiter(path)

    assert result.records_with_nonempty_15th_field == 1
    assert result.classification == "TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED"
    assert result.structural_normalization_allowed is False


def test_rejects_documented_width_without_observed_fourteenth_pipe(
    tmp_path: Path,
) -> None:
    path = _archive(tmp_path, [_fourteen_fields(trailing_pipe=False)])

    result = diagnose_ny_owner_name_trailing_delimiter(path)

    assert result.records_with_exactly_14_pipes == 0
    assert result.records_with_other_pipe_count == 1
    assert result.structural_normalization_allowed is False


def test_serialized_result_contains_no_raw_rows_or_owner_values(tmp_path: Path) -> None:
    path = _archive(tmp_path, [_fourteen_fields(trailing_pipe=True)])

    result = diagnose_ny_owner_name_trailing_delimiter(path)
    serialized = result.model_dump_json()

    assert "owner_names.txt" not in serialized
    assert "FINDERS.zip" not in serialized
    assert result.no_raw_record_returned is True
    assert result.no_owner_values_returned is True

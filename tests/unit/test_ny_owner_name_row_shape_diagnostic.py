from __future__ import annotations

import io
import json
import zipfile

from unclaimed_platform.adapters.sources.ny_owner_name_row_shape_diagnostic import (
    NyOwnerNameRowShapeDiagnosticAuthorization,
    diagnose_ny_owner_name_row_shape,
)


def _authorization() -> NyOwnerNameRowShapeDiagnosticAuthorization:
    return NyOwnerNameRowShapeDiagnosticAuthorization(
        mode="SYNTHETIC_TEST",
        approval_id="synthetic-row-shape-diagnostic",
        max_download_bytes=100_000,
        max_uncompressed_bytes=100_000,
        max_archive_members=1,
        max_physical_lines_to_scan=100,
    )


def _archive(lines: list[bytes]) -> bytes:
    payload = b"\n".join(lines) + b"\n"
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return buffer.getvalue()


def test_quote_aware_histogram_distinguishes_embedded_pipe() -> None:
    fields = [
        b"1",
        b"IN03",
        b"Description",
        b"1",
        b'"Synthetic|Owner"',
        b"Street",
        b"",
        b"",
        b"Albany",
        b"NY",
        b"12207",
        b"USA",
        b"Holder",
        b"2026",
    ]
    result = diagnose_ny_owner_name_row_shape(
        _authorization(),
        _archive([b"|".join(fields)]),
    )

    assert result.status == "DIAGNOSED"
    assert result.raw_field_count_histogram == {"15": 1}
    assert result.quote_aware_field_count_histogram == {"14": 1}
    assert result.exact_14_raw_line_count == 0
    assert result.exact_14_quote_aware_line_count == 1
    assert "Synthetic|Owner" not in result.model_dump_json()


def test_trailing_delimiter_remains_extra_field_in_both_counts() -> None:
    line = b"|".join([b"x"] * 14) + b"|"
    result = diagnose_ny_owner_name_row_shape(
        _authorization(),
        _archive([line]),
    )

    assert result.raw_field_count_histogram == {"15": 1}
    assert result.quote_aware_field_count_histogram == {"15": 1}
    assert result.trailing_delimiter_line_count == 1


def test_unbalanced_double_quote_is_aggregate_only() -> None:
    line = b"|".join([b"x"] * 13 + [b'"unfinished'])
    result = diagnose_ny_owner_name_row_shape(
        _authorization(),
        _archive([line]),
    )

    assert result.unbalanced_double_quote_line_count == 1
    serialized = json.dumps(result.model_dump(mode="json"))
    assert "unfinished" not in serialized


def test_scan_limit_is_enforced() -> None:
    line = b"|".join([b"x"] * 14)
    authorization = _authorization().model_copy(
        update={"max_physical_lines_to_scan": 2}
    )

    result = diagnose_ny_owner_name_row_shape(
        authorization,
        _archive([line, line, line]),
    )

    assert result.physical_lines_scanned == 2
    assert result.raw_field_count_histogram == {"14": 2}

from __future__ import annotations

import zipfile
from pathlib import Path

from unclaimed_platform.adapters.sources.ny_owner_name_product_slice_v1 import (
    run_ny_owner_name_product_slice,
)


def _row(code: bytes, *, extra_field: bool = False) -> bytes:
    fields = [
        b"PROPERTY-ID",
        code,
        b"DESCRIPTION",
        b"1",
        b"SYNTHETIC OWNER MUST NOT LEAK",
        b"1 PRIVATE STREET",
        b"",
        b"",
        b"ALBANY",
        b"NY",
        b"12207",
        b"USA",
        b"SYNTHETIC HOLDER",
        b"2026",
    ]
    if extra_field:
        fields.append(b"EXTRA")
    return b"|".join(fields) + b"\r\n"


def _archive(tmp_path: Path, rows: list[bytes]) -> Path:
    path = tmp_path / "FINDERS.zip"
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owners.txt", b"".join(rows))
    return path


def test_product_slice_classifies_conforming_rows_and_defers_other_shapes(tmp_path: Path) -> None:
    path = _archive(
        tmp_path,
        [
            _row(b"IN03"),
            _row(b"IN01"),
            _row(b"ZZ99"),
            _row(b"IN03", extra_field=True),
            _row(b"\xff\xff\xff\xff"),
        ],
    )

    result = run_ny_owner_name_product_slice(path)

    assert result.total_records == 5
    assert result.structurally_conforming_records == 4
    assert result.deferred_structural_records == 1
    assert result.authority_backed_insurance_records == 2
    assert result.primary_in03_candidate_records == 1
    assert result.other_insurance_records == 1
    assert result.no_authority_backed_insurance_match_records == 1
    assert result.property_type_unclassifiable_records == 1
    assert result.candidate_outcome == "CANDIDATES_PRESENT_AGGREGATE_ONLY"
    assert result.economic_actionability == "VALUE_EVIDENCE_REQUIRED"


def test_product_slice_documents_zero_candidate_without_inventing_value(tmp_path: Path) -> None:
    path = _archive(tmp_path, [_row(b"IN01"), _row(b"ZZ99")])

    result = run_ny_owner_name_product_slice(path)

    assert result.primary_in03_candidate_records == 0
    assert result.candidate_outcome == "ZERO_CANDIDATE_DOCUMENTED"
    assert result.economic_actionability == "ZERO_CANDIDATE_NO_CASE_ECONOMICS"
    assert result.recoverable_value_state == "UNKNOWN_FROM_SOURCE"
    assert result.source_amount_available is False


def test_serialized_product_slice_contains_no_owner_or_raw_values(tmp_path: Path) -> None:
    path = _archive(tmp_path, [_row(b"IN03")])

    serialized = run_ny_owner_name_product_slice(path).model_dump_json()

    assert "SYNTHETIC OWNER MUST NOT LEAK" not in serialized
    assert "PRIVATE STREET" not in serialized
    assert "PROPERTY-ID" not in serialized
    assert "FINDERS.zip" not in serialized


def test_only_exact_existing_authority_codes_are_insurance(tmp_path: Path) -> None:
    path = _archive(tmp_path, [_row(b"in03"), _row(b"IN03"), _row(b"IN99")])

    result = run_ny_owner_name_product_slice(path)

    assert result.authority_backed_insurance_records == 1
    assert result.primary_in03_candidate_records == 1
    assert result.no_authority_backed_insurance_match_records == 2

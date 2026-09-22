from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from unclaimed_platform.adapters.sources.contracts import AcquisitionMode, AcquisitionRequest
from unclaimed_platform.adapters.sources.new_york_osc import NewYorkOSCOwnerNameFileAdapter

ROOT = Path(__file__).resolve().parents[2]


def _request(*, approval_id: str | None = None, jurisdiction: str = "NY") -> AcquisitionRequest:
    return AcquisitionRequest(
        schema_version="1.1.0",
        request_id="42000000-0000-4000-8000-000000000001",
        source_id="ny.osc.unclaimed_funds.owner_name_file",
        jurisdiction=jurisdiction,
        mode=AcquisitionMode.REAL,
        requested_at="2026-09-17T18:00:00Z",
        acquisition_scope="RAW_INGEST_ONLY",
        max_bytes=1,
        approval_id=approval_id,
        expected_media_types=("application/zip", "application/octet-stream"),
        notes="Synthetic contract boundary only.",
    )


def _result_validator() -> Draft202012Validator:
    schema = json.loads(
        (ROOT / "schemas/agents/a01_acquisition_result.v1.1.schema.json").read_text(
            encoding="utf-8"
        )
    )
    assert isinstance(schema, dict)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_ny_owner_file_adapter_fails_closed_while_candidate_is_not_approved() -> None:
    result = NewYorkOSCOwnerNameFileAdapter().acquire(
        _request(approval_id="authorization-placeholder")
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "REAL_SOURCE_NOT_APPROVED"
    assert result.artifact is None
    _result_validator().validate(asdict(result))


def test_even_approved_boundary_stops_before_network_until_schema_discovery() -> None:
    result = NewYorkOSCOwnerNameFileAdapter(approved_for_use=True).acquire(
        _request(approval_id="authorization-placeholder")
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "FIRST_FILE_SCHEMA_DISCOVERY_REQUIRED"
    assert result.artifact is None
    assert result.provenance.retrieved_at is None
    _result_validator().validate(asdict(result))


def test_wrong_jurisdiction_fails_closed() -> None:
    result = NewYorkOSCOwnerNameFileAdapter(approved_for_use=True).acquire(
        _request(approval_id="authorization-placeholder", jurisdiction="CA")
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "JURISDICTION_MISMATCH"
    assert result.artifact is None

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from unclaimed_platform.adapters.sources.california_sco import CaliforniaSCOBulkAdapter
from unclaimed_platform.adapters.sources.contracts import AcquisitionMode, AcquisitionRequest
from unclaimed_platform.adapters.sources.mock import DeferredMockSourceAdapter


def request(
    source_id: str,
    mode: AcquisitionMode,
    approval_id: str | None = None,
) -> AcquisitionRequest:
    return AcquisitionRequest(
        schema_version="1.0.0",
        request_id="30000000-0000-4000-8000-000000000001",
        source_id=source_id,
        jurisdiction="CA",
        mode=mode,
        requested_at="2026-09-13T15:00:00Z",
        acquisition_scope="RAW_INGEST_ONLY",
        max_bytes=1024,
        approval_id=approval_id,
        expected_media_types=("application/json",),
        notes="Synthetic unit test.",
    )


def test_california_sco_adapter_fails_closed_without_source_approval() -> None:
    adapter = CaliforniaSCOBulkAdapter()
    result = adapter.acquire(
        request(adapter.source_id, AcquisitionMode.REAL, "approval-placeholder")
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "REAL_SOURCE_NOT_APPROVED"
    assert result.artifact is None


def test_california_sco_adapter_still_blocks_network_after_contract_approval() -> None:
    adapter = CaliforniaSCOBulkAdapter(approved_for_use=True)
    result = adapter.acquire(request(adapter.source_id, AcquisitionMode.REAL, "approval-001"))

    assert result.status == "BLOCKED"
    assert result.reason_code == "REAL_NETWORK_ACQUISITION_NOT_IMPLEMENTED"
    assert result.artifact is None


def test_deferred_mock_adapter_is_deterministic_and_schema_valid() -> None:
    adapter = DeferredMockSourceAdapter("ca.cdph.death_records")
    result = adapter.acquire(request(adapter.source_id, AcquisitionMode.MOCK))

    assert result.status == "MOCKED"
    assert result.artifact is not None
    assert result.artifact.synthetic is True

    schema_path = (
        Path(__file__).resolve().parents[2]
        / "schemas/agents/a01_acquisition_result.schema.json"
    )
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    payload = asdict(result)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(payload)

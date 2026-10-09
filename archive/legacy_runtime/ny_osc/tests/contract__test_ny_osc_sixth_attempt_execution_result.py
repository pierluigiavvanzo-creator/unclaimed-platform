from __future__ import annotations

import json
from pathlib import Path

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    NyTransientLocalExecutionResultV1_2,
)

ROOT = Path(__file__).resolve().parents[2]
RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_execution_result.v1.json"
)


def test_sixth_execution_result_is_valid_fail_closed_non_pii_evidence() -> None:
    payload = json.loads(RESULT.read_text(encoding="utf-8"))
    result = NyTransientLocalExecutionResultV1_2.model_validate(payload)

    assert result.contract_version == "1.2.0"
    assert result.status == "BLOCKED"
    assert result.reason_code == "QUOTE_DIALECT_AMBIGUOUS"
    assert result.local_file_deleted is True
    assert result.no_raw_path_returned is True
    assert result.no_owner_values_returned is True
    assert result.structural_diagnostic is None
    assert result.quote_dialect_diagnostic is not None
    assert result.quote_dialect_diagnostic.classification == (
        "LINE_END_AND_FIELD_COUNT_DIVERGENCE"
    )
    assert result.quote_dialect_diagnostic.raw_field_count == 14
    assert result.quote_dialect_diagnostic.quote_aware_field_count == 6
    assert result.schema_result is not None
    assert result.schema_result.aggregate_complete_record_count == 165438
    assert result.schema_result.property_type_ascii_record_count == 165438

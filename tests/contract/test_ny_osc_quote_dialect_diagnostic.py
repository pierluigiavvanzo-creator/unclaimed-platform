from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from unclaimed_platform.adapters.sources.ny_owner_name_schema_discovery import (
    NyOwnerNameQuoteDialectDiagnosticResult,
)

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = (
    ROOT
    / "schemas/agents"
    / "ny_owner_name_quote_dialect_diagnostic_result.schema.json"
)


def test_quote_dialect_diagnostic_model_matches_json_schema() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    diagnostic = NyOwnerNameQuoteDialectDiagnosticResult(
        classification="RAW_AND_QUOTE_AWARE_FIELD_COUNTS_DIVERGE",
        raw_field_count=15,
        quote_aware_field_count=14,
        raw_pipe_count=14,
        quote_aware_structural_pipe_count=13,
        suppressed_pipe_count=1,
        quote_byte_count=2,
        quote_open_event_count=1,
        quote_close_event_count=1,
        doubled_quote_pair_count=0,
        ended_inside_quote=False,
    )
    Draft202012Validator(schema).validate(diagnostic.model_dump(mode="json"))
    serialized = diagnostic.model_dump_json()
    assert "Synthetic Owner" not in serialized
    assert "Synthetic Address" not in serialized

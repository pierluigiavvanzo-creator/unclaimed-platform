from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas/common/ny_osc_nonconforming_row_policy_proposal.schema.json"
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_osc_owner_name_file_nonconforming_row_handling_policy.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_ny_nonconforming_row_policy_proposal_is_bounded_and_not_authorized() -> None:
    schema = _load(SCHEMA)
    proposal = _load(PROPOSAL)

    Draft202012Validator(schema).validate(proposal)

    policy = proposal["proposed_policy"]
    auth = proposal["authorization_boundary"]

    assert policy["policy_id"] == "ROW_DEFER_CONTINUE_METADATA_ONLY"
    assert policy["row_field_count_nonconformance"]["parse_any_field_from_deferred_row"] is False
    assert policy["completeness"]["silent_row_omission_allowed"] is False
    assert policy["persistence_boundary"]["aggregate_metadata_only"] is True
    assert policy["persistence_boundary"]["owner_row_persistence_allowed"] is False
    assert auth["runtime_implementation_authorized"] is False
    assert auth["real_source_execution_authorized"] is False
    assert auth["source_activation_authorized"] is False
    assert auth["beneficiary_matching_authorized"] is False

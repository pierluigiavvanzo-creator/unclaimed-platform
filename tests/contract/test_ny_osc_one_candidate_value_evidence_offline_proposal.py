from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_osc_one_candidate_value_evidence_offline_proposal.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_one_candidate_value_evidence_offline_proposal.schema.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    return Draft202012Validator(_load(SCHEMA))


def test_one_candidate_value_evidence_proposal_validates() -> None:
    proposal = _load(PROPOSAL)
    _validator().validate(proposal)

    assert proposal["status"] == "PROPOSED_NOT_IMPLEMENTED_NOT_AUTHORIZED"
    assert proposal["work_class"] == "A_PRODUCT_CRITICAL"
    assert proposal["baseline"]["primary_in03_candidate_records"] == 203921
    assert proposal["baseline"]["candidate_materialization_state"] == (
        "NOT_AUTHORIZED_AGGREGATE_ONLY"
    )


def test_selection_is_deterministic_non_pii_and_single_candidate() -> None:
    selection = _load(PROPOSAL)["candidate_selection_contract"]

    assert selection["mode"] == "FIRST_ELIGIBLE_RECORD_IN_SOURCE_ORDER"
    assert selection["max_candidates"] == 1
    assert selection["required_exact_property_type_code"] == "IN03"
    assert selection["required_property_owner_count"] == 1
    assert selection["requires_nonempty_property_id"] is True
    assert selection["pii_based_ranking_allowed"] is False
    assert selection["random_selection_allowed"] is False
    assert selection["selection_uses_owner_pii"] is False
    assert selection["stop_after_first_match"] is True


def test_materialization_scope_excludes_address_and_durable_owner_pii() -> None:
    materialization = _load(PROPOSAL)["materialization_contract"]

    assert materialization["transient_fields_allowed"] == [
        "Property ID",
        "Property Type Code",
        "Property Owner Count",
        "Owner Name",
        "Holder Name",
        "Holder Report Year",
    ]
    assert materialization["address_fields_allowed"] is False
    assert materialization["raw_row_persistence_allowed"] is False
    assert materialization["owner_name_persistence_allowed"] is False
    assert materialization["property_id_persistence_allowed"] is False
    assert materialization["owner_field_logging_allowed"] is False
    assert materialization["row_specific_human_inspection_allowed"] is False
    assert materialization["same_session_disposal_required"] is True
    assert materialization["persistent_candidate_contains_owner_pii"] is False


def test_value_evidence_reuses_fail_closed_existing_economics() -> None:
    value = _load(PROPOSAL)["value_evidence_contract"]

    assert value["owner_file_amount_available"] is False
    assert value["existing_precontact_value_state"] == "UNKNOWN_PRE_CLAIM_REVIEW"
    assert value["invent_amount_allowed"] is False
    assert value["claim_submission_allowed"] is False
    assert value["identity_resolution_allowed"] is False
    assert value["beneficiary_matching_allowed"] is False
    assert value["outreach_allowed"] is False
    assert (
        "UNKNOWN_PRE_CLAIM_REVIEW"
        in value["supported_outcomes"]
    )


def test_reuse_plan_prefers_existing_product_components() -> None:
    proposal = _load(PROPOSAL)
    decisions = {
        item["path"]: item["decision"]
        for item in proposal["reuse_assessment"]
    }

    assert decisions["schemas/common/case.schema.json"] == "REUSE"
    assert decisions["schemas/common/evidence.schema.json"] == "REUSE"
    assert (
        decisions["src/unclaimed_platform/domain/ny_mvp1_value_evidence.py"]
        == "REUSE"
    )
    assert (
        decisions["src/unclaimed_platform/domain/ny_mvp1_follow_up_cost.py"]
        == "REUSE"
    )
    assert (
        decisions[
            "src/unclaimed_platform/domain/ny_mvp1_case_economics_integration.py"
        ]
        == "REUSE"
    )
    assert decisions["src/unclaimed_platform/api/reviewer.py"] == "ADAPT"


def test_proposal_does_not_authorize_real_execution_or_pii() -> None:
    proposal = _load(PROPOSAL)
    boundary = proposal["implementation_boundaries"]
    no_grant = proposal["authorization_does_not_grant"]

    assert boundary["proposal_only"] is True
    assert boundary["runtime_code_modified"] is False
    assert boundary["source_network_access"] is False
    assert boundary["download"] is False
    assert boundary["owner_pii_processing"] is False
    assert boundary["candidate_materialization"] is False
    assert boundary["value_research"] is False

    assert no_grant["runtime_implementation"] is False
    assert no_grant["download"] is False
    assert no_grant["owner_pii_processing"] is False
    assert no_grant["candidate_materialization"] is False
    assert no_grant["value_research"] is False
    assert no_grant["identity_resolution"] is False
    assert no_grant["beneficiary_matching"] is False
    assert no_grant["outreach"] is False
    assert no_grant["claim_activity"] is False


def test_schema_rejects_scope_expansion() -> None:
    proposal = copy.deepcopy(_load(PROPOSAL))
    proposal["materialization_contract"]["address_fields_allowed"] = True

    with pytest.raises(ValidationError):
        _validator().validate(proposal)


def test_schema_rejects_candidate_count_expansion() -> None:
    proposal = copy.deepcopy(_load(PROPOSAL))
    proposal["candidate_selection_contract"]["max_candidates"] = 2

    with pytest.raises(ValidationError):
        _validator().validate(proposal)

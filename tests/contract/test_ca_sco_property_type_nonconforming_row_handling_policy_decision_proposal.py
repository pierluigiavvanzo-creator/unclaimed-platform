from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/common/"
    "property_type_nonconforming_row_handling_policy_decision_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_decision.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def test_policy_decision_proposal_validates_and_is_not_runtime_authorized() -> None:
    proposal = _load(PROPOSAL_PATH)
    _validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    policy = proposal["proposed_policy"]
    assert isinstance(policy, dict)
    assert policy["policy_id"] == "WHOLE_SOURCE_STOP"
    assert policy["proposal_selection_status"] == (
        "PROPOSED_FOR_HUMAN_REVIEW_NOT_AUTHORIZED"
    )

    boundary = proposal["selection_and_implementation_boundary"]
    assert isinstance(boundary, dict)
    assert boundary["policy_proposed_for_human_review"] is True
    for key, value in boundary.items():
        if key != "policy_proposed_for_human_review":
            assert value is False


def test_base_and_t1_through_t6_are_machine_locked() -> None:
    proposal = _load(PROPOSAL_PATH)
    base = proposal["base_state"]
    assert isinstance(base, dict)
    assert base["branch"] == (
        "m3-ca-sco-property-type-nonconforming-row-handling-proposal-review"
    )
    assert base["head_sha"] == "6ef0cbaed7536c61d00888644bc463d9894418f6"
    assert base["head_ci_run"] == "35094679116"
    assert base["handling_proposal_review_decision"] == (
        "PASS_WITH_MANDATORY_POLICY_DECISION_TIGHTENINGS"
    )

    tightenings = proposal["mandatory_tightenings"]
    assert isinstance(tightenings, dict)
    assert len(tightenings) == 6
    assert all(value is True for value in tightenings.values())


def test_disposition_and_continuation_are_separate_and_fail_closed() -> None:
    proposal = _load(PROPOSAL_PATH)
    policy = proposal["proposed_policy"]
    assert isinstance(policy, dict)

    disposition = policy["control_disposition"]
    continuation = policy["source_continuation"]
    assert isinstance(disposition, dict)
    assert isinstance(continuation, dict)

    assert disposition["status_code"] == "PROPERTY_TYPE_NONCONFORMING_STOPPED"
    assert disposition["reason_code"] == "PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE"
    assert disposition["metadata_only"] is True
    assert disposition["retains_real_row_or_field_content"] is False
    assert disposition["row_specific_human_inspection"] is False

    assert continuation["continue_after_nonconforming_row"] is False
    assert continuation["later_rows_processed_after_trigger"] is False
    assert continuation["silent_row_skip_allowed"] is False
    assert continuation["silent_source_continuation_allowed"] is False


def test_privacy_persistence_and_future_continuation_boundaries_are_locked() -> None:
    proposal = _load(PROPOSAL_PATH)
    policy = proposal["proposed_policy"]
    assert isinstance(policy, dict)

    persistence = policy["persistence_boundary"]
    assert isinstance(persistence, dict)
    assert persistence["may_persist_status_code"] is True
    assert persistence["may_persist_reason_code"] is True
    for key, value in persistence.items():
        if key not in {"may_persist_status_code", "may_persist_reason_code"}:
            assert value is False

    human = policy["human_review_boundary"]
    assert isinstance(human, dict)
    assert human["metadata_only_event_required_by_policy"] is False
    assert human["row_specific_human_inspection_authorized"] is False
    assert human[
        "future_row_specific_inspection_requires_separate_privacy_authorization"
    ] is True

    completeness = policy["completeness_and_audit"]
    assert isinstance(completeness, dict)
    assert completeness["continuation_enabled"] is False
    assert completeness["deferred_row_can_silently_disappear"] is False
    assert completeness["continuation_completeness_evidence_required_now"] is False
    assert completeness[
        "future_continuation_requires_separate_completeness_audit_design"
    ] is True
    assert completeness[
        "future_continuation_identifiers_or_counters_require_privacy_review"
    ] is True


def test_validation_runtime_policy_registry_and_downstream_gates_remain_closed() -> None:
    proposal = _load(PROPOSAL_PATH)
    validation = proposal["unchanged_validation_contract"]
    assert isinstance(validation, dict)
    assert validation["regex"] == EXPECTED_REGEX
    assert validation["trim_before_validation"] is False
    assert validation["ascii_uppercase_before_validation"] is False
    assert validation["unicode_normalization_before_validation"] is False
    assert validation["alternate_token_acceptance"] is False
    assert validation["parser_or_projector_change"] is False

    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    expected_line = (
        'PROPERTY_TYPE_RE = re.compile(r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$")'
    )
    assert expected_line in runner_text

    auth = proposal["authorization_boundary"]
    assert isinstance(auth, dict)
    assert auth["proposal_preparation_authorized"] is True
    for key, value in auth.items():
        if key != "proposal_preparation_authorized":
            assert value is False

    implementation = proposal["implementation_state"]
    assert isinstance(implementation, dict)
    assert implementation["proposal_only"] is True
    for key, value in implementation.items():
        if key not in {"proposal_branch", "proposal_only"}:
            assert value is False

    policy = _load(POLICY_PATH)
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False

    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    source = next(
        item
        for item in registry["sources"]
        if item["source_id"] == "ca.sco.unclaimed_property.bulk"
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False

    safety = proposal["safety_state"]
    assert isinstance(safety, dict)
    assert safety["approved_real_sources"] == 0
    assert safety["semantic_compatibility_resolved"] is False
    assert safety["production_classification_active"] is False
    assert safety["downstream_gates_remain_closed"] is True
    assert proposal["consumed_authorizations_remain_non_reusable"] is True


def test_schema_rejects_runtime_selection_continuation_privacy_or_regex_widening() -> None:
    proposal = _load(PROPOSAL_PATH)
    validator = _validator()

    invalid_cases: list[dict[str, object]] = []

    selected = copy.deepcopy(proposal)
    selected["selection_and_implementation_boundary"]["policy_selected_for_runtime"] = True
    invalid_cases.append(selected)

    continuation = copy.deepcopy(proposal)
    continuation["proposed_policy"]["source_continuation"][
        "continue_after_nonconforming_row"
    ] = True
    invalid_cases.append(continuation)

    retention = copy.deepcopy(proposal)
    retention["proposed_policy"]["persistence_boundary"][
        "may_persist_real_row_or_field_content"
    ] = True
    invalid_cases.append(retention)

    runtime = copy.deepcopy(proposal)
    runtime["authorization_boundary"]["runtime_code_change_authorized"] = True
    invalid_cases.append(runtime)

    regex = copy.deepcopy(proposal)
    regex["unchanged_validation_contract"]["regex"] = ".*"
    invalid_cases.append(regex)

    for invalid in invalid_cases:
        with pytest.raises(ValidationError):
            validator.validate(invalid)

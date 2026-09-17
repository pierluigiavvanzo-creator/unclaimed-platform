from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SOURCE_ID = "ny.osc.unclaimed_funds.owner_name_file"


def _json(path: str) -> object:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def _validator(path: str) -> Draft202012Validator:
    payload = _json(path)
    assert isinstance(payload, dict)
    Draft202012Validator.check_schema(payload)
    return Draft202012Validator(payload, format_checker=FormatChecker())


def test_a01_v1_1_accepts_ny_real_contract_example_and_rejects_missing_approval() -> None:
    examples = _json("schemas/examples/a01_ny_owner_name_file.examples.json")
    assert isinstance(examples, dict)
    validator = _validator("schemas/agents/a01_acquisition_request.v1.1.schema.json")

    validator.validate(examples["ny.real.contract_only.valid"])
    with pytest.raises(ValidationError):
        validator.validate(examples["ny.real.invalid_missing_approval"])


def test_a01_v1_1_blocked_ny_result_is_schema_valid() -> None:
    examples = _json("schemas/examples/a01_ny_owner_name_file.examples.json")
    assert isinstance(examples, dict)
    validator = _validator("schemas/agents/a01_acquisition_result.v1.1.schema.json")
    validator.validate(examples["ny.blocked.schema_discovery_required"])


def test_registry_keeps_new_york_candidate_disabled_and_unapproved() -> None:
    registry = yaml.safe_load((ROOT / "sources/registry.yaml").read_text(encoding="utf-8"))
    sources = registry["sources"]
    ny = next(source for source in sources if source["source_id"] == SOURCE_ID)

    assert ny["jurisdiction"] == "NY"
    assert ny["enabled"] is False
    assert ny["approved_for_use"] is False
    assert ny["provenance_required"] is True
    assert "request-form" in ny["base_uri"]


def test_ny_policy_preserves_only_authority_disclosed_semantics_without_schema_invention() -> None:
    policy = _json("policies/states/NY/ny_osc_owner_name_file.v1.json")
    assert isinstance(policy, dict)

    semantics = policy["officially_disclosed_semantics"]
    assert [item["semantic_id"] for item in semantics] == [
        "owner_name",
        "last_known_address",
        "nature_of_property",
        "reported_when",
        "reported_by",
    ]
    assert [item["semantic_id"] for item in semantics if item["owner_pii"]] == [
        "owner_name",
        "last_known_address",
    ]

    physical = policy["physical_file_contract"]
    assert physical["state"] == "UNKNOWN_UNTIL_FIRST_AUTHORIZED_FILE"
    assert physical["physical_column_names_known"] is False
    assert physical["delimiter_known"] is False
    assert physical["encoding_known"] is False
    assert physical["property_nature_representation_known"] is False
    assert physical["parser_activation_allowed"] is False
    assert physical["normalization_allowed"] is False


def test_ny_insurance_vocabulary_is_source_specific_and_in03_is_primary() -> None:
    policy = _json("policies/states/NY/ny_osc_owner_name_file.v1.json")
    assert isinstance(policy, dict)
    insurance = policy["insurance_authority"]

    assert insurance["codes"] == {
        "IN01": "Individual Policy Benefits or Claim Payments",
        "IN02": "Group Policy Benefits or Claim Payments",
        "IN03": "Proceeds Due Beneficiaries",
        "IN04": "Proceeds from Matured Policies, Endowments or Annuities",
        "IN05": "Premium Refunds",
        "IN06": "Unidentified Remittances",
        "IN07": "Other Amounts Due Under Policy Terms",
        "IN12": "Retained Asset, Benefit Access or Similar Distribution Accounts",
        "IN77": "Limiting Age (superannuated) contracts",
    }
    assert insurance["mvp1_primary_code"] == "IN03"
    assert insurance["classification_activation_allowed"] is False
    assert insurance["property_type_representation_in_owner_file"] == (
        "UNKNOWN_UNTIL_FIRST_AUTHORIZED_FILE"
    )


def test_ny_privacy_gate_is_memory_only_and_requires_two_fresh_single_use_gates() -> None:
    policy = _json("policies/states/NY/ny_osc_owner_name_file.v1.json")
    assert isinstance(policy, dict)

    privacy = policy["privacy"]
    assert privacy["first_file_schema_discovery_mode"] == "MEMORY_ONLY"
    assert privacy["real_owner_pii_allowed_without_privacy_approval"] is False
    assert privacy["raw_file_persistence_allowed_during_first_schema_discovery"] is False
    assert privacy["real_owner_row_persistence_allowed_during_first_schema_discovery"] is False
    assert privacy["owner_field_logging_allowed"] is False

    gates = policy["authorization_gates"]
    request_gate = gates["request_link_gate"]
    download_gate = gates["first_download_transient_pii_gate"]
    assert request_gate["single_use"] is True
    assert request_gate["reusable"] is False
    assert request_gate["retry_authorized"] is False
    assert download_gate["single_use"] is True
    assert download_gate["reusable"] is False
    assert download_gate["retry_authorized"] is False
    assert download_gate["explicit_max_download_bytes_required"] is True
    assert download_gate["default_max_download_bytes"] is None


def test_ny_source_amount_is_explicitly_unknown_from_source() -> None:
    policy = _json("policies/states/NY/ny_osc_owner_name_file.v1.json")
    assert isinstance(policy, dict)
    economics = policy["economics"]
    assert economics == {
        "source_discloses_dollar_value": False,
        "recoverable_value_state": "UNKNOWN_FROM_SOURCE",
        "invent_amount_allowed": False,
    }

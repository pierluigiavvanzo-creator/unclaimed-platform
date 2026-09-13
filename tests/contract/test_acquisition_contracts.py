from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]


def load_json(relative_path: str) -> object:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def validator(relative_path: str) -> Draft202012Validator:
    schema = load_json(relative_path)
    assert isinstance(schema, dict)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_a01_request_contract_requires_approval_for_real_mode() -> None:
    examples = load_json("schemas/examples/a01_acquisition.examples.json")
    assert isinstance(examples, dict)
    request_validator = validator("schemas/agents/a01_acquisition_request.schema.json")

    request_validator.validate(examples["real.valid"])

    with pytest.raises(ValidationError):
        request_validator.validate(examples["real.invalid_missing_approval"])


def test_a01_result_contract_distinguishes_blocked_and_mocked_artifacts() -> None:
    examples = load_json("schemas/examples/a01_acquisition.examples.json")
    assert isinstance(examples, dict)
    result_validator = validator("schemas/agents/a01_acquisition_result.schema.json")

    result_validator.validate(examples["blocked.valid"])
    result_validator.validate(examples["mock.valid"])

    invalid = dict(examples["mock.valid"])
    invalid["artifact"] = None
    with pytest.raises(ValidationError):
        result_validator.validate(invalid)


def test_deferred_source_inventory_is_synthetic_only() -> None:
    payload = load_json("mocks/sources/ca_deferred_sources.json")
    assert isinstance(payload, dict)
    assert payload["synthetic_only"] is True
    cases = payload["cases"]
    assert isinstance(cases, list)

    source_ids = {case["source_id"] for case in cases if isinstance(case, dict)}
    assert source_ids == {
        "ca.sco.estates",
        "ca.cdi.company_profiles",
        "ca.cdi.naic_policy_locator",
        "ca.cdph.death_records",
        "ca.courts.probate",
    }
    assert all(case["acquisition_method"] == "MOCK" for case in cases)

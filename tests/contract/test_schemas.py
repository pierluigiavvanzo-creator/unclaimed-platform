from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]

CONTRACTS = {
    "case": "schemas/common/case.schema.json",
    "evidence": "schemas/common/evidence.schema.json",
    "hypothesis": "schemas/common/hypothesis.schema.json",
    "agent_message": "schemas/agents/agent_message.schema.json",
    "decision": "schemas/agents/decision.schema.json",
    "audit_event": "schemas/common/audit_event.schema.json",
    "source": "schemas/common/source.schema.json",
}


def load_json(relative_path: str) -> dict[str, object]:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def examples() -> dict[str, dict[str, object]]:
    raw = load_json("schemas/examples/contracts.examples.json")
    return {key: value for key, value in raw.items() if isinstance(value, dict)}


@pytest.mark.parametrize(("name", "schema_path"), CONTRACTS.items())
def test_contract_schema_and_examples(
    name: str,
    schema_path: str,
    examples: dict[str, dict[str, object]],
) -> None:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    validator.validate(examples[f"{name}.valid"])

    with pytest.raises(ValidationError):
        validator.validate(examples[f"{name}.invalid"])


def test_agent_registry_is_complete_unique_and_valid() -> None:
    schema = load_json("schemas/agents/agent_registry.schema.json")
    Draft202012Validator.check_schema(schema)
    registry = load_json("config/agents.registry.json")
    Draft202012Validator(schema).validate(registry)

    agents = registry["agents"]
    assert isinstance(agents, list)
    ids = [agent["agent_id"] for agent in agents if isinstance(agent, dict)]
    assert len(ids) == len(set(ids))
    assert set(ids) == {f"A{i:02d}" for i in range(24)}


def test_source_registry_shape_is_valid() -> None:
    schema = load_json("schemas/common/source_registry.schema.json")
    Draft202012Validator.check_schema(schema)
    registry = yaml.safe_load((ROOT / "sources/registry.yaml").read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(registry)


def test_decision_contract_fails_closed_on_unknown_status(
    examples: dict[str, dict[str, object]],
) -> None:
    schema = load_json("schemas/agents/decision.schema.json")
    validator = Draft202012Validator(schema)
    decision = dict(examples["decision.valid"])
    decision["status"] = "UNKNOWN"

    with pytest.raises(ValidationError):
        validator.validate(decision)

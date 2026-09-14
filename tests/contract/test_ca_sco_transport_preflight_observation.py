import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).parents[2]
SCHEMA_PATH = ROOT / "schemas" / "common" / "source_transport_preflight_execution.schema.json"
EVIDENCE_PATH = (
    ROOT
    / "sources"
    / "evidence"
    / "ca_sco_unclaimed_property_bulk.transport_preflight.execution.v1.json"
)
REGISTRY_PATH = ROOT / "sources" / "registry.yaml"
POLICY_PATH = (
    ROOT / "policies" / "states" / "CA" / "ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
ONE_SHOT_WORKFLOW = ROOT / ".github" / "workflows" / "ca-sco-transport-preflight-once.yml"


def _evidence() -> dict[str, object]:
    return json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))


def test_real_transport_observation_matches_versioned_schema() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    payload = _evidence()
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    validator.validate(payload)


def test_real_transport_observation_records_only_metadata_and_zero_body() -> None:
    payload = _evidence()
    endpoint_discovery = payload["endpoint_discovery"]
    transport = payload["transport"]
    safety = payload["safety_state"]

    assert isinstance(endpoint_discovery, dict)
    assert isinstance(transport, dict)
    assert isinstance(safety, dict)

    assert endpoint_discovery["extracted_endpoint"] == (
        "https://claimit.ca.gov/upd-property-records/00_All_Records.zip"
    )
    assert transport["http_status"] == 200
    assert transport["final_host"] == "claimit.ca.gov"
    assert transport["content_type"] == "application/zip"
    assert transport["content_length"] == 3_203_972_130
    assert transport["response_body_bytes_read"] == 0
    assert payload["controls"]["response_body_bytes_allowed"] == 0
    assert safety["acquisition_performed"] is False
    assert safety["source_approved"] is False
    assert safety["source_enabled"] is False
    assert safety["real_pii_processed"] is False
    assert safety["beneficiary_matching_performed"] is False
    assert safety["outreach_performed"] is False


def test_observation_does_not_change_source_registry_or_access_policy() -> None:
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    source = next(
        item
        for item in registry["sources"]
        if item["source_id"] == "ca.sco.unclaimed_property.bulk"
    )
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))

    assert source["enabled"] is False
    assert source["approved_for_use"] is False
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["beneficiary_matching_authorized"] is False
    assert policy["outreach_authorized"] is False
    assert policy["approval_ref"] is None
    assert policy["allow_pii"] is False


def test_one_shot_network_workflow_is_removed_after_observation() -> None:
    assert not ONE_SHOT_WORKFLOW.exists()

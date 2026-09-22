from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/common/property_type_semantic_execution_authorization.schema.json"
AUTH_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_semantic_execution_approval.v1.json"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
SOURCE_ID = "ca.sco.unclaimed_property.bulk"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_bounded_execution_and_transient_privacy_authorization_is_valid() -> None:
    schema = _load(SCHEMA_PATH)
    approval = _load(AUTH_PATH)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(approval)

    scope = approval["authorized_scope"]
    privacy = approval["privacy_controls"]
    caps = approval["execution_caps"]
    assert isinstance(scope, dict)
    assert isinstance(privacy, dict)
    assert isinstance(caps, dict)

    assert scope["bounded_semantic_execution"] is True
    assert scope["transient_row_privacy_exposure"] is True
    assert scope["network_one_shot_workflow"] is True
    assert scope["source_approval"] is False
    assert scope["registry_activation"] is False
    assert scope["identity_resolution"] is False
    assert scope["beneficiary_matching"] is False
    assert scope["outreach"] is False

    assert privacy["memory_only"] is True
    assert privacy["transient_buffer_retention_days"] == 0
    assert privacy["immediate_disposal"] is True
    assert privacy["raw_body_persistence"] is False
    assert privacy["full_row_persistence"] is False
    assert privacy["property_id_persistence"] is False
    assert privacy["owner_holder_persistence"] is False
    assert privacy["per_row_property_type_persistence"] is False
    assert privacy["record_values_in_logs"] is False

    assert caps["members"] == 4
    assert caps["rows_max_per_member"] == 4
    assert caps["rows_max_total"] == 16
    assert caps["head_requests_max"] == 1
    assert caps["range_requests_max"] == 4
    assert caps["http_requests_max_total"] == 5
    assert caps["range_response_bytes_max_each"] == 131_072
    assert caps["source_response_body_bytes_max_total"] == 524_288
    assert caps["uncompressed_transient_bytes_max_each"] == 262_144
    assert caps["uncompressed_transient_bytes_max_total"] == 1_048_576
    assert caps["logical_record_bytes_max"] == 32_768
    assert caps["additional_range_allowed"] is False
    assert caps["full_body_fallback_allowed"] is False


def test_source_approval_and_registry_remain_separately_closed() -> None:
    policy = _load(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))

    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["authorized_processing_purposes"] == []
    assert policy["allowed_fields"] == []
    assert policy["allow_pii"] is False

    source = next(
        item for item in registry["sources"] if item["source_id"] == SOURCE_ID
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False

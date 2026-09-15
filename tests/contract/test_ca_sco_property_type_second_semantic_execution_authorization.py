from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/common/property_type_second_semantic_execution_authorization.schema.json"
)
AUTH_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_second_semantic_execution_approval.v1.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_second_semantic_execution.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)
EXECUTION_REF = "APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED"
PRIVACY_REF = "APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED"
OLD_EXECUTION_REF = (
    "OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED"
)
OLD_PRIVACY_REF = (
    "OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "ca_sco_property_type_semantic_verification_second_execution_auth",
        RUNNER_PATH,
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_second_execution_authorization_validates_and_is_single_use() -> None:
    schema = _load(SCHEMA_PATH)
    authorization = _load(AUTH_PATH)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    ).validate(authorization)

    assert authorization["authorization_status"] == "GRANTED_NOT_YET_CONSUMED"
    assert authorization["execution_approval_ref"] == EXECUTION_REF
    assert authorization["privacy_approval_ref"] == PRIVACY_REF
    assert authorization["single_use"] is True
    assert authorization["runner_schema_version"] == "1.1.0"
    assert authorization["execution_approval_ref"] != OLD_EXECUTION_REF
    assert authorization["privacy_approval_ref"] != OLD_PRIVACY_REF


def test_authorization_matches_reviewed_proposal_and_runner_caps() -> None:
    authorization = _load(AUTH_PATH)
    proposal = _load(PROPOSAL_PATH)
    runner = _load_runner()
    caps = authorization["execution_caps"]
    scope = authorization["authorized_scope"]
    proposal_caps = proposal["transport_caps"]
    assert isinstance(caps, dict)
    assert isinstance(scope, dict)
    assert isinstance(proposal_caps, dict)

    assert authorization["proposal_sha"] == "ac6d234dda19b1eb8c8f8ceb0206730bcc419bcb"
    assert caps["members"] == proposal["sample_plan"]["canonical_member_count"] == 4
    assert caps["rows_max_per_member"] == runner.MAX_ROWS_PER_MEMBER == 4
    assert caps["rows_max_total"] == runner.MAX_ROWS_TOTAL == 16
    assert caps["head_requests_max"] == runner.MAX_HEAD_REQUESTS == 1
    assert caps["range_requests_max"] == runner.MAX_RANGE_REQUESTS == 4
    assert caps["http_requests_max_total"] == runner.MAX_HTTP_REQUESTS == 5
    assert caps["range_response_bytes_max_each"] == runner.RANGE_RESPONSE_BYTES
    assert caps["source_response_body_bytes_max_total"] == runner.MAX_TOTAL_RESPONSE_BYTES
    assert (
        caps["uncompressed_transient_bytes_max_each"]
        == runner.MAX_UNCOMPRESSED_BYTES_PER_MEMBER
    )
    assert (
        caps["uncompressed_transient_bytes_max_total"]
        == runner.MAX_UNCOMPRESSED_BYTES_TOTAL
    )
    assert caps["logical_record_bytes_max"] == runner.MAX_LOGICAL_RECORD_BYTES
    assert caps["http_requests_max_total"] == proposal_caps["http_requests_max_total"]
    assert caps["automatic_widening_allowed"] is False
    assert scope["bounded_semantic_execution"] is True
    assert scope["transient_row_privacy_exposure"] is True
    assert scope["network_one_shot_workflow"] is True


def test_authorization_does_not_open_downstream_gates() -> None:
    authorization = _load(AUTH_PATH)
    scope = authorization["authorized_scope"]
    privacy = authorization["privacy_controls"]
    assert isinstance(scope, dict)
    assert isinstance(privacy, dict)

    for key in (
        "source_approval",
        "registry_activation",
        "production_classification",
        "identity_resolution",
        "genealogy",
        "beneficiary_matching",
        "outreach",
        "claim_submission",
    ):
        assert scope[key] is False

    for key in (
        "raw_body_persistence",
        "full_row_persistence",
        "property_id_persistence",
        "owner_holder_persistence",
        "per_row_property_type_persistence",
        "offending_bytes_persistence",
        "offending_value_hash_persistence",
        "offending_value_length_persistence",
        "record_values_in_logs",
    ):
        assert privacy[key] is False


def test_temporary_workflow_is_pinned_if_present() -> None:
    if not WORKFLOW_PATH.exists():
        return

    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "m3-ca-sco-property-type-second-semantic-execution" in text
    assert f"--approval-ref {EXECUTION_REF}" in text
    assert f"--privacy-approval-ref {PRIVACY_REF}" in text
    assert "property_type_semantic_verification_execution.v1_1.schema.json" in text
    assert "--live-network" in text

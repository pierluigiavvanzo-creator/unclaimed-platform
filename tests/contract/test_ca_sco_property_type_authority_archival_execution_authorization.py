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
    / "schemas/common/property_type_authority_archival_execution_authorization.schema.json"
)
ARTIFACT_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_authority_archival_execution_authorization.v1.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_authority_provenance_acquisition.v1.json"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
APPROVAL_PATH = (
    ROOT
    / "sources/evidence/ca_sco_property_type_authority_archival_execution_approval.v1.json"
)
ARCHIVE_METADATA_PATH = (
    ROOT / "sources/evidence/ca_sco_property_type_authority_archive.v1.json"
)
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-authority-archival-once.yml"
)
SOURCE_ID = "ca.sco.unclaimed_property.bulk"
FRESH_APPROVAL = "APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT"
VERIFIED_AUTHORIZATION_SHA = "d20bc80f50af56c10085eec7123aa0691e26ea1a"
OLD_EXECUTION_APPROVAL = "APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED"
OLD_PRIVACY_APPROVAL = "APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def test_artifact_is_valid_pending_and_offline() -> None:
    artifact = _load(ARTIFACT_PATH)
    _validator().validate(artifact)

    assert artifact["status"] == "PENDING_HUMAN_AUTHORIZATION"
    assert artifact["network_execution_authorized"] is False
    assert artifact["workflow_creation_authorized"] is False
    assert artifact["single_use"] is True
    assert artifact["reusable"] is False
    assert artifact["approval_must_pin_artifact_sha"] is True


def test_progressed_authorization_state_is_bounded_when_present() -> None:
    if not APPROVAL_PATH.exists():
        assert not WORKFLOW_PATH.exists()
        return

    approval = _load(APPROVAL_PATH)
    assert approval["approval_ref"] == FRESH_APPROVAL
    assert approval["authorization_artifact_package_sha"] == VERIFIED_AUTHORIZATION_SHA
    assert approval["single_use"] is True
    assert approval["reusable"] is False
    assert approval["status"] in {"GRANTED_NOT_YET_CONSUMED", "CONSUMED"}

    if approval["status"] == "CONSUMED":
        assert approval.get("execution_run_id")
        assert approval.get("consumed_at_utc")

    if WORKFLOW_PATH.exists():
        assert APPROVAL_PATH.exists()


def test_post_execution_archive_evidence_is_bounded_when_present() -> None:
    if not ARCHIVE_METADATA_PATH.exists():
        return

    assert APPROVAL_PATH.exists()
    approval = _load(APPROVAL_PATH)
    evidence = _load(ARCHIVE_METADATA_PATH)

    assert approval["status"] == "CONSUMED"
    assert evidence["approval_ref"] == FRESH_APPROVAL
    assert evidence["authorization_artifact_package_sha"] == VERIFIED_AUTHORIZATION_SHA
    assert evidence["requested_url"] == (
        "https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf"
    )
    assert evidence["final_url"] == evidence["requested_url"]
    assert evidence["retrieval_method"] == "GET"
    assert evidence["redirect_count"] == 0
    assert evidence["http_status"] == 200
    assert evidence["content_type"] == "application/pdf"
    assert 0 < int(evidence["response_body_bytes"]) <= 16777216
    assert len(str(evidence["sha256"])) == 64
    assert evidence["semantic_extraction_performed"] is False
    assert evidence["post_archive_human_review_required"] is True

    archive_path = ROOT / str(evidence["archive_path"])
    assert archive_path.exists()


def test_fresh_approval_is_distinct_from_consumed_execution_approvals() -> None:
    artifact = _load(ARTIFACT_PATH)
    assert artifact["required_approval_ref"] == FRESH_APPROVAL
    assert artifact["required_approval_ref"] != OLD_EXECUTION_APPROVAL
    assert artifact["required_approval_ref"] != OLD_PRIVACY_APPROVAL
    assert artifact["consumed_prior_approvals_reusable"] is False


def test_execution_boundary_matches_reviewed_authority_proposal() -> None:
    artifact = _load(ARTIFACT_PATH)
    proposal = _load(PROPOSAL_PATH)
    target = proposal["authority_targets"][0]
    boundary = proposal["network_boundary"]
    assert isinstance(target, dict)
    assert isinstance(boundary, dict)

    assert artifact["proposal_package_sha"] == (
        "963c205b662cf56260ca7af14d71c65a6916c30f"
    )
    assert artifact["authority_url"] == target["canonical_url"]
    assert artifact["exact_host"] == target["host"]
    assert artifact["method"] == target["retrieval_method"]
    assert artifact["requests_max_total"] == boundary["requests_max_total"] == 1
    assert artifact["retries_max"] == boundary["retries_max"] == 0
    assert artifact["redirects_allowed"] == boundary["redirects_allowed"] is False
    assert artifact["response_body_bytes_max"] == boundary["response_body_bytes_max"]
    assert artifact["pdf_magic_required"] is True


def test_archive_and_semantic_boundaries_match_reviewed_proposal() -> None:
    artifact = _load(ARTIFACT_PATH)
    proposal = _load(PROPOSAL_PATH)
    archive = proposal["archival_contract"]
    semantic = proposal["semantic_boundary"]
    assert isinstance(archive, dict)
    assert isinstance(semantic, dict)

    assert artifact["archive_path_template"] == archive["archive_path_template"]
    assert artifact["metadata_path"] == archive["metadata_path"]
    assert artifact["hash_algorithm"] == archive["hash_algorithm"] == "SHA-256"
    assert artifact["semantic_extraction_allowed"] is False
    assert archive["semantic_extraction_during_retrieval_allowed"] is False
    assert artifact["post_archive_human_review_required"] is True
    assert semantic["claims_require_post_archive_human_review"] is True


def test_downstream_gates_remain_closed() -> None:
    artifact = _load(ARTIFACT_PATH)
    policy = _load(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))

    assert artifact["downstream_gates_remain_closed"] is True
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    source = next(
        item for item in registry["sources"] if item["source_id"] == SOURCE_ID
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False


def test_schema_blocks_silent_authorization_or_scope_widening() -> None:
    artifact = _load(ARTIFACT_PATH)
    validator = _validator()

    authorized = copy.deepcopy(artifact)
    authorized["network_execution_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(authorized)

    reusable = copy.deepcopy(artifact)
    reusable["reusable"] = True
    with pytest.raises(ValidationError):
        validator.validate(reusable)

    widened = copy.deepcopy(artifact)
    widened["requests_max_total"] = 2
    with pytest.raises(ValidationError):
        validator.validate(widened)

    retry = copy.deepcopy(artifact)
    retry["retries_max"] = 1
    with pytest.raises(ValidationError):
        validator.validate(retry)

    redirect = copy.deepcopy(artifact)
    redirect["redirects_allowed"] = True
    with pytest.raises(ValidationError):
        validator.validate(redirect)

    semantic = copy.deepcopy(artifact)
    semantic["semantic_extraction_allowed"] = True
    with pytest.raises(ValidationError):
        validator.validate(semantic)

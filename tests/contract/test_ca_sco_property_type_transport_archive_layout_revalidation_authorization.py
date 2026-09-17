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
    / "schemas/common/"
    "property_type_transport_archive_layout_revalidation_authorization.schema.json"
)
AUTH_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation_approval.v1.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"

EXECUTION_REF = (
    "OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_"
    "EXECUTION_BOUNDED_B8F703DB"
)
PRIVACY_REF = (
    "OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB"
)
CONSUMED_EXECUTION_REF = (
    "OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_"
    "REAL_SOURCE_EXECUTION_BOUNDED_A2139884"
)
CONSUMED_PRIVACY_REF = (
    "OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_"
    "TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "ca_sco_property_type_semantic_verification_revalidation_auth",
        RUNNER_PATH,
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_revalidation_authorization_validates_and_is_fresh_single_use() -> None:
    schema = _load(SCHEMA_PATH)
    authorization = _load(AUTH_PATH)

    Draft202012Validator.check_schema(schema)
    Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    ).validate(authorization)

    assert authorization["authorization_status"] == "GRANTED_NOT_CONSUMED"
    assert authorization["fresh"] is True
    assert authorization["single_use"] is True
    assert authorization["reusable"] is False
    assert authorization["execution_approval_ref"] == EXECUTION_REF
    assert authorization["structural_byte_privacy_approval_ref"] == PRIVACY_REF
    assert authorization["execution_approval_ref"] != CONSUMED_EXECUTION_REF
    assert authorization["structural_byte_privacy_approval_ref"] != CONSUMED_PRIVACY_REF
    assert authorization["consumption_trigger"] == "FIRST_AUTHORIZED_CA_SCO_NETWORK_REQUEST"


def test_authorization_is_pinned_to_accepted_review_and_exact_endpoint() -> None:
    authorization = _load(AUTH_PATH)
    base = authorization["authorization_base"]
    review = authorization["accepted_review"]
    proposal = authorization["reviewed_proposal"]
    endpoint = authorization["endpoint_binding"]

    assert isinstance(base, dict)
    assert isinstance(review, dict)
    assert isinstance(proposal, dict)
    assert isinstance(endpoint, dict)

    assert base["branch"] == "m3-unified-mvp1"
    assert base["head_sha"] == "3d4d8a76e47d88eca77ca6d899b85341ba8beaf2"
    assert base["ci_run"] == "35195330933"
    assert base["ci_conclusion"] == "SUCCESS"

    assert review["head_sha"] == "b8f703db18207661cd799b0baf1f0dac1bfdc398"
    assert review["ci_run"] == "35187432747"
    assert proposal["head_sha"] == "359b1c1a86d34edabcd028e5e5fbb6fc3acba781"
    assert proposal["ci_run"] == "35139290645"
    assert proposal["selected_strategy"] == (
        "BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION"
    )

    assert endpoint["endpoint"] == (
        "https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip"
    )
    assert endpoint["https_only"] is True
    assert endpoint["exact_host"] == "claimit.ca.gov"


def test_authorization_matches_frozen_proposal_caps_and_privacy_boundary() -> None:
    authorization = _load(AUTH_PATH)
    proposal = _load(PROPOSAL_PATH)

    caps = authorization["execution_caps"]
    structural = authorization["structural_constraints"]
    privacy = authorization["privacy_controls"]
    design = proposal["proposed_revalidation_design"]
    archive = design["archive_layout_phase"]

    assert isinstance(caps, dict)
    assert isinstance(structural, dict)
    assert isinstance(privacy, dict)
    assert isinstance(design, dict)
    assert isinstance(archive, dict)

    assert caps["head_requests_max"] == design["transport_phase"]["head_requests_max"] == 1
    assert caps["range_requests_max"] == archive["range_requests_max"] == 4
    assert caps["http_requests_max_total"] == 5
    assert caps["range_response_bytes_max_each"] == archive["range_response_bytes_max_each"]
    assert caps["source_response_body_bytes_max_total"] == (
        archive["total_source_response_body_bytes_max"]
    )
    assert caps["full_body_fallback_allowed"] is False
    assert caps["automatic_widening_allowed"] is False
    assert caps["automatic_retry_allowed"] is False

    assert structural["classic_zip_eocd_required"] is True
    assert structural["zip64_supported"] is False
    assert structural["multi_disk_supported"] is False
    assert structural["central_directory_metadata_only"] is True
    assert structural["decompression_allowed"] is False
    assert structural["csv_parsing_allowed"] is False
    assert structural["row_or_field_inspection_allowed"] is False
    assert structural["arithmetic_offset_rebase_allowed"] is False
    assert structural["if_match_required"] is True

    proposal_privacy = proposal["privacy_controls"]
    assert privacy["structural_bytes_memory_only"] == (
        proposal_privacy["structural_bytes_memory_only"]
    )
    assert privacy["retention_days"] == proposal_privacy["retention_days"] == 0
    assert privacy["raw_range_bytes_persisted"] is False
    assert privacy["compressed_payload_parsed_or_decompressed"] is False
    assert privacy["csv_rows_parsed"] is False
    assert privacy["protected_fields_observed"] is False
    assert privacy["noncanonical_member_names_persisted"] is False
    assert privacy["allowed_persisted_derived_fields"] == (
        proposal_privacy["allowed_persisted_derived_fields"]
    )


def test_authorization_gate_performed_no_network_and_adopted_no_baseline() -> None:
    authorization = _load(AUTH_PATH)
    proposal = _load(PROPOSAL_PATH)
    effect = authorization["current_gate_effect"]
    candidate = proposal["baseline_state"]["candidate_replacement_baseline"]

    assert isinstance(effect, dict)
    assert isinstance(candidate, dict)

    assert effect == {
        "network_request_performed": False,
        "head_performed": False,
        "range_get_performed": False,
        "structural_revalidation_performed": False,
        "baseline_candidate_established": False,
        "baseline_adopted": False,
        "runner_modified": False,
        "source_policy_modified": False,
        "registry_modified": False,
    }
    assert candidate["content_length"] is None
    assert candidate["etag"] is None
    assert all(
        item["local_header_offset"] is None
        for item in candidate["canonical_member_offsets"]
    )


def test_authorization_does_not_mutate_runner_or_open_downstream_gates() -> None:
    authorization = _load(AUTH_PATH)
    runner = _load_runner()
    scope = authorization["authorized_scope"]

    assert isinstance(scope, dict)
    assert runner.EXPECTED_LENGTH == 162_416_884
    assert runner.EXPECTED_ETAG == '"b25b315b6cd8007624387c3a00d4b1fe"'
    assert [member.local_header_offset for member in runner.CANONICAL_MEMBERS] == [
        0,
        59_747_797,
        96_862_896,
        134_174_190,
    ]
    assert runner.PROPERTY_TYPE_RE.pattern == r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"

    assert scope["baseline_adoption"] is False
    assert scope["runner_constant_update"] is False
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

    assert authorization["next_gate"] == (
        "EXECUTE_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_"
        "BASELINE_REFRESH_REVALIDATION_ONCE"
    )

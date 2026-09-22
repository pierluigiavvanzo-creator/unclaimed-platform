import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).parents[2]
PROPOSAL_SCHEMA = (
    ROOT
    / "schemas"
    / "common"
    / "source_data_scope_segment_inspection_proposal.schema.json"
)
EXECUTION_SCHEMA = (
    ROOT
    / "schemas"
    / "common"
    / "source_data_scope_inspection_execution.schema.json"
)
PROPOSAL = (
    ROOT
    / "sources"
    / "proposals"
    / "ca_sco_segment_500_plus.data_scope_inspection.v1.json"
)
TRANSPORT_EVIDENCE = (
    ROOT
    / "sources"
    / "evidence"
    / "ca_sco_segment_500_plus.transport_preflight.execution.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _execution_fixture() -> dict[str, object]:
    return {
        "schema_version": "1.0.0",
        "execution_id": "synthetic.contract.fixture",
        "source_id": "ca.sco.unclaimed_property.bulk",
        "source_segment_id": "ca.sco.unclaimed_property.bulk.500_plus",
        "jurisdiction": "CA",
        "execution_approval_ref": "SYNTHETIC_TEST_ONLY",
        "executed_at": "2026-09-14T00:00:00Z",
        "target": {
            "endpoint": (
                "https://claimit.ca.gov/upd-property-records/"
                "04_From_500_To_Beyond.zip"
            ),
            "expected_content_length": 162_416_884,
            "expected_etag": '"b25b315b6cd8007624387c3a00d4b1fe"',
            "expected_media_type": "application/zip",
            "expected_accept_ranges": "bytes",
        },
        "controls": {
            "request_mode": "HTTP_RANGE_GET_ONLY",
            "full_body_request_allowed": False,
            "tail_bytes_max": 131_072,
            "central_directory_bytes_max": 4_194_304,
            "member_response_bytes_max_each": 1_048_576,
            "actual_member_probe_bytes_each": 65_536,
            "uncompressed_header_bytes_max_each": 65_536,
            "range_requests_max": 12,
            "total_response_body_bytes_max": 14_811_136,
            "csv_data_rows_allowed": 0,
            "record_values_persistence_allowed": False,
        },
        "transport_verification": {
            "head_status": 200,
            "content_length": 162_416_884,
            "content_type": "application/zip",
            "accept_ranges": "bytes",
            "etag": '"b25b315b6cd8007624387c3a00d4b1fe"',
            "last_modified": "Wed, 09 Sep 2026 16:32:34 GMT",
        },
        "range_requests": [],
        "archive": {
            "parse_status": "BLOCKED",
            "zip64": False,
            "member_count": None,
            "csv_candidate_count": None,
            "members": [],
        },
        "csv_header_candidates": [],
        "total_response_body_bytes_read": 0,
        "safety_state": {
            "full_archive_downloaded": False,
            "raw_body_persisted": False,
            "temporary_source_files_created": False,
            "csv_data_rows_parsed": 0,
            "record_values_persisted": False,
            "real_pii_processing_authorized": False,
            "identity_resolution_performed": False,
            "beneficiary_matching_performed": False,
            "outreach_performed": False,
            "source_approved": False,
            "source_enabled": False,
        },
        "result_status": "BLOCKED",
        "stop_reason": "SYNTHETIC_TEST_ONLY",
    }


def test_500_plus_data_scope_proposal_is_non_authorizing_and_valid() -> None:
    validator = Draft202012Validator(
        _load(PROPOSAL_SCHEMA),
        format_checker=FormatChecker(),
    )
    payload = _load(PROPOSAL)
    validator.validate(payload)

    assert payload["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    assert payload["network_execution_authorized"] is False
    assert payload["network_request_performed"] is False
    assert payload["body_access_performed"] is False
    assert payload["body_bytes_read"] == 0
    assert payload["inspection_scope"]["csv_data_rows_allowed"] == 0
    assert payload["inspection_scope"]["record_values_allowed"] is False


def test_500_plus_proposal_transport_matches_observed_segment_metadata() -> None:
    payload = _load(PROPOSAL)
    evidence = _load(TRANSPORT_EVIDENCE)
    transport = evidence["transport"]
    controls = payload["transport_controls"]

    assert isinstance(transport, dict)
    assert isinstance(controls, dict)
    assert controls["endpoint"] == transport["final_endpoint"]
    assert controls["expected_content_length"] == transport["content_length"]
    assert controls["expected_etag"] == transport["response_headers"]["etag"]
    assert (
        controls["accept_ranges_required"]
        == transport["response_headers"]["accept-ranges"]
    )
    assert transport["response_body_bytes_read"] == 0


def test_proposal_contract_rejects_network_authorization_claim() -> None:
    validator = Draft202012Validator(
        _load(PROPOSAL_SCHEMA),
        format_checker=FormatChecker(),
    )
    payload = copy.deepcopy(_load(PROPOSAL))
    payload["network_execution_authorized"] = True
    assert list(validator.iter_errors(payload))


def test_execution_contract_accepts_blocked_synthetic_fixture() -> None:
    validator = Draft202012Validator(
        _load(EXECUTION_SCHEMA),
        format_checker=FormatChecker(),
    )
    validator.validate(_execution_fixture())


def test_execution_contract_rejects_record_level_scope_escalation() -> None:
    validator = Draft202012Validator(
        _load(EXECUTION_SCHEMA),
        format_checker=FormatChecker(),
    )
    payload = _execution_fixture()
    payload["safety_state"]["csv_data_rows_parsed"] = 1
    assert list(validator.iter_errors(payload))

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).parents[2]
EVIDENCE = (
    ROOT
    / "sources"
    / "evidence"
    / "ca_sco_segment_500_plus.data_scope.execution.v1.json"
)
SCHEMA = ROOT / "schemas" / "common" / "source_data_scope_inspection_execution.schema.json"
POLICY = (
    ROOT
    / "policies"
    / "states"
    / "CA"
    / "ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY = ROOT / "sources" / "registry.yaml"
WORKFLOW = ROOT / ".github" / "workflows" / "ca-sco-500-plus-data-scope-once.yml"

EXPECTED_LABELS = [
    "PROPERTY_ID",
    "PROPERTY_TYPE",
    "CASH_REPORTED",
    "SHARES_REPORTED",
    "NAME_OF_SECURITIES_REPORTED",
    "NO_OF_OWNERS",
    "OWNER_NAME",
    "OWNER_STREET_1",
    "OWNER_STREET_2",
    "OWNER_STREET_3",
    "OWNER_CITY",
    "OWNER_STATE",
    "OWNER_ZIP",
    "OWNER_COUNTRY_CODE",
    "CURRENT_CASH_BALANCE",
    "NUMBER_OF_PENDING_CLAIMS",
    "NUMBER_OF_PAID_CLAIMS",
    "HOLDER_NAME",
    "HOLDER_STREET_1",
    "HOLDER_STREET_2",
    "HOLDER_STREET_3",
    "HOLDER_CITY",
    "HOLDER_STATE",
    "HOLDER_ZIP",
    "CUSIP",
]
EXPECTED_MEMBERS = [
    "From_500_To_Beyond_1_of_4.csv",
    "From_500_To_Beyond_2_of_4.csv",
    "From_500_To_Beyond_3_of_4.csv",
    "From_500_To_Beyond_4_of_4.csv",
]


def _load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_real_500_plus_structure_evidence_validates() -> None:
    payload = _load_json(EVIDENCE)
    schema = _load_json(SCHEMA)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    validator.validate(payload)

    assert payload["result_status"] == "SUCCEEDED_STRUCTURE_ONLY"
    assert payload["stop_reason"] is None
    assert payload["total_response_body_bytes_read"] == 393_216
    assert len(payload["range_requests"]) == 5
    assert all(item["http_status"] == 206 for item in payload["range_requests"])


def test_real_500_plus_archive_and_headers_are_structure_only() -> None:
    payload = _load_json(EVIDENCE)
    archive = payload["archive"]
    headers = payload["csv_header_candidates"]
    safety = payload["safety_state"]

    assert isinstance(archive, dict)
    assert isinstance(headers, list)
    assert isinstance(safety, dict)
    assert archive["parse_status"] == "PARSED"
    assert archive["zip64"] is False
    assert archive["member_count"] == 4
    assert archive["csv_candidate_count"] == 4
    assert [item["name"] for item in archive["members"]] == EXPECTED_MEMBERS

    assert len(headers) == 4
    for index, header in enumerate(headers):
        assert header["member_name"] == EXPECTED_MEMBERS[index]
        assert header["labels"] == EXPECTED_LABELS
        assert header["column_count"] == 25
        assert header["delimiter"] == ","
        assert header["encoding"] == "utf-8"
        assert header["header_confidence"] == "HIGH_DETERMINISTIC_LABEL_HEURISTIC"
        assert "OWNER_NAME" in header["potential_pii_labels"]
        assert "HOLDER_NAME" in header["potential_pii_labels"]

    assert safety["full_archive_downloaded"] is False
    assert safety["raw_body_persisted"] is False
    assert safety["temporary_source_files_created"] is False
    assert safety["csv_data_rows_parsed"] == 0
    assert safety["record_values_persisted"] is False
    assert safety["real_pii_processing_authorized"] is False
    assert safety["identity_resolution_performed"] is False
    assert safety["beneficiary_matching_performed"] is False
    assert safety["outreach_performed"] is False
    assert safety["source_approved"] is False
    assert safety["source_enabled"] is False


def test_execution_does_not_authorize_source_or_leave_network_workflow() -> None:
    policy = _load_json(POLICY)
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    source = next(
        item
        for item in registry["sources"]
        if item["source_id"] == "ca.sco.unclaimed_property.bulk"
    )

    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["allow_pii"] is False
    assert policy["beneficiary_matching_authorized"] is False
    assert policy["outreach_authorized"] is False
    assert source["enabled"] is False
    assert source["approved_for_use"] is False
    assert not WORKFLOW.exists()

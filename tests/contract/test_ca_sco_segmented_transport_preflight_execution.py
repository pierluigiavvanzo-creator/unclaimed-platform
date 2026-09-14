import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).parents[2]
EVIDENCE_DIR = ROOT / "sources" / "evidence"
SCHEMA = (
    ROOT / "schemas" / "common" / "source_transport_preflight_execution.schema.json"
)
FULL = EVIDENCE_DIR / (
    "ca_sco_unclaimed_property_bulk.transport_preflight.execution.v1.json"
)
WORKFLOW = ROOT / ".github" / "workflows" / "ca-sco-segmented-head-preflight-once.yml"
EVIDENCE = {
    "Properties reported at $.00 to $9.99": (
        EVIDENCE_DIR / "ca_sco_segment_00_to_9_99.transport_preflight.execution.v1.json",
        "https://claimit.ca.gov/upd-property-records/01_From_0_To_Below_10.zip",
        1_321_027_390,
    ),
    "Properties reported at $10 to $99.99": (
        EVIDENCE_DIR / "ca_sco_segment_10_to_99_99.transport_preflight.execution.v1.json",
        "https://claimit.ca.gov/upd-property-records/02_From_10_To_Below_100.zip",
        1_261_492_445,
    ),
    "Properties reported at $100 to $499.99": (
        EVIDENCE_DIR / "ca_sco_segment_100_to_499_99.transport_preflight.execution.v1.json",
        "https://claimit.ca.gov/upd-property-records/03_From_100_To_Below_500.zip",
        459_105_796,
    ),
    "Properties reported at $500 and up": (
        EVIDENCE_DIR / "ca_sco_segment_500_plus.transport_preflight.execution.v1.json",
        "https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip",
        162_416_884,
    ),
}


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_segmented_head_evidence_validates_and_reads_zero_body() -> None:
    validator = Draft202012Validator(_load(SCHEMA), format_checker=FormatChecker())
    for label, (path, endpoint, content_length) in EVIDENCE.items():
        payload = _load(path)
        validator.validate(payload)
        assert payload["target_link_label"] == label
        assert payload["result_status"] == "SUCCEEDED"
        transport = payload["transport"]
        safety = payload["safety_state"]
        assert isinstance(transport, dict)
        assert isinstance(safety, dict)
        assert transport["final_endpoint"] == endpoint
        assert transport["http_status"] == 200
        assert transport["content_type"] == "application/zip"
        assert transport["content_length"] == content_length
        assert transport["response_headers"]["accept-ranges"] == "bytes"
        assert transport["response_body_bytes_read"] == 0
        assert payload["controls"]["response_body_bytes_allowed"] == 0
        assert safety["acquisition_performed"] is False
        assert safety["source_approved"] is False
        assert safety["source_enabled"] is False
        assert safety["real_pii_processed"] is False
        assert safety["beneficiary_matching_performed"] is False
        assert safety["outreach_performed"] is False


def test_500_plus_is_smallest_observed_segment_and_far_below_full_archive() -> None:
    sizes = {label: expected[2] for label, expected in EVIDENCE.items()}
    assert min(sizes, key=sizes.get) == "Properties reported at $500 and up"
    full = _load(FULL)
    full_transport = full["transport"]
    assert isinstance(full_transport, dict)
    full_size = full_transport["content_length"]
    assert isinstance(full_size, int)
    assert sizes["Properties reported at $500 and up"] * 10 < full_size


def test_segmented_one_shot_workflow_removed_after_observation() -> None:
    assert not WORKFLOW.exists()

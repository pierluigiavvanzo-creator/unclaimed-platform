from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_PATH = ROOT / ".github/workflows/ca-sco-transport-archive-layout-revalidation-once.yml"
TRIGGER_PATH = ROOT / ".github/ca-sco-transport-archive-layout-revalidation-once.trigger.json"
AUTH_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation_approval.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_transport_archive_layout_revalidation.py"
EXECUTION_REF = (
    "OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_"
    "EXECUTION_BOUNDED_B8F703DB"
)
PRIVACY_REF = (
    "OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_"
    "BOUNDED_B8F703DB"
)
AUTHORIZATION_HEAD = "4079fb44b36699e9b05821761c222d063a89648d"
ACCEPTED_REVIEW_HEAD = "b8f703db18207661cd799b0baf1f0dac1bfdc398"
REVIEWED_PROPOSAL_HEAD = "359b1c1a86d34edabcd028e5e5fbb6fc3acba781"


def _load_runner():
    spec = importlib.util.spec_from_file_location("ca_sco_structural_execution_stage", RUNNER_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_execution_stage_is_exactly_bounded_and_preflight_gated() -> None:
    assert WORKFLOW_PATH.exists()
    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    for expected in (
        "m3-ca-sco-transport-archive-layout-revalidation-once",
        EXECUTION_REF,
        PRIVACY_REF,
        "GITHUB_RUN_ATTEMPT",
        "automatic/manual retry is not authorized",
        "if: steps.gate.outputs.execute == 'true'",
        "retention-days: 7",
        "MAX_RANGE_RESPONSE_BYTES == 131072",
        "MAX_TOTAL_SOURCE_BODY_BYTES == 524288",
    ):
        assert expected in text
    assert "workflow_dispatch" not in text


def test_execution_stage_uses_fresh_authorization_and_frozen_caps() -> None:
    authorization = json.loads(AUTH_PATH.read_text(encoding="utf-8"))
    assert authorization["authorization_status"] == "GRANTED_NOT_CONSUMED"
    assert authorization["execution_approval_ref"] == EXECUTION_REF
    assert authorization["structural_byte_privacy_approval_ref"] == PRIVACY_REF
    assert authorization["single_use"] is True
    assert authorization["reusable"] is False
    assert authorization["accepted_review"]["head_sha"] == ACCEPTED_REVIEW_HEAD
    assert authorization["reviewed_proposal"]["head_sha"] == REVIEWED_PROPOSAL_HEAD
    assert authorization["execution_caps"] == {
        "head_requests_max": 1,
        "range_requests_max": 4,
        "http_requests_max_total": 5,
        "range_response_bytes_max_each": 131072,
        "source_response_body_bytes_max_total": 524288,
        "full_body_fallback_allowed": False,
        "automatic_widening_allowed": False,
        "automatic_retry_allowed": False,
    }


def test_structural_runner_matches_authorized_non_payload_boundary() -> None:
    runner = _load_runner()
    assert runner.ENDPOINT == (
        "https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip"
    )
    assert runner.HOST == "claimit.ca.gov"
    assert runner.MAX_HEAD_REQUESTS == 1
    assert runner.MAX_RANGE_REQUESTS == 4
    assert runner.MAX_HTTP_REQUESTS == 5
    assert runner.MAX_RANGE_RESPONSE_BYTES == 131072
    assert runner.MAX_TOTAL_SOURCE_BODY_BYTES == 524288
    assert runner.EXECUTION_APPROVAL_REF == EXECUTION_REF
    assert runner.STRUCTURAL_BYTE_PRIVACY_APPROVAL_REF == PRIVACY_REF
    source = RUNNER_PATH.read_text(encoding="utf-8")
    assert "import zlib" not in source
    assert "import csv" not in source
    assert "import zipfile" not in source


def test_optional_trigger_is_pinned_if_present() -> None:
    if not TRIGGER_PATH.exists():
        return
    marker = json.loads(TRIGGER_PATH.read_text(encoding="utf-8"))
    assert marker["authorization_checkpoint_sha"] == AUTHORIZATION_HEAD
    assert marker["execution_approval_ref"] == EXECUTION_REF
    assert marker["structural_byte_privacy_approval_ref"] == PRIVACY_REF
    assert marker["accepted_review_sha"] == ACCEPTED_REVIEW_HEAD
    assert marker["reviewed_proposal_sha"] == REVIEWED_PROPOSAL_HEAD
    assert marker["single_use"] is True
    assert isinstance(marker["implementation_checkpoint_sha"], str)
    assert len(marker["implementation_checkpoint_sha"]) == 40

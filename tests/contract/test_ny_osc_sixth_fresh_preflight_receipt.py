from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = (
    ROOT / "schemas/common/ny_osc_sixth_fresh_listing_preflight_receipt.schema.json"
)
RECEIPT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_fresh_listing_preflight_receipt.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _not_performed_receipt() -> dict[str, object]:
    receipt = deepcopy(_load(RECEIPT))
    receipt.update(
        {
            "runner_checkpoint": None,
            "status": "NOT_PERFORMED",
            "remote_preflight_performed": False,
            "preflight_authorization_ref": None,
            "performed_at_utc": None,
            "observed_listing": {
                "remote_name": None,
                "size_display": None,
                "last_modified_display": None,
            },
        }
    )
    return receipt


def _exact_match_receipt() -> dict[str, object]:
    receipt = _not_performed_receipt()
    receipt.update(
        {
            "runner_checkpoint": "a" * 40,
            "status": "EXACT_MATCH",
            "remote_preflight_performed": True,
            "preflight_authorization_ref": "SIXTH_FRESH_PREFLIGHT_APPROVAL_REF",
            "performed_at_utc": "2026-09-20T19:30:00Z",
            "observed_listing": {
                "remote_name": "FINDERS.zip",
                "size_display": "390.51 MB",
                "last_modified_display": "9/16/2026, 1:33:31 PM",
            },
        }
    )
    return receipt


def test_current_sixth_preflight_receipt_validates_against_contract() -> None:
    Draft202012Validator(_load(SCHEMA)).validate(_load(RECEIPT))


def test_not_performed_fixture_is_fail_closed_and_non_pii() -> None:
    receipt = _not_performed_receipt()
    Draft202012Validator(_load(SCHEMA)).validate(receipt)

    assert receipt["status"] == "NOT_PERFORMED"
    assert receipt["remote_preflight_performed"] is False
    assert receipt["download_performed"] is False
    assert receipt["owner_file_opened"] is False
    assert receipt["owner_pii_processed"] is False
    assert receipt["contains_owner_pii"] is False


def test_exact_match_preflight_receipt_validates() -> None:
    Draft202012Validator(_load(SCHEMA)).validate(_exact_match_receipt())


def test_exact_match_rejects_any_listing_drift() -> None:
    receipt = _exact_match_receipt()
    receipt["observed_listing"]["size_display"] = "390.52 MB"

    with pytest.raises(ValidationError):
        Draft202012Validator(_load(SCHEMA)).validate(receipt)


def test_drifted_preflight_receipt_requires_real_difference() -> None:
    receipt = _exact_match_receipt()
    receipt["status"] = "DRIFTED"
    receipt["observed_listing"]["last_modified_display"] = "9/20/2026, 7:30:00 PM"
    Draft202012Validator(_load(SCHEMA)).validate(receipt)

    receipt["observed_listing"] = {
        "remote_name": "FINDERS.zip",
        "size_display": "390.51 MB",
        "last_modified_display": "9/16/2026, 1:33:31 PM",
    }
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(SCHEMA)).validate(receipt)


def test_exact_match_requires_git_runner_checkpoint_and_authorization_ref() -> None:
    receipt = _exact_match_receipt()
    receipt["runner_checkpoint"] = "not-a-git-sha"
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(SCHEMA)).validate(receipt)

    receipt = _exact_match_receipt()
    receipt["preflight_authorization_ref"] = ""
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(SCHEMA)).validate(receipt)


def test_current_sixth_preflight_is_exact_match_non_pii() -> None:
    receipt = _load(RECEIPT)
    assert receipt["status"] == "EXACT_MATCH"
    assert receipt["remote_preflight_performed"] is True
    assert receipt["download_performed"] is False
    assert receipt["owner_file_opened"] is False
    assert receipt["owner_pii_processed"] is False
    assert receipt["contains_owner_pii"] is False

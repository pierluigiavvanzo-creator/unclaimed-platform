import json
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError
import pytest

from unclaimed_platform.domain.mvp1_vertical_slice import synthetic_ny_mvp1_case_review

_REPO_ROOT = Path(__file__).resolve().parents[2]
_SCHEMA_PATH = _REPO_ROOT / "schemas" / "ui" / "mvp1_synthetic_case_review.schema.json"


def _validator() -> Draft202012Validator:
    schema = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
    return Draft202012Validator(schema)


def test_synthetic_mvp1_case_review_validates_against_schema() -> None:
    payload = synthetic_ny_mvp1_case_review().model_dump(mode="json")

    _validator().validate(payload)


def test_contract_rejects_real_source_access() -> None:
    payload = synthetic_ny_mvp1_case_review().model_dump(mode="json")
    payload["provenance"]["real_source_accessed"] = True

    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_contract_rejects_invented_amounts() -> None:
    payload = synthetic_ny_mvp1_case_review().model_dump(mode="json")
    payload["economics"]["invented_amounts"] = True

    with pytest.raises(ValidationError):
        _validator().validate(payload)

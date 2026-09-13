import json
from pathlib import Path

from fastapi.testclient import TestClient
from jsonschema import Draft202012Validator, FormatChecker

from unclaimed_platform.api.app import app


def test_m3_operations_console_response_matches_versioned_schema() -> None:
    response = TestClient(app).get("/api/reviewer/m3/operations")
    assert response.status_code == 200

    schema_path = Path(__file__).parents[2] / "schemas" / "ui" / "m3_operations_console.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    validator.validate(response.json())

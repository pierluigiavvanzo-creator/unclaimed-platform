import argparse
import importlib.util
import json
from copy import deepcopy
from pathlib import Path
from types import ModuleType

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).parents[2]
SCHEMA_PATH = ROOT / "schemas" / "common" / "source_transport_preflight_execution.schema.json"
EXAMPLE_PATH = (
    ROOT / "schemas" / "examples" / "ca_sco_transport_preflight_execution.examples.json"
)
SCRIPT_PATH = ROOT / "scripts" / "ca_sco_transport_preflight.py"


def _load_runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location("ca_sco_transport_preflight", SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _args() -> argparse.Namespace:
    return argparse.Namespace(
        approval_ref="OWNER_CHAT_APPROVAL_TEST",
        official_source_page="https://www.sco.ca.gov/upd_download_property_records.html",
        link_label="All properties",
        allow_host=["claimit.ca.gov"],
        timeout_seconds=10,
        max_redirects=3,
        output=Path("unused.json"),
    )


def _validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_execution_schema_and_synthetic_example_are_valid() -> None:
    payload = json.loads(EXAMPLE_PATH.read_text(encoding="utf-8"))[
        "valid_synthetic_observation"
    ]
    _validator().validate(payload)


@pytest.mark.parametrize(
    ("path", "unsafe_value"),
    [
        (("controls", "request_method"), "GET"),
        (("controls", "response_body_bytes_allowed"), 1),
        (("controls", "persist_response_body"), True),
        (("controls", "pii_processing_allowed"), True),
        (("controls", "beneficiary_matching_allowed"), True),
        (("controls", "outreach_allowed"), True),
        (("transport", "response_body_bytes_read"), 1),
        (("safety_state", "acquisition_performed"), True),
        (("safety_state", "source_approved"), True),
        (("safety_state", "source_enabled"), True),
        (("safety_state", "real_pii_processed"), True),
        (("safety_state", "beneficiary_matching_performed"), True),
        (("safety_state", "outreach_performed"), True),
    ],
)
def test_execution_schema_rejects_unsafe_state(
    path: tuple[str, str],
    unsafe_value: object,
) -> None:
    payload = json.loads(EXAMPLE_PATH.read_text(encoding="utf-8"))[
        "valid_synthetic_observation"
    ]
    mutated = deepcopy(payload)
    mutated[path[0]][path[1]] = unsafe_value
    with pytest.raises(ValidationError):
        _validator().validate(mutated)


def test_runner_completes_metadata_only_head_without_body(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    runner = _load_runner()
    endpoint = "https://claimit.ca.gov/example/all.csv"
    monkeypatch.setattr(
        runner,
        "discover_endpoint",
        lambda *_args, **_kwargs: (endpoint, "claimit.ca.gov"),
    )
    monkeypatch.setattr(
        runner,
        "_head_once",
        lambda *_args, **_kwargs: (
            200,
            {"content-type": "text/csv", "content-length": "321"},
        ),
    )

    result = runner.execute(_args())

    assert result["result_status"] == "SUCCEEDED"
    assert result["controls"]["request_method"] == "HEAD"
    assert result["controls"]["response_body_bytes_allowed"] == 0
    assert result["transport"]["response_body_bytes_read"] == 0
    assert result["transport"]["download_endpoint_request_performed"] is True
    assert result["transport"]["content_length"] == 321
    assert result["safety_state"]["acquisition_performed"] is False
    _validator().validate(result)


def test_runner_blocks_redirect_to_non_allowlisted_host_without_following(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    runner = _load_runner()
    endpoint = "https://claimit.ca.gov/example/all.csv"
    calls: list[str] = []

    monkeypatch.setattr(
        runner,
        "discover_endpoint",
        lambda *_args, **_kwargs: (endpoint, "claimit.ca.gov"),
    )

    def fake_head(
        url: str,
        *_args: object,
        **_kwargs: object,
    ) -> tuple[int, dict[str, str]]:
        calls.append(url)
        return 302, {"location": "https://outside.example/file.csv"}

    monkeypatch.setattr(runner, "_head_once", fake_head)
    result = runner.execute(_args())

    assert result["result_status"] == "BLOCKED_REDIRECT_HOST"
    assert calls == [endpoint]
    assert result["transport"]["response_body_bytes_read"] == 0
    assert result["safety_state"]["acquisition_performed"] is False
    _validator().validate(result)


def test_runner_fails_closed_before_head_when_endpoint_discovery_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    runner = _load_runner()
    head_called = False

    def fail_discovery(*_args: object, **_kwargs: object) -> tuple[str, str]:
        raise RuntimeError("missing target anchor")

    def fake_head(
        *_args: object,
        **_kwargs: object,
    ) -> tuple[int, dict[str, str]]:
        nonlocal head_called
        head_called = True
        return 200, {}

    monkeypatch.setattr(runner, "discover_endpoint", fail_discovery)
    monkeypatch.setattr(runner, "_head_once", fake_head)
    result = runner.execute(_args())

    assert result["result_status"] == "FAILED_ENDPOINT_DISCOVERY"
    assert result["transport"]["download_endpoint_request_performed"] is False
    assert head_called is False
    assert result["transport"]["response_body_bytes_read"] == 0

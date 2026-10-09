from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "scripts/ny_osc_gate4_transient_local.ps1"


def test_fourth_runner_is_offline_prepared_and_fail_closed() -> None:
    text = RUNNER.read_text(encoding="utf-8")

    assert "--expected-attempt-number 4" in text
    assert "APPROVO NY OSC FOURTH TRANSIENT LOCAL FILE BOUNDED ONCE" in text
    assert (
        "APPROVO NY OSC OWNER NAME FILE FOURTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
        in text
    )
    assert "GRANTED_NOT_CONSUMED" in text
    assert "runner_ci_conclusion" in text
    assert "SUCCESS" in text
    assert "downloads_max -ne 1" in text
    assert "retries_max -ne 0" in text
    assert "parser_chunk_bytes -ne 65536" in text
    assert "Remove-Item -LiteralPath $TempDir -Recurse -Force" in text

    first_status_check = text.index('status -ne "GRANTED_NOT_CONSUMED"')
    temp_creation = text.index("New-Item -ItemType Directory")
    assert first_status_check < temp_creation


def test_fourth_runner_contains_no_network_client() -> None:
    text = RUNNER.read_text(encoding="utf-8").lower()
    forbidden = (
        "invoke-webrequest",
        "invoke-restmethod",
        "start-bitstransfer",
        "curl.exe",
        "wget.exe",
    )
    for token in forbidden:
        assert token not in text

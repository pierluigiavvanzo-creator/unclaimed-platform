from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "scripts/ny_osc_gate5_transient_local.ps1"


def test_fifth_runner_is_offline_prepared_and_fail_closed() -> None:
    text = RUNNER.read_text(encoding="utf-8")

    assert "--expected-attempt-number 5" in text
    assert "APPROVO NY OSC FIFTH TRANSIENT LOCAL FILE BOUNDED ONCE" in text
    assert "APPROVO NY OSC OWNER NAME FILE FIFTH BOUNDED TRANSIENT PII ATTEMPT ONCE" in text
    assert "8ce856ddbeac5d2300f808729a887803e212b240" in text
    assert "35460348569" in text
    assert "GRANTED_NOT_CONSUMED" in text
    assert "runner_ci_conclusion" in text
    assert "SUCCESS" in text
    assert "downloads_max -ne 1" in text
    assert "retries_max -ne 0" in text
    assert 'expected_delimiter -ne "|"' in text
    assert "parser_chunk_bytes -ne 65536" in text
    assert 'required_execution_result_contract_version -ne "1.1.0"' in text
    assert 'required_structural_diagnostic_contract_version -ne "1.0.0"' in text
    assert "structural_diagnostic_persistence_allowed -ne $true" in text
    assert "Remove-Item -LiteralPath $TempDir -Recurse -Force" in text

    first_status_check = text.index('status -ne "GRANTED_NOT_CONSUMED"')
    temp_creation = text.index("New-Item -ItemType Directory")
    assert first_status_check < temp_creation

    proposal_check = text.index("proposal_checkpoint -ne $ExpectedProposalCheckpoint")
    runner_ci_check = text.index('runner_ci_conclusion -ne "SUCCESS"')
    bounds_check = text.index("downloads_max -ne 1")
    privacy_check = text.index(
        "processing_scope.transient_owner_pii_in_memory_allowed -ne $true"
    )
    assert proposal_check < temp_creation
    assert runner_ci_check < temp_creation
    assert bounds_check < temp_creation
    assert privacy_check < temp_creation


def test_fifth_runner_contains_no_network_client() -> None:
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

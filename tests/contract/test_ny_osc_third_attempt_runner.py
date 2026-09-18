from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/ny_osc_gate3_transient_local.ps1"


def test_third_runner_checks_every_gate_before_local_preparation() -> None:
    text = SCRIPT.read_text(encoding="utf-8")

    checks = [
        text.index('$LocalApprovalRecord.status -ne "GRANTED_NOT_CONSUMED"'),
        text.index('$Gate2ApprovalRecord.status -ne "GRANTED_NOT_CONSUMED"'),
        text.index("$LocalApprovalRecord.attempt_number -ne 3"),
        text.index("$LocalApprovalRecord.owner_authorization"),
        text.index("$Gate2ApprovalRecord.owner_authorization"),
        text.index('$LocalApprovalRecord.runner_ci_conclusion -ne "SUCCESS"'),
        text.index('$Gate2ApprovalRecord.runner_ci_conclusion -ne "SUCCESS"'),
    ]
    temp_creation = text.index("New-Item -ItemType Directory")
    download_prompt = text.index('Read-Host "Press Enter')

    assert all(check < temp_creation < download_prompt for check in checks)


def test_third_runner_is_attempt_specific_and_has_no_network_client() -> None:
    text = SCRIPT.read_text(encoding="utf-8")
    lowered = text.lower()

    assert "third_attempt_transient_local_approval" in text
    assert "third_attempt_transient_pii_approval" in text
    assert "--expected-attempt-number 3" in text
    assert "second_attempt_transient" not in text

    forbidden_network_commands = (
        "invoke-webrequest",
        "invoke-restmethod",
        "start-bitstransfer",
        "curl.exe",
        "wget.exe",
    )
    assert all(command not in lowered for command in forbidden_network_commands)

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/ny_osc_gate2_retry_transient_local.ps1"


def test_retry_script_checks_consumption_before_creating_download_directory() -> None:
    text = SCRIPT.read_text(encoding="utf-8")

    local_check = text.index('$LocalApprovalRecord.status -ne "GRANTED_NOT_CONSUMED"')
    pii_check = text.index('$Gate2ApprovalRecord.status -ne "GRANTED_NOT_CONSUMED"')
    temp_creation = text.index("New-Item -ItemType Directory")
    download_prompt = text.index('Read-Host "Press Enter')

    assert local_check < temp_creation < download_prompt
    assert pii_check < temp_creation < download_prompt

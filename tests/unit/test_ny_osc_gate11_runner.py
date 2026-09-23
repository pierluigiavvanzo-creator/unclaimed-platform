from pathlib import Path


def test_gate11_runner_uses_automatic_download_start_detection() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    runner = repo_root / "scripts" / "ny_osc_gate11_transient_local.ps1"
    source = runner.read_text(encoding="utf-8")

    assert "$ExpectedAttemptNumber = 11" in source
    assert "ONE_BOUND_GATE11_EXECUTION" in source
    assert "ny_osc_gate11_execute.py" in source
    assert "$MinimumFreshnessRemainingSeconds = 180" in source
    assert "$DownloadStartPollMilliseconds = 100" in source
    assert "Gate 11 automatic download-start detector is ARMED." in source
    assert "Get-ChildItem -LiteralPath $TempDir -File -Force" in source
    assert "$_.Length -gt 0" in source
    assert "Start-Sleep -Milliseconds $DownloadStartPollMilliseconds" in source
    assert (
        "$AuthorizedDownloadStartedAtUtc = "
        '$Now.ToUniversalTime().ToString("o")'
    ) in source
    assert "Do not press Enter when the transfer starts" in source
    assert "As soon as the browser shows that the transfer HAS STARTED" not in source
    assert source.count("Read-Host") == 1
    assert "Press Enter only after that same single download finishes" in source


def test_gate11_runner_stops_before_prompt_when_freshness_margin_is_too_small() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    source = (
        repo_root / "scripts" / "ny_osc_gate11_transient_local.ps1"
    ).read_text(encoding="utf-8")

    margin_check = (
        "if ($RemainingSeconds -lt $MinimumFreshnessRemainingSeconds)"
    )
    prompt = "Gate 11 automatic download-start detector is ARMED."
    assert margin_check in source
    assert source.index(margin_check) < source.index(prompt)
    assert "did not detect download start inside the fresh preflight window" in source


def test_gate11_runner_has_no_direct_network_client() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    source = (
        repo_root / "scripts" / "ny_osc_gate11_transient_local.ps1"
    ).read_text(encoding="utf-8").lower()

    assert "invoke-webrequest" not in source
    assert "invoke-restmethod" not in source
    assert "start-bitstransfer" not in source
    assert "curl " not in source
    assert "wget " not in source


def test_gate11_runner_is_bound_to_refreshed_listing_metadata() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    source = (
        repo_root / "scripts" / "ny_osc_gate11_transient_local.ps1"
    ).read_text(encoding="utf-8")

    assert source.count("9/23/2026, 1:12:44 PM") == 2
    assert "9/16/2026, 1:33:31 PM" not in source

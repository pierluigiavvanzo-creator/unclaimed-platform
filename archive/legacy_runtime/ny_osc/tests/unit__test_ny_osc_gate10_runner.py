from pathlib import Path


def test_gate10_runner_is_product_slice_bound_and_download_start_freshness_bound() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    runner = repo_root / "scripts" / "ny_osc_gate10_transient_local.ps1"
    source = runner.read_text(encoding="utf-8")

    assert "$ExpectedAttemptNumber = 10" in source
    assert "ONE_BOUND_GATE10_EXECUTION" in source
    assert "ny_osc_gate10_execute.py" in source
    assert 'As soon as the browser shows that the transfer HAS STARTED, press Enter' in source
    assert '$AuthorizedDownloadStartedAtUtc = [DateTimeOffset]::UtcNow' in source
    assert 'Press Enter only after that same single download finishes' in source
    assert "property_type_code_only_buffering_allowed" in source


def test_gate10_runner_has_no_network_client_or_retry_loop() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    source = (repo_root / "scripts" / "ny_osc_gate10_transient_local.ps1").read_text(
        encoding="utf-8"
    ).lower()

    assert "invoke-webrequest" not in source
    assert "invoke-restmethod" not in source
    assert "start-bitstransfer" not in source
    assert "curl " not in source
    assert "wget " not in source
    assert "while (" not in source

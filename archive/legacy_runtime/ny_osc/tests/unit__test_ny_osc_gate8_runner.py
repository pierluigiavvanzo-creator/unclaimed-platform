from pathlib import Path


def test_gate8_runner_binds_freshness_to_confirmed_download_start() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    runner = repo_root / "scripts" / "ny_osc_gate8_transient_local.ps1"
    source = runner.read_text(encoding="utf-8")

    prompt = 'As soon as the browser shows that the transfer HAS STARTED, press Enter'
    marker = '$AuthorizedDownloadStartedAtUtc = [DateTimeOffset]::UtcNow'
    completion = 'Press Enter only after that same single download finishes'

    assert prompt in source
    assert marker in source
    assert completion in source
    assert source.index(prompt) < source.index(marker) < source.index(completion)
    assert "authorized_download_started_at_utc=sys.argv[7]" in source
    assert "ny_owner_name_transient_local_execution_v1_5" in source
    assert "ONE_BOUND_GATE8_EXECUTION" in source
    assert "$ExpectedAttemptNumber = 8" in source


def test_gate8_runner_has_no_direct_source_network_client_or_retry_loop() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    runner = repo_root / "scripts" / "ny_osc_gate8_transient_local.ps1"
    source = runner.read_text(encoding="utf-8").lower()

    assert "invoke-webrequest" not in source
    assert "invoke-restmethod" not in source
    assert "start-bitstransfer" not in source
    assert "curl " not in source
    assert "wget " not in source
    assert "while (" not in source
    assert "retries_max -ne 0" in source

from unclaimed_platform.adapters.sources.ny_owner_name_runner_registry import (
    CURRENT_P1_POWERSHELL_ENTRYPOINT,
    CURRENT_P1_RUNTIME_MODULE,
    HISTORICAL_RUNNERS,
    historical_runner,
)


def test_historical_runner_lineage_is_complete_and_non_reusable() -> None:
    assert [item.attempt_number for item in HISTORICAL_RUNNERS] == list(range(1, 12))
    assert all(
        item.status == "HISTORICAL_CONSUMED_NON_REUSABLE"
        for item in HISTORICAL_RUNNERS
    )


def test_historical_lookup_is_metadata_only() -> None:
    assert historical_runner(11).runtime_module.endswith(
        "ny_owner_name_transient_local_execution_v1_8"
    )


def test_current_p1_runner_is_single_canonical_active_surface() -> None:
    assert CURRENT_P1_RUNTIME_MODULE.endswith("ny_owner_name_p1_targetability_local")
    assert CURRENT_P1_POWERSHELL_ENTRYPOINT == "scripts/ny_osc_gate.ps1"

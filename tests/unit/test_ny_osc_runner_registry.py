from pathlib import Path

from unclaimed_platform.adapters.sources.ny_owner_name_runner_registry import (
    CURRENT_P1_POWERSHELL_ENTRYPOINT,
    CURRENT_P1_PYTHON_ENTRYPOINT,
    CURRENT_P1_RUNTIME_MODULE,
    HISTORICAL_RUNNERS,
    historical_runner,
)

ROOT = Path(__file__).resolve().parents[2]


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


def test_historical_registry_matches_preserved_entrypoints() -> None:
    for item in HISTORICAL_RUNNERS:
        gate_path = ROOT / item.gate_script
        assert gate_path.is_file()
        gate_text = gate_path.read_text(encoding="utf-8")

        if item.python_entrypoint is None:
            assert item.runtime_module in gate_text
            continue

        python_path = ROOT / item.python_entrypoint
        assert python_path.is_file()
        assert python_path.name in gate_text
        python_text = python_path.read_text(encoding="utf-8")
        assert item.runtime_module in python_text


def test_current_p1_runner_is_single_canonical_active_surface() -> None:
    assert CURRENT_P1_RUNTIME_MODULE.endswith("ny_owner_name_p1_targetability_local")
    assert CURRENT_P1_POWERSHELL_ENTRYPOINT == "scripts/ny_osc_gate.ps1"
    assert (ROOT / CURRENT_P1_POWERSHELL_ENTRYPOINT).is_file()
    assert (ROOT / CURRENT_P1_PYTHON_ENTRYPOINT).is_file()

    gate_text = (ROOT / CURRENT_P1_POWERSHELL_ENTRYPOINT).read_text(encoding="utf-8")
    assert Path(CURRENT_P1_PYTHON_ENTRYPOINT).name in gate_text

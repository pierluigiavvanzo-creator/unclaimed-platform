from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_canonical_ny_osc_gate_entrypoint_targets_current_p1_only() -> None:
    script = (ROOT / "scripts" / "ny_osc_gate.ps1").read_text(encoding="utf-8")
    assert "ny_mvp1_p1_targetability_execute.py" in script
    assert "ny_osc_gate11_execute.py" not in script
    assert "ny_osc_gate10_execute.py" not in script
    assert "ny_osc_gate9_execute.py" not in script
    assert "Historical ny_osc_gate2..11 scripts" in script

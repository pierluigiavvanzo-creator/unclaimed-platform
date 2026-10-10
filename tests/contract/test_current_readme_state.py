from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_readme_reports_current_stage_b_gate_state() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "all seven real-P1 gates: **NOT_GRANTED**" in readme
    assert "real NY OSC preflight: **NOT AUTHORIZED / NOT PERFORMED**" in readme
    assert "HUMAN_NY_OSC_SEVENTH_FRESH_LISTING_PREFLIGHT_AUTHORIZATION" not in readme
    assert "GRANTED_NOT_CONSUMED / SINGLE_USE / NON_REUSABLE" not in readme

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

ACTIVE_AUDITS = {
    ".gitkeep",
    "DECISION_ENGINE_BENCHMARK_AUDIT_V1_OFFLINE.md",
    "ENTITY_RESOLUTION_REUSE_BENCHMARK_V1_OFFLINE.md",
    "MVP1_COMPETITIVE_MOAT_GATE_2026-09-24.md",
    "NY_MVP1_REAL_P1_CONTROLLER_LEGAL_BASIS_TRANSPARENCY_READINESS_REVIEW.md",
    "NY_MVP1_STAGE_B_PILOT_P1_ACCELERATION_REVIEW.md",
    "NY_MVP1_STAGE_B_US_CONTROLLER_L2A_MANUAL_PROVIDER_REVIEW.md",
    "TECHNICAL_PLATFORM_AUDIT_2026-09-25.md",
    "UNCLAIMED_P1_FINAL_READINESS_AUDIT_2026-10-05.md",
    "US_CONTROLLER_PROVIDER_FALLBACK_BENCHMARK_2026-09-25.md",
}


def test_active_audit_directory_contains_only_current_authority() -> None:
    audit_dir = ROOT / "docs" / "audits"
    assert {path.name for path in audit_dir.iterdir() if path.is_file()} == ACTIVE_AUDITS
    assert (ROOT / "docs" / "archive" / "audits").is_dir()


def test_legacy_ny_osc_attempt_runtimes_are_not_active() -> None:
    source_dir = ROOT / "src" / "unclaimed_platform" / "adapters" / "sources"
    assert not list(source_dir.glob("ny_owner_name_transient_local_execution*.py"))
    assert not list((ROOT / "scripts").glob("ny_osc_gate*"))
    assert (ROOT / "archive" / "legacy_runtime" / "ny_osc").is_dir()


def test_current_p1_runtime_is_present() -> None:
    required = [
        ROOT / "src" / "unclaimed_platform" / "adapters" / "sources" / "ny_owner_name_p1_targetability_local.py",
        ROOT / "src" / "unclaimed_platform" / "domain" / "ny_mvp1_p1_authorization.py",
        ROOT / "scripts" / "ny_mvp1_p1_targetability_execute.py",
        ROOT / "scripts" / "ny_mvp1_p1_targetability_local.ps1",
    ]
    assert all(path.is_file() for path in required)


def test_shared_governance_is_v2_2() -> None:
    master = (ROOT / "AGENTS_MASTER.md").read_text(encoding="utf-8")
    assert "**Version:** 2.2" in master
    assert "**Date:** 2026-10-08" in master

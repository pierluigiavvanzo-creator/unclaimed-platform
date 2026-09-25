from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BENCHMARK = ROOT / "benchmarks" / "entity_resolution_v1" / "benchmark.py"
WORKFLOW = ROOT / ".github" / "workflows" / "entity-resolution-reuse-benchmark-v1.yml"


def test_entity_resolution_benchmark_is_synthetic_and_isolated() -> None:
    benchmark = BENCHMARK.read_text(encoding="utf-8")
    workflow = WORKFLOW.read_text(encoding="utf-8")

    assert "ENTITY_RESOLUTION_REUSE_BENCHMARK_V1_OFFLINE" in benchmark
    assert '"synthetic_only": True' in benchmark
    assert '"contains_real_pii": False' in benchmark
    assert '"remote_source_access": False' in benchmark

    assert "splink==4.0.17" in workflow
    assert "dedupe==3.0.3" in workflow
    assert "BTrees==6.4" in workflow
    assert "rapidfuzz==3.14.6" in workflow
    assert "pandas==3.0.6" in workflow

    assert "entity-resolution-reuse-benchmark-v1-offline" in workflow
    assert "branches:" in workflow
    assert "main" not in workflow


def test_entity_resolution_benchmark_does_not_touch_real_source_or_p1_gate() -> None:
    benchmark = BENCHMARK.read_text(encoding="utf-8")

    forbidden = [
        "osc.ny.gov",
        "claimit.ca.gov",
        "OWNER NAME FILE",
        "owner_authorization",
        "execution_approval_ref",
        "REVIEWER_API_BASE_URL",
    ]
    for token in forbidden:
        assert token not in benchmark

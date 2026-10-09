from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STALE_POSIX = "docs" + "/audits/"
STALE_WINDOWS = "docs" + "\\audits\\"

# Hash-bound to the consumed sixth-attempt checkpoint (see test_ny_osc_gate6_runner_static
# PROTECTED_PATHS): their historical docs/audits references must stay byte-identical.
IMMUTABLE_HISTORICAL = {
    Path("sources/proposals/ny_osc_owner_name_file_sixth_bounded_attempt_authorization.v1.json"),
}


def test_historical_audits_live_only_in_docs_archive() -> None:
    old_dir = ROOT / "docs" / "audits"
    assert not old_dir.exists() or not any(old_dir.glob("*.md"))
    archive = ROOT / "docs" / "archive"
    assert archive.is_dir()
    assert any(archive.glob("*.md"))


def test_active_surfaces_do_not_reference_removed_docs_audits_path() -> None:
    roots = (
        ROOT / "src",
        ROOT / "scripts",
        ROOT / "tests",
        ROOT / "sources" / "proposals",
        ROOT / "policies",
    )
    allowed_suffixes = {".py", ".ps1", ".json", ".yaml", ".yml", ".md"}
    stale: list[str] = []

    for base in roots:
        if not base.exists():
            continue
        paths = [base] if base.is_file() else base.rglob("*")
        for path in paths:
            if not path.is_file() or path.suffix.lower() not in allowed_suffixes:
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if path.relative_to(ROOT) in IMMUTABLE_HISTORICAL:
                continue
            if STALE_POSIX in content or STALE_WINDOWS in content:
                stale.append(str(path.relative_to(ROOT)))

    assert stale == []

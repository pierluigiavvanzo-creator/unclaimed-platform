from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

ACTIVE_ROOTS = (
    ROOT / ".github",
    ROOT / "apps",
    ROOT / "scripts",
    ROOT / "src",
    ROOT / "schemas" / "ui",
)
ACTIVE_FILES = (
    ROOT / ".env.example",
    ROOT / "pyproject.toml",
    ROOT / "docker-compose.yml",
)
FORBIDDEN_PATH_NAMES = {
    "vercel.json",
    ".vercel",
    ".vercelignore",
    "now.json",
}
FORBIDDEN_TEXT = "vercel"


def _tracked_runtime_files() -> list[Path]:
    files: list[Path] = []
    for root in ACTIVE_ROOTS:
        if not root.exists():
            continue
        files.extend(path for path in root.rglob("*") if path.is_file())
    files.extend(path for path in ACTIVE_FILES if path.exists())
    return sorted(set(files))


def test_no_active_provider_specific_vercel_paths() -> None:
    offenders = [
        path.relative_to(ROOT).as_posix()
        for path in _tracked_runtime_files()
        if any(part.lower() in FORBIDDEN_PATH_NAMES for part in path.parts)
    ]

    assert offenders == []


def test_no_active_vercel_commands_or_configuration_references() -> None:
    offenders: list[str] = []

    for path in _tracked_runtime_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        if FORBIDDEN_TEXT in text.lower():
            offenders.append(path.relative_to(ROOT).as_posix())

    assert offenders == []

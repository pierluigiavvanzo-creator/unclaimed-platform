from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
APP = ROOT / "apps" / "reviewer-console" / "src" / "app"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_frontend_product_ux_v1_routes_exist() -> None:
    expected = [
        APP / "ux-lab" / "page.tsx",
        APP / "ux-lab" / "concept-a" / "page.tsx",
        APP / "ux-lab" / "concept-b" / "page.tsx",
        APP / "ux-lab" / "concept-c" / "page.tsx",
        APP / "ux-lab" / "components.tsx",
        APP / "ux-lab" / "ux-lab.module.css",
    ]

    for path in expected:
        assert path.exists(), f"missing UX-lab artifact: {path}"


def test_frontend_product_ux_v1_is_explicitly_synthetic_and_non_authorizing() -> None:
    combined = "\n".join(
        _read(path)
        for path in [
            APP / "ux-lab" / "page.tsx",
            APP / "ux-lab" / "concept-a" / "page.tsx",
            APP / "ux-lab" / "concept-b" / "page.tsx",
            APP / "ux-lab" / "concept-c" / "page.tsx",
            APP.parent / "lib" / "ux-lab-data.ts",
        ]
    )

    assert "SYNTHETIC UX DATA" in combined
    assert "NO REAL PII" in combined
    assert "NOT AN AUTHORIZATION SURFACE" in combined
    assert "Future US registry" in combined
    assert "Future Canada registry" in combined
    assert "FUTURE_NOT_SUPPORTED" in combined
    assert "NONE FROM UX LAB" in combined


def test_frontend_product_ux_v1_does_not_add_remote_data_access() -> None:
    routes = [
        APP / "ux-lab" / "page.tsx",
        APP / "ux-lab" / "concept-a" / "page.tsx",
        APP / "ux-lab" / "concept-b" / "page.tsx",
        APP / "ux-lab" / "concept-c" / "page.tsx",
    ]

    for route in routes:
        source = _read(route)
        assert "fetch(" not in source
        assert "axios" not in source
        assert "REVIEWER_API_BASE_URL" not in source


def test_existing_console_links_to_ux_lab_without_replacing_it() -> None:
    home = _read(APP / "page.tsx")

    assert 'href="/ux-lab"' in home
    assert "M3 Operations Console" in home
    assert "getOperationsSnapshot" in home

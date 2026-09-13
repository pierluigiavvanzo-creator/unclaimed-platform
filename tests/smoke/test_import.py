def test_application_imports() -> None:
    from unclaimed_platform.api.app import app

    assert app.title == "Unclaimed Platform"

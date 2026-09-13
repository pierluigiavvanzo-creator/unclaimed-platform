"""Vercel deployment entrypoint for the authoritative FastAPI application.

This module intentionally contains no domain or reviewer logic. It only makes the
repository's ``src`` layout importable when Vercel loads the root ``app.py`` and
then re-exports the existing FastAPI application instance.
"""

import sys
from importlib import import_module
from pathlib import Path

_SRC_DIR = Path(__file__).resolve().parent / "src"
_SRC_PATH = str(_SRC_DIR)
if _SRC_PATH not in sys.path:
    sys.path.insert(0, _SRC_PATH)

app = import_module("unclaimed_platform.api.app").app

__all__ = ["app"]

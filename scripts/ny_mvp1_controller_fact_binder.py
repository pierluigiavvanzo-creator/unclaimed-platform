from __future__ import annotations

import argparse
import json
from pathlib import Path

from unclaimed_platform.domain.ny_mvp1_controller_fact_binder import (
    assess_controller_facts,
    load_controller_facts,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate Stage B controller facts and emit a non-sensitive assessment."
    )
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser


def main() -> int:
    args = _parser().parse_args()
    facts = load_controller_facts(args.input)
    assessment = assess_controller_facts(facts)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(assessment.model_dump(mode="json"), indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

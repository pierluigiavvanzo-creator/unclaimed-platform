"""Canonical NY OSC runner registry.

Historical transient-local runtimes are preserved because their approvals/checkpoints
are historical evidence and must not be rewritten. This registry provides one
canonical lineage map. It grants no authorization. The only current Stage B runtime
is the P1 targetability runner.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

HistoricalStatus = Literal["HISTORICAL_CONSUMED_NON_REUSABLE"]


@dataclass(frozen=True)
class HistoricalRunnerBinding:
    attempt_number: int
    gate_script: str
    runtime_module: str
    status: HistoricalStatus = "HISTORICAL_CONSUMED_NON_REUSABLE"


_BASE_RUNTIME = (
    "unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution"
)

HISTORICAL_RUNNERS: tuple[HistoricalRunnerBinding, ...] = (
    HistoricalRunnerBinding(
        1,
        "scripts/ny_osc_gate2_transient_local.ps1",
        _BASE_RUNTIME,
    ),
    HistoricalRunnerBinding(
        2,
        "scripts/ny_osc_gate2_retry_transient_local.ps1",
        _BASE_RUNTIME,
    ),
    HistoricalRunnerBinding(
        3,
        "scripts/ny_osc_gate3_transient_local.ps1",
        _BASE_RUNTIME,
    ),
    HistoricalRunnerBinding(
        4,
        "scripts/ny_osc_gate4_transient_local.ps1",
        _BASE_RUNTIME,
    ),
    HistoricalRunnerBinding(
        5,
        "scripts/ny_osc_gate5_transient_local.ps1",
        _BASE_RUNTIME,
    ),
    HistoricalRunnerBinding(
        6,
        "scripts/ny_osc_gate6_transient_local.ps1",
        f"{_BASE_RUNTIME}_v1_2",
    ),
    HistoricalRunnerBinding(
        7,
        "scripts/ny_osc_gate7_transient_local.ps1",
        f"{_BASE_RUNTIME}_v1_4",
    ),
    HistoricalRunnerBinding(
        8,
        "scripts/ny_osc_gate8_transient_local.ps1",
        f"{_BASE_RUNTIME}_v1_5",
    ),
    HistoricalRunnerBinding(
        9,
        "scripts/ny_osc_gate9_transient_local.ps1",
        f"{_BASE_RUNTIME}_v1_6",
    ),
    HistoricalRunnerBinding(
        10,
        "scripts/ny_osc_gate10_transient_local.ps1",
        f"{_BASE_RUNTIME}_v1_7",
    ),
    HistoricalRunnerBinding(
        11,
        "scripts/ny_osc_gate11_transient_local.ps1",
        f"{_BASE_RUNTIME}_v1_8",
    ),
)

CURRENT_P1_RUNTIME_MODULE = (
    "unclaimed_platform.adapters.sources.ny_owner_name_p1_targetability_local"
)
CURRENT_P1_PYTHON_ENTRYPOINT = "scripts/ny_mvp1_p1_targetability_execute.py"
CURRENT_P1_POWERSHELL_ENTRYPOINT = "scripts/ny_osc_gate.ps1"


def historical_runner(attempt_number: int) -> HistoricalRunnerBinding:
    """Return immutable lineage metadata; never an execution authorization."""

    for binding in HISTORICAL_RUNNERS:
        if binding.attempt_number == attempt_number:
            return binding
    raise ValueError("historical NY OSC attempt must be between 1 and 11")

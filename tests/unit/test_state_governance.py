from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal
from pathlib import Path
from uuid import UUID

import pytest

from unclaimed_platform.core.audit import AuditEventWriter
from unclaimed_platform.core.budget_engine import BudgetError, BudgetLedger
from unclaimed_platform.core.orchestrator import Orchestrator, TransitionCommand
from unclaimed_platform.core.policy_engine import PolicyEffect, PolicyEngine, PolicyRule
from unclaimed_platform.core.state_machine import (
    InvalidTransitionError,
    StateMachine,
    UnknownStateError,
    WorkflowPolicy,
)

ROOT = Path(__file__).resolve().parents[2]


def load_machine() -> StateMachine:
    policy = WorkflowPolicy.from_json_file(
        ROOT / "policies/workflow/state_transitions.v1.json"
    )
    return StateMachine(policy)


def allow_rules() -> dict[str, PolicyRule]:
    return {
        "case.advance": PolicyRule(
            rule_id="case.advance",
            effect=PolicyEffect.ALLOW,
            reason_code="POLICY_ALLOW",
            reason="Synthetic M2 transition policy allows the requested transition.",
        )
    }


def fixed_clock() -> datetime:
    return datetime(2026, 9, 13, 12, 0, tzinfo=UTC)


def fixed_id() -> UUID:
    return UUID("11111111-1111-4111-8111-111111111111")


def test_workflow_policy_loads_and_declares_terminal_states() -> None:
    machine = load_machine()

    assert machine.policy.schema_version == "1.0.0"
    assert machine.policy.initial_state == "NEW"
    assert machine.policy.terminal_states == frozenset({"STOPPED", "COMPLETED"})


def test_allowed_transition_succeeds() -> None:
    machine = load_machine()

    assert machine.transition("NEW", "PROCESSING") == "PROCESSING"


def test_forbidden_transition_fails_closed() -> None:
    machine = load_machine()

    with pytest.raises(InvalidTransitionError):
        machine.transition("NEW", "COMPLETED")


def test_unknown_state_is_rejected() -> None:
    machine = load_machine()

    with pytest.raises(UnknownStateError):
        machine.transition("NEW", "DOES_NOT_EXIST")


def test_terminal_state_has_no_outbound_transition() -> None:
    machine = load_machine()

    with pytest.raises(InvalidTransitionError):
        machine.transition("COMPLETED", "PROCESSING")


def test_missing_policy_routes_to_human_review_without_budget_consumption() -> None:
    budget = BudgetLedger(Decimal("10"))
    audit = AuditEventWriter(clock=fixed_clock, id_factory=fixed_id)
    orchestrator = Orchestrator(
        state_machine=load_machine(),
        policy_engine=PolicyEngine(),
        budget=budget,
        audit=audit,
    )

    result = orchestrator.execute(
        TransitionCommand(
            case_id="case-1",
            current_state="NEW",
            requested_state="PROCESSING",
            policy_id="missing.rule",
            budget_cost=Decimal("3"),
        )
    )

    assert result.status == "HUMAN_REVIEW"
    assert result.state == "HUMAN_REVIEW"
    assert result.reason_code == "POLICY_NOT_FOUND"
    assert budget.consumed == Decimal("0")
    assert audit.verify_chain()


def test_budget_exhaustion_stops_without_mutating_consumed_amount() -> None:
    budget = BudgetLedger(Decimal("2"))
    audit = AuditEventWriter(clock=fixed_clock, id_factory=fixed_id)
    orchestrator = Orchestrator(
        state_machine=load_machine(),
        policy_engine=PolicyEngine(allow_rules()),
        budget=budget,
        audit=audit,
    )

    result = orchestrator.execute(
        TransitionCommand(
            case_id="case-1",
            current_state="NEW",
            requested_state="PROCESSING",
            policy_id="case.advance",
            budget_cost=Decimal("3"),
        )
    )

    assert result.status == "STOP"
    assert result.state == "NEW"
    assert result.reason_code == "BUDGET_EXHAUSTED"
    assert budget.consumed == Decimal("0")
    assert audit.events[-1].event_type == "TRANSITION_BLOCKED_BUDGET"


def test_successful_orchestration_consumes_budget_and_audits_transition() -> None:
    budget = BudgetLedger(Decimal("10"))
    audit = AuditEventWriter(clock=fixed_clock, id_factory=fixed_id)
    orchestrator = Orchestrator(
        state_machine=load_machine(),
        policy_engine=PolicyEngine(allow_rules()),
        budget=budget,
        audit=audit,
    )

    result = orchestrator.execute(
        TransitionCommand(
            case_id="case-1",
            current_state="NEW",
            requested_state="PROCESSING",
            policy_id="case.advance",
            budget_cost=Decimal("3"),
        )
    )

    assert result.status == "CONTINUE"
    assert result.state == "PROCESSING"
    assert budget.consumed == Decimal("3")
    assert audit.events[-1].event_type == "STATE_TRANSITION"
    assert audit.verify_chain()


def test_invalid_transition_does_not_consume_budget() -> None:
    budget = BudgetLedger(Decimal("10"))
    orchestrator = Orchestrator(
        state_machine=load_machine(),
        policy_engine=PolicyEngine(allow_rules()),
        budget=budget,
        audit=AuditEventWriter(clock=fixed_clock, id_factory=fixed_id),
    )

    with pytest.raises(InvalidTransitionError):
        orchestrator.execute(
            TransitionCommand(
                case_id="case-1",
                current_state="NEW",
                requested_state="COMPLETED",
                policy_id="case.advance",
                budget_cost=Decimal("3"),
            )
        )

    assert budget.consumed == Decimal("0")


def test_negative_budget_values_are_rejected() -> None:
    with pytest.raises(BudgetError):
        BudgetLedger(Decimal("-1"))

    ledger = BudgetLedger(Decimal("1"))
    with pytest.raises(BudgetError):
        ledger.reserve(Decimal("-0.01"))


def test_audit_writer_builds_hash_chain() -> None:
    ids = iter(
        [
            UUID("11111111-1111-4111-8111-111111111111"),
            UUID("22222222-2222-4222-8222-222222222222"),
        ]
    )
    writer = AuditEventWriter(clock=fixed_clock, id_factory=lambda: next(ids))

    first = writer.append(
        case_id="case-1",
        event_type="FIRST",
        actor_type="SYSTEM",
        actor_id="test",
        payload={"synthetic": True},
    )
    second = writer.append(
        case_id="case-1",
        event_type="SECOND",
        actor_type="SYSTEM",
        actor_id="test",
        payload={"synthetic": True},
    )

    assert first.previous_event_hash is None
    assert second.previous_event_hash == first.event_hash
    assert writer.verify_chain()

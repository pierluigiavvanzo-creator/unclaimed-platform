from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from unclaimed_platform.core.audit import AuditEventWriter
from unclaimed_platform.core.budget_engine import BudgetLedger
from unclaimed_platform.core.policy_engine import PolicyEffect, PolicyEngine
from unclaimed_platform.core.state_machine import StateMachine


@dataclass(frozen=True)
class TransitionCommand:
    case_id: str
    current_state: str
    requested_state: str
    policy_id: str
    budget_cost: Decimal
    actor_id: str = "A00"


@dataclass(frozen=True)
class OrchestrationResult:
    status: str
    state: str
    reason_code: str
    budget_consumed: Decimal
    audit_event_hash: str | None


class Orchestrator:
    """A00 skeleton: deterministic policy -> state -> budget -> audit orchestration."""

    def __init__(
        self,
        *,
        state_machine: StateMachine,
        policy_engine: PolicyEngine,
        budget: BudgetLedger,
        audit: AuditEventWriter,
    ) -> None:
        self._state_machine = state_machine
        self._policy_engine = policy_engine
        self._budget = budget
        self._audit = audit

    def execute(self, command: TransitionCommand) -> OrchestrationResult:
        policy = self._policy_engine.evaluate(command.policy_id)

        if policy.effect is PolicyEffect.STOP:
            stopped_state = self._state_machine.transition(command.current_state, "STOPPED")
            event = self._audit.append(
                case_id=command.case_id,
                event_type="TRANSITION_BLOCKED_POLICY",
                actor_type="AGENT",
                actor_id=command.actor_id,
                payload={
                    "current_state": command.current_state,
                    "requested_state": command.requested_state,
                    "reason_code": policy.reason_code,
                },
            )
            return OrchestrationResult(
                status="STOP",
                state=stopped_state,
                reason_code=policy.reason_code,
                budget_consumed=self._budget.consumed,
                audit_event_hash=event.event_hash,
            )

        target_state = command.requested_state
        status = "CONTINUE"
        if policy.effect is PolicyEffect.HUMAN_REVIEW:
            target_state = "HUMAN_REVIEW"
            status = "HUMAN_REVIEW"

        self._state_machine.transition(command.current_state, target_state)

        if status == "CONTINUE":
            reservation = self._budget.reserve(command.budget_cost)
            if not reservation.authorized:
                stopped_state = self._state_machine.transition(command.current_state, "STOPPED")
                event = self._audit.append(
                    case_id=command.case_id,
                    event_type="TRANSITION_BLOCKED_BUDGET",
                    actor_type="AGENT",
                    actor_id=command.actor_id,
                    payload={
                        "current_state": command.current_state,
                        "requested_state": command.requested_state,
                        "reason_code": reservation.reason_code,
                    },
                )
                return OrchestrationResult(
                    status="STOP",
                    state=stopped_state,
                    reason_code=reservation.reason_code,
                    budget_consumed=self._budget.consumed,
                    audit_event_hash=event.event_hash,
                )

        event = self._audit.append(
            case_id=command.case_id,
            event_type="STATE_TRANSITION",
            actor_type="AGENT",
            actor_id=command.actor_id,
            payload={
                "from_state": command.current_state,
                "to_state": target_state,
                "reason_code": policy.reason_code,
            },
        )
        return OrchestrationResult(
            status=status,
            state=target_state,
            reason_code=policy.reason_code,
            budget_consumed=self._budget.consumed,
            audit_event_hash=event.event_hash,
        )

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum


class PolicyEffect(StrEnum):
    ALLOW = "ALLOW"
    HUMAN_REVIEW = "HUMAN_REVIEW"
    STOP = "STOP"


@dataclass(frozen=True)
class PolicyRule:
    rule_id: str
    effect: PolicyEffect
    reason_code: str
    reason: str


@dataclass(frozen=True)
class PolicyResult:
    effect: PolicyEffect
    reason_code: str
    reason: str
    rule_id: str | None


class PolicyEngine:
    """Minimal deterministic policy engine with fail-closed missing-rule behavior."""

    def __init__(self, rules: Mapping[str, PolicyRule] | None = None) -> None:
        self._rules = dict(rules or {})

    def evaluate(self, rule_id: str) -> PolicyResult:
        rule = self._rules.get(rule_id)
        if rule is None:
            return PolicyResult(
                effect=PolicyEffect.HUMAN_REVIEW,
                reason_code="POLICY_NOT_FOUND",
                reason=f"No deterministic policy rule exists for {rule_id}",
                rule_id=None,
            )
        return PolicyResult(
            effect=rule.effect,
            reason_code=rule.reason_code,
            reason=rule.reason,
            rule_id=rule.rule_id,
        )

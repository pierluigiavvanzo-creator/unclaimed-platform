from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


class BudgetError(ValueError):
    """Base error for invalid budget operations."""


@dataclass(frozen=True)
class BudgetResult:
    authorized: bool
    reason_code: str
    requested: Decimal
    consumed: Decimal
    remaining: Decimal


class BudgetLedger:
    """Deterministic in-memory budget ledger for M2 governance tests."""

    def __init__(self, limit: Decimal) -> None:
        if limit < 0:
            raise BudgetError("budget limit cannot be negative")
        self._limit = limit
        self._consumed = Decimal("0")

    @property
    def limit(self) -> Decimal:
        return self._limit

    @property
    def consumed(self) -> Decimal:
        return self._consumed

    @property
    def remaining(self) -> Decimal:
        return self._limit - self._consumed

    def reserve(self, amount: Decimal) -> BudgetResult:
        if amount < 0:
            raise BudgetError("budget reservation cannot be negative")

        if self._consumed + amount > self._limit:
            return BudgetResult(
                authorized=False,
                reason_code="BUDGET_EXHAUSTED",
                requested=amount,
                consumed=self._consumed,
                remaining=self.remaining,
            )

        self._consumed += amount
        return BudgetResult(
            authorized=True,
            reason_code="BUDGET_RESERVED",
            requested=amount,
            consumed=self._consumed,
            remaining=self.remaining,
        )

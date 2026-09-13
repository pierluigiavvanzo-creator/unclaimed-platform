from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path


class StateMachineError(ValueError):
    """Base error for deterministic workflow-state failures."""


class UnknownStateError(StateMachineError):
    """Raised when a state is not declared in the active workflow policy."""


class InvalidTransitionError(StateMachineError):
    """Raised when a requested transition is not explicitly whitelisted."""


@dataclass(frozen=True)
class WorkflowPolicy:
    schema_version: str
    initial_state: str
    terminal_states: frozenset[str]
    transitions: Mapping[str, frozenset[str]]

    @classmethod
    def from_mapping(cls, raw: Mapping[str, object]) -> "WorkflowPolicy":
        schema_version = raw.get("schema_version")
        initial_state = raw.get("initial_state")
        terminal_states = raw.get("terminal_states")
        transitions = raw.get("transitions")

        if not isinstance(schema_version, str) or not schema_version:
            raise StateMachineError("workflow policy requires schema_version")
        if not isinstance(initial_state, str) or not initial_state:
            raise StateMachineError("workflow policy requires initial_state")
        if not isinstance(terminal_states, Sequence) or isinstance(terminal_states, str):
            raise StateMachineError("terminal_states must be an array")
        if not isinstance(transitions, Mapping):
            raise StateMachineError("transitions must be an object")

        normalized: dict[str, frozenset[str]] = {}
        for source, targets in transitions.items():
            if not isinstance(source, str):
                raise StateMachineError("state names must be strings")
            if not isinstance(targets, Sequence) or isinstance(targets, str):
                raise StateMachineError(f"targets for {source} must be an array")
            target_names = frozenset(str(target) for target in targets)
            normalized[source] = target_names

        states = frozenset(normalized)
        if initial_state not in states:
            raise StateMachineError("initial_state must be declared in transitions")

        terminal_set = frozenset(str(state) for state in terminal_states)
        unknown_terminals = terminal_set - states
        if unknown_terminals:
            raise StateMachineError(
                f"unknown terminal states: {', '.join(sorted(unknown_terminals))}"
            )

        unknown_targets = {
            target
            for targets in normalized.values()
            for target in targets
            if target not in states
        }
        if unknown_targets:
            raise StateMachineError(
                f"unknown transition targets: {', '.join(sorted(unknown_targets))}"
            )

        non_empty_terminals = [state for state in terminal_set if normalized[state]]
        if non_empty_terminals:
            raise StateMachineError(
                "terminal states cannot have outbound transitions: "
                + ", ".join(sorted(non_empty_terminals))
            )

        return cls(
            schema_version=schema_version,
            initial_state=initial_state,
            terminal_states=terminal_set,
            transitions=normalized,
        )

    @classmethod
    def from_json_file(cls, path: Path) -> "WorkflowPolicy":
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise StateMachineError("workflow policy root must be an object")
        return cls.from_mapping(raw)


class StateMachine:
    def __init__(self, policy: WorkflowPolicy) -> None:
        self._policy = policy

    @property
    def policy(self) -> WorkflowPolicy:
        return self._policy

    def assert_known_state(self, state: str) -> None:
        if state not in self._policy.transitions:
            raise UnknownStateError(f"unknown workflow state: {state}")

    def can_transition(self, current_state: str, target_state: str) -> bool:
        self.assert_known_state(current_state)
        self.assert_known_state(target_state)
        return target_state in self._policy.transitions[current_state]

    def transition(self, current_state: str, target_state: str) -> str:
        if not self.can_transition(current_state, target_state):
            raise InvalidTransitionError(
                f"transition not allowed: {current_state} -> {target_state}"
            )
        return target_state

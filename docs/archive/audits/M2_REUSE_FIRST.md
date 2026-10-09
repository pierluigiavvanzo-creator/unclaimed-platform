# M2 REUSE FIRST — State & Governance Core

Date checked: 2026-09-13

## Scope

Evaluate mature reusable options before implementing the deterministic M2 state machine.
Policy, budget and audit skeletons are small domain-specific governance components and use Python
standard-library primitives rather than adding third-party dependencies.

## Candidate 1 — python-statemachine

```yaml
name: python-statemachine
url: https://github.com/fgmacedo/python-statemachine
pypi: https://pypi.org/project/python-statemachine/
license: MIT
last_activity: active; PyPI 3.2.1 released 2026-08-01
stars_or_adoption_signal: PyPI classifies project Production/Stable
python_compatibility: Python >=3.10 including 3.11
security_notes: no project-specific security review performed; extra dependency not required for M2
fit_for_task: high for general FSM features, but broader than the M2 whitelist requirement
integration_cost: low-to-medium; requires adapting library semantics to versioned fail-closed policy
benchmark_result: feature fit exceeds basic transition need but adds abstraction not required by M2
decision: REJECT
reason: M2 requires a tiny explicit versioned whitelist whose critical behavior must remain visible and directly testable.
```

## Candidate 2 — transitions

```yaml
name: transitions
url: https://github.com/pytransitions/transitions
pypi: https://pypi.org/project/transitions/
license: MIT
last_activity: active repository; open PR activity observed in September 2026
stars_or_adoption_signal: mature long-lived Python FSM project
python_compatibility: Python 3 compatible; current project target remains Python 3.11
security_notes: no project-specific security review performed; dependency is unnecessary for current scope
fit_for_task: high for general state machines, including advanced/hierarchical behaviors not needed in M2
integration_cost: low-to-medium
benchmark_result: capable but materially broader than a five-state deterministic whitelist
decision: INSPIRE
reason: retain explicit whitelist and fail-closed tests now; reconsider if later workflow complexity requires hierarchical/concurrent states.
```

## Decision

Implement the M2 state machine custom using only standard-library data structures. This is not a
preference for custom code in general: it is a bounded exception because the required behavior is
small, product-critical, versioned as data, and easier to audit directly than through a general FSM
framework. Re-evaluate reuse if state complexity materially increases.

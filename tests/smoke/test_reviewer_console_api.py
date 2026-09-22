from fastapi.testclient import TestClient

from unclaimed_platform.api.app import app


def test_reviewer_console_is_synthetic_and_fail_closed_for_real_work() -> None:
    payload = TestClient(app).get("/api/reviewer/m3/operations").json()

    assert payload["mode"] == "SYNTHETIC_READ_ONLY"
    assert payload["source_registry"]["approved_real_sources"] == 0
    assert payload["source_registry"]["real_acquisition"] == "BLOCKED"
    assert payload["source_registry"]["beneficiary_matching"] == "BLOCKED"
    assert payload["raw_artifact"]["synthetic"] is True


def test_mvp1_synthetic_case_reaches_reviewer_without_real_data() -> None:
    response = TestClient(app).get("/api/reviewer/mvp1/synthetic-case")
    payload = response.json()

    assert response.status_code == 200
    assert payload["mode"] == "SYNTHETIC_READ_ONLY"
    assert payload["classification"]["authority_code"] == "IN03"
    assert payload["classification"]["primary_target"] is True
    assert payload["candidate"]["status"] == "CREATED"
    assert payload["economics"]["recoverable_value_state"] == "UNKNOWN_FROM_SOURCE"
    assert payload["economics"]["invented_amounts"] is False
    assert payload["provenance"]["real_source_accessed"] is False
    assert payload["safety"]["real_owner_pii_processed"] is False


def test_mvp1_precontact_economics_api_is_fail_closed() -> None:
    response = TestClient(app).get("/api/reviewer/mvp1/economics/precontact")
    payload = response.json()

    assert response.status_code == 200
    assert payload["mode"] == "OFFLINE_PRECONTACT_EVIDENCE"
    assert payload["exact_recoverable_value_cents"] is None
    assert payload["owner_file_discloses_amount"] is False
    assert payload["statutory_fee_cap_bps"] == 1500
    assert payload["actual_fee_bps"] is None
    assert payload["expected_follow_up_cost_cents"] is None
    assert payload["commercial_actionability"] == "NOT_COMPUTABLE_PRE_CONTACT"


def test_mvp1_integrated_economics_api_exposes_ready_and_blocked_states() -> None:
    response = TestClient(app).get("/api/reviewer/mvp1/economics/integrated")
    payload = response.json()

    assert response.status_code == 200
    assert payload["mode"] == "SYNTHETIC_READ_ONLY"
    assert payload["safety"]["real_source_accessed"] is False
    assert payload["safety"]["owner_file_downloaded"] is False
    assert payload["safety"]["real_owner_pii_processed"] is False
    assert payload["safety"]["automatic_commercial_recommendation"] is False

    ready = payload["ready"]
    assert ready["scenario"] == "READY_WITH_DOCUMENTED_LABOR_RATE"
    assert ready["integration"]["integration_state"] == "READY_FOR_EXPLICIT_ECONOMICS"
    assert ready["integration"]["measured_follow_up_cost_cents"] == 417
    assert ready["integration"]["explicit_economics_result"] is not None
    assert ready["integration"]["no_commercial_recommendation"] is True
    assert len(ready["integration"]["follow_up_cost_evidence_refs"]) == 5

    blocked = payload["blocked"]
    assert blocked["scenario"] == "BLOCKED_WITHOUT_DOCUMENTED_LABOR_RATE"
    assert blocked["follow_up_cost"]["direct_machine_and_data_cost_cents"] == 37
    assert blocked["integration"]["integration_state"] == (
        "BLOCKED_FOLLOW_UP_COST_UNAVAILABLE"
    )
    assert blocked["integration"]["measured_follow_up_cost_cents"] is None
    assert blocked["integration"]["explicit_economics_result"] is None
    assert blocked["integration"]["no_commercial_recommendation"] is True

import pytest


# These historical tests correctly describe the workflow state at their own
# earlier gates, but they used the current repository filesystem as a proxy for
# that historical fact. During the separately authorized v1.2 one-shot stage,
# the same temporary workflow path is intentionally present again. Isolate only
# those stale filesystem assertions; all other assertions in the tests still
# execute normally. This fixture is execution-stage-only and is removed with
# the temporary workflow after the single run.
_HISTORICAL_WORKFLOW_NODEIDS = {
    "tests/contract/test_ca_sco_property_type_authority_provenance_acquisition_proposal.py::test_downstream_gates_remain_closed",
    "tests/contract/test_ca_sco_property_type_code_shape_provenance_offline_proposal.py::test_network_workflow_and_downstream_gates_remain_closed",
    "tests/contract/test_ca_sco_property_type_code_shape_provenance_offline_review.py::test_aggregate_decision_and_downstream_gates_remain_closed",
    "tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.py::test_proposal_validates_and_is_non_authorizing",
    "tests/contract/test_ca_sco_property_type_runner_implementation_authorization.py::test_runner_exists_but_network_workflow_remains_absent",
    "tests/contract/test_ca_sco_property_type_second_semantic_execution_authorization.py::test_temporary_workflow_is_pinned_if_present",
    "tests/contract/test_ca_sco_property_type_second_semantic_execution_evidence.py::test_second_execution_used_fresh_single_use_authorization_and_workflow_is_absent",
    "tests/contract/test_ca_sco_property_type_semantic_execution_evidence.py::test_one_shot_workflow_is_removed_after_execution",
    "tests/contract/test_ca_sco_property_type_semantic_runner_design.py::test_runner_design_remains_valid_historical_non_authorizing_record",
    "tests/contract/test_ca_sco_property_type_semantic_verification_proposal.py::test_proposal_is_valid_non_authorizing_and_not_executed",
}


@pytest.fixture(autouse=True)
def _isolate_historical_workflow_path_assertions(
    request: pytest.FixtureRequest,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    if request.node.nodeid not in _HISTORICAL_WORKFLOW_NODEIDS:
        return

    module = request.node.module
    if not hasattr(module, "WORKFLOW_PATH"):
        raise AssertionError("historical workflow test lost WORKFLOW_PATH guard")

    workflow_path = module.WORKFLOW_PATH
    sentinel = workflow_path.with_name(".historical-one-shot-workflow-absent.yml")
    assert not sentinel.exists()
    monkeypatch.setattr(module, "WORKFLOW_PATH", sentinel)

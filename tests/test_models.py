from pyker.models import ComputationResult


def test_computation_result() -> None:
    model = ComputationResult(key="k1", value="v1")

    assert model.key == "k1"
    assert model.value == "v1"

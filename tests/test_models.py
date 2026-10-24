from pyker.models import ComputationResult, HandCombination


def test_computation_result() -> None:
    model = ComputationResult(key="k1", value="v1")

    assert model.key == "k1"
    assert model.value == "v1"


def test_hand_combination_values_are_stable_and_start_from_one() -> None:
    assert HandCombination.FLUSH_ROYAL.value == 1
    assert HandCombination.STRAIGHT_FLUSH.value == 2
    assert HandCombination.FOUR_OF_A_KIND.value == 3
    assert HandCombination.FULL_HOUSE.value == 4
    assert HandCombination.FLUSH.value == 5
    assert HandCombination.STRAIGHT.value == 6
    assert HandCombination.THREE_OF_A_KIND.value == 7
    assert HandCombination.TWO_PAIR.value == 8
    assert HandCombination.ONE_PAIR.value == 9
    assert HandCombination.HIGH_CARD.value == 10


def test_hand_combination_order_is_lower_equals_stronger() -> None:
    assert HandCombination.FLUSH_ROYAL < HandCombination.STRAIGHT_FLUSH
    assert HandCombination.STRAIGHT_FLUSH < HandCombination.FOUR_OF_A_KIND
    assert HandCombination.FOUR_OF_A_KIND < HandCombination.FULL_HOUSE
    assert HandCombination.FULL_HOUSE < HandCombination.FLUSH
    assert HandCombination.FLUSH < HandCombination.STRAIGHT
    assert HandCombination.STRAIGHT < HandCombination.THREE_OF_A_KIND
    assert HandCombination.THREE_OF_A_KIND < HandCombination.TWO_PAIR
    assert HandCombination.TWO_PAIR < HandCombination.ONE_PAIR
    assert HandCombination.ONE_PAIR < HandCombination.HIGH_CARD


def test_hand_combination_member_names_are_machine_friendly() -> None:
    assert [member.name for member in HandCombination] == [
        "FLUSH_ROYAL",
        "STRAIGHT_FLUSH",
        "FOUR_OF_A_KIND",
        "FULL_HOUSE",
        "FLUSH",
        "STRAIGHT",
        "THREE_OF_A_KIND",
        "TWO_PAIR",
        "ONE_PAIR",
        "HIGH_CARD",
    ]

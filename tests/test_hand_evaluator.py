import pytest

from pyker.hand_evaluator import Evaluator
from pyker.models import Card, Hand, HandCombination


def test_evaluator_calls_preprocess_in_constructor(monkeypatch: pytest.MonkeyPatch) -> None:
    called = {"value": False}

    def fake_preprocess(self: Evaluator) -> None:
        called["value"] = True

    monkeypatch.setattr(Evaluator, "preprocess", fake_preprocess)

    Evaluator(Hand())

    assert called["value"] is True


def test_evaluate_returns_combination_and_hand_number() -> None:
    hand = Hand([Card.from_str("As"), Card.from_str("Kd"), Card.from_str("2h")])

    combination, score = Evaluator(hand).evaluate()

    assert combination is HandCombination.HIGH_CARD
    assert score == hand.number()


def test_evaluate_single_card_returns_high_card_and_rank_index() -> None:
    hand = Hand([Card.from_str("As")])

    combination, score = Evaluator(hand).evaluate()

    assert combination is HandCombination.HIGH_CARD
    assert score == hand.cards[0][0]


def test_evaluate_two_cards_pair_returns_one_pair_and_rank_index() -> None:
    hand = Hand([Card.from_str("As"), Card.from_str("Ah")])

    combination, score = Evaluator(hand).evaluate()

    assert combination is HandCombination.ONE_PAIR
    assert score == 0


def test_evaluate_two_cards_high_card_uses_kicker_strength() -> None:
    stronger_hand = Hand([Card.from_str("As"), Card.from_str("Kd")])
    weaker_hand = Hand([Card.from_str("As"), Card.from_str("Qd")])

    stronger_combination, stronger_score = Evaluator(stronger_hand).evaluate()
    weaker_combination, weaker_score = Evaluator(weaker_hand).evaluate()

    assert stronger_combination is HandCombination.HIGH_CARD
    assert weaker_combination is HandCombination.HIGH_CARD
    assert stronger_score < weaker_score

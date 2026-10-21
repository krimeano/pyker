import pytest

from pyker.models import Card, DECK_SIZE


def test_index_to_tuple_and_string_examples() -> None:
    assert Card.from_index(0) == (0, 0)
    assert str(Card.from_index(0)) == "As"

    assert Card.from_index(1) == (0, 1)
    assert str(Card.from_index(1)) == "Ad"

    assert Card.from_index(6) == (1, 2)
    assert str(Card.from_index(6)) == "Kc"

    assert Card.from_index(51) == (12, 3)
    assert str(Card.from_index(51)) == "2h"


def test_tuple_and_string_to_index() -> None:
    assert int(Card.from_tuple((0, 0))) == 0
    assert int(Card.from_tuple((1, 2))) == 6
    assert int(Card.from_str("2h")) == 51
    assert int(Card.from_str("As")) == 0


def test_card_is_tuple_like() -> None:
    card = Card.from_str("Qd")

    assert isinstance(card, tuple)
    assert card[0] == 2
    assert card[1] == 1


def test_invalid_inputs_raise_value_error() -> None:
    with pytest.raises(ValueError):
        Card.from_index(-1)
    with pytest.raises(ValueError):
        Card.from_index(DECK_SIZE)
    with pytest.raises(ValueError):
        Card.from_str("10h")
    with pytest.raises(ValueError):
        Card.from_str("Ax")

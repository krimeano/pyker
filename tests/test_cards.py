import pytest

from pyker.models import Card, DECK_SIZE, Deck, Hand, Pocket, Table


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


def test_hand_supports_len_and_add_methods() -> None:
    hand = Hand()
    assert len(hand) == 0

    hand.add_card(Card.from_str("As"))
    hand.add_cards([Card.from_str("Kd"), Card.from_str("Qc")])

    assert len(hand) == 3
    assert [str(card) for card in hand] == ["As", "Kd", "Qc"]


def test_hand_add_combines_pocket_and_table() -> None:
    pocket = Pocket([Card.from_str("As"), Card.from_str("Ah")])
    table = Table([Card.from_str("Kd"), Card.from_str("Qc"), Card.from_str("Jc")])

    full_hand = pocket + table

    assert isinstance(full_hand, Hand)
    assert [str(card) for card in full_hand] == ["As", "Ah", "Kd", "Qc", "Jc"]


def test_table_add_with_list_returns_hand() -> None:
    deck = Deck()
    table = Table()

    flop = deck.get_cards(3)
    new_table = table + flop

    assert isinstance(new_table, Hand)
    assert not isinstance(new_table, Table)
    assert [str(card) for card in new_table] == ["As", "Ad", "Ac"]


def test_table_add_cards_with_deck_result_keeps_order() -> None:
    deck = Deck()
    table = Table()

    table.add_cards(deck.get_cards(3))
    table.add_cards(deck.get_cards(1))
    table.add_cards(deck.get_cards(1))

    assert [str(card) for card in table] == ["As", "Ad", "Ac", "Ah", "Ks"]


def test_hand_init_more_than_seven_cards_raises_not_implemented() -> None:
    deck = Deck()

    with pytest.raises(NotImplementedError):
        Hand(deck.get_cards(8))


def test_hand_add_card_more_than_seven_cards_raises_not_implemented() -> None:
    deck = Deck()
    hand = Hand(deck.get_cards(7))

    with pytest.raises(NotImplementedError):
        hand.add_card(deck.get_card())


def test_hand_add_cards_more_than_seven_cards_raises_not_implemented() -> None:
    deck = Deck()
    hand = Hand(deck.get_cards(6))

    with pytest.raises(NotImplementedError):
        hand.add_cards(deck.get_cards(2))


def test_hand_add_operator_more_than_seven_cards_raises_not_implemented() -> None:
    deck = Deck()
    left = Pocket(deck.get_cards(4))
    right = Table(deck.get_cards(4))

    with pytest.raises(NotImplementedError):
        _ = left + right


def test_hand_number_empty_hand_is_zero() -> None:
    assert Hand().number() == 0


def test_hand_number_is_order_independent_and_uses_sorted_indexes() -> None:
    hand_unsorted = Hand([Card.from_str("2h"), Card.from_str("Ah"), Card.from_str("As")])
    hand_sorted = Hand([Card.from_str("As"), Card.from_str("Ah"), Card.from_str("2h")])

    expected = 1 + 3 + 1275  # C(0,0) + C(3,1) + C(51,2)
    assert hand_unsorted.number() == expected
    assert hand_sorted.number() == expected

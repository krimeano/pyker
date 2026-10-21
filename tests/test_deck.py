import pytest

from pyker.models import DECK_SIZE, Card, Deck


def test_new_deck_is_in_ndo_order() -> None:
    deck = Deck()

    cards = deck.get_cards(DECK_SIZE)

    assert cards == [Card.from_index(i) for i in range(DECK_SIZE)]
    assert str(cards[0]) == "As"
    assert str(cards[-1]) == "2h"
    assert deck.remaining == 0


def test_burn_discards_one_card() -> None:
    deck = Deck()

    deck.burn()

    assert str(deck.get_card()) == "Ad"
    assert deck.remaining == DECK_SIZE - 2


def test_shuffle_resets_draw_position_and_keeps_52_unique_cards() -> None:
    deck = Deck()
    deck.get_cards(7)

    deck.shuffle()

    cards = deck.get_cards(DECK_SIZE)
    assert len(cards) == DECK_SIZE
    assert len({int(card) for card in cards}) == DECK_SIZE


def test_reset_restores_ndo_order() -> None:
    deck = Deck()
    deck.shuffle()

    deck.reset()

    assert deck.get_cards(4) == [Card.from_index(i) for i in range(4)]


def test_not_enough_cards_raises_index_error() -> None:
    deck = Deck()
    deck.get_cards(DECK_SIZE)

    with pytest.raises(IndexError):
        deck.get_card()
    with pytest.raises(IndexError):
        deck.get_cards(1)
    with pytest.raises(IndexError):
        deck.burn()


def test_get_cards_negative_n_raises_value_error() -> None:
    deck = Deck()

    with pytest.raises(ValueError):
        deck.get_cards(-1)

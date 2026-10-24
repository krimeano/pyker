"""Hand evaluation helpers."""

from __future__ import annotations

from pyker.models.cards import Hand
from pyker.models.entities import HandCombination


class Evaluator:
    """Evaluates a hand strength placeholder API."""

    __slots__ = ("_hand",)

    def __init__(self, hand: Hand) -> None:
        self._hand = hand
        self.preprocess()

    def preprocess(self) -> None:
        for _card in self._hand:
            pass

    def evaluate(self) -> tuple[HandCombination, int]:
        if len(self._hand) == 1:
            return HandCombination.HIGH_CARD, self._hand.cards[0][0]

        if len(self._hand) == 2:
            ranks = sorted(card[0] for card in self._hand)
            if ranks[0] == ranks[1]:
                return HandCombination.ONE_PAIR, ranks[0]
            return HandCombination.HIGH_CARD, (ranks[0] * 13) + ranks[1]

        return HandCombination.HIGH_CARD, self._hand.number()

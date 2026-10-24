"""Small data structures used by the application."""

from dataclasses import dataclass
from enum import IntEnum


class HandCombination(IntEnum):
    """Poker hand combinations ordered by strength (lower is stronger)."""

    FLUSH_ROYAL = 1
    STRAIGHT_FLUSH = 2
    FOUR_OF_A_KIND = 3
    FULL_HOUSE = 4
    FLUSH = 5
    STRAIGHT = 6
    THREE_OF_A_KIND = 7
    TWO_PAIR = 8
    ONE_PAIR = 9
    HIGH_CARD = 10


@dataclass(slots=True)
class ComputationResult:
    """Represents a computed intermediate value."""

    key: str
    value: str

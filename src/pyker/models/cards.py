"""Card model and converters for a standard 52-card deck."""

from __future__ import annotations

import random
from collections.abc import Iterable, Iterator, Sequence
from typing import Final, cast

SUITS: Final[tuple[str, ...]] = ("s", "d", "c", "h")
RANKS: Final[tuple[str, ...]] = (
    "A",
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
)

SUIT_COUNT: Final[int] = len(SUITS)
RANK_COUNT: Final[int] = len(RANKS)
DECK_SIZE: Final[int] = SUIT_COUNT * RANK_COUNT

_SUIT_TO_INDEX: Final[dict[str, int]] = {name: ix for ix, name in enumerate(SUITS)}
_RANK_TO_INDEX: Final[dict[str, int]] = {name: ix for ix, name in enumerate(RANKS)}


class Card(tuple[int, int]):
    """Tuple-like card representation: (rank_index, suit_index)."""

    __slots__ = ()

    def __new__(cls, rank_index: int, suit_index: int) -> Card:
        if not 0 <= rank_index < RANK_COUNT:
            raise ValueError(f"rank_index out of range: {rank_index}")
        if not 0 <= suit_index < SUIT_COUNT:
            raise ValueError(f"suit_index out of range: {suit_index}")
        return cast(Card, super().__new__(cls, (rank_index, suit_index)))

    @property
    def rank_index(self) -> int:
        return self[0]

    @property
    def suit_index(self) -> int:
        return self[1]

    @property
    def rank(self) -> str:
        return RANKS[self.rank_index]

    @property
    def suit(self) -> str:
        return SUITS[self.suit_index]

    def __int__(self) -> int:
        return self.rank_index * SUIT_COUNT + self.suit_index

    def __index__(self) -> int:
        return int(self)

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def __repr__(self) -> str:
        return f"Card({self.rank_index}, {self.suit_index})"

    @classmethod
    def from_index(cls, index: int) -> Card:
        if not 0 <= index < DECK_SIZE:
            raise ValueError(f"index out of range: {index}")
        rank_index, suit_index = divmod(index, SUIT_COUNT)
        return cls(rank_index, suit_index)

    @classmethod
    def from_tuple(cls, value: tuple[int, int]) -> Card:
        rank_index, suit_index = value
        return cls(rank_index, suit_index)

    @classmethod
    def from_str(cls, value: str) -> Card:
        raw = value.strip()
        if len(raw) != 2:
            raise ValueError(f"Card string must be 2 chars like 'As': {value!r}")
        rank = raw[0].upper()
        suit = raw[1].lower()

        if rank not in _RANK_TO_INDEX:
            raise ValueError(f"Unknown rank: {rank}")
        if suit not in _SUIT_TO_INDEX:
            raise ValueError(f"Unknown suit: {suit}")

        return cls(_RANK_TO_INDEX[rank], _SUIT_TO_INDEX[suit])


class Hand:
    """Ordered set of cards used for pocket and table collections."""

    __slots__ = ("_cards",)

    def __init__(self, cards: Iterable[Card] | None = None) -> None:
        self._cards: list[Card] = list(cards) if cards is not None else []

    def __iter__(self) -> Iterator[Card]:
        return iter(self._cards)

    def __getitem__(self, index: int) -> Card:
        return self._cards[index]

    def __len__(self) -> int:
        return len(self._cards)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._cards!r})"

    @property
    def cards(self) -> list[Card]:
        return list(self._cards)

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def add_cards(self, cards: Iterable[Card]) -> None:
        self._cards.extend(cards)

    def __add__(self, other: Hand | Sequence[Card]) -> Hand:
        if isinstance(other, Hand):
            right = other._cards
        else:
            right = list(other)
        return Hand([*self._cards, *right])


class Pocket(Hand):
    """Player pocket cards."""


class Table(Hand):
    """Community cards on the table."""



class Deck:
    """Standard 52-card deck in NDO order by default (As ... 2h)."""

    __slots__ = ("_cards", "_position")

    def __init__(self) -> None:
        self._cards: list[Card] = [Card.from_index(i) for i in range(DECK_SIZE)]
        self._position = 0

    @property
    def remaining(self) -> int:
        return DECK_SIZE - self._position

    def _ensure_available(self, count: int) -> None:
        if self.remaining < count:
            raise IndexError(f"Not enough cards in deck: requested={count}, remaining={self.remaining}")

    def shuffle(self) -> None:
        """Shuffle the full 52-card deck and reset draw position."""
        random.shuffle(self._cards)
        self._position = 0

    def reset(self) -> None:
        """Restore NDO ordering (As ... 2h) and reset draw position."""
        self._cards = [Card.from_index(i) for i in range(DECK_SIZE)]
        self._position = 0

    def get_card(self) -> Card:
        """Draw one card from the top of the deck."""
        self._ensure_available(1)
        card = self._cards[self._position]
        self._position += 1
        return card

    def get_cards(self, n: int) -> list[Card]:
        """Draw `n` cards from the top of the deck."""
        if n < 0:
            raise ValueError(f"n must be >= 0, got {n}")
        self._ensure_available(n)
        start = self._position
        end = start + n
        self._position = end
        return self._cards[start:end]

    def burn(self) -> None:
        """Discard one card from the top without returning it."""
        self._ensure_available(1)
        self._position += 1

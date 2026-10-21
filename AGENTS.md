# AGENTS context

Machine-readable project context for future coding sessions.

## Current card/deck decisions

- `Card` is tuple-like: `(rank_index, suit_index)`.
- `SUITS = ('s', 'd', 'c', 'h')`.
- `RANKS = ('A', 'K', 'Q', 'J', 'T', '9', ..., '2')`.
- `int(Card) = rank_index * 4 + suit_index`.
- `DECK_SIZE = 52`.

## Deck contract (implemented)

- `Deck` represents a standard 52-card deck, no jokers.
- New deck and `reset()` are in NDO order by card index: `As ... 2h`.
- `shuffle()` always shuffles the full deck and resets draw position to the top.
- Draw operations use an internal index pointer (no list `pop(0)` behavior).
- `get_card()` returns one top card.
- `get_cards(n)` returns `n` top cards; for `n < 0` raises `ValueError`.
- `burn()` discards one top card and returns nothing.
- If there are not enough cards, `get_card()`, `get_cards(n)`, and `burn()` raise `IndexError`.

## Scope constraints (for now)

- No discard-pile entity.
- No reshuffling from discard pile.
- No jokers.
- Target use case is hold'em-style dealing, but implementation stays generic.

# pyker

Basic Python 3 project scaffold with `src` layout and `pytest` tests.

## Project structure

- `src/pyker/main.py` - main entry module
- `src/pyker/models/` - data structure models
- `src/pyker/cache/` - file-backed cache helpers for intermediate results
- `src/pyker/lorem/` - `lorem` package
- `src/pyker/ipsum/` - `ipsum` package
- `src/pyker/ipsum/dolor.py` - `ipsum.dolor` module
- `tests/` - pytest tests

## Runtime cache (no database)

This project uses text and binary files for intermediate computed results.

- Default cache directory: `var/cache/`
- Override with env var: `PYKER_CACHE_DIR`
- Keep cache files out of git

## Why use `python -m ...`

Use module execution (`python -m pyker.main`) as the default.
It runs code in package context, so package imports are stable when the project grows.

## Quick start

```zsh
/Users/palutser/IdeaProjects/pyker/.venv/bin/python -m pip install -e ".[dev]"
/Users/palutser/IdeaProjects/pyker/.venv/bin/python -m pyker.main
/Users/palutser/IdeaProjects/pyker/.venv/bin/python -m pytest
```

## Card model

`Card` is a tuple-like type with shape `(rank_index, suit_index)`.

- `SUITS = ('s', 'd', 'c', 'h')`
- `RANKS = ('A', 'K', 'Q', 'J', 'T', '9', ..., '2')`
- `index = rank_index * 4 + suit_index`

Examples:

- `Card.from_index(0)` -> `(0, 0)` -> `"As"`
- `Card.from_index(6)` -> `(1, 2)` -> `"Kc"`
- `int(Card.from_str("2h"))` -> `51`

## Deck model

`Deck` models a 52-card deck without jokers for hold'em-style dealing.

- Default order (`reset` / new deck) is NDO and matches card indexes: `As ... 2h`
- `shuffle()` always shuffles the full deck and resets draw position
- `get_card()` draws one card from the top
- `get_cards(n)` draws `n` cards; raises `IndexError` if there are not enough cards
- `burn()` discards one top card; raises `IndexError` if the deck is empty

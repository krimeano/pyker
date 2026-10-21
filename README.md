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

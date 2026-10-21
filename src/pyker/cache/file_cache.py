"""Simple file-backed cache for text and binary artifacts."""

from __future__ import annotations

import os
import re
from pathlib import Path

_CACHE_ENV = "PYKER_CACHE_DIR"
_SAFE_KEY_RE = re.compile(r"[^a-zA-Z0-9._-]+")


def get_cache_dir() -> Path:
    """Return the cache directory and ensure it exists."""
    configured = os.environ.get(_CACHE_ENV)
    cache_dir = Path(configured) if configured else Path("var/cache")
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


def _sanitize_key(key: str) -> str:
    safe_key = _SAFE_KEY_RE.sub("_", key).strip("._-")
    if not safe_key:
        raise ValueError("Cache key must contain at least one safe character")
    return safe_key


class FileCache:
    """Store and load cached artifacts from the filesystem."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or get_cache_dir()
        self.root.mkdir(parents=True, exist_ok=True)

    def _path_for(self, key: str, suffix: str) -> Path:
        return self.root / f"{_sanitize_key(key)}{suffix}"

    def write_text(self, key: str, payload: str, *, encoding: str = "utf-8") -> Path:
        path = self._path_for(key, ".txt")
        path.write_text(payload, encoding=encoding)
        return path

    def read_text(self, key: str, *, encoding: str = "utf-8") -> str:
        return self._path_for(key, ".txt").read_text(encoding=encoding)

    def write_bytes(self, key: str, payload: bytes) -> Path:
        path = self._path_for(key, ".bin")
        path.write_bytes(payload)
        return path

    def read_bytes(self, key: str) -> bytes:
        return self._path_for(key, ".bin").read_bytes()

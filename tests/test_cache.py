import pytest

from pyker.cache import FileCache


def test_file_cache_text_roundtrip(tmp_path) -> None:
    cache = FileCache(root=tmp_path)

    cache.write_text("alpha", "hello")

    assert cache.read_text("alpha") == "hello"


def test_file_cache_bytes_roundtrip(tmp_path) -> None:
    cache = FileCache(root=tmp_path)

    cache.write_bytes("blob", b"\x00\x01")

    assert cache.read_bytes("blob") == b"\x00\x01"


def test_file_cache_rejects_invalid_key(tmp_path) -> None:
    cache = FileCache(root=tmp_path)

    with pytest.raises(ValueError):
        cache.write_text("!!!", "bad")

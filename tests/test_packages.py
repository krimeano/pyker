from pyker.lorem import lorem_text
from pyker.ipsum import ipsum_text, dolor


def test_lorem_text() -> None:
    assert lorem_text() == "lorem"


def test_ipsum_text() -> None:
    assert ipsum_text() == "ipsum dolor"


def test_dolor_export() -> None:
    assert dolor.dolor_text() == "dolor"

"""`ipsum` package."""

from . import dolor

__all__ = ["ipsum_text", "dolor"]


def ipsum_text() -> str:
    """Return a placeholder string that includes dolor text."""
    return f"ipsum {dolor.dolor_text()}"

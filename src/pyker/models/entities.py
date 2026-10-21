"""Small data structures used by the application."""

from dataclasses import dataclass


@dataclass(slots=True)
class ComputationResult:
    """Represents a computed intermediate value."""

    key: str
    value: str

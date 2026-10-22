"""Combinatorics helpers."""

from typing import Final

MAX_BINOMIAL_N: Final[int] = 52
MAX_BINOMIAL_K: Final[int] = 7

# Lazy cache for C(n, k) values with n<=52 and k<=min(7, n).
_BINOMIAL_TABLE: dict[tuple[int, int], int] | None = None


def binary_coefficient(n: int, k: int) -> int:
    """Return binomial coefficient C(n, k)."""

    if n < 0:
        raise ValueError("n must be non-negative")
    if k < 0:
        raise ValueError("k must be non-negative")

    if k > n:
        raise ValueError("k must be less than or equal to n")

    if n == 0 or k == 0 or k == n:
        return 1
    # Use symmetry to minimize the number of multiplication/division steps.
    k = min(k, n - k)

    result = 1

    for i in range(1, k + 1):
        result = result * (n - k + i) // i

    return result


def _build_binomial_table(max_n: int = MAX_BINOMIAL_N, max_k: int = MAX_BINOMIAL_K) -> dict[tuple[int, int], int]:
    """Build C(n, k) for 0<=n<=max_n and 0<=k<=min(max_k, n)."""
    table: dict[tuple[int, int], int] = {}
    for n in range(max_n + 1):
        for k in range(min(max_k, n) + 1):
            table[(n, k)] = binary_coefficient(n, k)
    return table


def get_binomial_table() -> dict[tuple[int, int], int]:
    """Return lazily initialized C(n, k) table for n<=52 and k<=min(7, n)."""
    global _BINOMIAL_TABLE
    if _BINOMIAL_TABLE is None:
        _BINOMIAL_TABLE = _build_binomial_table()
    return _BINOMIAL_TABLE

"""Combinatorics helpers."""


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

    if k > n / 2:
        k = n - k  # Use symmetry property

    return binary_coefficient(n, k - 1) * (n - k + 1) // k

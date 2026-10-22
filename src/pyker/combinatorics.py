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

    # Use symmetry to minimize the number of multiplication/division steps.
    if k > n // 2:
        k = n - k

    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
    return result

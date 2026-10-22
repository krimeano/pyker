"""Combinatorics helpers."""

# On-demand cache for C(n, k) values.
_BINOMIAL_CACHE: dict[tuple[int, int], int] = {}


def binary_coefficient(n: int, k: int) -> int:
    """Return binomial coefficient C(n, k)."""

    if n < 0:
        raise ValueError("n must be non-negative")
    if k < 0:
        raise ValueError("k must be non-negative")

    if k > n:
        raise ValueError("k must be less than or equal to n")

    # Use symmetry to minimize the number of multiplication/division steps.
    k = min(k, n - k)

    key = (n, k)
    cached = _BINOMIAL_CACHE.get(key)
    if cached is not None:
        return cached

    if k == 0:
        _BINOMIAL_CACHE[key] = 1
        return 1

    result = 1

    for i in range(1, k + 1):
        result = result * (n - k + i) // i

    _BINOMIAL_CACHE[key] = result
    return result

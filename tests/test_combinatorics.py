import math

import pytest

from pyker.combinatorics import MAX_BINOMIAL_K, MAX_BINOMIAL_N, binary_coefficient, get_binomial_table


@pytest.mark.parametrize(
    ("n", "k", "expected"),
    [
        (0, 0, 1),
        (1, 0, 1),
        (1, 1, 1),
        (5, 1, 5),
        (5, 2, 10),
        (6, 3, 20),
        (10, 5, 252),
    ],
)
def test_binary_coefficient_known_values(n: int, k: int, expected: int) -> None:
    assert binary_coefficient(n, k) == expected


@pytest.mark.parametrize("n", [2, 5, 10, 20])
def test_binary_coefficient_matches_math_comb(n: int) -> None:
    for k in range(n + 1):
        assert binary_coefficient(n, k) == math.comb(n, k)


def test_binary_coefficient_uses_symmetry() -> None:
    assert binary_coefficient(10, 8) == binary_coefficient(10, 2)


@pytest.mark.parametrize(
    ("n", "k", "message"),
    [
        (-1, 0, "n must be non-negative"),
        (5, -1, "k must be non-negative"),
        (4, 5, "k must be less than or equal to n"),
    ],
)
def test_binary_coefficient_invalid_inputs_raise_value_error(n: int, k: int, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        binary_coefficient(n, k)


def test_binomial_table_domain_and_values() -> None:
    table = get_binomial_table()

    expected_size = sum(min(MAX_BINOMIAL_K, n) + 1 for n in range(MAX_BINOMIAL_N + 1))
    assert len(table) == expected_size

    for n in range(MAX_BINOMIAL_N + 1):
        for k in range(min(MAX_BINOMIAL_K, n) + 1):
            assert table[(n, k)] == binary_coefficient(n, k)

    assert (MAX_BINOMIAL_N, MAX_BINOMIAL_K + 1) not in table


def test_binomial_table_is_cached() -> None:
    first = get_binomial_table()
    second = get_binomial_table()
    assert first is second

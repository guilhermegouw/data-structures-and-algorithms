import pytest

from .challenge import get_equilibrium_indexes, naive_get_equilibrium_indexes


@pytest.mark.parametrize(
    "input, expected",
    [
        ([-7, 1, 5, 2, -4, 3, 0], [3, 6]),
        ([1, 3, 5, 2, 2], [2]),
        ([0, -1, 2, -1, 0], [0, 2, 4]),
    ],
)
def test_naive_get_equilibrium_indexes(input, expected):
    assert naive_get_equilibrium_indexes(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ([-7, 1, 5, 2, -4, 3, 0], [3, 6]),
        ([1, 3, 5, 2, 2], [2]),
        ([0, -1, 2, -1, 0], [0, 2, 4]),
    ],
)
def test_get_equilibrium_indexes(input, expected):
    assert get_equilibrium_indexes(input) == expected


"""
Exploring the problem:
Case 1:

equilibrium_indexes = []
[1, 2, 3]

index = 0 => val = 1
left_sum = 0
right_sum = 2 + 3 => 5
left_sum != right_sum

index = 1 => val = 2
left_sum = 1
right_sum = 3 => 3
left_sum != right_sum

index = 2 => val = 3
left_sum = 1 + 2 => 3
right_sum = 0
left_sum != right_sum

Array is finished no equilibrium_indexes.


Case 2:
equilibrium_indexes = []
[0, 0, 0]

index = 0 => val = 0
left_sum = 0
right_sum = 0 + 0 => 0
left_sum == right_sum
equilibrium_indexes = [0]

index = 1 => val = 0
left_sum = 0
right_sum = 0
left_sum == right_sum
equilibrium_indexes = [0, 1]

index = 2 => val = 0
left_sum = 0 + 0 => 0
right_sum = 0
left_sum == right_sum
equilibrium_indexes = [0, 1, 2]
"""

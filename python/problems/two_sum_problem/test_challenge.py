import pytest
from challenge import get_sum_of_two


@pytest.mark.parametrize(
    "input, target, expected",
    [
        ([1, 2], 4, []),
        ([1, 2, 3], 6, []),
        ([1, 2, 3], 5, [2, 3]),
        ([1, 2, 3, 4], 5, [2, 3]),
        ([3, 5, -4, 8, 11, 1, -1, 6], 10, [-1, 11]),
    ],
)
def test_get_sum_of_two(input, target, expected):
    result = get_sum_of_two(input, target)
    assert sorted(result) == sorted(expected)

import pytest
from challenge import validate_subsequence


@pytest.mark.parametrize(
    "array, sequence, expected",
    [
        ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True),
        ([1, 2, 3, 4, 5], [1, 3, 5], True),
        ([1, 2, 3, 4, 5], [2, 4], True),
        ([1, 2, 3, 4, 5], [1, 2, 5], True),
        ([1, 2, 3, 4, 5], [1], True),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),
        ([5], [5], True),
        ([1, 2, 3, 4, 5], [1, 6], False),
        ([1, 2, 3, 4, 5], [5, 3], False),
        ([1, 2, 3], [1, 2, 3, 4], False),
        ([1, 2, 2, 3, 4, 5], [2, 2, 5], True),
        ([1, 2, 3, 2, 4, 5], [1, 2, 5], True),
        ([1, 2, 3, 2, 4, 5], [3, 2, 5], True),
        ([-5, 10, -3, 7, 9], [-5, -3, 9], True),
        ([-5, -3, -1, 0, 2], [0, 2], True),
        ([100, 1000, 10000, 100000], [100, 100000], True),
        ([5, 1000, -20, 8, 3], [5, -20, 3], True),
        ([10, 22, 9, 33, 21, 50, 41, 60], [10, 9, 50, 60], True),
        ([0, 1, 2, 3, 4, 5, 6, 7], [0, 3, 7], True),
        ([8, 7, 6, 5, 4, 3, 2, 1], [8, 6, 1], True)
    ]
)
def test_validate_subsequence(array, sequence, expected):
    assert validate_subsequence(array, sequence) == expected

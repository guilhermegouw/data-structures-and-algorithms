import pytest
from challenge import rotate_to_the_right_k_times


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1], 1, [1]),
        ([1, 2], 1, [2, 1]),
        ([1, 2, 3], 2, [2, 3, 1]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 2, 3], 4, [3, 1, 2]),
    ],
)
def test_rotate_to_the_right_k_times(arr, k, expected):
    assert rotate_to_the_right_k_times(arr, k) == expected

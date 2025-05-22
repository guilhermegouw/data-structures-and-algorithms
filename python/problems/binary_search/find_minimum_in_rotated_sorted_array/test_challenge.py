import pytest
from challenge import find_minimum_in_rotated_sorted_array


@pytest.mark.parametrize(
    "array, expected",
    [
        ([1], 0),
        ([1, 2], 0),
        ([2, 1], 1),
        ([1, 2, 3], 0),
        ([2, 3, 1], 2),
        ([3, 1, 2], 1),
        ([30, 40, 50, 10, 20], 3),
        ([3, 5, 7, 11, 13, 17, 19, 2], 7),
        ([4, 5, 6, 7, 0, 1, 2], 4),
    ]
)
def test_find_minimum_in_rotated_sorted_array(array, expected):
    assert find_minimum_in_rotated_sorted_array(array) == expected

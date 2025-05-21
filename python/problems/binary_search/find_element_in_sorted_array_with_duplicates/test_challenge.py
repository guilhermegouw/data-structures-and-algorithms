import pytest
from challenge import find_element_in_sorted_array_with_duplicates


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 1], 0, -1),
        ([1, 1], 1, 0),
        ([1, 1, 2], 2, 2),
        ([1, 1, 2, 2], 2, 2),
        ([1, 1, 2, 2, 2], 2, 2),
        ([1, 1, 2, 2, 2, 3], 3, 5),
        ([1, 1, 1, 1, 1, 1, 1, 1], 1, 0),
        ([], 1, -1),
        ([1], 1, 0),
        ([1], 2, -1),
        ([1, 3, 5, 7, 9], 5, 2),
        ([5, 5, 5, 5, 5, 5, 5, 5], 5, 0),
        ([3, 5, 5, 5, 5, 5, 5, 5], 3, 0),
        ([3, 3, 3, 3, 3, 5, 5, 5], 5, 5),
        ([1, 3, 5, 7, 9], 10, -1),
        ([1, 3, 5, 7, 9], 0, -1),
        ([1, 3, 5, 7, 9], 6, -1),
        ([1, 3, 5, 7, 9], 5, 2),
    ]
)
def test_find_element_in_sorted_array_with_duplicates(arr, target, expected):
    assert find_element_in_sorted_array_with_duplicates(arr, target) == expected

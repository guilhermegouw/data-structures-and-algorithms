import pytest
from challenge import first_element_not_smaller_than_target


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 3, 3, 5, 8, 8, 10], 2, 1),
        ([2, 3, 5, 7, 11, 13, 17, 19], 6, 3),
        ([1, 2, 3, 4, 5], 3, 2),
        ([5, 6, 7, 8, 9], 4, 0),
        ([1, 3, 5, 7, 10], 8, 4),
        ([2, 2, 2, 2, 2], 2, 0),
        ([1, 3, 3, 3, 5, 8], 3, 1),
        ([5], 5, 0),
        ([5], 3, 0),
        ([1, 3, 5, 7, 9], 9, 4),
        ([10, 11, 12, 13, 14], 12, 2)
    ]
)
def test_first_element_not_smaller_than_target(arr, target, expected):
    assert first_element_not_smaller_than_target(arr, target) == expected

import pytest
from challenge import find_the_first_true_in_a_sorted_boolean_array


@pytest.mark.parametrize(
    "array, expected",
    [
        ([False, False, True, True, True], 2),
        ([False, False, False, True, True, True], 3),
        ([False, False, False, False, True, True], 4),
        ([False, True, True, True, True], 1),
        ([False, False, False, False, False], -1),
    ]
)
def test_find_the_first_true_in_a_sorted_boolean_array(array, expected):
    assert find_the_first_true_in_a_sorted_boolean_array(array) == expected

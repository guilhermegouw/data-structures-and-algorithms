import pytest
from challenge import in_place_remove_duplicates


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 2], [1, 2]),
        ([1, 2, 2, 3, 3, 3], [1, 2, 3]),
    ],
)
def test_remove_duplicates(input, expected):
    assert in_place_remove_duplicates(input) == expected

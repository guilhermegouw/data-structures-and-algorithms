import pytest
from challenge import reverse_array


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [3, 2, 1]),
    ],
)
def test_reverse_array(input, expected):
    assert reverse_array(input) == expected

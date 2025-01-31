import pytest
from challenge import get_max_and_min


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1], (1, 1)),
        ([1, 2], (2, 1)),
        ([1, 2, 3], (3, 1)),
        ([-1, 2, -3], (2, -3)),
    ],
)
def test_get_max_and_min(input, expected):
    assert get_max_and_min(input) == expected

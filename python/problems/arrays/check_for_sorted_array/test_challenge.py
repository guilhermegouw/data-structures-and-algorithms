import pytest
from challenge import is_sorted


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1], True),
        ([1, 3], True),
        ([1, 3, 2], False),
    ],
)
def test_is_sorted(input, expected):
    assert is_sorted(input) == expected

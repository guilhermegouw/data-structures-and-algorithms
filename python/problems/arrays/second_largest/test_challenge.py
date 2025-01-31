import pytest
from challenge import get_second_largest


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1], None),
        ([1, 2], 1),
        ([1, 2, 3], 2),
        ([4, 1, 2, 3], 3),
    ],
)
def test_get_second_largest(input, expected):
    assert get_second_largest(input) == expected

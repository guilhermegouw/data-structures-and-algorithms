import pytest
from challenge import has_duplicates


@pytest.mark.parametrize(
        "array, expected",
        [
            ([1, 2], False),
            ([1, 2, 1], True),
            ([1, 2, 3], False),
            ([1, 2, 3, 1], True),
            ([1, 2, 4, 7, 2], True),
            ]
        )
def test_has_duplicates(array, expected):
    assert has_duplicates(array) is expected

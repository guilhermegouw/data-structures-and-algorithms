import pytest
from challenge import greatest_number


@pytest.mark.parametrize(
        "array, greatest_num",
        [
            ([1, 2, 3], 3),
            ([4, 2, 3], 4),
            ([1, 2, 3, 7, 4], 7),
            ([1, 1, 1], 1),
            ([5, 2, 3, 6], 6),
            ([1, 2, 3, 9, 8, 7], 9),
        ]
        )
def test_greatest_number(array, greatest_num):
    assert greatest_number(array) == greatest_num

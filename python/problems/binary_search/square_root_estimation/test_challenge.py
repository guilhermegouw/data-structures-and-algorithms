import pytest
from challenge import square_root_estimation


@pytest.mark.parametrize(
    "num, expected",
    [
        (16, 4),
        (8, 2),
        (10, 3),
        (15, 3),
        (20, 4),
        (0, 0),
        (1, 1),
        (1000000, 1000),
        (24, 4),
        (25, 5),
        (17, 4),
        (26, 5),
    ]
)
def test_square_root_estimation(num, expected):
    assert square_root_estimation(num) == expected

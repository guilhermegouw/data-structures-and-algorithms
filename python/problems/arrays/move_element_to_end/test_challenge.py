import pytest
from challenge import move_element_to_end


@pytest.mark.parametrize(
    "input, to_move, expected",
    [
        ([1, 2, 3], 4, [1, 2, 3]),
        ([1, 2, 3], 2, [1, 3, 2]),
        ([2, 1, 2, 2, 2, 3, 4, 2], 2, [1, 3, 4, 2, 2, 2, 2, 2]),
    ],
)
def test_move_element_to_end(input, to_move, expected):
    assert move_element_to_end(input, to_move) == expected

import pytest

from .static_array import StaticArray


def test_initialization():
    array = StaticArray(int, 4)
    assert array.capacity == 4
    assert array.data_type == int
    for elm in array.internal_array:
        assert elm is None
    with pytest.raises(
        TypeError,
        match="data_type must be a valid Python type",
    ):
        StaticArray("integer", 5)
    with pytest.raises(
        ValueError,
        match="Array capacity must be greater than 0.",
    ):
        StaticArray(int, 0)


def test_access():
    array = StaticArray(int, 5)
    assert array[0] is None
    with pytest.raises(IndexError, match="Index out of bound"):
        array[5]


def test_update():
    array = StaticArray(int, 5)
    array[0] = 1
    assert array[0] == 1
    assert not array[0] != 1
    with pytest.raises(
        TypeError, match="Expect type: <class 'int'> got type: <class 'str'>"
    ):
        array[1] = "one"

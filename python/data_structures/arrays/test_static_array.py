import pytest

from .static_array import StaticArray


def test_initialization():
    array = StaticArray(4, int)
    assert array.size == 4
    assert array.data_type == int
    for elm in array.elements:
        assert elm is None
    with pytest.raises(
        TypeError,
        match="datatype must be a valid type, e.g., int, float, str.",
    ):
        StaticArray(5, "integer")
    with pytest.raises(
        ValueError,
        match="Array size must be greater than 0.",
    ):
        StaticArray(0, int)


def test_access():
    array = StaticArray(5, int)
    assert array[0] is None
    with pytest.raises(IndexError, match="Index out of bounds."):
        array[5]


def test_update():
    array = StaticArray(5, int)
    array[0] = 1
    assert array[0] == 1
    assert not array[0] != 1
    with pytest.raises(
        TypeError, match="Expected type <class 'int'>, got <class 'str'>"
    ):
        array[1] = "one"

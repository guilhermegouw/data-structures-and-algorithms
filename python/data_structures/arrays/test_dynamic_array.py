import pytest

from .dynamic_array import DynamicArray


def test_initialization():
    array = DynamicArray(int)
    assert array.internal_array == [None, None]
    assert array.size == 0
    assert array.capacity == 2
    assert array.growth_factor == 2
    with pytest.raises(
        TypeError, match="data_type must be a valid Python type."
    ):
        array = DynamicArray("integer")


def test_append():
    array = DynamicArray(int)
    array.append(1)
    assert array.internal_array == [1, None]
    assert array.size == 1
    with pytest.raises(
        TypeError, match="Expected type <class 'int'>, got <class 'str'>"
    ):
        array.append("one")


def test_resize():
    array = DynamicArray(int)
    array.append(1)
    array.append(2)
    array.append(3)
    assert array.capacity == 4
    assert array.internal_array[:3] == [1, 2, 3]

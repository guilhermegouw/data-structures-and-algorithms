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
        TypeError,
        match="DynamicArray expect type: <class 'int'>"
        + " but got: <class 'str'>",
    ):
        array.append("one")


def test_resize():
    array = DynamicArray(int)
    array.append(1)
    array.append(2)
    array.append(3)
    assert array.capacity == 4
    assert array.internal_array[:3] == [1, 2, 3]


def test_retrieve():
    array = DynamicArray(int)
    array.append(1)
    array.append(2)
    array.append(3)
    assert array[0] == 1
    with pytest.raises(IndexError, match="Index out of bounds"):
        array[3]


def test_update():
    array = DynamicArray(int)
    array.append(1)
    array.append(2)
    array.append(3)
    array[0] = 4
    assert array[0] == 4
    with pytest.raises(IndexError, match="Index out of bounds"):
        array[3] = 5
    with pytest.raises(
        TypeError,
        match="DynamicArray expect type: <class 'int'> but got: <class 'str'>",
    ):
        array[0] = "One"


def test_insert():
    array = DynamicArray(str)
    array.append("apple")
    array.append("banana")
    array.insert(1, "strawberry")
    assert array.internal_array[: array.size] == [
        "apple",
        "strawberry",
        "banana",
    ]


def test_delete():
    array = DynamicArray(int)
    array.append(1)
    array.append(2)
    array.append(3)
    array.delete(0)
    assert array.internal_array[: array.size] == [2, 3]

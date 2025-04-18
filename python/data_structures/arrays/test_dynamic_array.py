import pytest

from .dynamic_array import DynamicArray
from .exceptions import ValueNotFound


def test_initialization():
    array = DynamicArray(int)
    assert array.internal_array == [None, None]
    assert len(array) == 0
    assert array.capacity == 2
    assert array.growth_factor == 2
    with pytest.raises(
        TypeError, match="data_type must be a valid Python type"
    ):
        array = DynamicArray("integer")


def test_append():
    array = DynamicArray(int)
    array.append(1)
    assert array == [1]
    assert len(array) == 1
    with pytest.raises(
        TypeError,
        match="Expect type: <class 'int'>" + " got type: <class 'str'>",
    ):
        array.append("one")


def test_resize():
    array = DynamicArray(int)
    array.append(1)
    array.append(2)
    array.append(3)
    assert array.capacity == 4
    assert array == [1, 2, 3]


def test_retrieve():
    array = DynamicArray(int)
    array.append(1)
    array.append(2)
    array.append(3)
    assert array[0] == 1
    with pytest.raises(IndexError, match="Index out of bound"):
        array[3]


def test_update():
    array = DynamicArray(int)
    array.append(1)
    array.append(2)
    array.append(3)
    array[0] = 4
    assert array[0] == 4
    with pytest.raises(IndexError, match="Index out of bound"):
        array[3] = 5
    with pytest.raises(
        TypeError,
        match="Expect type: <class 'int'> got type: <class 'str'>",
    ):
        array[0] = "One"


def test_insert():
    array = DynamicArray(str)
    array.append("apple")
    array.append("banana")
    array.insert(1, "strawberry")
    assert len(array) == 3
    assert array == [
        "apple",
        "strawberry",
        "banana",
    ]
    with pytest.raises(
        TypeError,
        match="Expect type: <class 'str'> got type: <class 'int'>",
    ):
        array.insert(2, 4)
    with pytest.raises(IndexError, match="Index out of bound"):
        array.insert(4, "orange")


def test_delete():
    array = DynamicArray(int)
    array.append(1)
    array.append(2)
    array.append(3)
    array.delete(0)
    assert array == [2, 3]
    assert len(array) == 2
    with pytest.raises(IndexError, match="Index out of bound"):
        array.delete(2)


def test_search():
    array = DynamicArray(str)
    array.append("apple")
    array.append("banana")
    array.append("pear")
    assert array.search("pear") == 2
    with pytest.raises(
        ValueNotFound, match="The value blueberry was not found"
    ):
        array.search("blueberry")


def test_remove():
    array = DynamicArray(str)
    array.append("apple")
    array.append("banana")
    array.append("pear")
    array.remove("banana")
    assert array == ["apple", "pear"]
    with pytest.raises(ValueNotFound, match="The value banana was not found"):
        array.remove("banana")

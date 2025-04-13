import pytest

from .exceptions import ValueNotFound
from .ordered_array import OrderedArray


def test_initialization():
    array = OrderedArray(int)
    assert array.internal_array == [None, None]
    assert len(array) == 0
    assert array.capacity == 2
    assert array.growth_factor == 2
    with pytest.raises(
        TypeError, match="data_type must be a valid Python type"
    ):
        array = OrderedArray("integer")


def test_retrieve():
    array = OrderedArray(int)
    array.add(1)
    array.add(2)
    array.add(3)
    assert array[0] == 1
    with pytest.raises(IndexError, match="Index out of bound"):
        array[3]


def test_add():
    array = OrderedArray(int)
    array.add(5)
    array.add(3)
    array.add(1)
    assert array == [1, 3, 5]


def test_remove():
    array = OrderedArray(str)
    array.add("apple")
    array.add("banana")
    array.add("pear")
    array.remove("banana")
    assert array == ["apple", "pear"]
    with pytest.raises(ValueNotFound, match="The value banana was not found"):
        array.remove("banana")


def test_resize():
    array = OrderedArray(int)
    array.add(1)
    array.add(2)
    array.add(3)
    assert array.capacity == 4
    assert array == [1, 2, 3]


def test_search():
    array = OrderedArray(int)
    array.add(9)
    array.add(1)
    array.add(8)
    array.add(2)
    array.add(7)
    assert array.search(7) == 2
    with pytest.raises(ValueNotFound, match="The value 3 was not found"):
        array.search(3)

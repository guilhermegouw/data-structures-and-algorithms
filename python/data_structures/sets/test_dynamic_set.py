import pytest

from .dynamic_set import DynamicSet


def test_initialization():
    dynamic_set = DynamicSet(int)
    assert dynamic_set.size == 0
    assert dynamic_set.capacity == 2
    assert dynamic_set == []


def test_append():
    dynamic_set = DynamicSet(int)
    dynamic_set.append(42)
    assert dynamic_set[0] == 42
    assert dynamic_set.size == 1
    assert dynamic_set == [42]


def test_type_contraints():
    dynamic_set = DynamicSet(int)
    with pytest.raises(
        TypeError, match="Expected type <class 'int'>, got <class 'str'>"
    ):
        dynamic_set.append("fourty two")
    with pytest.raises(
        TypeError, match="data_type must be a valid Python type"
    ):
        DynamicSet("integer")


def test_uniqueness():
    dynamic_set = DynamicSet(int)
    dynamic_set.append(42)
    with pytest.raises(ValueError, match="The value 42 already exists"):
        dynamic_set.append(42)


def test_resize():
    dynamic_set = DynamicSet(int)
    assert dynamic_set.capacity == 2
    dynamic_set.append(42)
    dynamic_set.append(43)
    dynamic_set.append(44)
    assert dynamic_set.size == 3
    assert dynamic_set.capacity == 4
    assert 42 in dynamic_set
    assert 43 in dynamic_set
    assert 44 in dynamic_set


def test_retrieve():
    dynamic_set = DynamicSet(int)
    dynamic_set.append(42)
    dynamic_set.append(43)
    assert dynamic_set[0] == 42
    assert dynamic_set[1] == 43
    with pytest.raises(IndexError, match="Index out of range"):
        _ = dynamic_set[2]


def test_update():
    dynamic_set = DynamicSet(int)
    dynamic_set.append(42)
    dynamic_set.append(43)
    assert dynamic_set == [42, 43]
    assert dynamic_set.size == 2
    dynamic_set[0] = 44
    assert dynamic_set[0] == 44
    assert dynamic_set.size == 2
    dynamic_set[1] = 43
    assert dynamic_set[1] == 43
    assert dynamic_set.size == 2
    with pytest.raises(ValueError, match="The value 43 already exists"):
        dynamic_set[0] = 43


def test_insert():
    dynamic_set = DynamicSet(int)
    dynamic_set.append(1)
    dynamic_set.insert(0, 42)
    assert dynamic_set == [42, 1]
    assert len(dynamic_set) == 2
    dynamic_set.insert(2, 43)
    assert dynamic_set == [42, 1, 43]


def test_delete():
    dynamic_set = DynamicSet(int)
    dynamic_set.append(1)
    dynamic_set.append(2)
    dynamic_set.append(3)
    assert dynamic_set == [1, 2, 3]
    dynamic_set.delete(0)
    assert dynamic_set == [2, 3]

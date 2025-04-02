import pytest

from .static_set import ItemAlreadyExistsError, StaticSet


def test_initialization():
    static_set = StaticSet(4, int)
    assert static_set.size == 4
    assert static_set.data_type == int
    for elm in static_set.elements:
        assert elm is None
    with pytest.raises(
        TypeError,
        match="data_type must be a valid type, e.g., int, float, str.",
    ):
        StaticSet(5, "integer")
    with pytest.raises(
        ValueError,
        match="Set size must be greater than 0.",
    ):
        StaticSet(0, int)


def test_access():
    static_set = StaticSet(5, int)
    assert static_set[0] is None
    with pytest.raises(IndexError, match="Index out of bounds."):
        static_set[5]


def test_update():
    static_set = StaticSet(5, int)
    static_set[0] = 1
    assert static_set[0] == 1
    assert not static_set[0] != 1
    with pytest.raises(
        TypeError, match="Expected type <class 'int'>, got <class 'str'>"
    ):
        static_set[1] = "one"
    with pytest.raises(
        ItemAlreadyExistsError, match="Item '1' already exists in the set"
    ):
        static_set[1] = 1


def test_search():
    static_set = StaticSet(5, int)
    static_set[0], static_set[1], static_set[2] = 1, 2, 3
    assert static_set.search(3) == 2
    assert static_set.search(4) == -1

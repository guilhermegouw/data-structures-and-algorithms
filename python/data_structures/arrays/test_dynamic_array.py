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

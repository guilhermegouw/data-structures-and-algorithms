import pytest

from .base_array import BaseArray


def test_initialization():
    array = BaseArray(int, 5)
    assert array.data_type == int
    assert array.capacity == 5
    assert array.size == 0
    assert array.internal_array == [None, None, None, None, None]
    with pytest.raises(
        TypeError, match="data_type must be a valid Python type"
    ):
        BaseArray("invalid")


@pytest.mark.parametrize(
    "valid_type, valid_value",
    [
        (int, 42),
        (float, 42.0),
        (str, "Python"),
        (list, [1, 2, 3]),
        (tuple, (3, 2, 1)),
        (dict, {"one": 1}),
        (bool, True),
    ],
)
def test_validate_type(valid_type, valid_value):
    array = BaseArray(valid_type)
    array._validate_type(valid_value)


@pytest.mark.parametrize(
    "valid_type, invalid_value, error_msg",
    [
        (int, 4.2, "Expect type: <class 'int'> got type: <class 'float'>"),
        (float, 42, "Expect type: <class 'float'> got type: <class 'int'>"),
        (str, True, "Expect type: <class 'str'> got type: <class 'bool'>"),
        (
            list,
            (1, 2),
            "Expect type: <class 'list'> got type: <class 'tuple'>",
        ),
        (
            tuple,
            [3, 2],
            "Expect type: <class 'tuple'> got type: <class 'list'>",
        ),
        (dict, {"one"}, "Expect type: <class 'dict'> got type: <class 'set'>"),
        (bool, "True", "Expect type: <class 'bool'> got type: <class 'str'>"),
    ],
)
def test_validate_type_invalid_values(valid_type, invalid_value, error_msg):
    array = BaseArray(valid_type)
    with pytest.raises(TypeError, match=error_msg):
        array._validate_type(invalid_value)

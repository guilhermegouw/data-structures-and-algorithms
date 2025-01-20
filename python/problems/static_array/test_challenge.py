import pytest
from challenge import Array


def test_can_instantiate_array():
    assert Array(3, int)

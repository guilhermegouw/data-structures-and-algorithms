from .base_array import BaseArray
from .exceptions import ValueNotFound


class DynamicArray(BaseArray):
    def __init__(self, data_type) -> None:
        super().__init__(data_type, 2)
        self.growth_factor = 2

    def _resize(self):
        new_array = [None] * (self.capacity * self.growth_factor)
        for i in range(self.size):
            new_array[i] = self.internal_array[i]
        self.internal_array = new_array
        self.capacity *= self.growth_factor

    def append(self, value):
        self._validate_type(value)
        if self.size == self.capacity:
            self._resize()
        self.internal_array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        self._validate_type(value)
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize()
        for i in range(self.size, index, -1):
            self.internal_array[i] = self.internal_array[i - 1]
        self.internal_array[index] = value
        self.size += 1

    def delete(self, index):
        self._validate_index(index)
        for i in range(index, self.size - 1):
            self.internal_array[i] = self.internal_array[i + 1]
        self.internal_array[self.size - 1] = None
        self.size -= 1

    def search(self, value):
        self._validate_type(value)
        for i in range(self.size):
            if self.internal_array[i] == value:
                return i
        raise ValueNotFound(value)

    def remove(self, value):
        index = self.search(value)
        self.delete(index)

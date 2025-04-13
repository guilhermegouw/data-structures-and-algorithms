from .base_array import BaseArray
from .exceptions import ValueNotFound


class OrderedArray(BaseArray):
    def __init__(self, data_type):
        super().__init__(data_type, 2)
        self.growth_factor = 2

    def _insert(self, index, value):
        self._validate_type(value)
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize()
        for i in range(self.size, index, -1):
            self.internal_array[i] = self.internal_array[i - 1]
        self.internal_array[index] = value
        self.size += 1

    def _resize(self):
        new_array = [None] * (self.capacity * self.growth_factor)
        for i in range(self.size):
            new_array[i] = self.internal_array[i]
        self.internal_array = new_array
        self.capacity *= self.growth_factor

    def _delete(self, index):
        self._validate_index(index)
        for i in range(index, self.size - 1):
            self.internal_array[i] = self.internal_array[i + 1]
        self.internal_array[self.size - 1] = None
        self.size -= 1

    def remove(self, value):
        index = self.search(value)
        self._delete(index)

    def add(self, value):
        self._validate_type(value)
        for i in range(self.size):
            if self.internal_array[i] > value:
                self._insert(i, value)
                return
        self._insert(self.size, value)

    def search(self, value):
        left = 0
        right = self.size - 1
        while left <= right:
            middle = (left + right) // 2
            if value > self[middle]:
                left = middle + 1
            elif value < self[middle]:
                right = middle - 1
            else:
                return middle
        raise ValueNotFound(value)

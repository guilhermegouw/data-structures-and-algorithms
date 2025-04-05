class DynamicArray:
    def __init__(self, data_type) -> None:
        if not isinstance(data_type, type):
            raise TypeError("data_type must be a valid Python type.")
        self.data_type = data_type
        self.capacity = 2
        self.internal_array = [None] * self.capacity
        self.size = 0
        self.growth_factor = 2

    def __getitem__(self, index):
        self._validate_index(index)
        return self.internal_array[index]

    def __setitem__(self, index, value):
        self._validate_index(index)
        self._validate_type(value)
        self.internal_array[index] = value

    def _validate_index(self, index):
        if index not in range(self.size):
            raise IndexError("Index out of bounds")

    def _validate_type(self, value):
        if not isinstance(value, self.data_type):
            raise TypeError(
                f"DynamicArray expect type: {self.data_type}"
                + f" but got: {type(value)}"
            )

    def _resize(self):
        new_array = [None] * (self.capacity * self.growth_factor)
        for i in range(self.capacity):
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
        for i in range(self.size - 1):
            self.internal_array[i] = self.internal_array[i + 1]
        self.internal_array[self.size - 1] = None
        self.size -= 1

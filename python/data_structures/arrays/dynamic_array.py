class DynamicArray:
    def __init__(self, data_type) -> None:
        if not isinstance(data_type, type):
            raise TypeError("data_type must be a valid Python type.")
        self.data_type = data_type
        self.capacity = 2
        self.internal_array = [None] * self.capacity
        self.size = 0
        self.growth_factor = 2

    def append(self, value):
        if not isinstance(value, self.data_type):
            raise TypeError(
                f"Expected type {self.data_type}, got {type(value)}"
            )
        if self.size == self.capacity:
            self._resize()
        self.internal_array[self.size] = value
        self.size += 1

    def _resize(self):
        new_array = [None] * (self.capacity * self.growth_factor)
        for i in range(self.capacity):
            new_array[i] = self.internal_array[i]
        self.internal_array = new_array
        self.capacity *= self.growth_factor

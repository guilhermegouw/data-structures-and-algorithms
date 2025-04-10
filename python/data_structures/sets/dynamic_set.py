class DynamicSet:
    def __init__(self, data_type):
        if not isinstance(data_type, type):
            raise TypeError("data_type must be a valid Python type")
        self.capacity = 2
        self.internal_array = [None] * self.capacity
        self.size = 0
        self.data_type = data_type
        self.growth_factor = 2

    def __getitem__(self, index):
        self._validate_index(index)
        return self.internal_array[index]

    def __setitem__(self, index, value):
        self._validate_index(index)
        self._validate_type(value)
        if value != self.internal_array[index]:
            self._check_if_value_already_exists(value)
        self.internal_array[index] = value

    def __len__(self):
        return self.size

    def __eq__(self, other):
        if isinstance(other, DynamicSet) or isinstance(other, list):
            if len(self) != len(other):
                return False
            for i in range(self.size):
                if self[i] != other[i]:
                    return False
            return True
        return NotImplemented

    def _validate_type(self, value):
        if not isinstance(value, self.data_type):
            raise TypeError(
                f"Expected type {self.data_type}, got {type(value)}"
            )

    def _validate_index(self, index):
        if index not in range(self.size):
            raise IndexError("Index out of range")

    def _check_if_value_already_exists(self, value):
        if value in self.internal_array[: self.size]:
            raise ValueError(f"The value {value} already exists")

    def _resize(self):
        new_array = [None] * (self.capacity * self.growth_factor)
        for i in range(self.size):
            new_array[i] = self.internal_array[i]
        self.internal_array = new_array
        self.capacity *= self.growth_factor

    def append(self, value):
        self._validate_type(value)
        self._check_if_value_already_exists(value)
        if self.size == self.capacity:
            self._resize()
        self.internal_array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        self._validate_type(value)
        self._check_if_value_already_exists(value)
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
        self.internal_array[self.size] = None
        self.size -= 1


if __name__ == "__main__":
    dynamic_set = DynamicSet(int)
    dynamic_set.append(1)
    dynamic_set.insert(0, 2)

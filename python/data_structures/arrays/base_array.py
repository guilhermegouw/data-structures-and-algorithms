class BaseArray:
    def __init__(self, data_type, capacity=2):
        if not isinstance(data_type, type):
            raise TypeError("data_type must be a valid Python type")
        if capacity <= 0:
            raise ValueError("Array capacity must be greater than 0.")
        self.data_type = data_type
        self.capacity = capacity
        self.size = 0
        self.internal_array = [None] * self.capacity

    def __getitem__(self, index):
        self._validate_index(index)
        return self.internal_array[index]

    def __setitem__(self, index, value):
        self._validate_index(index)
        self._validate_type(value)
        self.internal_array[index] = value

    def __len__(self):
        return self.size

    def __eq__(self, other):
        if isinstance(other, BaseArray) or isinstance(other, list):
            if len(self) != len(other):
                return False
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True
        return NotImplemented

    def __iter__(self):
        for i in range(self.size):
            yield self.internal_array[i]

    def __str__(self):
        return str(self.internal_array)

    def _validate_type(self, value):
        if not isinstance(value, self.data_type):
            raise TypeError(
                f"Expect type: {self.data_type} got type: {type(value)}"
            )

    def _validate_index(self, index):
        if index not in range(self.size):
            raise IndexError("Index out of bound")

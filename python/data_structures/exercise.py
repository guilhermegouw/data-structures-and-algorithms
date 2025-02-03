class StaticArray:
    def __init__(self, size: int, data_type: type) -> None:
        if size <= 0:
            raise ValueError("The size of the array must be greater than 0.")
        if not isinstance(data_type, type):
            raise TypeError("data_type must be a valid Python type.")

        self.size = size
        self.data_type = data_type
        self.elements = [None] * size
        self.current_count = 0

    def _validate_index(self, index: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds.")

    def _validate_type(self, value):
        if not isinstance(type(value), type):
            raise TypeError("Expected type: {data_type}, got {type(value)}")

    def __getitem__(self, index: int):
        self._validate_index(index)
        return self.elements[index]

    def __setitem__(self, index: int, value):
        self._validate_index(index)
        self._validate_type(value)
        self.elements[index] = value

    def insert(self, index: int, value):
        if self.current_count >= self.size:
            raise OverflowError("Array is full.")
        self._validate_index(index)
        self._validate_type(value)
        for i in range(index, self.size - 1):
            self.elements[i] = self.elements[i - 1]

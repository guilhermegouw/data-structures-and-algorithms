class DynamicArray:
    def __init__(self, data_type) -> None:
        if not isinstance(data_type, type):
            raise TypeError("data_type must be a valid Python type.")
        self.data_type = data_type
        self.capacity = 2
        self.internal_array = [None] * self.capacity
        self.size = 0
        self.growth_factor = 2

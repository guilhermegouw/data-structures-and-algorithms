class ValueNotFound(Exception):
    def __init__(self, value):
        self.value = value
        self.message = f"The value {self.value} was not found"
        super().__init__(self.message)

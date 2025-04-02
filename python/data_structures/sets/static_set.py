"""
Challenge: Static Set Implementation

Description
Implement a Static Set data structure that mimics traditional fixed-size
sets.
This implementation should enforce the fundamental characteristics of sets
while providing basic sets operations.

Core Characteristics
- Fixed size (defined at initialization)
- Homogeneous elements (single data type)
- Index-based access (0-based indexing)
- No dynamic resizing
- No repeated items

Required Operations
1. Initialize
   - Create set with specified size and data type
   - Should validate size and type parameters

2. Access - O(1)
   - Get element at given index
   - Should handle out-of-bounds errors

3. Update - O(1)
   - Set element at given index
   - Should validate element type
   - Should validate element doesn't already exists
   - Should handle out-of-bounds errors

4. Search - O(n)
   - Find index of given element
   - Return -1 if element not found

Additional Requirements
- Proper error handling for all edge cases
- Type checking for homogeneous elements
- Bounds checking for all operations
- Clear error messages

Example Usage

Initialize set of size 5 for integers
arr = StaticSet(5, int)

Access and update
value = set[0]    # value = 1
set[0] = 10      # [10, 2, None, None, None]

Search
index = set.search(2)  # index = 1
"""


class ItemAlreadyExistsError(Exception):
    """Exception raised when attempting to add an item that already exists in the StaticSet."""

    def __init__(self, item, message=None):
        self.item = item
        self.message = message or f"Item '{item}' already exists in the set"
        super().__init__(self.message)


class StaticSet:
    def __init__(self, size, data_type) -> None:
        if size <= 0:
            raise ValueError("Set size must be greater than 0.")
        if not isinstance(data_type, type):
            raise TypeError(
                "data_type must be a valid type, e.g., int, float, str."
            )
        self.size = size
        self.data_type = data_type
        self.elements = [None] * self.size

    def _validate_index(self, index):
        if index not in range(self.size):
            raise IndexError("Index out of bounds.")

    def _validate_type(self, value):
        if not isinstance(value, self.data_type):
            raise TypeError(
                f"Expected type {self.data_type}, got {type(value)}"
            )

    def _validate_item_not_repeated(self, value):
        if value in self.elements:
            raise ItemAlreadyExistsError(value)

    def __getitem__(self, index):
        self._validate_index(index)
        return self.elements[index]

    def __setitem__(self, index, value):
        self._validate_index(index)
        self._validate_type(value)
        self._validate_item_not_repeated(value)
        self.elements[index] = value

    def search(self, value):
        for i in range(self.size):
            if self.elements[i] == value:
                return i
        return -1

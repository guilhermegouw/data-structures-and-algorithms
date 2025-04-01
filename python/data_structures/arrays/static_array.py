"""
Challenge: Static Array Implementation

Description
Implement a Static Array data structure that mimics traditional fixed-size
arrays.
This implementation should enforce the fundamental characteristics of arrays
while providing basic array operations.

Core Characteristics
- Fixed size (defined at initialization)
- Homogeneous elements (single data type)
- Index-based access (0-based indexing)
- No dynamic resizing

Required Operations
1. Initialize
   - Create array with specified size and data type
   - Should validate size and type parameters

2. Access - O(1)
   - Get element at given index
   - Should handle out-of-bounds errors

3. Update - O(1)
   - Set element at given index
   - Should validate element type
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

Initialize array of size 5 for integers
arr = StaticArray(5, int)

Access and update
value = arr[0]    # value = 1
arr[0] = 10      # [10, 2, None, None, None]

Search
index = arr.search(2)  # index = 1
"""


class StaticArray:
    def __init__(self, size, datatype) -> None:
        if size <= 0:
            raise ValueError("Array size must be greater than 0.")
        if not isinstance(datatype, type):
            raise TypeError(
                "datatype must be a valid type, e.g., int, float, str."
            )
        self.size = size
        self.data_type = datatype
        self.elements = [None] * size

    def _validate_index(self, index):
        if index not in range(self.size):
            raise IndexError("Index out of bounds.")

    def _validate_type(self, value):
        if not isinstance(value, self.data_type):
            raise TypeError(
                f"Expected type {self.data_type}, got {type(value)}"
            )

    def __getitem__(self, index):
        self._validate_index(index)
        return self.elements[index]

    def __setitem__(self, index, value):
        self._validate_index(index)
        self._validate_type(value)
        self.elements[index] = value

    def search(self, value):
        for i in range(self.size):
            if self.elements[i] == value:
                return i
        return -1

    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":
    arr = StaticArray(5, int)
    print(arr)
    print(arr[0])
    arr[0] = 10
    print(arr)
    print(arr.search(2))

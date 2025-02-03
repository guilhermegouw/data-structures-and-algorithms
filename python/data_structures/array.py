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

5. Insert
   - Add element at specified index
   - Should track current number of elements
   - Should handle array full condition
   - Should handle type validation

6. Delete
   - Remove element at specified index
   - Should handle out-of-bounds errors
   - Should shift remaining elements

Additional Requirements
- Proper error handling for all edge cases
- Type checking for homogeneous elements
- Bounds checking for all operations
- Clear error messages

Example Usage

Initialize array of size 5 for integers
arr = StaticArray(5, int)

Insert elements
arr.insert(0, 1)  # [1, None, None, None, None]
arr.insert(1, 2)  # [1, 2, None, None, None]

Access and update
value = arr[0]    # value = 1
arr[0] = 10      # [10, 2, None, None, None]

Search
index = arr.search(2)  # index = 1

Delete
arr.delete(0)    # [2, None, None, None, None]
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
        self.current_count = 0

    def _validate_index(self, index):
        if index < 0 or index >= self.size:
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

    def insert(self, index, value):
        if self.current_count >= self.size:
            raise OverflowError("Array is full...")
        self._validate_index(index)
        self._validate_type(value)
        for i in range(self.current_count, index, -1):
            self.elements[i] = self.elements[i - 1]
        self.elements[index] = value
        self.current_count += 1

    def delete(self, index):
        self._validate_index(index)
        if self.current_count == 0:
            raise IndexError("Cannot delete from an empty array.")
        for i in range(index, self.current_count - 1):
            self.elements[i] = self.elements[i + 1]
        self.elements[self.current_count - 1] = None
        self.current_count -= 1

    def search(self, value):
        for i in range(self.current_count):
            if self.elements[i] == value:
                return i
        return -1

    def __str__(self):
        return str(self.elements[: self.current_count])


if __name__ == "__main__":
    arr = StaticArray(5, int)
    arr.insert(0, 1)  # [1, None, None, None, None]
    arr.insert(1, 2)  # [1, 2, None, None, None]
    print(arr)  # Output: [1, 2]
    print(arr[0])  # Access element at index 0 -> 1
    arr[0] = 10  # Update element at index 0 -> [10, 2, None, None, None]
    print(arr)  # Output: [10, 2]
    print(arr.search(2))  # Search for 2 -> 1
    arr.delete(0)  # Delete element at index 0 -> [2, None, None, None, None]
    print(arr)  # Output: [2]

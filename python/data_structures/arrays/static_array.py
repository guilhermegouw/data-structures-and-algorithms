"""
Challenge: Static Array Implementation

Description
Implement a Static Array data structure that mimics traditional fixed-size
arrays.
This implementation should enforce the fundamental characteristics of arrays
while providing basic array operations.

Core Characteristics
- Fixed size (defined at initialization)
- Homogeneous internal_array (single data type)
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
- Type checking for homogeneous internal_array
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

from .base_array import BaseArray


class StaticArray(BaseArray):
    def __init__(self, datatype, capacity):
        super().__init__(datatype, capacity)
        self.size = capacity

    def search(self, value):
        for i in range(self.size):
            if self.internal_array[i] == value:
                return i
        return -1

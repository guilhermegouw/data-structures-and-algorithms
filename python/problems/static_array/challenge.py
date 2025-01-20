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

3. Update** - O(1)
   - Set element at given index
   - Should validate element type
   - Should handle out-of-bounds errors

4. Search** - O(n)
   - Find index of given element
   - Return -1 if element not found

5. Insert**
   - Add element at specified index
   - Should track current number of elements
   - Should handle array full condition
   - Should handle type validation

6. Delete**
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


class Array:
    def __init__(self, size, dtype):
        self.size = size
        self.dtype = dtype

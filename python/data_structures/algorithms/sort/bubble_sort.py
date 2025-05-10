"""
Bubble Sort:
- The algorithm makes multiple passes through the array
- In each pass:
  - Starting from index 0, it compares adjacent elements
  - If the current element is greater than the next element:
    - Swap the elements
    - Record that a swap occurred
  - Move to the next pair of elements
- After each pass:
  - The largest unsorted element will have "bubbled up" to its correct position
  - We can reduce our search space by excluding the last sorted element
- If no swaps occurred during a pass, the array is already sorted and we can
stop
"""
from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    is_sorted = False
    limit = len(array) - 1
    while not is_sorted:
        swaps = 0
        for i in range(limit):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps += 1
        limit -= 1
        if swaps == 0:
            is_sorted = True
    return array

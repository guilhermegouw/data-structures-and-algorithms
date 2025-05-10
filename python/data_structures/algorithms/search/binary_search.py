from typing import List, Optional


def binary_search(array: List[int], value: int) -> Optional[int]:
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == value:
            return middle
        elif value > array[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return None

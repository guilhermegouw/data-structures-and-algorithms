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

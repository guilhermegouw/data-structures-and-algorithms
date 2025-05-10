"""
Selection Sort:
  - The algorithm divides the array into two portions: sorted (initially empty)
  and unsorted (initially the entire array)
  - In each pass:
    - It starts with the first element of the unsorted portion (initially
    index 0)
    - It identifies the smallest element in the unsorted portion by:
      - Setting the first unsorted element as the current minimum
      - Comparing each remaining unsorted element with the current minimum
      - Updating the minimum if a smaller element is found
    - After examining the entire unsorted portion, it swaps the identified
    minimum with the first element of the unsorted portion
    - The sorted portion grows by one element, and the process repeats
  - The algorithm continues until the entire array is sorted (the unsorted
    portion becomes empty)
"""


def selection_sort(array: list) -> list:
    for i in range(len(array)):
        lowest_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_idx]:
                lowest_idx = j
        if lowest_idx != i:
            array[i], array[lowest_idx] = array[lowest_idx], array[i]
    return array

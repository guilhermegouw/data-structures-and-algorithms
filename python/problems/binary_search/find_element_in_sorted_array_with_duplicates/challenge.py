"""
Challenge: Find Element in Sorted Array with Duplicates

Given a sorted array of integers and a target integer, find the first
occurrence of the target and return its index.
Return -1 if the target is not in the array.

Input:
    arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
    target = 3
Output: 1
Explanation: The first occurrence of 3 is at index 1.

Input:
    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6
Output: -1
Explanation: 6 does not exist in the array.
"""


def find_element_in_sorted_array_with_duplicates(array, target):
    position = -1
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            position = middle
            right = middle - 1
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return position


find_element_in_sorted_array_with_duplicates([1, 1, 2], 2)

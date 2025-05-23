"""
Challenge: Find Minimum in Rotated Sorted Array

A sorted array of unique integers was rotated at an unknown pivot.
For example:
    [10, 20, 30, 40, 50] -> [30, 40, 50, 10, 20].

Find the index of the minimum element in this array.

Input:
    [30, 40, 50, 10, 20]
Output:
    3

Explanation: The smallest element is 10, and its index is 3.

Input:
    [3, 5, 7, 11, 13, 17, 19, 2]

Output:
    7

Explanation: The smallest element is 2, and its index is 7.
"""

# # Pythonic
# def find_minimum_in_rotated_sorted_array(array):
#     return array.index(min(array))


def find_minimum_in_rotated_sorted_array(array):
    position = -1
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] <= array[-1]:
            right = middle - 1
            position = middle
        else:
            left = middle + 1
    return position


find_minimum_in_rotated_sorted_array([3, 5, 7, 11, 13, 17, 19, 2])

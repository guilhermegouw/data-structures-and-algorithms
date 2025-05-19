"""
Challenge: First Element Not Smaller Than Target

Given an array of integers sorted in increasing order and a target, find the
index of the first element in the array that is larger than or equal to the
target.
Assume that it is guaranteed to find a satisfying number.

Input:
    arr = [1, 3, 3, 5, 8, 8, 10]
    target = 2
Output:
    1

Explanation: The first element larger than 2 is 3, which has index 1.

Input:
    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6
Output:
    3

Explanation: The first element larger than 6 is 7, which has index 3.
"""


def first_element_not_smaller_than_target(arr, target):
    index = -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] >= target:
            index = middle
            right = middle - 1
        else:
            left = middle + 1
    return index

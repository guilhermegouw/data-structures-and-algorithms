"""
Challenge: Find the First True in a Sorted Boolean Array

An array of boolean values is divided into two sections:
    - The left section consists of all false
    - The right section consists of all true.

Find the First True in a Sorted Boolean Array of the right section,
i.e., the index of the first true element.
If there is no true element, return -1.

Input: arr = [false, false, true, true, true]
Output: 2

Explanation: The first true's index is 2.
"""


def find_the_first_true_in_a_sorted_boolean_array(array):
    index = -1
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] is True:
            index = middle
            right = middle - 1
        else:
            left = middle + 1
    return index

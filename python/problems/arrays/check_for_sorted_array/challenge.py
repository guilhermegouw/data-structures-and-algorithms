"""
Write a function that determines if the array is sorted 
in ascending order.

input:
[1, 3, 5, 6, 7]
output:
True

input:
[1, 2, 5, 4, 6]
output:
False
"""


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def pythonic_is_sorted(arr):
    return all([arr[i] <= arr[i + 1] for i in range(len(arr) - 1)])

"""
Write a function to find the largest and smallest elements 
in an array.

input:
[1, 2, 3, 4, 5]

output:
(5, 1)
"""


def get_max_and_min(arr):
    min_value = float("inf")
    max_value = float("-inf")
    for num in arr:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    return (max_value, min_value)


def pythonic_get_max_and_min(arr):
    return (max(arr), min(arr))

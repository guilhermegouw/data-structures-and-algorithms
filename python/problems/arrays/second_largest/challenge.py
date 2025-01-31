"""
Find the Second Largest Element
Write a function to find the second largest element in an array.

Input:
    [1, 2, 3, 4, 5]

Output:
    4
"""


def get_second_largest(arr):
    if not arr or len(arr) < 2:
        return None
    largest = float("-inf")
    second_largest = float("-inf")
    for item in arr:
        if item > largest:
            second_largest = largest
            largest = item
        elif item > second_largest:
            second_largest = item
    return second_largest if second_largest != float("-inf") else None


get_second_largest([4, 1, 2, 3])

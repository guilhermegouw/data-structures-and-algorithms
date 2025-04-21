"""
Challenge: Has Duplicates
Level: Easy
Description: Write a function that takes a list and returns
if the list contains duplicated values or not.

Input:
    [1, 3, 5, 7, 9, 0, 1] The number 1 appears at the beginning
    and at the end so, it has duplicates.
Output:
    True
"""


# def has_duplicates(array: list) -> bool:
#     """
#     Quadratic Solution
#     """
#     for i in range(len(array)):
#         for j in range(i+1, len(array)):
#             if array[i] == array[j]:
#                 return True
#     return False


# def has_duplicates(array: list) -> bool:
#     """
#     Set Solution
#     """
#     uniques = set(array)
#     return len(array) > len(uniques)


def has_duplicates(array: list) -> bool:
    """
    Uniques dict Solution O(N)
    """
    uniques = {}
    for item in array:
        if item in uniques:
            return True
        else:
            uniques[item] = True
    return False

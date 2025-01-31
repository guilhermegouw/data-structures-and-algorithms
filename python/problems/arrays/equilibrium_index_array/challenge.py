"""
The equilibrium index in an array is an index where the sum of the elements
to the left of the index is equal to the sum of the elements to the right of the index.
If there is no such index, return []

Example:
Input: A = [-7, 1, 5, 2, -4, 3, 0]
Output: [3, 6]
Explanation:

At index 3, left sum is (-7 + 1 + 5) = -1 and right sum is (-4 + 3 + 0) = -1.
At index 6, left sum is (-7 + 1 + 5 + 2 - 4 + 3) = 0 and right sum is 0.
Input: A = [1, 2, 3]
Output: -1 (no equilibrium index)
"""


def naive_get_equilibrium_indexes(lst):
    equilibrium_indexes = []
    for i in range(len(lst)):
        leftSum = sum(lst[:i])
        rightSum = sum(lst[i + 1 :])
        if leftSum == rightSum:
            equilibrium_indexes.append(i)
    return equilibrium_indexes


def get_equilibrium_indexes(lst):
    equilibrium_indexes = []
    total_sum = sum(lst)
    left_sum = 0

    for i in range(len(lst)):
        right_sum = total_sum - left_sum - lst[i]
        if left_sum == right_sum:
            equilibrium_indexes.append(i)
        left_sum += lst[i]
    return equilibrium_indexes

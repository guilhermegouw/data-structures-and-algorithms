"""
Challenge: Rotate An Array
Level: Medium

Write a function that takes an array and a k integer and, returns an array
rotated to the right by k steps.

When you rotate an array to the right, each element shifts one position to the
right, and the last element moves to the first position. You repeat this
process k times.

Input:
    nums = [1, 2, 3, 4, 5]
    k = 1

Output = [5, 1, 2, 3, 4]
"""

from collections import deque

# First solution
# def rotate_to_the_right_k_times(arr: list[int], k: int) -> list[int]:
#     for _ in range(k):
#         last_item = arr.pop()
#         arr.insert(0, last_item)
#     return arr


# Second solution
def rotate_to_the_right_k_times(arr: list[int], k: int) -> list[int]:
    dq = deque(arr)
    dq.rotate(k % len(arr))
    return list(dq)

"""
Challenge: Square Root Estimation

Given an integer, find its square root without using the built-in square root
function. Only return the integer part (truncate the decimals).

Input:
    16
Output:
    4

Input:
    8
Output:
    2

Explanation: square root of 8 is 2.83..., return the integer part, 2
"""


def square_root_estimation(num):
    """
    The square root of a number will always be equals or smaller than the
    number it self.
    It searches for the value within the interval (0 - number) that
    multiplied by it self is closest to the number.
    """
    int_square_root = 0
    left = 0
    right = num
    while left <= right:
        middle = (left + right) // 2
        if int(middle * middle) <= num:
            int_square_root = middle
            left = middle + 1
        else:
            right = middle - 1
    return int_square_root

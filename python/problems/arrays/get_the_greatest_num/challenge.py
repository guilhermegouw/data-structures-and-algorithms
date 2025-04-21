"""
Challenge: Greatest Number
Level: Easy
Description: Write a function that takes an array of integers
and returns the greatest.

Input: [9, 1, 8, 2, 7, 4]
Output: 9
"""


def greatest_number(array: list) -> int:
    greatest_num = array[0]
    for num in array:
        if num > greatest_num:
            greatest_num = num
    return greatest_num

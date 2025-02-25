"""
Challlenge: Move Element To End
Level: Medium

You're given an array of integers and an integer. Write a function that moves
all instances of that integer in the array to the end of the array and returns
the array.
The function should perform this in place(it should mutate the input array)
and doesn't need to maintain the order of the other integers.

Input:
array = [2, 1, 2, 2, 2, 3, 4, 2]
to_move = 2

Output:
[1, 3, 4, 2, 2, 2, 2, 2]
"""


def move_element_to_end(arr, to_move):
    new_arr = [element for element in arr if element != to_move]
    targets = len(arr) - len(new_arr)
    return new_arr + [to_move] * targets

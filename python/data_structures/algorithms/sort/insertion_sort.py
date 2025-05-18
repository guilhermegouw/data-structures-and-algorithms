"""
Insertion Sort:
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        to_insert = array[i]
        position = i - 1
        while position >= 0 and array[position] > to_insert:
            array[position + 1] = array[position]
            position -= 1
        array[position + 1] = to_insert
    return array


insertion_sort([9, 2, 8, 3, 7, 4, 6, 5, 1])

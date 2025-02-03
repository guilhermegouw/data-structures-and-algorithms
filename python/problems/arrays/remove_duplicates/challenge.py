"""
Challenge: Remove Duplicates from Sorted Array
Level: Easy

Return a new array with duplicates removed, preserving order.

Input:
[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

Output:
[1, 2, 3, 4]
"""


def remove_duplicates(arr):
    if not arr:
        return []
    uniques = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != uniques[-1]:
            uniques.append(arr[i])
    return uniques


"""
In Place solution:

[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

If iterate from i = 0  until the last element.
i = 0 => arr[0] = 1 => arr[0 + 1] = 2
arr[0] != arr[1] => i ++

i = 1 => arr[1] = 2 => arr[1 + 1] = 2
arr[1] == arr[2] => remove(arr[i])

arr = [1, 2, 3, 3, 3, 4, 4, 4, 4]
i = 1 => arr[1] = 2 => arr[1 + 1] = 3
arr[1] != arr[2] => i += 1

arr = [1, 2, 3, 3, 4, 4, 4, 4]
i = 2 => arr[2] = 3 => arr[2 + 1] = 3
arr[2] == arr[3] => remove(arr[i])

arr = [1, 2, 3, 4, 4, 4, 4]
i = 2 => arr[2] = 3 => arr[2 + 1] = 4
arr[2] != arr[3] => i += 1

arr = [1, 2, 3, 4, 4, 4, 4]
i = 3 => arr[3] = 4 => arr[3 + 1] = 4
arr[3] == arr[4] => remove(arr[i])

arr = [1, 2, 3, 4, 4, 4]
i = 3 => arr[3] = 4 => arr[3 + 1] = 4
arr[3] == arr[4] => remove(arr[i])

arr = [1, 2, 3, 4, 4]
i = 3 => arr[3] = 4 => arr[3 + 1] = 4
arr[3] == arr[4] => remove(arr[i])

arr = [1, 2, 3, 4]
i = 3 => arr[3] = 4 => arr[3 + 1] = doesn't exists
stop return arr
"""


# def in_place_remove_duplicates(arr):  # Inefficient use of arr.remove()
#     i = 0
#     while i < len(arr) - 1:
#         if arr[i] == arr[i + 1]:
#             arr.remove(arr[i])
#         else:
#             i += 1
#     return arr

"""
[1, 2, 2, 3, 4, 4, 4, 5]

write_pos = 1
read_pos = 1
if arr[read_pos] != arr[write_pos -1] => 2 != 1
    arr[write_pos] = arr[read_pos]
    write_pos += 1
    read_pos += 1
else:
    read_pos += 1


read_pos = 1
write_pos = 1
2 != 1 => write_pos += 1, read_pos += 1, arr[write_pos] = 2, arr[read_pos] = 2

read_pos = 2
write_pos = 2
2 == 2 => read_pos += 1

read_pos = 3
write_pos = 2
3 != 2 => write_pos += 1, read_pos += 1, arr[2] = 2, arr[3] = 3
[1, 2, 3, 3, 4, 4, 4, 5]

read_pos = 4
write_pos = 3
4 != 3 => write_pos += 1, read_pos += 1, arr[3] = 3, arr[4] = 4
[1, 2, 3, 4, 4, 4, 4, 5]

read_pos = 5
write_pos = 4
4 == 4 => read_pos += 1
[1, 2, 3, 4, 4, 4, 4, 5]

read_pos = 6
write_pos = 4
4 == 4 => read_pos += 1
[1, 2, 3, 4, 4, 4, 4, 5]

read_pos = 7
write_pos = 4
5 != 4 => write_pos += 1, read_pos += 1, arr[4] = 4, arr[7] = 5
[1, 2, 3, 4, 5, 4, 4, 5]

return arr[:write_pos] => arr[:5] => [1, 2, 3, 4, 5]
"""


def in_place_remove_duplicates(arr):
    if not arr:
        return []

    write_idx = 1
    for read_idx in range(1, len(arr)):
        if arr[read_idx] != arr[write_idx - 1]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    return arr[:write_idx]

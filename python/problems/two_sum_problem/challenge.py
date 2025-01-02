"""
Write a function that takes in a non-empty array of disctinct integers and an 
integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers 
in the array; you can't add a single integer to itself in order to obtain the 
target sum.

You can assume that there will be at most one pair of numbers summing up to
the target sum.

SAMPLE INPUT:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

SAMPLE OUTPUT:
[-1, 11]
"""

"""
BRUTE FORCE

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

(First element)
3 + 5 = 8 => 8 != 10
3 + -4 = -1 => -1 != 10
3 + 8 = 11 => 11 != 10
3 + 11 = 14 => 14 != 10
3 + 1 = 4 => 4 != 10
3 + -1 = 2 => 2 != 10
3 + 6 = 9 => 9 != 10

(Second element)
5 + -4 = 1 => 1 != 10
5 + 8 = 13 => 13 != 10
5 + 11 = 16 => 16 != 10
5 + 1 = 6 => 6 != 10
5 + -1 = 4 => 4 != 10
5 + 6 = 11 => 11 != 10

(Third element)
-4 + 8 = 4 => 4 != 10
-4 + 11 = 7 => 7 != 10
-4 + 1 = -3 => -3 != 10
-4 + -1 = -5 => -5 != 10
-4 + 6 = 2 => 2 != 10

(Fourth element)
8 + 11 = 19 => 19 != 10
8 + 1 = 9 => 9 != 10
8 + -1 = 7 => 7 != 10
8 + 6 = 14 => 14 != 10

(Fifth element)
11 + 1 = 12 => 12 != 10
11 + -1 = 10 => 10 == 10 => return [11, -1]
"""


# def get_sum_of_two(arr, target_sum):
#     for i in range(len(arr) - 1):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target_sum:
#                 return [arr[i], arr[j]]
#     return []
#
"""
2 POINTER TECHNIQUE

CASE 1:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

Sort the array: [-4, -1, 1, 3, 5, 6, 8, 11]

target = 10
pointer_left = -4
pointer_right = 11
target - pointer_left => 10 -(-4) = 14 > pointer_right (11)

target = 10
pointer_left = -1
pointer_right = 11
target - pointer_left => 10 -(-1) = 11 == pointer_right (11)
return [pointer_left, pointer_right]

CASE 2:
array = [1, 2, 3]
targetSum = 5

Sort the array: [1, 2, 3]

target = 5
pointer_left = 1
pointer_right = 3
target - pointer_left => 5 - 1 = 4 > pointer_right (3)

target = 5
pointer_left = 2
pointer_right = 3
target - pointer_left => 5 - 2 = 3 == pointer_right (3)
return [pointer_left, pointer_right]
"""

#
# def get_sum_of_two(arr, target_sum):
#     arr.sort()
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target_sum:
#             return [arr[left], arr[right]]
#         elif current_sum < target_sum:
#             left += 1
#         else:
#             right -= 1
#     return []

"""
USING A SET

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
seen = {}
i = 0
array[i] = 3 => 3 or target_sum - array[i] not in seen  => seen.add(array[i])
set{3}

i = 1
array[i] = 5 => 5 or target_sum - array[i] not in seen  => seen.add(array[i])
set{3, 5}

i = 2
array[i] = -4 => -4 or target_sum - array[i] not in seen  => seen.add(array[i])
set{3, 5, -4}

i = 3
array[i] = 8 => 8 or target_sum - array[i] not in seen  => seen.add(array[i])
set{3, 5, -4, 8}

i = 4
array[i] = 11 => 11 or target_sum - array[i] not in seen  => seen.add(array[i])
set{3, 5, -4, 8, 11}

i = 5
array[i] = 1 => 1 or target_sum - array[i] not in seen  => seen.add(array[i])
set{3, 5, -4, 8, 11, 1}

i = 6
array[i] = -1 => -1 not in seen but, 11 is!
return [array[i], target_sum - array[i]]
"""


def get_sum_of_two(arr, target_sum):
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return [num, complement]
        seen.add(num)
    return []


get_sum_of_two([1, 2, 3], 5)

"""
Challenge: Validate Subsequence
Level: Easy

Description:
Given two-non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent
in the array but that are in the same order as they appear in the array.
For instance:
The numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so the
numbers [2, 4]. Note that a single number in an array and the array itself are
both balid subsequences of the array.

Input:
array = [ 5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

Output:
True
"""


# def validate_subsequence(array, sequence):
#     array_idx = 0
#     sequence_idx = 0
#     while (
#             array_idx < len(array)
#             and sequence_idx < len(sequence)
#           ):
#         if sequence[sequence_idx] == array[array_idx]:
#             sequence_idx += 1
#             array_idx += 1
#             if sequence_idx == len(sequence):
#                 return True
#         else:
#             array_idx += 1
#     return False

# def validate_subsequence(array, sequence):
#     seq_idx = 0
#     for value in array:
#         if seq_idx == len(sequence):
#             return True
#         if sequence[seq_idx] == value:
#             seq_idx += 1
#     return seq_idx == len(sequence)

def validate_subsequence(array, sequence):
    seq_pos = 0
    for num in array:
        if seq_pos < len(sequence) and num == sequence[seq_pos]:
            seq_pos += 1
    return seq_pos == len(sequence)

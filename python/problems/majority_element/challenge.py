"""
Write a function that takes in a non-empty, unordered array of positive
integers and returns the array's majority element without sorting the array
and without using more than constant space.
An array's majority element is an element of the array that appears in over
half of its indices. Note that the most common element of an array(the element
that appears the most times in the array) isn't necessarily the array's
majority element;
For Example:
The arrays [3, 2, 2, 1] and [3, 4, 2, 2, 1]
Both have 2 as their most common element, yet neither of this arrays have a
majority element, because neither 2 nor any other element appears in over half
of the respective array's indices.
You can assume that the input array will always have a majority element.

Input: array = [1, 2, 3, 2, 2, 1, 2]
Output: 2 // 2 occurs in 4/7 array indices, making it the majority element.
"""

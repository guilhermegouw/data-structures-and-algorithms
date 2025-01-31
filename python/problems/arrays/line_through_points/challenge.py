"""
Challenge: Line Through Points
Level: Very Hard

You're giving an array of points plotted on a 2D graph (the xy-plane). Write a
function that returns the maximun number of points that a single line (or
potentialy multiple lines) on the graph passes through.
The input array will contain points represented ba an array of two integers
[x, y]. The input array will never contain duplicate points and will always
contain at least one point.

Input:

points = [
        [1, 1],
        [2, 2],
        [3, 3],
        [0, 4],
        [-2, 6],
        [4, 0],
        [2, 1],
    ]

Output: 4

A line passes though points: [-2, 6], [0, 4], [2, 2], [4, 0].
"""

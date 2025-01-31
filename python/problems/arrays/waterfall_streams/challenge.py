"""
Challenge: Waterfall Streams
Level: Very Hard

You're given a two-dimentional array that represents the structure of an indoor
waterfall and a positive integer that represents the column that the
waterfall's water source will start at. More specifically, the water source
will start directly above the structure and will flow downwards.

Each row in the array contains 0s and 1s, where a 0 represents a free space
and a 1 represents a block that water can't pass through. You can imagine that
the last row of the array contains buckets that the water will eventually flow
into; thus, the last row of the array will always contaim only 0s. You can also
You can also imagine that there are walls on both sides of the structure,
meaning that the water will never leave the structure; it will either be
trapped against a wall or flow into one of the buckets in the last row.

As water flows downwards, it it hits a block, it splits evenly to the left and
right-hand side of that block. In other words, 50% of the water flows left and
50% of the water flows right. If a water stream is unable to flow to the left
or to the right (because of a block or a wall), the water stream in question
becomes trapped and can no longer continue to flow in that direction; it
efectively get stuck at the structure and can no longer flow downwards, meaning
that 50% of the previous water stream is forever lost.

Lastly, the input array will always contain at least two rows and one column,
and the space directly bellow the water source (in the first row of the array)
will always be empty, allowing the water to start flowing downwards.

Write a function that returns the percentage of water inside of each of the
bottom buckets after the water has flowed though the entire structure.


Input:
    array = [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
        ]

Output: [0, 0, 0, 25, 25, 0, 0]


The water will flow as follows:
    [
        [0, 0, 0, ., 0, 0, 0]
        [1, ., ., ., ., ., 0]
        [0, ., 1, 1, 1, ., 0]
        [., ., ., ., ., ., .]
        [1, 1, 1, ., ., 1, 0]
        [0, 0, 0, ., ., 0, 1]
        [0, 0, 0, ., ., 0, 0]
    ]
"""

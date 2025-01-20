"""
Challenge: Sweet And Savory
You're hosting an event at a food festival and want to showcase the best
possible pairing of two dishes from the festival that complement each other's
flavor profile.
Each dish has a flavor profile represented by an integer. A negative integer
means a dish is sweet, while a positive integer means a dish is savory. The
absolute value of that integer represents the intensity of that flavor.
For example:
A flavor profile of -3 is slightly sweet, one of -10 is extremely sweet, one
of 2 is mildly savory, and one of 8 is significantly savory.
You're given an array of these dishes and a target combined flavor profile.
Write a function that return the best possible pairing two dishes (the pairing
with a total flavor profile that's closest to the target one).
Note that this pairing must include one sweet and one savory dish. You're also
concerned about about the dish being too savory, so your pairing should never
be more savory than the target profile.
All dishes will have a positive or negative flavor profile; there are no dishes
with a 0 value. For simplicity, you can assume that there will be at most one
best solution. If there isn't a valid solution, your function should
return [0, 0]. The returned array should be sorted, meaning the sweet dish
should always come first.

Input 1: dishes = [-3, -5, 1, 7] target = 8
Output 1: [-3, 7] // The combined profile of 4 is closest without going over.

Input 2: dishes = [3, 5, 7, 2, 6, 8, 1] target = 10
Output 2: [0, 0] // There are no sweet dishes.
"""

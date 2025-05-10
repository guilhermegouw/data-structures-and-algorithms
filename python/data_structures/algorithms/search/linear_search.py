def binary_search(array, value):
    left = 0
    right = len(array) - 1
    while left < right:
        middle = (left + right) // 2
        if value > array[middle]:
            left = middle + 1
        elif value < array[middle]:
            right = middle - 1
        elif value == array[middle]:
            return middle
    return -1

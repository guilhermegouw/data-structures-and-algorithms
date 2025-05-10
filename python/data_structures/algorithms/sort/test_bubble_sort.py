from bubble_sort import bubble_sort


def test_already_sorted_array():
    sorted_array = [0, 1, 2, 3, 4]
    assert bubble_sort(sorted_array) == sorted_array


def test_not_sorted_array():
    sorted_array = [0, 4, 2, 3, 1]
    assert bubble_sort(sorted_array) == [0, 1, 2, 3, 4]


def test_another_not_sorted_array():
    sorted_array = [4, 2, 7, 1, 3]
    assert bubble_sort(sorted_array) == [1, 2, 3, 4, 7]

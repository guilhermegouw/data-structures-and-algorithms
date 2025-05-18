from insertion_sort import insertion_sort


def test_already_sorted_array():
    sorted_array = [0, 1, 2, 3, 4]
    assert insertion_sort(sorted_array) == sorted_array


def test_not_sorted_array():
    sorted_array = [0, 4, 2, 3, 1]
    assert insertion_sort(sorted_array) == [0, 1, 2, 3, 4]


def test_another_not_sorted_array():
    sorted_array = [4, 2, 7, 1, 3]
    assert insertion_sort(sorted_array) == [1, 2, 3, 4, 7]

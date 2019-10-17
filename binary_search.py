# coding: utf-8

# пример простейшего примера бинарного поиска


def binary_search(sort_list, item):
    low = 0
    high = len(sort_list) - 1
    while low <= high:
        mid = (low + high) // 2

        if sort_list[mid] == item:
            return sort_list[mid]
        if sort_list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


sample_list = [1, 2, 5, 7, 9, 11, 23, 54, 87, 121, 123, 543]
print(binary_search(sample_list, 5412))

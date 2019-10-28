#! coding: utf-8

# простейшая реализация алгоритма быстрой сортировки


def quick_sort(arr):  # алгоритм быстрой сортировки. Опорным выбирается 0 элемент массива.
    if len(arr) <= 2:
        return arr
    else:
        basis = arr[0]
        less = [i for i in arr[1:] if i < basis]
        greater = [i for i in arr[1:] if i > basis]
        return quick_sort(less) + [basis] + quick_sort(greater)

test_arr = [34, 1, 12, 87, 33, 6]
print(quick_sort(test_arr))
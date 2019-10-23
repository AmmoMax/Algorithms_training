# coding: utf-8

# простейшая реализация алгоритма сортировки выбором.


def find_smallest(arr):  # функция поиска индекса наименьшего элемента в массиве
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index += i
    return smallest_index

test_arr = [23, 9, 232, 685, 3, 454, 12]
print(find_smallest(test_arr))
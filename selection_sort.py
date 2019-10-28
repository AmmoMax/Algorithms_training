# coding: utf-8

# простейшая реализация алгоритма сортировки выбором.
# Simple Selection Sort Algorithm

test_arr = [23, 9, 232, 685, 3, 454, 12]
test_arr2 = []
test_arr3 = [23]


def find_smallest(arr):  # функция поиска индекса наименьшего элемента в массиве
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):  # функция сортировки выбором
    res_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # находим наименьший элемент входного массива
        res_arr.append(arr.pop(smallest))  # добавляем наименьший элемент в финальный массив и удаляем из входного массива
    return res_arr


print(selection_sort(test_arr3))

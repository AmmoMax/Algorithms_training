# coding: utf-8

# Simple Selection Sort Algorithm

test_arr = [23, 9, 232, 685, 3, 454, 12]
test_arr2 = []
test_arr3 = [23]


def find_smallest(arr):  # find smallest element in array
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):  # Selection Sort function
    res_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # find smallest element of input array
        res_arr.append(arr.pop(smallest))  # add smallest to result and del from input array
    return res_arr


print(selection_sort(test_arr))

#! coding: utf-8

# простейшая реализация алгоритма быстрой сортировки

"""
TODO:
 сортировка массива со всеми одинаковыми элементами
 сортировка массива с несколькими одинаковыми элементами
"""

import cProfile
import random
import sys

sys.setrecursionlimit(100000)  # задаем параметр для определения максимальной глубины рекурсии

rr1 = random.randint(1, 1000)
rr2 = random.randint(1001, 3000)


test_arr_4 = [i for i in range(rr1, rr2)]
test_arr = [34, 1, 1, 87, 33, 6]
test_arr_2 = [1, 1, 1]


def quick_sort(arr):  # алгоритм быстрой сортировки. Опорным выбирается 0 элемент массива.
    if len(arr) < 2:
        return arr
    else:
        basis = arr[0]  # выбираем опорный элемент
        less = [i for i in arr[1:] if i <= basis]  # формируем список с элементами < опорного
        greater = [i for i in arr[1:] if i > basis]  # список с элементами > опорного
        return quick_sort(less) + [basis] + quick_sort(greater)  # возвращаем финальный список


print(f'len array: {len(test_arr_4)}')
cProfile.run("quick_sort(test_arr_4)")

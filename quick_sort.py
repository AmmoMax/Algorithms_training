#! coding: utf-8

# простейшая реализация алгоритма быстрой сортировки
# худший случай - O(n^2)
# средний случай - O(n * log n)

"""
TODO:

работа с большим входным размером. Например длиной > 100 000 элементов

"""

import cProfile
import random
import sys

sys.setrecursionlimit(100000)  # задаем параметр для определения максимальной глубины рекурсии

rr1 = random.randint(1, 10000)
rr2 = random.randint(10001, 15000)

test_arr = [i for i in range(rr1, rr2)]


def quick_sort_recur(arr):  # Вариант через рекурсию в функциональном виде
    if len(arr) <= 1:
        return arr
    else:
        # basis = random.choice(arr)  # выбираем случайный опорный элемент
        basis = arr[0]  # выбираем случайный опорный элемент
        less = [i for i in arr[1:] if i <= basis]  # формируем список с элементами < опорного
        greater = [i for i in arr[1:] if i > basis]  # список с элементами > опорного
        return quick_sort_recur(less) + [basis] + quick_sort_recur(greater)  # возвращаем финальный список


print(f'len array: {len(test_arr)}')
cProfile.run("quick_sort_recur(test_arr)")

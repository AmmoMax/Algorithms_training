# coding: utf-8

# пример простейшего примера бинарного поиска
# TODO LIST - проверить и реализовать все нижеперечисленные ба
# — не работает с массивом из 0/1/2 элементов
# — не находит первый или последний элемент
# — некорректно работает, если элемента в массиве нет
# — некорректно работает, если в массиве есть повторяющиеся элементы
# — обращение к элементами за пределами массива
# — козырная, которая была в JDK, переполнение целого при вычислении среднего индекса


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

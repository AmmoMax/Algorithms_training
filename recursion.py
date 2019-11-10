# coding: utf-8

# simple recursion func


def countdown(i):  # вывод обратного отсчет с помощью рекурсии
    print(i)
    if i <= 0:
        pass
        # использую pass вместо return, т.к. pass - ничего не делать, а return - вернуть управление потоку выполнения
    else:
        countdown(i - 1)


# countdown(5)


def fact(x):  # функция возвращающая факториал числа как пример рекурсивного алгоритма
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(10))


def summ(arr):  # функция возвращает сумму элементов положительного списка с помощью рекурсивного вызова
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])


print(summ([1, 99, 100]))

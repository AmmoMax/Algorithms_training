# coding: utf-8

# пример реализации простейшего алгоритма поиска в ширину.
#

from collections import deque

graph = {}
graph['you'] = ['alex', 'bob', 'claire']
graph['alex'] = ['jim', 'bill']
graph['bob'] = ['harry']
graph['claire'] = []
graph['jim'] = []
graph['bill'] = []


def name_starts(name):
    if str(name).startswith('h'):
        return True


def search(name):
    search_queue = deque()  # добавляем дек для хранения всех соседей
    search_queue += graph['you']
    searched = []

    while search_queue:
        person = search_queue.popleft()  # извлекаем из очереди первого человека
        if not person in searched:
            if name_starts(person):
                print(f'We are find him: {person}')  # нашли искомого человека
                return True
            else:
                search_queue += graph[person]  # не нашли искомого человека и добавляем всех его друзей в список
                searched.append(person)  # добавляем в список уже проверенных
    return False


search('you')
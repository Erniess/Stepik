# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
#
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
#
# ﻿Эквивалент на Python:
#
# class A:
#     pass
#
# class B(A, C):
#     pass
#
# class C(A):
#     pass
import json


def tree(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited


data = json.loads(input())
j_cls = {}
for key in data:
    if key['name'] not in j_cls: j_cls[key['name']] = []
    if key['parents']:
        for par in key['parents']:
            if par not in j_cls: j_cls[par] = []
            if par not in j_cls[par]: j_cls[par].append(key['name'])

print('\n'.join(sorted(['{} : {}'.format(key['name'], len(tree(j_cls, key['name']))) for key in data])))
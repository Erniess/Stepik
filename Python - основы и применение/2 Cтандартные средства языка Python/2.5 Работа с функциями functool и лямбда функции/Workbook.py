# Работа с функциями: functool и лямбда функции

n, k = 1, 5 #map(int, input().split())
print(n+k)

x = 10, 20, 31, 35, 16, 19, 18 # input().split()
xs = (int(i) for i in x)


def even(x):
    return x % 2 == 0

evens = list(filter(even, xs))
print(evens)

x = 10, 20, 31, 35, 16, 19, 18 # input().split()
xs = (int(i) for i in x)

evens_2 = list(filter(lambda x: x % 2 == 0, xs))
print(evens_2)

# Сортировка
x = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

# длинная запись
def length(name):
    return len(" ".join(name))


name_lengths = [length(name) for name in x]
print('name_lengths', name_lengths)

x.sort(key=length)
print(x)
# короткая запись
x.sort(key=lambda name: len(' '.join(name)))
print(x)

# Библиотека operator
import operator as op

print(op.add(4, 5))
print(op.mul(4, 5))
print(op.contains([1, 2, 3], 4)) # 4 не входит в список [1, 2, 3]

x = [1, 2, 3]
f = op.itemgetter(1) #
print(f(x))

x = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

x.sort(key=op.itemgetter(-1))
print(x)

# Библиотека functools

from functools import partial

x = int('1101', base=2)
print(x)
int_2 = partial(int, base=2)
x = int_2('1101')
print(x)

x = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(x)
sort_by_last(x)
print(x)

y = ['abc', 'cba', 'abb']
sort_by_last(y)
print(y)
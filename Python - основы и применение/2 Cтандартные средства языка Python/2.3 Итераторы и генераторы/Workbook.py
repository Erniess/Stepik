# Итераторы и генераторы
# Итератор
from random import random

class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

x = RandomIterator(3)
print(next(x)) # next(x) -> x.__next__() x -- iterator
print(next(x))
print(next(x))

for x in RandomIterator(1): # добавляем метот __iter__
    print(x)

class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration

class MyList(list):
    def __iter__(self):
        print('__iter__', self)
        x = DoubleElementListIterator(self)
        print(x)
        return x

for pair in MyList([1, 2, 3, 4]):
    print(pair)

# Генератор

def simple_gen():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    yield 2
    print('Checkpoint 3')

gen = simple_gen()
x = next(gen)
print(x)
x = next(gen)
print(x)


class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

def random_generator(k):
    for i in range(k):
        yield random()

gen = random_generator(3)
for i in gen:
    print(i)

def simple_gen():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    return "No more elements"
    yield 2
    print('Checkpoint 3')

gen = simple_gen()
x = next(gen)
print(x)

print([i for i in range(4)])
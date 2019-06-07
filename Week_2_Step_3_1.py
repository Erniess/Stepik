# В данной задаче мы просим вас реализовать класс multifilter,
# который будет выполнять ту же функцию, что и стандартный класс filter,
# но будет использовать не одну функцию, а несколько.
#
# Решение о допуске элемента будет приниматься на основании того,
# сколько функций допускают этот элемент, и сколько не допускают.
# Обозначим эти количества за pos и neg.
#
# Введем понятие решающей функции – это функция, которая принимает два аргумента –
# количества pos и neg, и возвращает True, если элемент допущен, и False иначе.

# Решение 1 через __next__
class multifilter:
    def __next__(self):
        if self.i < len(self.iterable):
            pos = 0
            neg = 0
            for f in self.funcs:
                if f(self.iterable[self.i]): pos += 1
                else: neg += 1
            self.i += 1
            if self.judge(pos, neg): return self.iterable[self.i - 1]
            else: return next(self)
        else:
            raise StopIteration

    def judge_half(pos, neg):
        return True if pos >= neg else False
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return True if pos >= 1 else False
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return True if neg == 0 else False
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.i = 0
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        return self
        # возвращает итератор по результирующей последовательности

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]
print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))

# Решение 2 через yield
class multifilter:

    def judge_half(pos, neg):
        return True if pos >= neg else False
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return True if pos >= 1 else False
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return True if neg == 0 else False
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.i = 0
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        for i in self.iterable:
            pos = neg = 0
            for f in self.funcs:
                if f(i): pos += 1
                else: neg += 1
            if self.judge(pos, neg): yield i

a = [i for i in range(31)]
print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
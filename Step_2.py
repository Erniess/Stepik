# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
# которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
# предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то
# количество монет, не превышая ее вместимость.

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = 0

    def can_add(self, v):
        return True if v + self.content <= self.capacity else False

    def add(self, v):
        self.content += v


copies = [MoneyBox(10), MoneyBox(20), MoneyBox(0)]
for cop in copies:
    print(cop.__dict__)
    print(cop.can_add(11))
    if cop.can_add(11): cop.add(11)
    print(cop.__dict__)


# Вам дается последовательность целых чисел и вам нужно ее обработать и
# вывести на экран сумму первой пятерки чисел из этой последовательности,
# затем сумму второй пятерки, и т. д.

class Buffer:
    def __init__(self):
        self.temp = []

    def add(self, *a):
        self.temp.extend(a)

        while len(self.temp) >= 5:
            print(sum(self.temp[:5]))
            del self.temp[:5]

    def get_current_part(self):
        return self.temp

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())
buf.add(4, 5, 6)
print(buf.get_current_part())
buf.add(7, 8, 9, 10)
print(buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(buf.get_current_part())

# Какие числа будут выведены в результате выполнения данного кода?
class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar() # создает и задает значение val для а
a.foo() # задает значение val для A

c = A()

print(a.val)
print(b.val)
print(c.val)
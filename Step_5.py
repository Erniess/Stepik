# Реализуйте структуру данных, представляющую собой расширенную структуру стек.
# Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека,
# и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления.
#
# Операция сложения на стеке определяется следующим образом. Со стека снимается верхний
# элемент (top1), затем снимается следующий верхний элемент (top2), и затем как результат
# операции сложения на вершину стека кладется элемент, равный top1 + top2.
#
# Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2)
# и целочисленного деления (top1 // top2).


class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())
        # операция сложения

    def sub(self):
        self.append(self.pop() - self.pop())
        # операция вычитания

    def mul(self):
        self.append(self.pop() * self.pop())
        # операция умножения

    def div(self):
        self.append(self.pop() // self.pop())
        # операция целочисленного деления


ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
print(ex_stack)
ex_stack.div()
print(ex_stack)
ex_stack.sub()
print(ex_stack)

# Одно из применений множественного наследование – расширение функциональности класса
# каким-то заранее определенным способом. Например, если нам понадобится логировать
# какую-то информацию при обращении к методам класса.

import time

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, arg):
        self.log(arg)
        super().append(arg)

a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)
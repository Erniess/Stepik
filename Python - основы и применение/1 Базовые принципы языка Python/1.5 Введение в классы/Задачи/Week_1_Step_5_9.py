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
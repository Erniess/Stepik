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
# Ошибки исключения

class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")

while True:
    try:
        name = "Anton"
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print("Please try again")
    else:
        break

# еализуйте класс PositiveList, отнаследовав его от класса list,
# для хранения положительных целых чисел.
# Также реализуйте новое исключение NonPositiveError.

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else: raise NonPositiveError

somelist = PositiveList([3, 5, 3])
print(somelist)
somelist.append(0)
print(somelist)
somelist.append(-1)
print(somelist)
somelist.append(2)
print(somelist)
somelist.append(-3)
print(somelist)
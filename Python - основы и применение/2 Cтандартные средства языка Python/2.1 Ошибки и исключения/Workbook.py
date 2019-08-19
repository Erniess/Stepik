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

class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EvenLengthMixin):
    pass

ml = MyList([1, 12, 4, 17, 3])
ml.sort()
print(ml)
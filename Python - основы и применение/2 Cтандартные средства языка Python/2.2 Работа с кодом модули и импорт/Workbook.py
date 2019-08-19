#  Работа с кодом: модули и импорт
# импорт класса и функции из программы import_lesson

class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")

print("Import is executed")
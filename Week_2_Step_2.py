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

def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)

f = lambda x: f(x - 1) + f(x - 2) if x >= 2 else 1

# Имя модуля
if __name__ == "__main__":
    print(__name__)
    print(fib(31))

# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит,
# когда с момента исходной даты date пройдет число дней, равное days.
# Ввод:
# 2015 12 31
# 1
# Вывод:
# 2016 1 1

import datetime

new_date = datetime.date(*map(int, "2015 12 31".split())) + datetime.timedelta(days=int(1))
print(new_date.year, new_date.month, new_date.day)

# Алиса владеет интересной информацией, которую хочет заполучить Боб.
# Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
# У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.
#
# Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями,
# но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.
#
# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
# Она представила информацию в виде строки, и затем записала в бинарный файл результат работы
# метода simplecrypt.encrypt.
#
# Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt
# узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.
#
# Ответом для данной задачи служит расшифрованная интересная информация Алисы.

from simplecrypt import encrypt, decrypt

with open("encrypted.bin", "rb") as inp, open("passwords.txt", "r") as f:
    encrypted = inp.read()
    passwords = f.read().split()

for password in passwords:
    print(password)
    try:
        print(decrypt(password, encrypted).decode('utf8'))
    except:
        continue
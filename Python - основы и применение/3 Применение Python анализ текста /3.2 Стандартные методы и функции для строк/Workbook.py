# Стандартные методы и функции для строк

print('abc' in 'abcba')
print('abce' in 'abcba')
print('cabcd'.find('aec')) # индекс первого вхождения или -1
print(str.find.__doc__)
print('cabcd'.find('abc', 1))
print('cabcd'[1:].find('abc'))

print('cabcd'.index('abc')) # индекс первого вхождения или ValueError
#print('cabcd'.index('aec'))

s = "The dog in black fled across the desert, and the gunslinger followed"
print(s.startswith("The man in black"))
print(s.startswith.__doc__)

print(s.startswith(("The woman", "The dog", "The man in black")))

s = "image.png"
print(s.endswith(".png"))

s = "ababa"
print(s.count("aba"))
print(s.count.__doc__)

print(s.find(("aba")))
print(s.rfind(("aba"))) # Поиск вхождения справа

s = "The dog in black fled across the desert, and the gunslinger followed"
print(s.upper())
print(s.lower())
print(s.count("the"))
print(s.lower().count("the"))

s = "1,2,3,4"
print(s)
print(s.replace(",", ", ", 2))
print(s.replace.__doc__)

s = "1 2 3 4"
print(s.split(" ", 2))
print(s.split.__doc__)

s = "1\t\t2        3 4"
print(s.split())

s = "     1 2 3 4   "
print(repr(s.rstrip()))
print(repr(s.lstrip()))
print(repr(s.strip()))

s = "_*__1, 2, 3, 4__*_"
print(repr(s.rstrip("*_")))
print(repr(s.lstrip("*_")))
print(repr(s.strip("*_")))

numbers = map(str, [1, 2, 3, 4, 5])
print(repr(" ").join(numbers))

# Форматирование

capital = 'London is the capital of Greate Britain'
template = '{} is the capital of {}'
print(template.format('London', 'Greate Britain'))
print(template.format('Vaduz', 'Liechtenstein'))

# Порядок форматирования
template = '{1} is the capital of {0}'
print(template.format('Vaduz', 'Liechtenstein'))

# Именованные аргументы
template = '{capital} is the capital of {country}'
print(template.format(country='Vaduz', capital='Liechtenstein'))

# Форматирование ответа по аргументам
import requests
template = 'Response from {0.url} with code {0.status_code}'

res = requests.get('https://docs.python.org/3.5/')
print(template.format(res))

res = requests.get('https://docs.python.org/3.5/random')
print(template.format(res))

# Округление до определенного количества цифр после запятой
from random import random

x = random()
print(x)
print('{:.3}'.format(x))


# Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
# За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
#


#s, a, b = str(input()), str(input()), str(input())
s = 'ababa'
a = 'a'
b = 'b'

if a in b and a in s:
    print('Impossible')
else:
    operation_number = 0
    while a in s and operation_number <= 1000:
        s = s.replace(a, b)
        operation_number += 1
    print(operation_number)

# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
#
# Выведите одно число – количество вхождений строки t в строку s.

# s, t = str(input()), str(input())
s = "aaaaa"
t = "a"

operation_number = 0

for i in range(len(s)):
    if s.startswith(t):
        operation_number += 1
    s = s[1:]
print(operation_number)

s = "abababa"
t = "aba"

k = len([i for i in range(0, len(s) - len(t) + 1) if s[i:].startswith(t)])
print(k)
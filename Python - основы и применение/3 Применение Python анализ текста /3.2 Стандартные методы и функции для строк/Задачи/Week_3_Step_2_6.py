# Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
# За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
#

# Решние 1
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

# Решние 2
#s, a, b = str(input()), str(input()), str(input())
operation_number = 0

while s.count(a) and operation_number <= 1000:
    s = s.replace(a, b)
    operation_number += 1
print(operation_number if operation_number <= 1000 else 'Impossible')

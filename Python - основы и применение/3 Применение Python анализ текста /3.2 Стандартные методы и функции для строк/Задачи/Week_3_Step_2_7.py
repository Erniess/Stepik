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
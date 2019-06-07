#print(sum([int(input()) for i in range(int(input()))]))

# Вывести повторы в списске
objects = [1, 2, 1, 2, 3]
ans = 0
tmp = []
for obj in objects:
    if obj not in tmp:
        tmp.append(obj)
        ans += 1
print(len(set(id(i) for i in objects)))

# Факториал числа
f = lambda x: x * f(x-1) if x >= 2 else 1
print(f(10))

# Ближайшее число которое делится на 5 и не меньше введенного
closest_mod_5 = lambda x: x if x % 5 == 0 else x + 5 - x % 5
print(closest_mod_5(12))

# Поведение аргументов при вызове функции
def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print(s(11,10,b=10))

# Пары чисел Cn(x, y)
f = lambda x, y: f(x - 1, y) + f(x - 1, y - 1) if y != 0 and y <= x else 1 if y == 0 else 0
print(f(10,5))

def f(x, y):
    return f(x - 1, y) + f(x - 1, y - 1) if y != 0 and y <= x else 1 if y == 0 else 0


n, k = map(int, input().split())
print(f(n, k))

# Эмуляция пространства имен
""" Sample Input:

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
"""

n = int(input())
db = {'global' : {'parent' : None, 'vars' : []}}

def get(namesp, arg):
    return namesp if arg in db[namesp]['vars'] else get(db[namesp]['parent'], arg) if db[namesp]['parent'] else None


for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'add': db[namesp]['vars'].append(arg)
    elif cmd == 'create': db[namesp] = {'parent' : arg, 'vars' : []}
    elif cmd == 'get': print(get(namesp, arg))


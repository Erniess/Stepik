# Пары чисел Cn(x, y)
f = lambda x, y: f(x - 1, y) + f(x - 1, y - 1) if y != 0 and y <= x else 1 if y == 0 else 0
print(f(10,5))

def f(x, y):
    return f(x - 1, y) + f(x - 1, y - 1) if y != 0 and y <= x else 1 if y == 0 else 0


n, k = map(int, input().split())
print(f(n, k))
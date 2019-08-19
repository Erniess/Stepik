# Числа Фибоначчи
# Рекурсивный алгоритм 2 варианта
def fib1(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib1(k - 1) + fib1(k - 2)

fib2 = lambda x: fib2(x - 1) + fib2(x - 2) if x >= 2 else 1

# Табличный алгоритм
def fib3(n):
    F = [0 for _ in range(n)]
    F[0] = 0
    F[1] = 1
    for i in range(2, n):
        F[i] = F[i - 1] + F[i - 2]
    return F[n - 1]



if __name__ == "__main__":
    print(fib1(31))
    print(fib2(31))
    print(fib3(100))
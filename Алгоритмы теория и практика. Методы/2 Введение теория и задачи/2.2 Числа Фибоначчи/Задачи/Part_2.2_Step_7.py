# Задача на программирование: последняя цифра большого числа Фибоначчи

def fib_digit(n):
    if n == 1 or n == 2: return 1
    a, b = 1, 1
    for _ in range(2, n):
        b = (a + b) % 10
        a = b - a
    return b

def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
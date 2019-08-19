# Задача на программирование: небольшое число Фибоначчи

def fib(n):
    if n == 1: return 1
    ans = [0] * n
    ans[0] = 1
    ans[1] = 1
    for i in range(2, n):
        ans[i] = ans[i - 1] + ans[i - 2]
    return ans[n - 1]

def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()
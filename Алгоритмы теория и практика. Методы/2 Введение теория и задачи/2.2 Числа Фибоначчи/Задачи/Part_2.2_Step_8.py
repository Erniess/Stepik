# Задача на программирование повышенной сложности:
# огромное число Фибоначчи по модулю

def fib_mod(n, m):
    if n == 1 or n == 2: return 1
    ans = [0, 1]
    a, b = ans
    for _ in range(2, m*6):
        a, b = b, (a + b) % m
        ans.append(b)
        if ans[:2] == ans[-2:]:
            del ans[-2:]
            break
    return ans[n%len(ans)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
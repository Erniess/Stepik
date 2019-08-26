import timeit

def nod1(a, b):
    d = 1
    for i in range(2, max(a, b)):
        if a % i == 0 and b % i == 0:
            d = i
    return d

# Алгоритм Евклида
def nod2(a, b):
    if a == 0: return b
    if b == 0: return a
    if a >= b:
        return nod2(a % b, b)
    if b >= a:
        return nod2(a, b % a)

start_time = timeit.default_timer()
print(nod1(3918848, 1653264))
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
print(nod2(3918848, 1653264))
print(timeit.default_timer() - start_time)

# Алгоритм Лемма

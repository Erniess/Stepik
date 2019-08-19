#print(sum([int(input()) for i in range(int(input()))]))

# Факториал числа
f = lambda x: x * f(x-1) if x >= 2 else 1
print(f(10))

# Поведение аргументов при вызове функции
def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print(s(11,10,b=10))

# Какие числа будут выведены в результате выполнения данного кода?
class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar() # создает и задает значение val для а
a.foo() # задает значение val для A

c = A()

print(a.val)
print(b.val)
print(c.val)

#Какие числа будут выведены в результате выполнения данного кода?

class Base:
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1

    def add_many(self, x):
        for i in range(x):
            self.add_one()

class Derived(Base):
    def add_one(self):
        self.val += 10


a = Derived()
a.add_one()

b = Derived()
b.add_many(3)

print(a.val)
print(b.val)

# class A:
#    def foo(self):
#       print("A")
#
# class B(A):
#    pass
#
# class C(A):
#    def foo(self):
#       print("C")
#
# class D:
#    def foo(self):
#       print("D")
#
# class E(B, C, D):
#    pass
#
# E().foo()

class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass

class E(B, C, D):
    pass

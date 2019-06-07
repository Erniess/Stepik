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
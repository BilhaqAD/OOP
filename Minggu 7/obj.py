# __repr__ is for developers, __str__ is for customers
class A:
    def __init__(self, a_var):
        self.a_var = a_var

    def __str__(self):
        return self.a_var

    def __repr__(self):
        return self.a_var

class B:
    def __init__(self, b_var):
        self.b_var = b_var

    def __repr__(self):
        return self.b_var

a = A(4)
b = B("Hello")
print(b.b_var)          # Hello
print(b.a)              # AttributeError: 'B' object has no attribute 'a'
print(b.a.a_var)        # AttributeError: 'A' object has no attribute 'a_var'
class Parent:
    def __init__(self):
        self.a = 1
        self.b = 2

    def function(self):
        print('Parent')

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.c = 3
        self.d = 4

c = Child()
print(c.a)
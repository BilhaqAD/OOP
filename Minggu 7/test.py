class Shape():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Rectangle(Shape):
    def __init__(self, x, y ):
        super().__init__(x, y)

    def area(self):
        pass


class Square(Shape):
    def __init__(self, x):
        super().__init__(x, x)

rect = Rectangle(4, 3)
# print(rect.area())
sqr = Square(5)
# print(sqr.area())

shape = [rect, sqr]
for s in shape:
    print(s.area())
    

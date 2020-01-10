class Square:

    def __init__(self, x):
        self.x = x

    def area(self):
        print("Area of Square", self.x * self.x)

class Rectangle(Square):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def area(self):
        super().area()
        print("Area of Rectange", self.x * self.y)
        
r = Rectangle(5,10)
r.area()

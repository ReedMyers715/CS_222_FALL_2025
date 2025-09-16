import math
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def DisplayArea(self):
        print(f"The area of {self.name} is {self.area():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, w, l):
        super().__init__("Rectangle")
        self.width = w
        self.length = l
    
    def area(self):
        return self.width * self.length
    
class Triangle(Shape):
    def __init__(self, b, h):
        super().__init__("Triangle")
        self.base = b
        self.height = h

    def area(self):
        return 0.5 * self.base * self.height
    
def main():
    c = Circle(10)
    c.DisplayArea
    r = Rectangle(5, 3)
    r.DisplayArea
    t = Triangle(9, 4)
    t.DisplayArea
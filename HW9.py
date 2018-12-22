import math


class Rectangle:
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return self.l * 2 + self.w * 2


class Triangle:
    def __init__(self, side1, side2, side3):
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        return math.sqrt((self.perimeter() / 2) * (self.perimeter() / 2 - self.s1) * (self.perimeter() / 2 - self.s2) *
                         (self.perimeter() / 2 - self.s3))


class Equilateral(Triangle):
    def __init__(self, sides):
        super().__init__(sides, sides, sides)
        self.s = sides

    def area(self):
        return (self.s ** 2 * math.sqrt(3)) / 4


tria = Equilateral(5)
print("tria = Equilateral(5)")
print("Perimeter:", str(tria.perimeter()))
print("Area:", str(tria.area()), "(" + (str(round(tria.area())) + ")"))
print()
trib = Triangle(3, 4, 5)
print("trib = Triangle(3, 4, 5)")
print("Perimeter:", str(trib.perimeter()))
print("Area:", str(trib.area()), "(" + (str(round(trib.area())) + ")"))
print()
rect = Rectangle(5, 3)
print("rect = Rectangle(5, 3)")
print("Perimeter:", str(rect.perimeter()))
print("Area:", str(rect.area()))

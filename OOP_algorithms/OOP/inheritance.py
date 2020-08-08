from triangle_class import Triangle
from triangle_class import Isosceles

class Rectangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


class Square(Rectangle):

    def __init__(self, side):

        #super() allows to obtain a direct reference of the superclass
        #after dot we're calling superclass' constructor
        super().__init__(side, side)



if __name__ == '__main__':
    rectangle = Rectangle(base = 5, height = 15)
    print(rectangle.area())

    square = Square(side = 20)
    print(square.area())

    triangle = Triangle(1, 3, 6)
    print(triangle.perimeter())

    isosceles = Isosceles(5, 6)
    print(isosceles.perimeter())

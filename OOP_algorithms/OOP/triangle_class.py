class Triangle:

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3


class Isosceles(Triangle):

    def __init__(self, side_l, side_b):

        super().__init__(side_l, side_l, side_b)



class Equilateral(Triangle):

    def __init__(self, side_l):

        super().__init__(side_l, side_l, side_l)

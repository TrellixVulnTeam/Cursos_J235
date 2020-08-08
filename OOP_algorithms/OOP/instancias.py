class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self, other_coordinate):
        x_diff = (self.x - other_coordinate.x)**2
        y_diff = (self.y - other_coordinate.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coor_1 = Coordinate(3, 56)
    coor_2 = Coordinate(96, 51)

    print(coor_1.distance(coor_2), 'meters')
    print(coor_2.distance(coor_1), 'meters')

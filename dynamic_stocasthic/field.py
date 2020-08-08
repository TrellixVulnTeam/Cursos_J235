"""
This class is meant to link both Drunk and Coordinate classes.
"""

class Field:

    #Init an empty dictionary which purpose is store the locations of the
    #drunks within the field using coordinates
    def __init__(self):
        self.coordinates_dict = {}

    #As the line of the method show off, this is meant to add a drunk into the
    #dictionary with a given location
    def add(self, drunk, coordinate):
        self.coordinates_dict[drunk] = coordinate

    #This one is meant to move the drunk guy calling the method move() of the
    #Drunk class and rewrite its position within the dictionary
    def move_drunk(self, drunk):
        delta_x, delta_y = drunk.walk()
        current_coordinate = self.coordinates_dict[drunk]
        new_coordinate = current_coordinate.move(delta_x, delta_y)

        self.coordinates_dict[drunk] = new_coordinate

    def obtain_coordinate(self, drunk):
        return self.coordinates_dict[drunk]

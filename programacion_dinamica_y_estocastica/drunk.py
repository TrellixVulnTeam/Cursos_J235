"""
This class is meant to create a Drunk object in order to move randomly within
a field
"""
import random

class Drunk:

    def __init__(self, name):
        self.name = name


class DrunkGuy(Drunk):

    def __init__(self, nombre):
        super().__init__(nombre)

    def walk(self):
        #random.choice() randomly selects an option of a given list
        return random.choice([(1,0), (-1,0), (0,1), (0,-1)])

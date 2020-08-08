from drunk import DrunkGuy
from coordinates import Coordinate
from field import Field


def walk(field, drunk_obj, steps):
    start = field.obtain_coordinate(drunk_obj)

    for _ in range(steps):
        field.move_drunk(drunk_obj)

    return start.distance(field.obtain_coordinate(drunk_obj))

def simulate_walk(steps, tries, drunk_guy):
    #Initializing our variables
    drunk_obj = drunk_guy('John') #Note this is equal to →
    #drunk_obj = DrunkGuy(name = 'John')

    origin = Coordinate(0, 0)
    distances = []

    #This is the simulation:
    for _ in range(tries):
        field = Field()
        field.add(drunk_obj, origin)

        #Using auxiliar function
        simulation = walk(field, drunk_obj, steps)
        distances.append(simulate_walk)

    return distances


def main(distance, tries, drunk_guy):
    """
    This is the core of simulation
    """

    for steps in distance:
        #The simulation returns an array of distances

        distances = simulate_walk (steps, tries, drunk_guy)
        print(type(sum(distances)))
        average = sum(distances) / len(distances)

        maximum = max(distances)
        minimum = min(distances)

        print(f'{drunk_guy.__name__} walked randomly {steps}')
        print(maximum)
        print(minimum)


if __name__ == "__main__":
    distances = [10, 100, 1000]
    tries = 100

    main(distances, tries, DrunkGuy)

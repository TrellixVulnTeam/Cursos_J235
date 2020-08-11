class Vehicle:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color

        #private variable
        self._state = 'Not moving'

        #Here we're calling the class Engine to
        #initialize the private var engine
        self._engine = Engine(cylinders = '4')


    def in_movement(self, speed = 4):

        #0 < speed < 4 → slow/moderate
        #4 < speed < 9 → fast
        # speed > 9    → GT mode

        if speed in range(4, 9):
            self._state = 'Moving fast...'
            self.inject_gasoline(10)
        elif speed < 4:
            self.inject_gasoline(5)
        else:
            self.turn_on_GT()


class Engine:

    def __init__(self, cylinders, type = 'gasoline'):
        self.cylinders = cylinders
        #We don't need to initialize the default value type

        self._temperature = 0


    def inject_gasoline(self, quantity):
        while self._temperature < 120:
            open_injectors(amount_gasoline)


    def open_injectors(self, amount_gasoline):
        pass

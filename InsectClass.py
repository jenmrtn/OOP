import random

class Insect:

    def __init__(self):
        self.wings = '2'
        self.legs = '4'
        self.flight= ''

    def flightlength(self):
        self.flight= random.randint(0, 10)

    def get_flight(self):
        return self.flight

    def get_wings(self):
        return self.wings

    def get_legs(self):
        return self.legs
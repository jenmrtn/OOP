import random

# The Coin class simulates a coin that can
# be flipped.

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.
    #use uppercase for class definition name

    def __init__(self):
        self.__sideup = 'Heads'
        #this initializes the instance
        #this is defining attributes
        #Like self.bullets= xxx


    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
         #This is defining the methods
    # The get_sideup method returns the value
    # referenced by sideup.
        #Mutator method changes the value of an attribute. Also known as set method
        #Get method or Accessor method returns the value of an attribute
        #never combine the two
        # ONly want to accomplish one thing with a method
    def get_sideup(self):
            return self.__sideup
# TO hide an attribute put __ before the name
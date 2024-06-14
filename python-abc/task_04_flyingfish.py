#!/usr/bin/python3

"""
flyingfish
"""

class Fish:
    """
    defines a fish
    Attributes:
        Swim: bc the fish swims
        Habitat: bc the fish lives in water
    """
    def swim(self):
        """
        the fish swims
        """
        print("The fish is swimming")
    
    def habitat(self):
        """
        the fish lives in water
        """
        print("The fish lives in water")

class Bird:
    """
    defines a bird
    Attributes:
        fly: bc the bird flies
        habitat: bc the bird lives in the sky
    """
    def fly(self):
        """
        the bird flies
        """
        print("The bird is flying")
    
    def habitat(self):
        """
        the habitat of the bird
        """
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    flyingfish
    Attributes:
        Fish: the fish
        Bird: the bird
    """
    def fly(self):
        """
        the fish flies
        """
        print("The flying fish is soaring!")
    
    def swim(self):
        """
        the fish that flies is swimming
        """
        print("The flying fish is swimming!")
    
    def habitat(self):
        """
        the fish that flies lives in water and sky
        """
        print("The flying fish lives both in water and the sky!")

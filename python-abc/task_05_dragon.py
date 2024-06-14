#/usr/bin/python3

"""
dragon
"""

class SwimMixin:
    """
    defines swimmixin
    """
    def swim(self):
        """
        defines swim
        """
        print("The creature swims!")

class FlyMixin:
    """
    defines flymixin
    """
    def fly(self):
        """
        fly
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    dragon
    """
    def roar(self):
        """
        roar
        """
        print("The dragon roars!")

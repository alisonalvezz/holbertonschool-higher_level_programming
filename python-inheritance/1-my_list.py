#!/usr/bin/python3
"""
class mylist that inherits from list
"""

class MyList(list):
    """ My list"""

    def print_sorted(self):
        """ returns its list"""

        print(sorted(self))


#!/usr/bin/python3
"""
class mylist that inherits from list
"""

class MyList(list):
    """ My list"""

    def printed_sorted(self):
        """ returns its list"""

        print(sorted(self))


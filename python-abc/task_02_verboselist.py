#!/usr/bin/python3
"""
verboselist
"""

class VerboseList(list):
    """
    list class
    """

    def append(self, obj):
        """
        append
        """

        super().append(obj)
        print("Added[{}] to the list".format(obj))

    def extend(self, obj):
        """
        extend
        """

        super().extend(obj)
        print("Extended the list with [{}] items".format(len(obj)))

    def remove(self, obj):
        """
        remove
        """

        super().remove(obj)
        print("Removed [{}] from the list".format(obj))

    def pop(self, obj=-1):
        """
        pop
        """
        if obj is None:
            print(f"Popped [{self[-1]}] from the list")
        else:
            print("Popped [{}] from the list".format(self[obj]))
        super().pop(obj)

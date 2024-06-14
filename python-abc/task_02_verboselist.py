#!/usr/bin/python3
"""
Verbose List class that extends the built-in list class with additional verbose output.
"""

class VerboseList(list):
    """
    A list subclass that prints verbose messages for append, extend, remove, and pop operations.
    """

    def append(self, obj):
        """
        Appends an object to the list and prints a message.
        
        Args:
            obj: object to append to the list.
        """
        super().append(obj)
        print(f"Added [{obj}] to the list")

    def extend(self, iterable):
        """
        Extends the list with objects from an iterable and prints a message.
        
        Args:
            iterable: Iterable containing objects to extend the list with.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items")

    def remove(self, obj):
        """
        Removes the first occurrence of an object from the list and prints a message.
        
        Args:
            obj: Object to remove from the list.
        """
        super().remove(obj)
        print(f"Removed [{obj}] from the list")

    def pop(self, index=-1):
        """
        Removes and returns the item at the specified index from the list and prints a message.
        If no index is specified, removes and returns the last item in the list.
        
        Args:
            index: Index of the item to pop from the list (default is -1).

        Returns:
            object: Item popped from the list.
        """
        popped_item = super().pop(index)
        if index == -1:
            print(f"Popped [{popped_item}] from the list")
        else:
            print(f"Popped [{popped_item}] from index [{index}] in the list")
        return popped_item

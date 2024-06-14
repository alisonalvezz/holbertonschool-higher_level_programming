#!/usr/bin/python3
"""
countedIterator
"""


class CountedIterator:
    """
    will extend the builtin in iterator and keep track
    of the number of items iterated over
    """
    def __init__(self, iterable):
        """
        initializes the iterable
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        next method
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items in the iterator")

    def get_count(self):
        """
        get count
        returns:
            the count
        """
        return self.count

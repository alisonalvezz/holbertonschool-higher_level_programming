#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = set()

    for elements in set_1:
        if elements not in set_2:
            diff_set.add(elements)

    for elements in set_2:
        if elements not in set_1:
            diff_set.add(elements)

    return diff_set

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a_first = tuple_a[0]
        a_second = tuple_a[1]
    else:
        a_first = tuple_a[0] if len(tuple_a) > 0 else 0
        a_second = 0
    
    if len(tuple_b) >= 2:
        b_first = tuple_b[0]
        b_second = tuple_b[1]
    else:
        b_first = tuple_b[0] if len(tuple_b) > 0 else 0
        b_second = 0
    
    first_add = a_first + b_first
    second_add = a_second + b_second
    
    return (first_add, second_add)

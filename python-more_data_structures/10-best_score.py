#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    best_key = None
    best_score = None

    for key in a_dictionary:
        value = a_dictionary[key]

        if best_score is None or value > best_score:
            best_score = value
            best_key = key
        
    return best_key

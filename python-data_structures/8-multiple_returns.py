#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence = None
        lenght = 0
    else:
        length = len(sentence)
        first = sentence[0]
        return(length, first)

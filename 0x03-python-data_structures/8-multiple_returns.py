#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        output = (0, None)
        return (output)
    else:
        result = (length, sentence[0:1])
        return (result)

"""stats functions

This module does abc

Todo:
    * Clean code
    * Add return values

"""

def avgValue(values) :
    total = 0
    for v in values :
        total += v

    return total

def maxValue(values) :
    max = 0
    for v in values :
        if v > max :
            max = v

    return max

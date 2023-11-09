'''
ASSIGNMENT
Write a function log_scale(data, base) that takes a list of positive numbers data,
and a logarithmic base, and returns a new list with the logarithm of each number
in the original list, using the given base.

You may want to use the math.log() function.
'''

import math


def log_scale(data, base):
    output = []
    for x in data:
        output.append(math.log(x, base))
    return output
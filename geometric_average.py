"""this module contains method that returns geometric average by numbers"""

import math


def geometric_average(numbers: list):
    """returns geometric average by numbers"""
    return math.exp(math.fsum(math.log(n) for n in numbers) / len(numbers))

#!/usr/bin/env python3
"""A type-annotated function floor which takes a float n as argument
   and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """returns the floor of n"""
    return int(math.floor(n))

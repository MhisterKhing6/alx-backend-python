#!/usr/bin/env python3
"""
create a function that return a mulitplier of float
"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multipler: a function that returns a mulitplier of float
    Args:
        multiplier: a float
    returns : a function that returns a mulitplier of float
    """
    return lambda x: multiplier * x

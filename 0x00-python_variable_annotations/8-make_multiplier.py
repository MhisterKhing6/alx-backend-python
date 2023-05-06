#!/usr/bin/env python3
"""
create a function that return a mulitplier of float
"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    to_kv : returns a tuple of k and sqaure of v
    Args:
        k: a string
        v : an integer or a float
    returns : tupe of k and sqrrt of v
    """
    return lambda x: multiplier * x

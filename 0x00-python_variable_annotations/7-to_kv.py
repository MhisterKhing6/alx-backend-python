#!/usr/bin/env python3
"""
create a funcction that returns the sum of lists as a float
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv : returns a tuple of k and sqaure of v
    Args:
        k: a string
        v : an integer or a float
    returns : tupe of k and sqrrt of v
    """
    return (k, v**2)

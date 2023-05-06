#!/usr/bin/env python3
"""
Create a funtion Add with proper annotations of parameters
"""
from typing import List, Union, Tuple, Callable, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length : returns the lenght of element in interable
    args:
        lst : list of iterables elements
    """
    return [(i, len(i)) for i in lst]

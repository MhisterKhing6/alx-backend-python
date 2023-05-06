#!/usr/bin/env python3
"""
Create a funtion Add with proper annotations of parameters
"""
from typing import List, Union, Tuple, Callable, Sequence, Any
import typing


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_elemnt: Anoting a function with unkown container parameters
    args: 
    lst: the list of sequence to annotate
    """
    if lst:
        return lst[0]
    else:
        return None

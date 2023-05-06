#!/usr/bin/env python3
"""
Create a funtion Add with proper annotations of parameters
"""
from typing import List, Union, TypeVar, Mapping, Any


T = TypeVar('T')


def safely_get_value(
    dct:  Mapping, key: Any, default: T = None
                    ) -> Union[Any, T]:
    """
    safely_get_value: Anotate Generic variables with TypeVar in function
    args:
        dct: A map object
        key: a generic object
        default: A generic object
    """
    if key in dct:
        return dct[key]
    else:
        return default

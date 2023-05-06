#!/usr/bin/env python3
"""
Returns the sum of float values
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum : returns the sum of values in input_list
    Args:
        a : list of float values
    return sum of float values
    """
    return float(sum(input_list))

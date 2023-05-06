#!/usr/bin/env python3
"""
create a funcction that returns the sum of lists as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum : returns the sum of values in input_list
    Args:
        a : list of float values
    return sum of float values
    """
    return float(sum(mxd_lst))

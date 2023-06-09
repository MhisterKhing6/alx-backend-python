#!/usr/bin/env python3

'''
Write a function that run multiiple caro rutines in parallel
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    wait_n : runs multiple caro rutines in parallel
    Arguements:
        max_delay: The maximum time the funcion shoud sleed
        n : The number of caro rutines
    """
    res = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n))
        )
    return sorted(res)

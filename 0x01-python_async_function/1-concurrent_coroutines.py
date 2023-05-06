#!/usr/bin/env python3

'''
Write a function that run multiiple caro rutines in parallel
'''
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(number: int, max_delay: int = 10) -> list:
    """
    wait_n : runs multiple caro rutines in parallel
    Arguements:
        max_delay: The maximum time the funcion shoud sleed
        n : The number of caro rutines
    """
    res = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(number))
        )
    return sorted(res)

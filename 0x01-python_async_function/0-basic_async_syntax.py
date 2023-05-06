#!/usr/bin/env python3

'''
Write a funciton that waits random time
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random : wait for a random time before executing
    Arguements:
        max_delay: The maximum time the funcion shoud sleedp
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

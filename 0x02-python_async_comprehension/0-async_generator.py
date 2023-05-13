#!/usr/bin/env python3
"""
Asynchronous Comprehension.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    async_generator-> Yields a random value
    returns : a generator object
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)

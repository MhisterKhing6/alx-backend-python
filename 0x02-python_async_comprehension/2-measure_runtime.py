#!/usr/bin/env python3
"""Implementin async comprehension"""
import asyncio
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> int:
    """
    measure the time it takes for an asycnhronus operation to complete
    return list of floats
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start

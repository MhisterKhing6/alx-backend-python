#!/usr/bin/env python3
"""Implementin async comprehension"""
import asyncio
from typing import Iterable
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterable[float]:
    """
    async_comprehension: genrate results from a genrator function
    return list of floats
    """
    result = [i async for i in async_generator()]
    return result
